from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "skills"
    / "finance-top-journal-writing"
    / "scripts"
    / "lint_finance_draft.py"
)
CONSISTENCY_PATH = (
    ROOT
    / "skills"
    / "finance-top-journal-writing"
    / "scripts"
    / "check_manuscript_consistency.py"
)
SPEC = importlib.util.spec_from_file_location("lint_finance_draft", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class LintFinanceDraftTests(unittest.TestCase):
    def codes(self, text: str, journal: str | None = None) -> set[str]:
        return {finding.code for finding in MODULE.lint(text, journal)}

    def test_flags_placeholder_and_novelty(self) -> None:
        codes = self.codes("We are the first study to show [EFFECT SIZE NEEDED].")
        self.assertIn("placeholder", codes)
        self.assertIn("novelty-verification", codes)

    def test_flags_causal_language_for_review(self) -> None:
        self.assertIn(
            "causal-language-review",
            self.codes("The reform increases bank lending by 4 percentage points."),
        )

    def test_does_not_flag_explicit_causal_boundary(self) -> None:
        self.assertNotIn(
            "causal-language-review",
            self.codes("This association does not establish a causal effect."),
        )
        self.assertNotIn(
            "causal-language-review",
            self.codes("We do not identify a causal impact."),
        )

    def test_does_not_treat_ordinal_first_as_novelty(self) -> None:
        self.assertNotIn(
            "novelty-verification",
            self.codes("The response is concentrated in the first six event months."),
        )

    def test_flags_significance_without_magnitude(self) -> None:
        self.assertIn(
            "significance-without-magnitude",
            self.codes("The estimate is statistically significant."),
        )

    def test_does_not_flag_significance_with_magnitude(self) -> None:
        self.assertNotIn(
            "significance-without-magnitude",
            self.codes("The 4.2 percentage-point estimate is statistically significant."),
        )

    def test_journal_heading_prompt(self) -> None:
        self.assertIn("jfe-introduction-heading", self.codes("# Results\nText.", "JFE"))
        self.assertIn(
            "journal-heading-review",
            self.codes("# 1. Introduction\nText.", "RFS"),
        )


class ConsistencyInventoryTests(unittest.TestCase):
    def test_inventories_values_and_claim_markers(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            first = Path(temp_dir) / "abstract.md"
            second = Path(temp_dir) / "results.md"
            first.write_text(
                "The estimate is 4.2 percentage points and the sample size is 1,200. "
                "We predict defaults.",
                encoding="utf-8",
            )
            second.write_text(
                "The coefficient is 5.1 percentage points with 1,050 observations. "
                "This association is not a causal effect.",
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(CONSISTENCY_PATH), "--json", str(first), str(second)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            payload = json.loads(completed.stdout)
            self.assertIn("sample size", payload["labeled_values"])
            self.assertIn("coefficient", payload["labeled_values"])
            self.assertTrue(any(key.startswith("predict") for key in payload["claim_markers"]))
            self.assertTrue(any(key.startswith("caus") for key in payload["claim_markers"]))

    def test_missing_file_exits_nonzero(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(CONSISTENCY_PATH), "/definitely/missing/manuscript.md"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(completed.returncode, 0)


if __name__ == "__main__":
    unittest.main()
