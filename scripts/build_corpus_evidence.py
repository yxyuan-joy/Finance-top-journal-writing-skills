#!/usr/bin/env python3
"""Build public, aggregate writing-structure evidence from the local strict corpus.

The script performs a census, not a quality ranking. It exports bibliographic
metadata and structural flags only; it never copies article prose or local
paths into the repository. Human curation is a separate, documented stage.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


HEADING_RE = re.compile(r"(?m)^\s*#{1,6}\s+(.+?)\s*$")
WORD_RE = re.compile(r"\b[A-Za-z]+(?:[-'][A-Za-z]+)*\b")
LEADING_NUMBER_RE = re.compile(
    r"^\s*(?:(?:[IVXLCDM]+|\d+(?:\.\d+)*)[.)]?|[A-Z][.)])\s+",
    re.I,
)

CATEGORY_PATTERNS = {
    "abstract": re.compile(r"^abstract$", re.I),
    "introduction": re.compile(r"^introduction$", re.I),
    "literature": re.compile(r"(?:literature|related work|prior research)", re.I),
    "data_sample": re.compile(r"(?:data|sample|variable|measurement)", re.I),
    "institution_background": re.compile(
        r"(?:institutional|institution|background|setting|market structure)", re.I
    ),
    "method_identification": re.compile(
        r"(?:method|empirical strateg|identification|research design|estimation)", re.I
    ),
    "model_framework": re.compile(r"(?:model|framework|theory|equilibrium)", re.I),
    "result": re.compile(r"(?:result|finding|evidence|effect|analysis|test)", re.I),
    "robustness_extension": re.compile(
        r"(?:robust|additional|extension|sensitivity|placebo|alternative)", re.I
    ),
    "mechanism_channel": re.compile(r"(?:mechanism|channel|heterogene|why does|explanation)", re.I),
    "conclusion": re.compile(r"(?:conclusion|concluding|summary and conclusion|discussion)", re.I),
    "appendix_support": re.compile(r"(?:appendix|supporting information|supplement)", re.I),
    "references": re.compile(r"^(?:references|bibliography)$", re.I),
}

PUBLIC_FIELDS = [
    "article_id",
    "journal",
    "final_publication_year",
    "source_folder_year",
    "title",
    "doi",
    "source_integrity_status",
    "md_available",
    "word_count",
    "heading_count",
    *[f"has_{name}_heading" for name in CATEGORY_PATTERNS],
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict-csv", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--start-year", type=int, default=2020)
    parser.add_argument("--end-year", type=int, default=2025)
    return parser.parse_args()


def truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y"}


def normalize_heading(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).strip()
    value = LEADING_NUMBER_RE.sub("", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" .:")


def stable_article_id(row: dict[str, str]) -> str:
    key = "|".join(
        [row.get("journal", ""), row.get("publication_year", ""), row.get("doi", ""), row.get("title", "")]
    )
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def find_markdown(source_pdf: str) -> Path | None:
    if not source_pdf:
        return None
    pdf = Path(source_pdf)
    exact_name = pdf.name.replace("_origin.pdf", ".md")
    exact = pdf.with_name(exact_name)
    if exact.exists():
        return exact
    candidates = sorted(pdf.parent.glob("*.md")) if pdf.parent.exists() else []
    return candidates[0] if len(candidates) == 1 else None


def structural_record(row: dict[str, str]) -> tuple[dict[str, object], list[str]]:
    md_path = find_markdown(row.get("source_pdf_path", ""))
    text = md_path.read_text(encoding="utf-8", errors="replace") if md_path else ""
    raw_headings = HEADING_RE.findall(text)
    headings = [normalize_heading(item) for item in raw_headings]
    flags = {
        f"has_{name}_heading": any(pattern.search(heading) for heading in headings)
        for name, pattern in CATEGORY_PATTERNS.items()
    }
    record: dict[str, object] = {
        "article_id": stable_article_id(row),
        "journal": row.get("journal", ""),
        "final_publication_year": row.get("publication_year", ""),
        "source_folder_year": row.get("source_folder_year", ""),
        "title": row.get("title", ""),
        "doi": row.get("analysis_doi") or row.get("doi", ""),
        "source_integrity_status": row.get("source_integrity_status", ""),
        "md_available": bool(md_path),
        "word_count": len(WORD_RE.findall(text)),
        "heading_count": len(headings),
        **flags,
    }
    return record, headings


def load_rows(path: Path, start_year: int, end_year: int) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    selected = []
    for row in rows:
        year = row.get("publication_year", "")
        if not year.isdigit() or not start_year <= int(year) <= end_year:
            continue
        if "main_standard_original_flag" in row and not truthy(row.get("main_standard_original_flag")):
            continue
        selected.append(row)
    return selected


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def build_summary(records: list[dict[str, object]], start_year: int, end_year: int) -> dict[str, object]:
    by_journal: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        by_journal[str(record["journal"])].append(record)

    def summarize(items: list[dict[str, object]]) -> dict[str, object]:
        n = len(items)
        available = sum(bool(item["md_available"]) for item in items)
        flags = {}
        for name in CATEGORY_PATTERNS:
            key = f"has_{name}_heading"
            count = sum(bool(item[key]) for item in items)
            flags[name] = {"count": count, "share": round(count / n, 4) if n else None}
        return {
            "papers": n,
            "md_available": available,
            "md_coverage": round(available / n, 4) if n else None,
            "by_final_year": dict(sorted(Counter(str(item["final_publication_year"]) for item in items).items())),
            "heading_flags": flags,
        }

    return {
        "method": "full_census_of_strict_standard_original_sample",
        "years": [start_year, end_year],
        "papers": len(records),
        "journals": {journal: summarize(items) for journal, items in sorted(by_journal.items())},
        "limitations": [
            "Heading flags describe MinerU Markdown structure, not writing quality.",
            "Unheaded abstracts and introductions require journal-aware interpretation.",
            "Source-folder year may differ from final publication year.",
            "Human-curated exemplars are selected in a separate documented stage.",
        ],
    }


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    source_rows = load_rows(args.strict_csv, args.start_year, args.end_year)
    records: list[dict[str, object]] = []
    heading_counts: dict[str, Counter[str]] = defaultdict(Counter)

    for row in source_rows:
        record, headings = structural_record(row)
        records.append(record)
        heading_counts[str(record["journal"])].update(heading.lower() for heading in headings if heading)

    records.sort(key=lambda item: (item["journal"], int(str(item["final_publication_year"])), str(item["title"])))
    write_csv(args.output_dir / "article-index.csv", records, PUBLIC_FIELDS)

    heading_rows: list[dict[str, object]] = []
    for journal, counter in sorted(heading_counts.items()):
        for heading, count in counter.most_common():
            # Unique headings mostly reproduce article-specific titles or
            # table labels and add no aggregate structural evidence.
            if count < 2 or len(heading) > 120:
                continue
            heading_rows.append({"journal": journal, "normalized_heading": heading, "count": count})
    write_csv(
        args.output_dir / "heading-frequencies.csv",
        heading_rows,
        ["journal", "normalized_heading", "count"],
    )

    summary = build_summary(records, args.start_year, args.end_year)
    (args.output_dir / "aggregate-patterns.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"papers": len(records), "output_dir": str(args.output_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
