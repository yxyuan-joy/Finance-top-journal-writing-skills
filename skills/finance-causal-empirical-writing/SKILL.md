---
name: finance-causal-empirical-writing
description: Draft, revise, or audit causal empirical finance manuscripts for The Journal of Finance (JF), Journal of Financial Economics (JFE), or The Review of Financial Studies (RFS). Use when the main contribution depends on identifying an effect through a natural experiment, difference-in-differences, event study, instrumental variables, regression discontinuity, policy or regulatory change, institutional discontinuity, randomized intervention, matched design, or comparable quasi-experimental variation in corporate finance, household finance, banking, governance, international finance, FinTech, or related fields. Do not use when the paper is purely descriptive or predictive, when causal identification is incidental, or when the main contribution is an asset-pricing test or structural counterfactual.
---

# Finance Causal-Empirical Writing

Make the identifying argument inspectable. Use `$finance-top-journal-writing` with this skill when installed for full-paper and journal-adapter guidance.

Honor the user's requested output language. If none is specified, match the user's language. Preserve variable names, citation keys, equations, and technical labels when translating them would break traceability.

Use [evidence-basis.md](references/evidence-basis.md) as an optional searchable provenance catalog. Consult it only when a design-specific teaching anchor or provenance check would help; search by design/function and read only matching rows rather than loading all 60 papers. It is not a source of sentences or a claim that all designs need the same checks.

## Define the estimand before the design label

Write one sentence for each:

- treatment/intervention;
- outcome;
- unit of treatment and unit of observation;
- population and period;
- counterfactual comparison;
- estimand (ATE, ATT, LATE, local discontinuity effect, intent-to-treat, dynamic effect, or another object);
- identifying variation;
- maintained assumptions;
- interference, anticipation, selection, and measurement risks.

For a multi-stage treatment chain, separate assignment, the first-stage change in the economically relevant exposure, and the final outcome. State the estimand at each link and do not rename assignment as the downstream exposure merely because the latter is the paper's economic object.

Preserve evidence ownership across components. For each design, stage, or model block, keep its variation or model source, outcome or object, unit, estimand, population and period, maintained assumptions, inference or precision, and evidentiary job attached to that block. Keep first stage, reduced form, IV, dynamics, downstream outcomes, model results, and analogous components distinct. Do not transfer stronger identification, precision, scope, or interpretation from one component to another.

Do not claim that `DID`, `IV`, or `RDD` “solves endogeneity.” Explain why this variation recovers this estimand.

For a full-paper draft, identification audit, or incomplete design, copy and complete [estimand-threat-to-test-ledger.md](assets/estimand-threat-to-test-ledger.md). Do not load or emit the entire template for a narrow paragraph edit.

Read [design-router.md](references/design-router.md) for design-specific requirements.

## Build the identification narrative

Use this chain:

```text
economic question
→ institution and assignment/timing
→ counterfactual problem
→ identifying variation and comparison
→ assumptions
→ design-specific diagnostics
→ estimate and magnitude
→ mechanisms/boundaries
```

The institutional setting belongs next to the identification logic. Explain strategic behavior, concurrent policies, eligibility rules, implementation lags, and data recording when they affect treatment or outcomes.

## Draft sections

Read [section-blueprints.md](references/section-blueprints.md).

### Abstract

Select only the headline causal evidence and the diagnostic or trade-off that most changes its interpretation. Name the intervention or variation, population and comparison, central estimand and magnitude with units, and a compact scope boundary. Omit secondary designs and result inventories, and do not expose internal ledgers. Do not use causal verbs if the assumptions are unstated or unsupported.

### Introduction

Reach the causal question quickly. Explain why ordinary comparisons fail, how the setting creates leverage, what assumptions remain, and which evidence bears on them. Organize the preview around the headline estimand, the decisive credibility evidence, and any interpretation-changing trade-off; defer secondary designs and results to their sections. Present mechanism evidence after the main effect and avoid equating subgroup differences with channels.

### Institutional setting

Organize rules and dates around assignment, compliance, anticipation, and spillovers. A timeline or eligibility diagram can replace prose.

### Empirical design

Define the estimating equation, but make variation and counterfactual readable without it. Justify fixed effects, controls, weights, clustering, and sample restrictions by named threats. State the identifying assumption adjacent to the specification.

### Results

Report estimate, units, baseline mean or other benchmark, uncertainty, and target population. Separate first stage/reduced form/IV, intent-to-treat/treatment-on-treated, dynamics, downstream outcomes, and model-based results. Retain each component's own variation, sample and period, estimand, assumptions, and inference rather than borrowing labels or strength from another block.

## Match robustness to threats

Before writing robustness, create a threat-to-test matrix using [threats-and-validation.md](references/threats-and-validation.md). Typical threats include:

- differential pre-trends or sorting;
- anticipation and treatment timing;
- concurrent shocks or policies;
- endogenous compliance or weak first stage;
- manipulation near a cutoff;
- spillovers and general-equilibrium response;
- composition, attrition, or measurement change;
- inference under few clusters or serial correlation;
- treatment-effect heterogeneity and estimator weighting;
- external validity.

Do not imply that a placebo “proves” identification. State what it diagnoses and what remains.

## Separate mechanism evidence

Read [mechanisms-and-heterogeneity.md](references/mechanisms-and-heterogeneity.md). Label evidence as:

- intermediate outcome predicted by the channel;
- pre-specified cross-sectional prediction;
- timing evidence;
- competing-channel test;
- heterogeneity only;
- formal mediation under additional assumptions.

Use `supports`, `narrows`, or `is consistent with` unless the design directly distinguishes channels.

When multiple designs are available, state whether they perform distinct jobs or test the same claim under meaningfully different assignment processes, assumptions, populations, or periods. Preserve each component's variation or model source, outcome or object, unit, estimand, population and period, assumptions, inference or precision, and evidentiary job before synthesizing. For same-claim triangulation, report each design's estimand and leading threat, then explain exactly what convergence or divergence changes. Do not pool unlike estimates, transfer credibility across components, or describe several imperfect designs as if their mere number proves the claim.

Qualify a claim where the relevant limitation first matters. Consolidate remaining cross-cutting scope into a compact sentence, and do not repeat inventories of disclaimers across the abstract, introduction, results, and conclusion.

## Apply hard gates

1. The estimand and target population are explicit.
2. Treatment timing, assignment, and comparison are reproducible.
3. The main identifying assumption appears in plain language.
4. Diagnostics are interpreted without pass/fail certainty.
5. Estimates have units and economic benchmarks.
6. Standard errors match assignment/dependence; inference limitations remain visible.
7. Mechanism, heterogeneity, and mediation are not conflated.
8. Spillovers/equilibrium effects and external validity are discussed when material.
9. Abstract and conclusion do not claim more than the design.
10. Every mechanism claim names a distinctive prediction and at least one live competing account.

Deliver the requested text first. For a high-risk or incomplete design, add one compact `Identification boundary` and a deduplicated threat-to-test list; do not repeat the full estimand ledger, threat matrix, and gap list unless the user requests an audit or design blueprint.
