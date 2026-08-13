from __future__ import annotations

import csv
import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "general-writing": 50,
    "asset-pricing": 50,
    "causal-empirical": 60,
    "intermediation-markets": 60,
    "theory-structural": 50,
}
FIELDS = {
    "journal",
    "canonical_year",
    "doi",
    "title",
    "subtype",
    "selection_tier",
    "selected_sections",
    "teaching_function",
    "transfer_limit",
    "metadata_note",
}


class CuratedEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sets: dict[str, list[dict[str, str]]] = {}
        for name in EXPECTED:
            with (ROOT / "evidence" / "sets" / f"{name}.csv").open(
                encoding="utf-8", newline=""
            ) as handle:
                cls.sets[name] = list(csv.DictReader(handle))

    def test_exact_portfolio_sizes_and_schema(self) -> None:
        for name, expected in EXPECTED.items():
            rows = self.sets[name]
            self.assertEqual(len(rows), expected, name)
            self.assertEqual(set(rows[0]), FIELDS, name)

    def test_unique_dois_within_each_portfolio(self) -> None:
        for name, rows in self.sets.items():
            dois = [row["doi"].lower() for row in rows]
            self.assertEqual(len(dois), len(set(dois)), name)

    def test_every_record_is_actionable_and_bounded(self) -> None:
        for name, rows in self.sets.items():
            for row in rows:
                self.assertIn(row["journal"], {"JF", "JFE", "RFS"}, (name, row["doi"]))
                self.assertIn(
                    row["selection_tier"],
                    {"core", "section_specific", "supporting"},
                    (name, row["doi"]),
                )
                for field in (
                    "canonical_year",
                    "doi",
                    "title",
                    "subtype",
                    "selected_sections",
                    "teaching_function",
                    "transfer_limit",
                ):
                    self.assertTrue(row[field].strip(), (name, row["doi"], field))

    def test_general_portfolio_balances_journals(self) -> None:
        counts = Counter(row["journal"] for row in self.sets["general-writing"])
        self.assertLessEqual(max(counts.values()) - min(counts.values()), 1)

    def test_specialists_are_independent_not_general_subsets(self) -> None:
        general = {row["doi"].lower() for row in self.sets["general-writing"]}
        for name, rows in self.sets.items():
            if name == "general-writing":
                continue
            dois = {row["doi"].lower() for row in rows}
            self.assertGreaterEqual(len(dois - general), 25, name)

    def test_public_metadata_matches_census(self) -> None:
        with (ROOT / "evidence" / "corpus-census" / "article-index.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            census = {row["doi"].lower(): row for row in csv.DictReader(handle)}
        for name, rows in self.sets.items():
            for row in rows:
                source = census[row["doi"].lower()]
                self.assertEqual(row["journal"], source["journal"], (name, row["doi"]))
                self.assertEqual(row["canonical_year"], source["final_publication_year"], (name, row["doi"]))
                if not row["metadata_note"].strip():
                    self.assertEqual(row["title"], source["title"], (name, row["doi"]))

    def test_generated_overlap_summary_agrees(self) -> None:
        summary = json.loads(
            (ROOT / "evidence" / "sets" / "overlap-matrix.json").read_text(encoding="utf-8")
        )
        self.assertEqual(summary["sets"], EXPECTED)
        memberships = sum(len(rows) for rows in self.sets.values())
        unique_papers = len(
            {row["doi"].lower() for rows in self.sets.values() for row in rows}
        )
        self.assertEqual(summary["memberships"], memberships)
        self.assertEqual(summary["unique_papers"], unique_papers)

    def test_held_out_is_independent_within_each_portfolio(self) -> None:
        with (ROOT / "evidence" / "sets" / "held-out.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            held = list(csv.DictReader(handle))
        counts = Counter(row["evidence_set"] for row in held)
        held_dois_all = [row["doi"].lower() for row in held]
        selected_anywhere = {
            row["doi"].lower() for rows in self.sets.values() for row in rows
        }
        self.assertEqual(len(held_dois_all), len(set(held_dois_all)))
        self.assertTrue(selected_anywhere.isdisjoint(held_dois_all))
        for name, rows in self.sets.items():
            selected = {row["doi"].lower() for row in rows}
            held_dois = {
                row["doi"].lower() for row in held if row["evidence_set"] == name
            }
            self.assertGreaterEqual(counts[name], 8, name)
            self.assertTrue(selected.isdisjoint(held_dois), name)

    def test_ocr_correction_remains_documented(self) -> None:
        all_rows = {
            row["doi"].lower(): row
            for rows in self.sets.values()
            for row in rows
        }
        if "10.1093/rfs/hhaf045" in all_rows:
            row = all_rows["10.1093/rfs/hhaf045"]
            self.assertTrue(row["title"].startswith("Π-CAPM"))
            self.assertTrue(row["metadata_note"].strip())


if __name__ == "__main__":
    unittest.main()
