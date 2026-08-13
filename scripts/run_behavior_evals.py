#!/usr/bin/env python3
"""Grade saved model responses against versioned behavioral contracts.

This runner is model-agnostic: another agent or API writes one UTF-8 Markdown
response per case ID, and this script applies the declared deterministic
expectations and hard-failure matchers. It never claims to replace human review.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVAL_MODULE_PATH = ROOT / "scripts" / "run_skill_evals.py"
METADATA_FIELDS = {"model", "prompt_or_harness_version", "run_date", "notes"}
PLACEHOLDER_RE = re.compile(r"\[(?:RECORD|TODO|TBD)[^\]]*\]", re.I)


def load_eval_module():
    spec = importlib.util.spec_from_file_location("run_skill_evals_for_behavior", EVAL_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load run_skill_evals.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def assertion_matches(assertion: dict[str, Any], response: str) -> bool:
    flags = 0 if assertion.get("case_sensitive", False) else re.I
    matcher = assertion["matcher"]
    if matcher == "contains":
        return re.search(re.escape(assertion["value"]), response, flags) is not None
    if matcher == "contains_any":
        return any(re.search(re.escape(value), response, flags) for value in assertion["values"])
    if matcher == "contains_all":
        return all(re.search(re.escape(value), response, flags) for value in assertion["values"])
    if matcher == "regex":
        return re.search(assertion["pattern"], response, flags) is not None
    raise ValueError(f"unsupported matcher: {matcher}")


def grade_case(case: dict[str, Any], response: str) -> dict[str, Any]:
    expectations = [
        {
            "id": assertion["id"],
            "passed": assertion_matches(assertion, response),
            "description": assertion["description"],
        }
        for assertion in case["expectations"]
    ]
    hard_failures = [
        {
            "id": assertion["id"],
            "triggered": assertion_matches(assertion, response),
            "description": assertion["description"],
        }
        for assertion in case["hard_failures"]
    ]
    passed_expectations = sum(item["passed"] for item in expectations)
    triggered_failures = sum(item["triggered"] for item in hard_failures)
    return {
        "id": case["id"],
        "skill": case["skill"],
        "expectations": expectations,
        "hard_failures": hard_failures,
        "expectations_passed": passed_expectations,
        "expectations_total": len(expectations),
        "hard_failures_triggered": triggered_failures,
        "passed": passed_expectations == len(expectations) and triggered_failures == 0,
    }


def response_path(responses_dir: Path, case_id: str) -> Path | None:
    for candidate in (responses_dir / f"{case_id}.md", responses_dir / case_id / "response.md"):
        if candidate.is_file():
            return candidate
    return None


def substantive_response(path: Path) -> str | None:
    """Return response text, treating blank/comment-only scaffolds as missing."""

    response = path.read_text(encoding="utf-8")
    visible = re.sub(r"<!--.*?-->", "", response, flags=re.S).strip()
    return response if visible else None


def load_run_metadata(responses_dir: Path) -> tuple[dict[str, str] | None, list[str]]:
    """Require enough run identity to make a saved-response score auditable."""

    path = responses_dir / "run-metadata.json"
    if not path.is_file():
        return None, ["run-metadata.json is missing"]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [f"run-metadata.json is invalid JSON: {exc}"]
    if not isinstance(payload, dict) or set(payload) != METADATA_FIELDS:
        return None, [f"run-metadata.json fields must be {sorted(METADATA_FIELDS)}"]
    errors: list[str] = []
    for field in sorted(METADATA_FIELDS):
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip() or PLACEHOLDER_RE.search(value):
            errors.append(f"run-metadata.json {field} must be recorded, not left as a placeholder")
    if isinstance(payload.get("run_date"), str) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", payload["run_date"]):
        errors.append("run-metadata.json run_date must use YYYY-MM-DD")
    return payload, errors


def render_task(case: dict[str, Any]) -> str:
    """Render only task-local facts; never leak assertions into the blind run."""

    facts = "\n".join(f"- {fact}" for fact in case["provided_facts"])
    return (
        f"# {case['id']}\n\n"
        f"Target skill: `{case['skill']}`\n\n"
        "## Prompt\n\n"
        f"{case['prompt']}\n\n"
        "## Provided facts\n\n"
        f"{facts}\n\n"
        "## Isolation rule\n\n"
        "Use only the target skill and the facts above. Locate the target skill under "
        "the repository's `skills/` directory. Do not open the versioned "
        "behavior fixture or any evaluation assertions. Do not invent missing facts. "
        "Write the complete answer to `response.md` in this case directory.\n"
    )


def build_report(root: Path, responses_dir: Path) -> dict[str, Any]:
    module = load_eval_module()
    _, cases, schema_errors = module.load_and_validate_cases(root)
    run_metadata, metadata_errors = load_run_metadata(responses_dir)
    results: list[dict[str, Any]] = []
    missing: list[str] = []
    for case in cases:
        path = response_path(responses_dir, case["id"])
        if path is None:
            missing.append(case["id"])
            continue
        response = substantive_response(path)
        if response is None:
            missing.append(case["id"])
            continue
        result = grade_case(case, response)
        result["response_file"] = str(path)
        results.append(result)
    return {
        "schema_version": 1,
        "response_directory": str(responses_dir),
        "cases_expected": len(cases),
        "cases_graded": len(results),
        "missing_responses": missing,
        "schema_errors": schema_errors,
        "run_metadata": run_metadata,
        "metadata_errors": metadata_errors,
        "expectations_passed": sum(result["expectations_passed"] for result in results),
        "expectations_total": sum(result["expectations_total"] for result in results),
        "hard_failures_triggered": sum(result["hard_failures_triggered"] for result in results),
        "cases_passed": sum(result["passed"] for result in results),
        "passed": not schema_errors and not metadata_errors and not missing and all(result["passed"] for result in results),
        "results": results,
        "interpretation": "Deterministic assertion matches require human review for semantic false positives/negatives.",
    }


def scaffold(root: Path, output_dir: Path) -> int:
    module = load_eval_module()
    _, cases, errors = module.load_and_validate_cases(root)
    if errors:
        print(json.dumps({"errors": errors}, indent=2, ensure_ascii=False))
        return 1
    output_dir.mkdir(parents=True, exist_ok=True)
    created_tasks = 0
    created_responses = 0
    for case in cases:
        case_dir = output_dir / case["id"]
        case_dir.mkdir(parents=True, exist_ok=True)
        task_path = case_dir / "task.md"
        response_file = case_dir / "response.md"
        if not task_path.exists():
            task_path.write_text(render_task(case), encoding="utf-8")
            created_tasks += 1
        if not response_file.exists():
            response_file.write_text(
                "<!-- Write the model/agent response for this case below. -->\n",
                encoding="utf-8",
            )
            created_responses += 1
    metadata = output_dir / "run-metadata.json"
    if not metadata.exists():
        metadata.write_text(
            json.dumps(
                {
                    "model": "[RECORD MODEL]",
                    "prompt_or_harness_version": "[RECORD VERSION]",
                    "run_date": "[RECORD ISO DATE]",
                    "notes": "Record whether the agent saw only task-local facts and the selected skill.",
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )
    print(
        json.dumps(
            {
                "created_tasks": created_tasks,
                "created_responses": created_responses,
                "directory": str(output_dir),
            },
            ensure_ascii=False,
        )
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "responses",
        type=Path,
        nargs="?",
        help="directory containing CASE_ID/response.md files (legacy CASE_ID.md is also accepted)",
    )
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--scaffold", type=Path, help="create empty response files and metadata template")
    parser.add_argument("--json-out", type=Path, help="also write the complete JSON report")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if args.scaffold:
        return scaffold(root, args.scaffold.resolve())
    if args.responses is None:
        raise SystemExit("responses directory is required unless --scaffold is used")
    report = build_report(root, args.responses.resolve())
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json_out:
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
