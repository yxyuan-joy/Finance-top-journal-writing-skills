from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "run_skill_evals.py"
SPEC = importlib.util.spec_from_file_location("run_skill_evals", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

VALIDATOR_PATH = ROOT / "scripts" / "validate_repo.py"
VALIDATOR_SPEC = importlib.util.spec_from_file_location("validate_repo", VALIDATOR_PATH)
assert VALIDATOR_SPEC and VALIDATOR_SPEC.loader
VALIDATOR = importlib.util.module_from_spec(VALIDATOR_SPEC)
sys.modules[VALIDATOR_SPEC.name] = VALIDATOR
VALIDATOR_SPEC.loader.exec_module(VALIDATOR)


class SkillEvalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.routing, cls.behavior, cls.schema_errors = MODULE.load_and_validate_cases(ROOT)
        cls.report = MODULE.build_report(ROOT, include_details=True)

    def test_fixture_schema_and_minimum_coverage(self) -> None:
        self.assertEqual(self.schema_errors, [])
        self.assertGreaterEqual(len(self.routing), 29)
        self.assertGreaterEqual(len(self.behavior), 10)
        self.assertEqual(
            {case["skill"] for case in self.behavior},
            set(MODULE.SKILLS),
        )
        self.assertIn("zh", {case["language"] for case in self.routing})
        tags = {tag for case in self.routing for tag in case["tags"]}
        self.assertTrue(
            {"colloquial", "implicit-terminology", "cross-skill-conflict"} <= tags
        )

    def test_primary_rank_one_and_required_set_top_k(self) -> None:
        routing = self.report["routing"]
        self.assertEqual(routing["primary_rank_1"]["accuracy"], 1.0)
        self.assertEqual(routing["required_set_top_k"]["accuracy"], 1.0)
        self.assertEqual(routing["adjacent_negative_exclusion"]["accuracy"], 1.0)
        self.assertEqual(routing["no_route"]["accuracy"], 1.0)
        self.assertEqual(routing["failures"], [])

    def test_core_and_specialist_are_intended_co_route(self) -> None:
        case = next(
            item for item in self.report["routing"]["case_results"]
            if item["id"] == "route-causal-staggered-did-en"
        )
        self.assertEqual(case["predicted_primary"], MODULE.CORE_SKILL)
        self.assertEqual(
            case["predicted_top_k"],
            [MODULE.CORE_SKILL, "finance-causal-empirical-writing"],
        )
        self.assertTrue(case["passed"])

    def test_out_of_scope_prompts_are_not_routed(self) -> None:
        for prompt in (
            "Explain how to compute WACC for my company.",
            "Rewrite the abstract of my molecular-biology manuscript.",
            "现在应该买哪只股票？给我下周的收益预测。",
        ):
            routed = MODULE.route_prompt(prompt)
            self.assertEqual(routed["ranked"], [], prompt)
            self.assertEqual(routed["selected"], [], prompt)

    def test_description_and_route_collisions_are_reported(self) -> None:
        self.assertTrue(self.report["description_collisions"])
        for collision in self.report["description_collisions"]:
            self.assertGreater(collision["jaccard"], 0)
            self.assertTrue(collision["shared_terms"])
        route_collisions = self.report["routing"]["route_collisions"]
        self.assertTrue(route_collisions)
        self.assertTrue(
            all(len(collision["specialists"]) >= 2 for collision in route_collisions)
        )

    def test_behavioral_layer_validates_schema_only(self) -> None:
        behavior = self.report["behavioral_schema"]
        self.assertEqual(behavior["cases"], 10)
        self.assertEqual(behavior["by_skill"], {skill: 2 for skill in MODULE.SKILLS})
        self.assertGreaterEqual(behavior["expectations"], 20)
        self.assertGreaterEqual(behavior["hard_failures"], 20)
        self.assertNotIn("pass_rate", behavior)
        self.assertNotIn("model", behavior)

    def test_instructional_generalization_guard(self) -> None:
        self.assertEqual(VALIDATOR.validate_instructional_generalization(), [])
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            procedural = root / "procedural.md"
            procedural.write_text(
                "Reusable rule followed by https://doi.org/10.0000/example.",
                encoding="utf-8",
            )
            original_root = VALIDATOR.ROOT
            original_files = VALIDATOR.INSTRUCTIONAL_GENERALIZATION_FILES
            try:
                VALIDATOR.ROOT = root
                VALIDATOR.INSTRUCTIONAL_GENERALIZATION_FILES = ("procedural.md",)
                errors = VALIDATOR.validate_instructional_generalization()
            finally:
                VALIDATOR.ROOT = original_root
                VALIDATOR.INSTRUCTIONAL_GENERALIZATION_FILES = original_files
            self.assertEqual(len(errors), 1)
            self.assertIn("paper-level title or identifier", errors[0])

    def test_invalid_behavior_regex_is_a_schema_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            case_dir = root / "evals" / "cases"
            case_dir.mkdir(parents=True)
            source = json.loads(
                (ROOT / "evals" / "cases" / "behavior-v1.json").read_text(
                    encoding="utf-8"
                )
            )
            source["cases"][0]["expectations"][0] = {
                "id": "broken-regex",
                "target": "response",
                "matcher": "regex",
                "pattern": "(",
                "description": "A deliberately malformed expression.",
            }
            (case_dir / "behavior-v1.json").write_text(
                json.dumps(source, ensure_ascii=False), encoding="utf-8"
            )
            _, _, errors = MODULE.load_and_validate_cases(root)
            self.assertTrue(any("invalid regex" in error for error in errors), errors)

    def test_cli_returns_nonzero_for_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            case_dir = root / "evals" / "cases"
            skill_dir = root / "skills"
            case_dir.mkdir(parents=True)
            skill_dir.mkdir(parents=True)
            routing = json.loads(
                (ROOT / "evals" / "cases" / "routing-v1.json").read_text(
                    encoding="utf-8"
                )
            )
            routing["cases"][0]["expected_primary"] = "finance-causal-empirical-writing"
            routing["cases"][0]["negative_for"] = ["finance-asset-pricing-writing"]
            (case_dir / "routing-v1.json").write_text(
                json.dumps(routing, ensure_ascii=False), encoding="utf-8"
            )
            behavior = ROOT / "evals" / "cases" / "behavior-v1.json"
            (case_dir / "behavior-v1.json").write_text(
                behavior.read_text(encoding="utf-8"), encoding="utf-8"
            )
            for skill in MODULE.SKILLS:
                target = skill_dir / skill
                target.mkdir()
                source_text = (ROOT / "skills" / skill / "SKILL.md").read_text(
                    encoding="utf-8"
                )
                (target / "SKILL.md").write_text(source_text, encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(MODULE_PATH), "--root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            payload = json.loads(completed.stdout)
            self.assertFalse(payload["passed"])
            self.assertTrue(payload["routing"]["failures"])

    def test_cli_passes_without_third_party_dependencies(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-I", str(MODULE_PATH), "--root", str(ROOT)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["passed"])


if __name__ == "__main__":
    unittest.main()
