---
name: finance-top-journal-writing
description: Draft, restructure, revise, or audit complete finance manuscripts and individual sections intended for The Journal of Finance (JF), Journal of Financial Economics (JFE), or The Review of Financial Studies (RFS). Use for titles, abstracts, introductions, literature positioning, theory and hypotheses, institutional background, data and variable construction, empirical or modeling methods, results, robustness, mechanisms, heterogeneity, discussion, conclusions, table and figure narration, appendices, response-driven revisions, and full-paper coherence. Do not use for generic finance explanations, statistical analysis without a writing task, or non-finance manuscripts.
---

# Finance Top-Journal Writing

Build a defensible finance-paper argument from the author's evidence. Treat JF, JFE, and RFS as journals sharing a high bar for contribution and credibility, with some observable production conventions—not as three fixed prose personas.

Read [evidence-basis.md](references/evidence-basis.md) when choosing a paper architecture, checking the empirical basis of a recommendation, or looking for a functionally similar teaching anchor. Select by writing function and transfer limit; never imitate an exemplar's wording or length.

## Establish the writing contract

Before drafting, recover or ask for the smallest useful fact set:

1. Target journal and requested section or task.
2. Paper type: descriptive empirical, causal empirical, asset pricing, intermediation/markets, pure theory, structural/quantitative, or hybrid.
3. Research question and answer in one sentence each.
4. Data, sample, setting, method/model, and identifying variation.
5. Main estimates, units, uncertainty, economic magnitude, and boundary conditions.
6. Closest literature and exact distinction, with verified citations only.
7. Tables, figures, equations, or draft text that the output must match.

Do not block when some inputs are absent. Create a `Missing-evidence ledger`, use conspicuous placeholders such as `[EFFECT SIZE NEEDED]`, and draft only claims supported by supplied facts. Never invent a citation, coefficient, sample detail, institutional fact, theorem, or journal rule.

Read [evidence-and-claim-policy.md](references/evidence-and-claim-policy.md) before making substantive claims or when inputs are incomplete.

## Choose the task mode

- **Draft**: Build prose from an approved fact ledger and section brief.
- **Restructure**: Preserve claims and evidence, but rebuild paragraph order and transitions.
- **Revise**: Improve argument, precision, and readability while returning a material-change note.
- **Audit**: Diagnose problems and rank fixes; do not silently rewrite unless asked.
- **Full-paper pass**: Create a reverse outline, claim–evidence matrix, and cross-section consistency check before line editing.

For full papers, read [full-paper-workflow.md](references/full-paper-workflow.md). Copy the relevant templates from `assets/` into the working output when useful.

## Route by evidence logic

Use this skill alone for descriptive or mixed finance papers. When an installed specialist matches the paper's central evidence, also invoke at most one by default:

- expected returns, factors, SDFs, anomalies, portfolio tests, predictability, or fund performance → `$finance-asset-pricing-writing`;
- DID, event study, IV, RDD, policy shock, natural experiment, or randomized intervention → `$finance-causal-empirical-writing`;
- banks, nonbanks, credit supply, balance sheets, liquidity, dealers, price discovery, or market design → `$finance-intermediation-markets-writing`;
- primitives, equilibrium, propositions, structural estimation, calibration, counterfactuals, or welfare → `$finance-theory-structural-writing`.

Route by how the main claim is supported, not by a broad field label. A corporate bond return paper may be asset pricing; a governance natural experiment may be causal; a bank-run model may be theory.

## Build the section as an argument

Select only functional modules that the paper needs. Do not force every label into every manuscript.

Treat the architectures below as function checklists rather than fixed paragraph counts. They are synthesized from a full recent-corpus census plus deliberately selected teaching exemplars; do not imitate an exemplar's sentences, length, section count, or topic-specific claims.

| Section | Required job |
|---|---|
| Title | Name the phenomenon or relationship and, only when useful, the setting/design. Avoid claiming more than the evidence. |
| Abstract | Deliver question → approach → main finding with magnitude → interpretation/contribution. |
| Introduction | Establish economic tension → gap → approach/credibility → main evidence → contribution → scope. |
| Literature | Define the nearest conversation and the exact margin changed; integrate into the introduction unless a separate section earns its space. |
| Theory/hypotheses | State mechanism, assumptions, predictions, and discriminating evidence; omit ceremonial hypotheses. |
| Setting/data | Explain why the setting speaks to the question; define sample construction, measurement, timing, and exclusions. |
| Design/method | Connect estimand or model object to variation, assumptions, inference, and threats. |
| Results | State what is estimated, direction, magnitude, uncertainty, interpretation, and evidentiary limit. |
| Robustness | Organize tests by threats, not by the order in which regressions were run. |
| Mechanisms | Distinguish mechanism evidence from heterogeneity, mediation, and rejected alternatives. |
| Discussion/conclusion | Synthesize the answer, implications, limitations, and scope without introducing new results. |
| Tables/figures/appendix | Make each object serve a claim and keep definitions, samples, units, and notes self-contained. |

Read the section-specific reference before drafting:

- title or abstract → [title-and-abstract.md](references/title-and-abstract.md)
- introduction, contribution, or literature → [introduction-and-positioning.md](references/introduction-and-positioning.md)
- theory, hypotheses, setting, data, or design → [theory-data-and-design.md](references/theory-data-and-design.md)
- results, robustness, mechanism, discussion, or conclusion → [results-through-conclusion.md](references/results-through-conclusion.md)
- tables, figures, equations, or appendices → [tables-figures-and-appendices.md](references/tables-figures-and-appendices.md)

## Adapt to the target journal conservatively

Read [journal-adapters.md](references/journal-adapters.md) whenever the user specifies JF, JFE, or RFS.
Read [official-submission-sources.md](references/official-submission-sources.md) for compliance-related requests, then recheck the linked live page at submission time.

Apply only three classes of adaptation:

1. Follow the user's live template or current official instructions first.
2. Apply well-supported production conventions, such as heading treatment, when formatting a near-final manuscript.
3. Adjust emphasis only when the evidence design warrants it; never manufacture a journal-specific claim, contribution, or voice.

Do not infer current submission limits from published PDFs. Recheck official sources for word limits, anonymization, data/code rules, fees, file types, and required declarations.

## Draft paragraphs with one evidentiary job

For every substantive paragraph:

1. Lead with its claim or question.
2. Provide the necessary evidence, logic, or comparison.
3. Interpret the evidence at the supported strength.
4. State the boundary or transition when it prevents overreading.

Use topic sentences that advance the argument. Prefer concrete nouns and verbs. Keep technical detail when it establishes credibility; move implementation detail that does not change interpretation to an appendix.

## Calibrate language to evidence

- Use `is associated with`, `predicts`, or `is consistent with` for descriptive or predictive evidence.
- Use causal verbs only when the design and maintained assumptions identify the effect.
- Describe structural counterfactuals as model-implied and conditional on estimation, fit, and maintained structure.
- Describe mechanisms as supported, narrowed, or consistent unless competing channels are genuinely distinguished.
- Report economic magnitude with units and a meaningful benchmark; do not substitute statistical significance for importance.

## Run quality gates before delivery

Read [revision-and-quality-gates.md](references/revision-and-quality-gates.md), then verify:

1. Every number and citation traces to supplied or verified evidence.
2. The abstract, introduction, tables, results, and conclusion state the same main finding.
3. Causal strength matches identification strength.
4. Each robustness test maps to a named threat.
5. Contribution claims compare against the closest literature rather than a broad straw literature.
6. Terminology, samples, signs, units, and time windows are consistent.
7. The conclusion introduces no new estimate or citation-dependent claim.
8. The prose does not imitate a source paper or reproduce protected text.
9. No observed production pattern or exemplar habit is presented as a current journal requirement.

If a draft file is available, run:

```bash
python3 scripts/lint_finance_draft.py path/to/paper.md
```

Treat linter findings as review prompts, not automatic errors.

## Deliver a reviewable result

Return, in this order unless the user requests another format:

1. The revised or drafted text.
2. `Evidence placeholders` that still require author input.
3. `Material choices` explaining any changed claim strength, paragraph order, or section scope.
4. A short quality-gate result for high-risk tasks.

When auditing, instead return prioritized findings with location, consequence, and a concrete revision strategy. Preserve the author's contribution and voice; do not homogenize the paper into generic “top-journal English.”
