from __future__ import annotations

import importlib.util
import sys
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


if __name__ == "__main__":
    unittest.main()
