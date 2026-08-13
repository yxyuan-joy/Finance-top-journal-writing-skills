#!/usr/bin/env python3
"""Inventory repeated manuscript numbers and claim markers across text files.

This is a conservative review aid. It does not decide whether two values are
comparable or which artifact is authoritative.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path


NUMBER_RE = re.compile(
    r"(?<![A-Za-z])[-+]?\d[\d,]*(?:\.\d+)?(?:\s?(?:%|bp|bps|basis points?|"
    r"percentage points?|pp|million|billion|trillion))?",
    re.I,
)
LABELED_RE = re.compile(
    r"\b(?P<label>N|observations?|sample size|mean|baseline|coefficient|estimate|"
    r"alpha|return|effect|SE|standard error|CI|confidence interval)\b"
    r"[^\n.;:]{0,55}?(?P<value>[-+]?\d[\d,]*(?:\.\d+)?(?:\s?(?:%|bp|bps|"
    r"basis points?|percentage points?|pp|million|billion|trillion))?)",
    re.I,
)
CLAIM_RE = re.compile(
    r"\b(?P<claim>caus\w*|predict\w*|associat\w*|counterfactual|welfare|"
    r"mechanism|first study|only study)\b",
    re.I,
)


@dataclass(frozen=True)
class Occurrence:
    file: str
    line: int
    value: str
    context: str


def context(text: str, start: int, end: int, limit: int = 180) -> str:
    left = max(text.rfind("\n", 0, start), text.rfind(".", 0, start)) + 1
    right_candidates = [pos for pos in (text.find("\n", end), text.find(".", end)) if pos >= 0]
    right = min(right_candidates) + 1 if right_candidates else len(text)
    value = " ".join(text[left:right].split())
    return value if len(value) <= limit else value[: limit - 1] + "…"


def inspect(paths: list[Path]) -> dict[str, object]:
    labels: dict[str, list[Occurrence]] = defaultdict(list)
    claims: dict[str, list[Occurrence]] = defaultdict(list)
    number_inventory: dict[str, list[Occurrence]] = defaultdict(list)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for match in LABELED_RE.finditer(text):
            label = re.sub(r"\s+", " ", match.group("label").lower())
            labels[label].append(
                Occurrence(str(path), text.count("\n", 0, match.start()) + 1, match.group("value"), context(text, match.start(), match.end()))
            )
        for match in CLAIM_RE.finditer(text):
            claim = match.group("claim").lower()
            claims[claim].append(
                Occurrence(str(path), text.count("\n", 0, match.start()) + 1, match.group(), context(text, match.start(), match.end()))
            )
        for match in NUMBER_RE.finditer(text):
            value = re.sub(r"\s+", " ", match.group().strip().lower())
            number_inventory[value].append(
                Occurrence(str(path), text.count("\n", 0, match.start()) + 1, match.group(), context(text, match.start(), match.end()))
            )
    return {
        "files": [str(path) for path in paths],
        "labeled_values": {key: [asdict(item) for item in value] for key, value in sorted(labels.items())},
        "claim_markers": {key: [asdict(item) for item in value] for key, value in sorted(claims.items())},
        "repeated_numbers": {
            key: [asdict(item) for item in value]
            for key, value in sorted(number_inventory.items())
            if len(value) > 1
        },
        "review_note": "Different values are not automatically conflicts; compare definitions, samples, units, and specifications before reconciling.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="UTF-8 Markdown/text sections to compare")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a compact text inventory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    missing = [path for path in args.files if not path.is_file()]
    if missing:
        raise SystemExit("missing file(s): " + ", ".join(str(path) for path in missing))
    report = inspect(args.files)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0
    print("Files:")
    for path in report["files"]:
        print(f"- {path}")
    print("\nLabeled values:")
    for label, rows in report["labeled_values"].items():
        values = sorted({row["value"] for row in rows})
        print(f"- {label}: {', '.join(values)}")
        for row in rows:
            print(f"  {row['file']}:{row['line']}  {row['context']}")
    print("\nClaim markers:")
    for claim, rows in report["claim_markers"].items():
        locations = ", ".join(f"{row['file']}:{row['line']}" for row in rows)
        print(f"- {claim}: {locations}")
    print("\nReview note: " + report["review_note"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
