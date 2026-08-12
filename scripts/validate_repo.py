#!/usr/bin/env python3
"""Validate the repository's five self-contained Agent Skills."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path


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
        "evidence/curated-exemplars.csv",
        "evidence/held-out-candidates.csv",
        "evidence/corpus-census/aggregate-patterns.json",
        "evals/forward-test-results.md",
    ):
        if not (ROOT / required).exists():
            errors.append(f"missing repository file: {required}")

    curated_path = ROOT / "evidence" / "curated-exemplars.csv"
    if curated_path.exists():
        with curated_path.open(encoding="utf-8", newline="") as handle:
            curated = list(csv.DictReader(handle))
        expected_fields = {
            "journal",
            "canonical_year",
            "doi",
            "title",
            "archetype",
            "selection_tier",
            "selected_sections",
            "teaching_function",
            "transfer_limit",
            "metadata_note",
        }
        if not curated or set(curated[0]) != expected_fields:
            errors.append("evidence/curated-exemplars.csv: unexpected schema")
        counts = {
            journal: sum(row.get("journal") == journal for row in curated)
            for journal in ("JF", "JFE", "RFS")
        }
        if counts != {"JF": 12, "JFE": 12, "RFS": 12}:
            errors.append(f"evidence/curated-exemplars.csv: expected 12 per journal; found {counts}")
        dois = [row.get("doi", "").lower() for row in curated]
        if len(dois) != len(set(dois)):
            errors.append("evidence/curated-exemplars.csv: duplicate DOI")
        for row_number, row in enumerate(curated, start=2):
            if not row.get("teaching_function") or not row.get("transfer_limit"):
                errors.append(
                    f"evidence/curated-exemplars.csv:{row_number}: teaching function and transfer limit are required"
                )
            if row.get("selection_tier") not in {"core", "section_specific"}:
                errors.append(
                    f"evidence/curated-exemplars.csv:{row_number}: invalid selection_tier"
                )

    result = {
        "skills_expected": len(EXPECTED_SKILLS),
        "skills_found": len(actual),
        "errors": errors,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
