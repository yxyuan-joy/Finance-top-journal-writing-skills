from __future__ import annotations

import csv
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CuratedEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with (ROOT / "evidence" / "curated-exemplars.csv").open(
            encoding="utf-8", newline=""
        ) as handle:
            cls.rows = list(csv.DictReader(handle))

    def test_balanced_across_journals(self) -> None:
        self.assertEqual(Counter(row["journal"] for row in self.rows), {"JF": 12, "JFE": 12, "RFS": 12})

    def test_unique_dois(self) -> None:
        dois = [row["doi"].lower() for row in self.rows]
        self.assertEqual(len(dois), len(set(dois)))

    def test_every_record_has_function_and_limit(self) -> None:
        for row in self.rows:
            self.assertTrue(row["teaching_function"].strip(), row["doi"])
            self.assertTrue(row["transfer_limit"].strip(), row["doi"])

    def test_ocr_correction_and_print_boundary(self) -> None:
        by_doi = {row["doi"].lower(): row for row in self.rows}
        self.assertTrue(by_doi["10.1093/rfs/hhaf045"]["title"].startswith("Π-CAPM"))
        self.assertNotIn("10.1093/rfs/hhaf080", by_doi)
        self.assertIn("10.1093/rfs/hhaa119", by_doi)


if __name__ == "__main__":
    unittest.main()
