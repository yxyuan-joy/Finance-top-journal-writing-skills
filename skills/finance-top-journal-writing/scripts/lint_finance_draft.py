#!/usr/bin/env python3
"""Conservative static checks for finance-manuscript drafts.

The script surfaces review prompts. It does not grade scientific validity and
does not treat corpus-derived length or heading patterns as submission rules.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


PLACEHOLDER_PATTERNS = (
    re.compile(r"\[(?:[^\]]*?(?:needed|todo|tbd|insert|verify|citation)[^\]]*?)\]", re.I),
    re.compile(r"\b(?:TODO|TBD|FIXME|XXX)\b", re.I),
    re.compile(r"\?\?+"),
)
CAUSAL_PATTERN = re.compile(
    r"\b(?:caus(?:e|es|ed|al)|effect of|impact of|leads? to|drives?|"
    r"results? in|increases?|decreases?|reduces?|raises?)\b",
    re.I,
)
NOVELTY_PATTERN = re.compile(
    r"\b(?:the first|first paper|first study|only paper|only study|"
    r"unprecedented|never before|no prior (?:paper|study|work))\b",
    re.I,
)
SIGNIFICANCE_PATTERN = re.compile(r"\bstatistically significant\b", re.I)
NUMBER_PATTERN = re.compile(r"(?:\d|%|basis point|percentage point|standard deviation)", re.I)
ROBUST_PATTERN = re.compile(r"\b(?:robust to|remains robust|variety of robustness)\b", re.I)
THREAT_PATTERN = re.compile(
    r"\b(?:confound|selection|anticipat|pre-trend|measurement|spillover|"
    r"inference|cluster|functional form|alternative explanation|external validity)\w*\b",
    re.I,
)
HEADING_PATTERN = re.compile(r"(?m)^(#{1,6})\s+(.+?)\s*$")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[])|\n+")


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    line: int
    message: str
    excerpt: str


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def excerpt(value: str, limit: int = 180) -> str:
    clean = " ".join(value.split())
    return clean if len(clean) <= limit else clean[: limit - 1] + "…"


def sentence_offsets(text: str):
    cursor = 0
    for part in SENTENCE_SPLIT.split(text):
        stripped = part.strip()
        if not stripped:
            cursor += len(part)
            continue
        start = text.find(stripped, cursor)
        if start < 0:
            start = cursor
        yield stripped, start
        cursor = start + len(stripped)


def lint(text: str, journal: str | None = None) -> list[Finding]:
    findings: list[Finding] = []

    for pattern in PLACEHOLDER_PATTERNS:
        for match in pattern.finditer(text):
            findings.append(
                Finding(
                    "placeholder",
                    "major",
                    line_number(text, match.start()),
                    "Resolve or explicitly disclose this evidence placeholder before submission.",
                    excerpt(match.group()),
                )
            )

    for sentence, offset in sentence_offsets(text):
        if CAUSAL_PATTERN.search(sentence):
            findings.append(
                Finding(
                    "causal-language-review",
                    "review",
                    line_number(text, offset),
                    "Confirm that the design and maintained assumptions support this causal wording.",
                    excerpt(sentence),
                )
            )
        if NOVELTY_PATTERN.search(sentence):
            findings.append(
                Finding(
                    "novelty-verification",
                    "major",
                    line_number(text, offset),
                    "Verify this absolute novelty claim against the closest literature.",
                    excerpt(sentence),
                )
            )
        if SIGNIFICANCE_PATTERN.search(sentence) and not NUMBER_PATTERN.search(sentence):
            findings.append(
                Finding(
                    "significance-without-magnitude",
                    "review",
                    line_number(text, offset),
                    "Add magnitude, units, and a meaningful benchmark if this is a central result.",
                    excerpt(sentence),
                )
            )
        if ROBUST_PATTERN.search(sentence) and not THREAT_PATTERN.search(sentence):
            findings.append(
                Finding(
                    "robustness-without-threat",
                    "review",
                    line_number(text, offset),
                    "Name the threat this robustness statement addresses and its residual limit.",
                    excerpt(sentence),
                )
            )

    headings = [match.group(2).strip() for match in HEADING_PATTERN.finditer(text)]
    lower_headings = [heading.lower() for heading in headings]
    journal_key = journal.upper() if journal else None
    if journal_key == "JFE" and not any("introduction" in h for h in lower_headings):
        findings.append(
            Finding(
                "jfe-introduction-heading",
                "review",
                1,
                "Recent JFE production normally uses an explicit numbered Introduction; check the live template.",
                "",
            )
        )
    if journal_key in {"JF", "RFS"} and any(h in {"introduction", "1. introduction", "i. introduction"} for h in lower_headings):
        findings.append(
            Finding(
                "journal-heading-review",
                "review",
                1,
                f"Recent {journal_key} production often leaves the introduction unheaded; follow the live template.",
                "",
            )
        )

    return sorted(findings, key=lambda item: (item.line, item.code, item.excerpt))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path, help="UTF-8 Markdown or text manuscript")
    parser.add_argument("--journal", choices=("JF", "JFE", "RFS"))
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument(
        "--fail-on-major",
        action="store_true",
        help="Exit 1 when a major finding is present; otherwise findings exit 0",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.draft.read_text(encoding="utf-8")
    findings = lint(text, args.journal)
    if args.json:
        print(json.dumps([asdict(item) for item in findings], indent=2, ensure_ascii=False))
    elif not findings:
        print("No heuristic findings. This is not a scientific-validity guarantee.")
    else:
        for item in findings:
            location = f"line {item.line}" if item.line else "document"
            print(f"[{item.severity}] {item.code} ({location}): {item.message}")
            if item.excerpt:
                print(f"  {item.excerpt}")
        print(f"\n{len(findings)} finding(s). Review prompts are not automatic errors.")
    if args.fail_on_major and any(item.severity == "major" for item in findings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
