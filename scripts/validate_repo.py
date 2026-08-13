#!/usr/bin/env python3
"""Validate the repository's five self-contained Agent Skills."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from run_skill_evals import build_report as build_eval_report


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EXPECTED_SKILLS = {
    "finance-top-journal-writing",
    "finance-asset-pricing-writing",
    "finance-causal-empirical-writing",
    "finance-intermediation-markets-writing",
    "finance-theory-structural-writing",
}
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
TODO_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[TODO", re.I)
NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")
EVIDENCE_SETS = {
    "general-writing": 50,
    "asset-pricing": 50,
    "causal-empirical": 60,
    "intermediation-markets": 60,
    "theory-structural": 50,
}
EVIDENCE_FIELDS = {
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


def parse_simple_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")
    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip():
            continue
        if ":" not in raw_line:
            raise ValueError(f"malformed frontmatter line: {raw_line}")
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in values:
            raise ValueError(f"duplicate frontmatter key: {key}")
        values[key] = value
    return values, text[match.end() :]


def validate_openai_yaml(path: Path, skill_name: str) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: missing"]
    text = path.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s+{key}:\s+\".+\"\s*$", text, re.M):
            errors.append(f"{path.relative_to(ROOT)}: missing quoted interface.{key}")
    prompt_match = re.search(r'^\s+default_prompt:\s+"(.+)"\s*$', text, re.M)
    if prompt_match and f"${skill_name}" not in prompt_match.group(1):
        errors.append(f"{path.relative_to(ROOT)}: default_prompt must mention ${skill_name}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_name = skill_dir.name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]
    text = skill_file.read_text(encoding="utf-8")
    try:
        frontmatter, body = parse_simple_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_file.relative_to(ROOT)}: {exc}"]

    if set(frontmatter) != {"name", "description"}:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: frontmatter keys must be exactly name, description"
        )
    if frontmatter.get("name") != skill_name:
        errors.append(f"{skill_file.relative_to(ROOT)}: name must match folder")
    if not NAME_RE.fullmatch(skill_name):
        errors.append(f"{skill_file.relative_to(ROOT)}: invalid skill name")
    description = frontmatter.get("description", "")
    if len(description) < 120:
        errors.append(f"{skill_file.relative_to(ROOT)}: description is too vague")
    if not all(journal in description for journal in ("Journal of Finance", "Journal of Financial Economics", "Review of Financial Studies")):
        errors.append(f"{skill_file.relative_to(ROOT)}: description must cover JF, JFE, and RFS")
    if len(text.splitlines()) > 500:
        errors.append(f"{skill_file.relative_to(ROOT)}: SKILL.md exceeds 500 lines")
    if TODO_RE.search(text):
        errors.append(f"{skill_file.relative_to(ROOT)}: contains unfinished TODO marker")
    if not body.strip():
        errors.append(f"{skill_file.relative_to(ROOT)}: empty body")

    for link in LINK_RE.findall(body):
        if "://" in link or link.startswith("#"):
            continue
        target = (skill_dir / link.split("#", 1)[0]).resolve()
        try:
            target.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"{skill_file.relative_to(ROOT)}: link escapes skill folder: {link}")
            continue
        if not target.exists():
            errors.append(f"{skill_file.relative_to(ROOT)}: broken link: {link}")

    if any(path.name.lower() == "readme.md" for path in skill_dir.rglob("*.md")):
        errors.append(f"{skill_dir.relative_to(ROOT)}: per-skill README is not allowed")
    errors.extend(validate_openai_yaml(skill_dir / "agents" / "openai.yaml", skill_name))
    return errors


def validate_local_links(path: Path) -> list[str]:
    """Check repository Markdown links without following external URLs."""

    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for link in LINK_RE.findall(text):
        clean = link.strip().strip("<>").split("#", 1)[0]
        if not clean or "://" in clean or clean.startswith("mailto:"):
            continue
        target = (path.parent / clean).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {link}")
            continue
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {link}")
    return errors


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_evidence_sets() -> list[str]:
    errors: list[str] = []
    census_path = ROOT / "evidence" / "corpus-census" / "article-index.csv"
    if not census_path.exists():
        return ["evidence/corpus-census/article-index.csv: missing"]
    census = {row["doi"].lower(): row for row in load_csv(census_path)}
    portfolios: dict[str, set[str]] = {}

    for set_name, expected_count in EVIDENCE_SETS.items():
        path = ROOT / "evidence" / "sets" / f"{set_name}.csv"
        if not path.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing")
            continue
        rows = load_csv(path)
        if len(rows) != expected_count:
            errors.append(
                f"{path.relative_to(ROOT)}: expected {expected_count} papers; found {len(rows)}"
            )
        if rows and set(rows[0]) != EVIDENCE_FIELDS:
            errors.append(f"{path.relative_to(ROOT)}: unexpected schema")
        dois = [row.get("doi", "").lower() for row in rows]
        portfolios[set_name] = set(dois)
        if len(dois) != len(set(dois)):
            errors.append(f"{path.relative_to(ROOT)}: duplicate DOI")
        for row_number, row in enumerate(rows, start=2):
            doi = row.get("doi", "").lower()
            if row.get("selection_tier") not in {"core", "section_specific", "supporting"}:
                errors.append(f"{path.relative_to(ROOT)}:{row_number}: invalid selection_tier")
            for field in EVIDENCE_FIELDS - {"metadata_note"}:
                if not row.get(field, "").strip():
                    errors.append(f"{path.relative_to(ROOT)}:{row_number}: missing {field}")
            source = census.get(doi)
            if source is None:
                errors.append(f"{path.relative_to(ROOT)}:{row_number}: DOI absent from census")
                continue
            for left, right in (
                ("journal", "journal"),
                ("canonical_year", "final_publication_year"),
            ):
                if row.get(left) != source.get(right):
                    errors.append(
                        f"{path.relative_to(ROOT)}:{row_number}: {left} disagrees with census"
                    )
            if not row.get("metadata_note", "").strip() and row.get("title") != source.get("title"):
                errors.append(
                    f"{path.relative_to(ROOT)}:{row_number}: title disagrees with census without metadata_note"
                )

        if set_name == "general-writing" and rows:
            counts = Counter(row["journal"] for row in rows)
            if set(counts) != {"JF", "JFE", "RFS"} or max(counts.values()) - min(counts.values()) > 1:
                errors.append(f"{path.relative_to(ROOT)}: general set must balance the three journals")

    general = portfolios.get("general-writing", set())
    if general:
        for set_name, dois in portfolios.items():
            if set_name == "general-writing":
                continue
            outside = len(dois - general)
            if outside < 25:
                errors.append(
                    f"evidence/sets/{set_name}.csv: only {outside} papers outside general set; expected >=25"
                )

    for set_name in EVIDENCE_SETS:
        skill_name = {
            "general-writing": "finance-top-journal-writing",
            "asset-pricing": "finance-asset-pricing-writing",
            "causal-empirical": "finance-causal-empirical-writing",
            "intermediation-markets": "finance-intermediation-markets-writing",
            "theory-structural": "finance-theory-structural-writing",
        }[set_name]
        reference = ROOT / "skills" / skill_name / "references" / "evidence-basis.md"
        if not reference.exists():
            errors.append(f"{reference.relative_to(ROOT)}: missing self-contained evidence basis")

    held_path = ROOT / "evidence" / "sets" / "held-out.csv"
    if held_path.exists():
        held_rows = load_csv(held_path)
        held_dois = [row.get("doi", "").lower() for row in held_rows]
        if len(held_dois) != len(set(held_dois)):
            errors.append(f"{held_path.relative_to(ROOT)}: duplicate DOI across held-out sets")
        selected_anywhere = set().union(*portfolios.values()) if portfolios else set()
        global_leaks = sorted(set(held_dois) & selected_anywhere)
        if global_leaks:
            errors.append(
                f"{held_path.relative_to(ROOT)}: held-out DOI selected in another portfolio: "
                + ", ".join(global_leaks)
            )
        held_counts = Counter(row.get("evidence_set", "") for row in held_rows)
        for set_name in EVIDENCE_SETS:
            if held_counts[set_name] < 8:
                errors.append(
                    f"{held_path.relative_to(ROOT)}: {set_name} needs at least 8 held-out papers"
                )
            leaks = [
                row.get("doi", "")
                for row in held_rows
                if row.get("evidence_set") == set_name
                and row.get("doi", "").lower() in portfolios.get(set_name, set())
            ]
            if leaks:
                errors.append(
                    f"{held_path.relative_to(ROOT)}: {set_name} held-out leakage: {', '.join(leaks)}"
                )
    return errors


def validate_skill_evals() -> list[str]:
    """Run deterministic routing and behavioral-fixture schema gates."""

    report = build_eval_report(ROOT)
    errors = [
        f"skill eval schema: {error}"
        for error in report["behavioral_schema"]["schema_errors"]
    ]
    errors.extend(
        "skill eval routing: "
        + failure["id"]
        + " failed "
        + ", ".join(failure["reasons"])
        for failure in report["routing"]["failures"]
    )
    return errors


def main() -> int:
    errors: list[str] = []
    actual = {path.name for path in SKILLS_DIR.iterdir() if path.is_dir()} if SKILLS_DIR.exists() else set()
    if actual != EXPECTED_SKILLS:
        errors.append(
            "skills/: expected exactly "
            + ", ".join(sorted(EXPECTED_SKILLS))
            + "; found "
            + ", ".join(sorted(actual))
        )
    for name in sorted(EXPECTED_SKILLS & actual):
        errors.extend(validate_skill(SKILLS_DIR / name))

    for required in (
        "README.md",
        "LICENSE",
        "CITATION.cff",
        "evidence/README.md",
        "evidence/curation-report.md",
        "evidence/sets/general-writing.csv",
        "evidence/sets/asset-pricing.csv",
        "evidence/sets/causal-empirical.csv",
        "evidence/sets/intermediation-markets.csv",
        "evidence/sets/theory-structural.csv",
        "evidence/sets/held-out.csv",
        "evidence/sets/overlap-matrix.json",
        "evidence/corpus-census/aggregate-patterns.json",
        "evidence/architecture-benchmark.md",
        "evals/README.md",
        "evals/cases/routing-v1.json",
        "evals/cases/behavior-v1.json",
        "evals/forward-test-results.md",
        "evals/manual-test-report-2026-08-13.md",
    ):
        if not (ROOT / required).exists():
            errors.append(f"missing repository file: {required}")

    errors.extend(validate_evidence_sets())
    errors.extend(validate_skill_evals())
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" not in markdown.parts:
            errors.extend(validate_local_links(markdown))

    result = {
        "skills_expected": len(EXPECTED_SKILLS),
        "skills_found": len(actual),
        "errors": errors,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
