from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "run_behavior_evals.py"
SPEC = importlib.util.spec_from_file_location("run_behavior_evals", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BehaviorEvalTests(unittest.TestCase):
    def test_assertion_matchers(self) -> None:
        response = "The association predicts defaults, but it does not establish causality."
        self.assertTrue(MODULE.assertion_matches({"matcher": "contains", "value": "association"}, response))
        self.assertTrue(MODULE.assertion_matches({"matcher": "contains_any", "values": ["effect", "predicts"]}, response))
        self.assertTrue(MODULE.assertion_matches({"matcher": "contains_all", "values": ["predicts", "causality"]}, response))
        self.assertTrue(MODULE.assertion_matches({"matcher": "regex", "pattern": r"does not establish\s+causality"}, response))

    def test_grade_case_enforces_expectations_and_hard_failures(self) -> None:
        case = {
            "id": "demo",
            "skill": "finance-top-journal-writing",
            "expectations": [
                {"id": "bounded", "matcher": "contains", "value": "association", "description": "bounded"}
            ],
            "hard_failures": [
                {"id": "invented", "matcher": "contains", "value": "proves causality", "description": "bad"}
            ],
        }
        passed = MODULE.grade_case(case, "This association is descriptive.")
        failed = MODULE.grade_case(case, "This proves causality.")
        self.assertTrue(passed["passed"])
        self.assertFalse(failed["passed"])

    def test_scaffold_creates_all_case_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "responses"
            self.assertEqual(MODULE.scaffold(ROOT, target), 0)
            behavior = json.loads((ROOT / "evals" / "cases" / "behavior-v1.json").read_text())
            for case in behavior["cases"]:
                case_dir = target / case["id"]
                self.assertTrue((case_dir / "task.md").is_file())
                self.assertTrue((case_dir / "response.md").is_file())
                task = (case_dir / "task.md").read_text(encoding="utf-8")
                self.assertIn(case["prompt"], task)
                self.assertNotIn("hard_failures", task)
            self.assertTrue((target / "run-metadata.json").is_file())

            # Scaffolding is idempotent and must not overwrite a completed response.
            first = target / behavior["cases"][0]["id"] / "response.md"
            first.write_text("completed answer\n", encoding="utf-8")
            self.assertEqual(MODULE.scaffold(ROOT, target), 0)
            self.assertEqual(first.read_text(encoding="utf-8"), "completed answer\n")

    def test_comment_only_scaffold_counts_as_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "responses"
            self.assertEqual(MODULE.scaffold(ROOT, target), 0)
            report = MODULE.build_report(ROOT, target)
            self.assertEqual(report["cases_graded"], 0)
            self.assertEqual(len(report["missing_responses"]), report["cases_expected"])
            self.assertFalse(report["passed"])

    def test_run_metadata_must_be_completed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "responses"
            self.assertEqual(MODULE.scaffold(ROOT, target), 0)
            _, errors = MODULE.load_run_metadata(target)
            self.assertTrue(errors)
            (target / "run-metadata.json").write_text(
                json.dumps(
                    {
                        "model": "test model",
                        "prompt_or_harness_version": "fixture-v1",
                        "run_date": "2026-08-13",
                        "notes": "isolated test run",
                    }
                ),
                encoding="utf-8",
            )
            payload, errors = MODULE.load_run_metadata(target)
            self.assertEqual(errors, [])
            self.assertEqual(payload["model"], "test model")

    def test_fixture_hard_failures_do_not_match_explicit_negation(self) -> None:
        behavior = json.loads((ROOT / "evals" / "cases" / "behavior-v1.json").read_text())
        cases = {case["id"]: case for case in behavior["cases"]}
        intermed = MODULE.grade_case(
            cases["behavior-intermed-credit-supply"],
            "Demand, selection, applications, approvals, interest rates, loan volume, and other lenders matter. "
            "The evidence does not identify a pure credit-supply contraction.",
        )
        self.assertEqual(intermed["hard_failures_triggered"], 0)
        theory = MODULE.grade_case(
            cases["behavior-theory-calibration-identification"],
            "Risk aversion is calibrated; the evidence does not show that risk aversion is identified. "
            "Targeted moments are not untargeted evidence. The 6% result is a model counterfactual.",
        )
        self.assertEqual(theory["hard_failures_triggered"], 0)


class GoldCaseTests(unittest.TestCase):
    def test_two_well_formed_gold_cases_per_skill(self) -> None:
        skills = {
            "finance-top-journal-writing",
            "finance-asset-pricing-writing",
            "finance-causal-empirical-writing",
            "finance-intermediation-markets-writing",
            "finance-theory-structural-writing",
        }
        root = ROOT / "evals" / "gold"
        self.assertEqual({path.name for path in root.iterdir() if path.is_dir()}, skills)
        for skill in skills:
            cases = [path for path in (root / skill).iterdir() if path.is_dir()]
            self.assertEqual(len(cases), 2)
            for case in cases:
                self.assertEqual(
                    {path.name for path in case.iterdir() if path.is_file()},
                    {"input.md", "expected-criteria.json", "reference-output.md"},
                )
                criteria = json.loads((case / "expected-criteria.json").read_text())
                self.assertEqual(criteria["case_id"], case.name)
                self.assertEqual(criteria["skill"], skill)
                self.assertIn("SYNTHETIC", (case / "input.md").read_text().upper())
                self.assertIn("SYNTHETIC", (case / "reference-output.md").read_text().upper())


if __name__ == "__main__":
    unittest.main()
