#!/usr/bin/env python3
"""Build compact, self-contained evidence references for the five skills.

The source CSVs contain bibliographic metadata and original synthesis only.
This script never reads or publishes article prose.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import TypedDict


ROOT = Path(__file__).resolve().parents[1]
class SetConfig(TypedDict):
    count: int
    skill: str
    label: str


SET_CONFIG: dict[str, SetConfig] = {
    "general-writing": {
        "count": 50,
        "skill": "finance-top-journal-writing",
        "label": "General writing",
    },
    "asset-pricing": {
        "count": 50,
        "skill": "finance-asset-pricing-writing",
        "label": "Asset pricing",
    },
    "causal-empirical": {
        "count": 60,
        "skill": "finance-causal-empirical-writing",
        "label": "Causal empirical finance",
    },
    "intermediation-markets": {
        "count": 60,
        "skill": "finance-intermediation-markets-writing",
        "label": "Intermediation and markets",
    },
    "theory-structural": {
        "count": 50,
        "skill": "finance-theory-structural-writing",
        "label": "Theory and structural finance",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail instead of writing stale files.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def compact(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_reference(set_id: str, config: SetConfig, rows: list[dict[str, str]]) -> str:
    journal_counts = Counter(row["journal"] for row in rows)
    subtype_counts = Counter(row["subtype"] for row in rows)
    lines = [
        "# Evidence Basis",
        "",
        "## Contents",
        "",
        "- [Use this reference](#use-this-reference)",
        "- [Portfolio](#portfolio)",
        "- [Subtype coverage](#subtype-coverage)",
        "- [Exemplar catalog](#exemplar-catalog)",
        "- [Interpretation boundary](#interpretation-boundary)",
        "",
        "## Use this reference",
        "",
        f"This skill is informed by an independently curated {len(rows)}-paper {config['label'].lower()} portfolio from the 2020–2025 JF/JFE/RFS strict ordinary-submission census. Use the catalog to choose a functionally similar architecture or to audit provenance. Do not copy sentences, paper length, section counts, or topic-specific claims.",
        "",
        "Selection required direct reading of the abstract, full introduction, the named body sections, and conclusion. Title and heading screens were discovery aids only. Each record states both a transferable writing function and a transfer limit.",
        "",
        "## Portfolio",
        "",
        "| Journal | Papers |",
        "|---|---:|",
    ]
    for journal in ("JF", "JFE", "RFS"):
        lines.append(f"| {journal} | {journal_counts[journal]} |")
    lines.extend([f"| Total | {len(rows)} |", "", "## Subtype coverage", ""])
    for subtype, count in sorted(subtype_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- `{subtype}`: {count}")
    lines.extend(
        [
            "",
            "## Exemplar catalog",
            "",
            "| Journal/year | DOI | Title | Tier | Writing function | Transfer limit |",
            "|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            "| {journal} {year} | `{doi}` | {title} | {tier} | {function} | {limit} |".format(
                journal=compact(row["journal"]),
                year=compact(row["canonical_year"]),
                doi=compact(row["doi"]),
                title=compact(row["title"]),
                tier=compact(row["selection_tier"]),
                function=compact(row["teaching_function"]),
                limit=compact(row["transfer_limit"]),
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "This is a teaching portfolio, not a quality ranking, training corpus, citation recommendation, or claim that the journals require these structures. `section_specific` and `supporting` mean only the named sections/functions are recommended as anchors. Current submission rules must be checked against the journals' live official pages.",
            "",
        ]
    )
    return "\n".join(lines)


def build_overlap(all_rows: dict[str, list[dict[str, str]]]) -> dict[str, object]:
    sets = {name: {row["doi"].lower() for row in rows} for name, rows in all_rows.items()}
    all_dois = set().union(*sets.values())
    matrix: dict[str, dict[str, dict[str, float | int]]] = {}
    for left, left_dois in sets.items():
        matrix[left] = {}
        for right, right_dois in sets.items():
            intersection = len(left_dois & right_dois)
            union_count = len(left_dois | right_dois)
            matrix[left][right] = {
                "intersection": intersection,
                "jaccard": round(intersection / union_count, 4) if union_count else 0,
            }
    general = sets["general-writing"]
    specialist_independence = {
        name: {
            "papers": len(dois),
            "overlap_with_general": len(dois & general),
            "outside_general": len(dois - general),
        }
        for name, dois in sets.items()
        if name != "general-writing"
    }
    return {
        "method": "doi_set_overlap",
        "memberships": sum(len(dois) for dois in sets.values()),
        "unique_papers": len(all_dois),
        "sets": {name: len(dois) for name, dois in sets.items()},
        "specialist_independence": specialist_independence,
        "pairwise": matrix,
    }


def main() -> int:
    args = parse_args()
    all_rows: dict[str, list[dict[str, str]]] = {}
    outputs: dict[Path, str] = {}
    for set_id, config in SET_CONFIG.items():
        csv_path = ROOT / "evidence" / "sets" / f"{set_id}.csv"
        rows = read_rows(csv_path)
        if len(rows) != config["count"]:
            raise ValueError(
                f"{csv_path.relative_to(ROOT)}: expected {config['count']} rows, found {len(rows)}"
            )
        all_rows[set_id] = rows
        output_path = ROOT / "skills" / config["skill"] / "references" / "evidence-basis.md"
        outputs[output_path] = render_reference(set_id, config, rows)

    overlap_path = ROOT / "evidence" / "sets" / "overlap-matrix.json"
    outputs[overlap_path] = json.dumps(build_overlap(all_rows), indent=2, ensure_ascii=False) + "\n"

    stale = []
    for path, content in outputs.items():
        if path.exists() and path.read_text(encoding="utf-8") == content:
            continue
        stale.append(path)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if args.check and stale:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT)}")
        return 1
    print(json.dumps({"generated": len(stale), "sets": {k: len(v) for k, v in all_rows.items()}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
