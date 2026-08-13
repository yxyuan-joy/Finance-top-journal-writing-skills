#!/usr/bin/env python3
"""Run dependency-free routing evals and validate behavioral eval schemas.

The routing layer is intentionally deterministic: it tests whether realistic
prompts can be mapped to the public skill descriptions without calling a
model. Behavioral cases are contracts consumed by ``run_behavior_evals.py``;
this script validates only that their assertions are machine-checkable.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "finance-top-journal-writing",
    "finance-asset-pricing-writing",
    "finance-causal-empirical-writing",
    "finance-intermediation-markets-writing",
    "finance-theory-structural-writing",
)
CORE_SKILL = SKILLS[0]
SPECIALISTS = SKILLS[1:]
CASE_SCHEMA_VERSION = 1
SPECIALIST_THRESHOLD = 5.0
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+)$", re.M)


@dataclass(frozen=True)
class Signal:
    """One scored concept; multiple synonyms count once."""

    label: str
    weight: float
    patterns: tuple[str, ...]


CORE_SIGNALS = {
    "action": (
        r"\b(?:draft|write|rewrite|revise|restructure|polish|edit|audit|critique|tighten|strengthen)\b",
        r"\brespond(?:ing)?\s+to\s+(?:a\s+)?reviewer\b",
        r"帮我(?:把)?\S{0,8}(?:写|改|看|审|捋|打磨)",
        r"起草|改写|重写|修改|润色|重构|重组|审读|审查|压缩|捋顺|捋清楚|打磨",
    ),
    "artifact": (
        r"\b(?:paper|manuscript|draft|model|title|abstract|introduction|literature\s+review|section|paragraph|results|methods?|discussion|conclusion|appendix|referee\s+report|response\s+letter)\b",
        r"论文|稿子|草稿|模型|标题|摘要|引言|文献综述|章节|段落|结果段|方法部分|机制段|讨论|结论|附录|回复信",
    ),
    "finance": (
        r"\b(?:jf|jfe|rfs|journal\s+of\s+finance|journal\s+of\s+financial\s+economics|review\s+of\s+financial\s+studies)\b",
        r"\b(?:finance|financial|asset\s+pricing|returns?|stocks?|bonds?|banks?|lending|credit|dealers?|liquidity|trading|investors?|funds?|corporate|governance|mergers?|payout|cash\s+holdings?|household\s+finance)\b",
        r"金融|财务|资产定价|股票|债券|收益|银行|信贷|贷款|流动性|交易|投资者|基金|公司治理|并购|现金持有|家庭金融",
    ),
}


PROFILE_SIGNALS: dict[str, tuple[Signal, ...]] = {
    "finance-asset-pricing-writing": (
        Signal("expected-return-object", 6.0, (r"expected\s+returns?", r"预期收益(?:率)?")),
        Signal("return-prediction", 6.0, (r"(?:predict|forecast)\w*\s+(?:future\s+)?(?:stock\s+)?returns?", r"return\s+predict\w*", r"收益率?预测|预测\S{0,6}收益")),
        Signal("cross-section", 5.0, (r"cross[- ]sectional\s+returns?", r"截面收益")),
        Signal("factor-or-sdf", 6.0, (r"factor\s+(?:model|pricing|premium|premia)", r"stochastic\s+discount\s+factor|\bsdf\b", r"因子模型|因子定价|随机贴现因子")),
        Signal("anomaly", 5.0, (r"\banomal(?:y|ies)\b", r"异象")),
        Signal("portfolio-test", 4.0, (r"portfolio\s+sort", r"high[- ]minus[- ]low|long[- ]short", r"组合排序|多空组合|高减低组合")),
        Signal("pricing-performance", 4.0, (r"pricing\s+errors?|risk\s+premi(?:um|a)|fund\s+performance", r"mutual\s+fund|hedge\s+fund", r"定价误差|风险溢价|基金绩效")),
        Signal("validation", 2.0, (r"out[- ]of[- ]sample|holdout|post[- ]publication", r"transaction\s+costs?|microcaps?|shorting", r"样本外|留出样本|交易成本|微型股")),
    ),
    "finance-causal-empirical-writing": (
        Signal("did", 7.0, (r"difference[- ]in[- ]differences|diff[- ]in[- ]diff|\bdid\b", r"双重差分|差分中的差分")),
        Signal("iv-rdd", 7.0, (r"instrumental\s+variables?|\biv\b|regression\s+discontinuity|\brdd\b", r"工具变量|断点回归")),
        Signal("experiment-or-shock", 5.0, (r"natural\s+experiment|quasi[- ]experiment|randomi[sz]ed", r"policy\s+(?:reform|shock|rollout)|regulatory\s+(?:change|reform|mandate)", r"自然实验|准实验|随机实验|政策改革|分批推行|监管冲击")),
        Signal("treated-comparison", 5.0, (r"treated\s+(?:and|versus|vs\.?)\s+(?:untreated|control)", r"parallel\s+trends?|staggered\s+adoption|pre[- ]trends?", r"处理组|对照组|平行趋势|政策前后")),
        Signal("instrument-diagnostics", 4.0, (r"first\s+stage|exclusion\s+restriction|\blate\b|running\s+variable|bandwidth", r"第一阶段|排除性约束|运行变量|带宽")),
        Signal("identification", 2.0, (r"causal\s+(?:effect|identification|estimand)|identif(?:y|ication)", r"因果效应|因果识别|识别假设")),
        Signal("event-study", 4.0, (r"event[- ]study|event[- ]time", r"事件研究|事件时间")),
    ),
    "finance-intermediation-markets-writing": (
        Signal("credit-supply", 7.0, (r"credit\s+supply|loan\s+supply", r"信贷供给|贷款供给")),
        Signal("bank-lending", 4.0, (r"bank\s+lending|loan\s+(?:approval|origination|quantity|pricing)", r"银行贷款|授信|贷款审批|贷款定价")),
        Signal("funding-balance-sheet", 3.0, (r"deposits?|funding\s+(?:shock|fragility|constraint)|balance[- ]sheet\s+constraint|collateral|screening", r"存款|融资约束|资产负债表|抵押品|筛选")),
        Signal("market-quality", 6.0, (r"price[- ]discovery|market[- ]liquidity|bid[- ]ask\s+spread|market\s+depth", r"价格发现|市场流动性|买卖价差|市场深度")),
        Signal("dealer-market-design", 6.0, (r"dealer[- ](?:inventory|balance[- ]sheet|quotes?)|order[- ]flow|market[- ]maker|trading\s+venue|market\s+design", r"做市商|交易商库存|订单流|交易场所|市场设计")),
        Signal("intermediary-fragility", 5.0, (r"bank\s+run|nonbank\s+intermediar|interbank\s+network|funding\s+fragility", r"银行挤兑|非银机构|银行间网络|融资脆弱性")),
        Signal("institution", 1.0, (r"\bbanks?\b|\bdealers?\b|\bintermediar", r"银行|中介机构|交易商")),
    ),
    "finance-theory-structural-writing": (
        Signal("formal-theory", 7.0, (r"propositions?|theorems?|proofs?|comparative\s+statics", r"命题|定理|证明|比较静态")),
        Signal("equilibrium", 5.0, (r"equilibrium\s+(?:characteri[sz]ation|concept|existence|uniqueness)", r"primitives?.{0,20}equilibrium|timing.{0,20}information.{0,20}equilibrium", r"均衡刻画|均衡概念|均衡存在|均衡唯一|原始参数")),
        Signal("structural", 7.0, (r"structural\s+(?:estimation|model|identification)", r"结构估计|结构模型|结构识别")),
        Signal("quantitative", 6.0, (r"calibrat(?:e|ed|ion)|quantitative\s+model", r"校准|定量模型")),
        Signal("counterfactual", 5.0, (r"counterfactual|policy\s+experiment", r"反事实|政策模拟")),
        Signal("welfare", 5.0, (r"welfare\s+(?:analysis|criterion|effect|gain|loss)", r"福利分析|福利标准|福利改善|福利损失")),
        Signal("model-fit", 3.0, (r"targeted\s+(?:and|versus|vs\.?)\s+untargeted\s+moments|model\s+fit", r"目标矩|非目标矩|模型拟合")),
        Signal("game-timing", 5.0, (r"agents?.{0,20}(?:move|act)\s+(?:first|sequentially)|sequential\s+game", r"先后行动|行动顺序|信息结构|博弈")),
    ),
}


ASSERTION_FIELDS = {"id", "target", "matcher", "description"}
MATCHER_VALUE_FIELDS = {
    "contains": "value",
    "contains_any": "values",
    "contains_all": "values",
    "regex": "pattern",
}
DESCRIPTION_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "do", "does", "economics",
    "empirical", "financial", "finance", "for", "from", "in", "is", "journal", "journals",
    "manuscript", "manuscripts", "of", "or", "paper", "papers", "review", "studies", "the",
    "to", "use", "when", "whose", "with", "write", "writing", "jf", "jfe", "rfs",
}


def _matches_any(text: str, patterns: Iterable[str]) -> bool:
    return any(re.search(pattern, text, re.I) for pattern in patterns)


def route_prompt(prompt: str) -> dict[str, Any]:
    """Rank skills and select the core plus at most one central specialist."""

    normalized = " ".join(prompt.lower().split())
    core_matches = {
        label: _matches_any(normalized, patterns)
        for label, patterns in CORE_SIGNALS.items()
    }
    eligible = all(core_matches.values())
    if not eligible:
        return {
            "ranked": [],
            "selected": [],
            "scores": {},
            "matched_signals": {},
            "core_gate": core_matches,
        }

    scores: dict[str, float] = {CORE_SKILL: 100.0 + sum(core_matches.values())}
    matched: dict[str, list[str]] = {CORE_SKILL: sorted(k for k, v in core_matches.items() if v)}
    for skill, signals in PROFILE_SIGNALS.items():
        hits = [signal for signal in signals if _matches_any(normalized, signal.patterns)]
        scores[skill] = round(sum(signal.weight for signal in hits), 3)
        matched[skill] = [signal.label for signal in hits]

    order = {skill: index for index, skill in enumerate(SKILLS)}
    ranked = sorted(
        (skill for skill, score in scores.items() if score > 0),
        key=lambda skill: (-scores[skill], order[skill]),
    )
    selected = [CORE_SKILL]
    specialist_ranking = [skill for skill in ranked if skill in SPECIALISTS]
    if specialist_ranking and scores[specialist_ranking[0]] >= SPECIALIST_THRESHOLD:
        selected.append(specialist_ranking[0])
    return {
        "ranked": ranked,
        "selected": selected,
        "scores": scores,
        "matched_signals": matched,
        "core_gate": core_matches,
    }


def _assert_string_list(value: Any, location: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"{location}: expected a non-empty list of strings")


def _validate_assertion(assertion: Any, location: str, errors: list[str]) -> None:
    if not isinstance(assertion, dict):
        errors.append(f"{location}: assertion must be an object")
        return
    matcher = assertion.get("matcher")
    required = ASSERTION_FIELDS | ({MATCHER_VALUE_FIELDS[matcher]} if matcher in MATCHER_VALUE_FIELDS else set())
    optional = {"case_sensitive"}
    if set(assertion) != required and not (set(assertion) == required | optional):
        errors.append(f"{location}: fields must be {sorted(required)} with optional case_sensitive")
    for field in ASSERTION_FIELDS - {"matcher"}:
        if not isinstance(assertion.get(field), str) or not assertion.get(field, "").strip():
            errors.append(f"{location}: {field} must be a non-empty string")
    if assertion.get("target") != "response":
        errors.append(f"{location}: target must be response")
    if matcher not in MATCHER_VALUE_FIELDS:
        errors.append(f"{location}: unsupported matcher {matcher!r}")
        return
    value_field = MATCHER_VALUE_FIELDS[matcher]
    if value_field == "values":
        _assert_string_list(assertion.get(value_field), f"{location}.{value_field}", errors)
    elif not isinstance(assertion.get(value_field), str) or not assertion.get(value_field, "").strip():
        errors.append(f"{location}.{value_field}: expected a non-empty string")
    if matcher == "regex" and isinstance(assertion.get("pattern"), str):
        try:
            re.compile(assertion["pattern"])
        except re.error as exc:
            errors.append(f"{location}.pattern: invalid regex: {exc}")
    if "case_sensitive" in assertion and not isinstance(assertion["case_sensitive"], bool):
        errors.append(f"{location}.case_sensitive: expected boolean")


def _validate_routing_case(case: Any, location: str, errors: list[str]) -> None:
    required = {"id", "prompt", "language", "expected_primary", "expected_supporting", "negative_for", "tags"}
    optional = {"top_k", "note"}
    if not isinstance(case, dict):
        errors.append(f"{location}: case must be an object")
        return
    if not required <= set(case) or set(case) - required - optional:
        errors.append(f"{location}: invalid routing-case fields")
    for field in ("id", "prompt"):
        if not isinstance(case.get(field), str) or not case.get(field, "").strip():
            errors.append(f"{location}: {field} must be a non-empty string")
    if case.get("language") not in {"en", "zh", "mixed"}:
        errors.append(f"{location}: language must be en, zh, or mixed")
    primary = case.get("expected_primary")
    if primary is not None and primary not in SKILLS:
        errors.append(f"{location}: unknown expected_primary {primary!r}")
    for field in ("expected_supporting", "negative_for", "tags"):
        value = case.get(field)
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{location}: {field} must be a list of strings")
        elif len(value) != len(set(value)):
            errors.append(f"{location}: {field} contains duplicates")
    for field in ("expected_supporting", "negative_for"):
        unknown = set(case.get(field, [])) - set(SKILLS)
        if unknown:
            errors.append(f"{location}: {field} contains unknown skills {sorted(unknown)}")
    required_skills = ({primary} if primary else set()) | set(case.get("expected_supporting", []))
    overlap = required_skills & set(case.get("negative_for", []))
    if overlap:
        errors.append(f"{location}: required and negative skills overlap: {sorted(overlap)}")
    if primary is None and case.get("expected_supporting"):
        errors.append(f"{location}: no-route case cannot have expected_supporting")
    top_k = case.get("top_k")
    if top_k is not None and (not isinstance(top_k, int) or isinstance(top_k, bool) or top_k < max(1, len(required_skills))):
        errors.append(f"{location}: top_k must cover the required skill set")


def _validate_behavior_case(case: Any, location: str, errors: list[str]) -> None:
    required = {"id", "skill", "prompt", "provided_facts", "expectations", "hard_failures", "tags"}
    if not isinstance(case, dict):
        errors.append(f"{location}: case must be an object")
        return
    if set(case) != required:
        errors.append(f"{location}: behavior-case fields must be {sorted(required)}")
    for field in ("id", "prompt"):
        if not isinstance(case.get(field), str) or not case.get(field, "").strip():
            errors.append(f"{location}: {field} must be a non-empty string")
    if case.get("skill") not in SKILLS:
        errors.append(f"{location}: unknown skill {case.get('skill')!r}")
    for field in ("provided_facts", "tags"):
        _assert_string_list(case.get(field), f"{location}.{field}", errors)
    for field in ("expectations", "hard_failures"):
        assertions = case.get(field)
        if not isinstance(assertions, list) or not assertions:
            errors.append(f"{location}.{field}: expected a non-empty assertion list")
            continue
        seen: set[str] = set()
        for index, assertion in enumerate(assertions):
            _validate_assertion(assertion, f"{location}.{field}[{index}]", errors)
            if isinstance(assertion, dict) and isinstance(assertion.get("id"), str):
                if assertion["id"] in seen:
                    errors.append(f"{location}.{field}: duplicate assertion id {assertion['id']!r}")
                seen.add(assertion["id"])


def load_and_validate_cases(root: Path = ROOT) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    """Load every versioned fixture and return routing cases, behavior cases, errors."""

    case_dir = root / "evals" / "cases"
    errors: list[str] = []
    routing: list[dict[str, Any]] = []
    behavior: list[dict[str, Any]] = []
    paths = sorted(case_dir.glob("*.json")) if case_dir.exists() else []
    if not paths:
        return [], [], ["evals/cases: no JSON case files found"]
    for path in paths:
        relative = path.relative_to(root)
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: cannot load JSON: {exc}")
            continue
        if not isinstance(payload, dict) or set(payload) != {"schema_version", "kind", "cases"}:
            errors.append(f"{relative}: root fields must be schema_version, kind, cases")
            continue
        if payload.get("schema_version") != CASE_SCHEMA_VERSION:
            errors.append(f"{relative}: unsupported schema_version {payload.get('schema_version')!r}")
        kind = payload.get("kind")
        if kind not in {"routing", "behavior"}:
            errors.append(f"{relative}: kind must be routing or behavior")
            continue
        cases = payload.get("cases")
        if not isinstance(cases, list) or not cases:
            errors.append(f"{relative}: cases must be a non-empty list")
            continue
        destination = routing if kind == "routing" else behavior
        for index, case in enumerate(cases):
            location = f"{relative}:cases[{index}]"
            if kind == "routing":
                _validate_routing_case(case, location, errors)
            else:
                _validate_behavior_case(case, location, errors)
            if isinstance(case, dict):
                destination.append(case)

    identifiers: dict[str, str] = {}
    for kind, cases in (("routing", routing), ("behavior", behavior)):
        for case in cases:
            case_id = case.get("id")
            if not isinstance(case_id, str):
                continue
            if case_id in identifiers:
                errors.append(f"duplicate case id {case_id!r} in {identifiers[case_id]} and {kind}")
            identifiers[case_id] = kind

    positive_counts = Counter()
    negative_counts = Counter()
    for case in routing:
        primary = case.get("expected_primary")
        if primary in SKILLS:
            positive_counts[primary] += 1
        for skill in case.get("expected_supporting", []):
            if skill in SKILLS:
                positive_counts[skill] += 1
        for skill in case.get("negative_for", []):
            if skill in SKILLS:
                negative_counts[skill] += 1
    for skill in SKILLS:
        if positive_counts[skill] < 5:
            errors.append(f"routing coverage: {skill} needs >=5 positives; found {positive_counts[skill]}")
        if negative_counts[skill] < 3:
            errors.append(f"routing coverage: {skill} needs >=3 adjacent negatives; found {negative_counts[skill]}")
    all_tags = {tag for case in routing for tag in case.get("tags", [])}
    for tag in ("colloquial", "implicit-terminology", "cross-skill-conflict"):
        if tag not in all_tags:
            errors.append(f"routing coverage: missing {tag!r} case")
    languages = {case.get("language") for case in routing}
    if not {"en", "zh"} <= languages:
        errors.append("routing coverage: both English and Chinese cases are required")

    behavior_counts = Counter(case.get("skill") for case in behavior)
    for skill in SKILLS:
        if behavior_counts[skill] < 2:
            errors.append(f"behavior coverage: {skill} needs >=2 cases; found {behavior_counts[skill]}")
    return routing, behavior, errors


def evaluate_routing(cases: list[dict[str, Any]]) -> dict[str, Any]:
    case_results: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    primary_total = primary_correct = 0
    required_total = required_correct = 0
    negative_total = negative_correct = 0
    no_route_total = no_route_correct = 0
    route_collisions: list[dict[str, Any]] = []

    for case in cases:
        routed = route_prompt(case["prompt"])
        ranked = routed["ranked"]
        selected = routed["selected"]
        predicted_primary = ranked[0] if ranked else None
        expected_primary = case["expected_primary"]
        required = ([expected_primary] if expected_primary else []) + case["expected_supporting"]
        top_k = case.get("top_k", max(1, len(required)))
        top = ranked[:top_k]
        primary_ok: bool | None = None
        required_ok: bool | None = None
        no_route_ok: bool | None = None
        if expected_primary is not None:
            primary_total += 1
            primary_ok = predicted_primary == expected_primary
            primary_correct += int(primary_ok)
        else:
            no_route_total += 1
            no_route_ok = not selected
            no_route_correct += int(no_route_ok)
        if required:
            required_total += 1
            required_ok = set(required) <= set(top)
            required_correct += int(required_ok)
        negative_hits = sorted(set(case["negative_for"]) & set(selected))
        negative_total += len(case["negative_for"])
        negative_correct += len(case["negative_for"]) - len(negative_hits)

        specialist_candidates = [
            skill for skill in SPECIALISTS
            if routed["scores"].get(skill, 0) >= SPECIALIST_THRESHOLD
        ]
        if len(specialist_candidates) > 1:
            route_collisions.append({
                "id": case["id"],
                "specialists": sorted(specialist_candidates, key=lambda s: -routed["scores"][s]),
                "scores": {skill: routed["scores"][skill] for skill in specialist_candidates},
            })

        reasons: list[str] = []
        if primary_ok is False:
            reasons.append("primary-rank-1")
        if required_ok is False:
            reasons.append("required-set-top-k")
        if no_route_ok is False:
            reasons.append("unexpected-route")
        if negative_hits:
            reasons.append("negative-skill-selected")
        result = {
            "id": case["id"],
            "expected_primary": expected_primary,
            "predicted_primary": predicted_primary,
            "expected_supporting": case["expected_supporting"],
            "required_top_k": top_k,
            "predicted_top_k": top,
            "selected": selected,
            "negative_hits": negative_hits,
            "scores": routed["scores"],
            "passed": not reasons,
        }
        case_results.append(result)
        if reasons:
            failures.append({"id": case["id"], "reasons": reasons, "result": result})

    def ratio(numerator: int, denominator: int) -> float | None:
        return round(numerator / denominator, 4) if denominator else None

    return {
        "cases": len(cases),
        "primary_rank_1": {
            "correct": primary_correct,
            "total": primary_total,
            "accuracy": ratio(primary_correct, primary_total),
        },
        "required_set_top_k": {
            "full_hits": required_correct,
            "total": required_total,
            "accuracy": ratio(required_correct, required_total),
        },
        "adjacent_negative_exclusion": {
            "excluded": negative_correct,
            "total": negative_total,
            "accuracy": ratio(negative_correct, negative_total),
        },
        "no_route": {
            "correct": no_route_correct,
            "total": no_route_total,
            "accuracy": ratio(no_route_correct, no_route_total),
        },
        "route_collisions": route_collisions,
        "failures": failures,
        "case_results": case_results,
    }


def _skill_description(root: Path, skill: str) -> str:
    text = (root / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = FRONTMATTER_RE.match(text)
    if not frontmatter:
        return ""
    match = DESCRIPTION_RE.search(frontmatter.group(1))
    return match.group(1).strip() if match else ""


def description_collisions(root: Path = ROOT) -> list[dict[str, Any]]:
    """Report lexical description overlap after removing repository boilerplate."""

    token_sets: dict[str, set[str]] = {}
    for skill in SKILLS:
        description = _skill_description(root, skill).lower()
        token_sets[skill] = {
            token for token in re.findall(r"[a-z][a-z-]{2,}", description)
            if token not in DESCRIPTION_STOPWORDS
        }
    results: list[dict[str, Any]] = []
    for left_index, left in enumerate(SKILLS):
        for right in SKILLS[left_index + 1:]:
            shared = token_sets[left] & token_sets[right]
            union = token_sets[left] | token_sets[right]
            if not shared:
                continue
            results.append({
                "left": left,
                "right": right,
                "jaccard": round(len(shared) / len(union), 4) if union else 0.0,
                "shared_terms": sorted(shared),
            })
    return sorted(results, key=lambda item: (-item["jaccard"], item["left"], item["right"]))


def build_report(root: Path = ROOT, include_details: bool = False) -> dict[str, Any]:
    routing_cases, behavior_cases, schema_errors = load_and_validate_cases(root)
    routing = evaluate_routing(routing_cases) if routing_cases else {
        "cases": 0,
        "primary_rank_1": {"correct": 0, "total": 0, "accuracy": None},
        "required_set_top_k": {"full_hits": 0, "total": 0, "accuracy": None},
        "adjacent_negative_exclusion": {"excluded": 0, "total": 0, "accuracy": None},
        "no_route": {"correct": 0, "total": 0, "accuracy": None},
        "route_collisions": [],
        "failures": [],
        "case_results": [],
    }
    behavior_summary = {
        "cases": len(behavior_cases),
        "by_skill": dict(sorted(Counter(case.get("skill") for case in behavior_cases).items())),
        "expectations": sum(len(case.get("expectations", [])) for case in behavior_cases),
        "hard_failures": sum(len(case.get("hard_failures", [])) for case in behavior_cases),
        "schema_errors": schema_errors,
    }
    passed = not schema_errors and not routing["failures"]
    report = {
        "schema_version": 1,
        "passed": passed,
        "routing": routing,
        "behavioral_schema": behavior_summary,
        "description_collisions": description_collisions(root),
    }
    if not include_details:
        report["routing"].pop("case_results", None)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--details", action="store_true", help="include per-case routing results")
    parser.add_argument("--json-out", type=Path, help="also write the JSON report to this path")
    args = parser.parse_args(argv)
    report = build_report(args.root.resolve(), include_details=args.details)
    rendered = json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)
    print(rendered)
    if args.json_out:
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
