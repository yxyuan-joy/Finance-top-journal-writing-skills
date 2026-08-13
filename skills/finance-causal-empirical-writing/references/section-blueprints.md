# Causal-Empirical Section Blueprints

Use this workflow after defining the estimand and identifying variation. Treat paragraph counts as flexible jobs, not a formula. A short paper can combine jobs; a complex multi-stage design may split them. The prose must expose the counterfactual and maintained assumptions before displaying diagnostic abundance.

## Sections

[Abstract](#abstract) · [Introduction](#introduction) · [Setting](#institutional-setting-and-data) · [Design](#empirical-design) · [Results](#results-and-threat-targeted-validation) · [Mechanisms](#mechanisms-and-heterogeneity) · [Conclusion](#conclusion)

## Abstract

### Sentence jobs

1. **Causal question.** Name the intervention or economically relevant exposure, outcome, and population.
2. **Identification.** State the assignment rule, shock, cutoff, instrument, or timing contrast and the comparison that supplies the counterfactual.
3. **Estimate.** Report the estimand, magnitude in original units, uncertainty, and a baseline or distributional benchmark.
4. **Credibility.** Name one design-defining diagnostic or institutional fact; do not list generic robustness checks.
5. **Mechanism and scope.** Give a supported channel or consequence and retain the key local-population, time-horizon, interference, or external-validity boundary.

### Required facts

Know treatment and outcome definitions, treatment and observation units, population/period, assignment/timing, comparison, estimand, estimate, inference, baseline, and central identifying assumption. If a central item is missing, use a placeholder or provide a design blueprint rather than a production-ready causal abstract.

### Overclaim traps

Do not say a policy date itself is exogenous. Do not rename assignment as treatment received. Do not present an intent-to-treat estimate as treatment-on-treated, an IV estimate as an average population effect, or a local RDD estimate as universal. A null pre-trend or placebo does not prove identification.

### Exit check

A reader should understand `who is compared with whom, why, for what estimand, with what magnitude, under which assumption`.

## Introduction

### Paragraph jobs

1. **Economic decision and causal question.** Establish the behavior, friction, or policy tradeoff and explain why the effect matters.
2. **Counterfactual problem.** Show why ordinary treated–untreated or before–after comparisons are confounded. Name the most important selection, timing, or equilibrium concern.
3. **Institutional leverage.** Explain the event, rule, threshold, instrument, or randomization and how it creates the relevant comparison. Include strategic responses when they threaten assignment.
4. **Estimand and assumption.** Name the target population, causal object, treatment contrast, and identifying assumption in plain language. For multi-stage chains, distinguish assignment, exposure, and outcome links.
5. **Headline result.** Report magnitude, units, uncertainty, baseline, time horizon, and whether the estimate is ITT, reduced form, IV/LATE, ATT, event-time effect, or another object.
6. **Design credibility.** Select the evidence most diagnostic of the leading threat. Explain what it alleviates and what remains rather than announcing that the design is robust.
7. **Mechanism and consequences.** Present timing, intermediate outcomes, cross-sectional predictions, or competing-channel tests after the main effect. Label heterogeneity as heterogeneity unless additional assumptions support mediation.
8. **Contribution.** Compare against the closest question and design. State whether the paper changes the estimated effect, identification, mechanism, incidence, or policy understanding—not merely that the setting or dataset is new.

Order evidence by inferential dependency, not automatically by outcome timing. When a policy shock is used to diagnose whether a preexisting choice was optimal, a defensible chain is:

```text
intervention changes the target behavior
→ valuation or welfare diagnostic answers the optimality question
→ reallocation or downstream outcomes explain why
→ heterogeneity shows where the diagnosis changes
```

The valuation or welfare block has a different evidentiary job from an operational outcome. State the extra assumptions it needs; a favorable market reaction is not a complete social-welfare test.

### Required facts

Complete an estimand ledger, institutional timeline, threat ranking, headline magnitude, and evidence-to-claim map before drafting. Use the fillable [estimand and threat-to-test ledger](../assets/estimand-threat-to-test-ledger.md).

### Overclaim traps

An unusual institution is not identification. Multiple imperfect designs do not mechanically combine into proof. A precise estimate is not necessarily credible, and an imprecise estimate is not zero. Subgroup differences are not channel effects without a distinctive prediction and credible comparison.

### Exit check

The introduction should let a skeptical reader reconstruct the causal chain and locate its weakest assumption before reaching the design section.

## Institutional setting and data

### Block jobs

1. **Rules and actors.** Explain who assigns or receives treatment, eligibility, discretion, enforcement, compliance, and incentives to sort or manipulate.
2. **Timeline.** Record eligibility measurement, announcement, anticipation window, assignment, implementation, outcome measurement, treatment reversals, and concurrent policies.
3. **Exposure map.** Distinguish nominal eligibility, assignment, take-up, intensity, first-stage exposure, spillovers, and downstream outcomes.
4. **Sample construction.** Define source data, units, dates, exclusions, linkage, attrition, missingness, outcome construction, and any treatment-induced measurement or composition changes.
5. **Descriptive evidence.** Use counts and baseline patterns to reveal support, overlap, treatment shares, timing, and outcome scale. Do not treat balance as causal validation.

### Overclaim traps

Administrative recording can change with policy implementation. Dropping late adopters or noncompliers can redefine the estimand and induce selection. An apparently untreated group may be indirectly exposed. Institutional details that alter treatment or comparison cannot be relegated to an appendix.

### Exit check

The reader should be able to draw the assignment and measurement timeline, distinguish treatment stages, and explain every material sample exclusion.

## Empirical design

### Block jobs

1. **Target estimand.** Define population, treatment contrast, outcome horizon, and weighting. For staggered adoption, state whether the target is cohort-time, event-time, or an aggregate ATT and which controls are eligible at each date.
2. **Estimating equation.** Define all terms, coefficient, fixed effects, controls, weights, functional form, and sample. Explain the variation remaining after fixed effects.
3. **Identification.** State the counterfactual assumption in plain language adjacent to the equation and connect it to the institution.
4. **Inference.** Match clustering or randomization inference to the assignment and dependence structure. Report few-cluster, serial-correlation, spatial/network, or generated-regressor limitations when relevant.
5. **Diagnostics plan.** Map each leading threat to a pre-specified diagnostic or sensitivity analysis and state what outcome would change the interpretation.
6. **Multi-stage or multiple-design logic.** Keep first stage, reduced form, IV, and downstream outcomes distinct. Give each secondary design one job—assignment credibility, mechanism, external validation, or aggregate consequence.

### Overclaim traps

Fixed effects do not create exogeneity. Controls affected by treatment can bias the target estimate. Estimator names do not resolve poor support, forbidden comparisons, treatment reversals, anticipation, or spillovers. Clustering corrects sampling uncertainty, not design bias.

### Exit check

Another researcher should be able to identify exactly which observations and contrasts identify the coefficient and what assumptions convert it into the named estimand.

## Results and threat-targeted validation

### Evidence-block jobs

1. **Assignment and first stage.** Show treatment take-up, intensity, manipulation, or first-stage strength before downstream outcomes when relevant.
2. **Main effect.** Report estimate, confidence interval, units, baseline, target population, horizon, and specification. Separate ITT, reduced form, IV/TOT, and dynamic effects.
3. **Dynamics and support.** Show anticipation windows, event-time support, cohort composition, omitted endpoints, or local bandwidth. Interpret leads as diagnostics with limited power.
4. **Threat-to-test evidence.** Organize by differential trends/sorting, concurrent shocks, compliance, manipulation, spillovers, composition, measurement, and inference—not by a miscellaneous list of alternative specifications.
5. **Sensitivity and bounds.** State attenuation, sign change, imprecision, or economically relevant confidence bounds. Preserve informative nulls and failed diagnostics.
6. **External validity and equilibrium.** Distinguish the identified local/partial-equilibrium effect from broader incidence, displacement, or general-equilibrium claims.

Before fixing subsection order, draw the dependency graph among the paper's claims. Place a result earlier when later interpretation logically requires it, even if the underlying outcome occurs later in calendar time. A first stage, valuation diagnostic, allocation response, mechanism test, and welfare calculation are not interchangeable `outcomes`; label the question each one unlocks.

### Overclaim traps

Do not mix an estimate from one specification with the N, baseline, or uncertainty from another. A stable coefficient across similar specifications does not address an untested threat. Nonsignificance is not equivalence. Removing exposed comparison units changes the population and perhaps the estimand; say so.

### Exit check

Each result block must start with the claim under test and end with what the evidence alleviates, what remains, and whether the headline claim must narrow.

## Mechanisms and heterogeneity

### Paragraph jobs

1. State the channel and a prediction that differs from at least one live alternative.
2. Classify the evidence: intermediate outcome, timing, cross-sectional prediction, competing-channel test, heterogeneity, or formal mediation.
3. Explain whether the original assignment identifies the mechanism quantity or merely the main treatment effect.
4. Report the evidence with units and uncertainty, including null or contrary results.
5. Use `supports`, `narrows`, or `is consistent with` unless the design directly separates channels under explicit additional assumptions.

### Exit check

No subgroup table should be called mechanism evidence solely because effects differ. Do not condition on post-treatment variables without explaining the changed estimand and selection risk.

## Conclusion

### Paragraph jobs

1. Answer the opening question with the correct estimand, population, setting, and horizon.
2. State the main economic implication and the evidence most important for credibility.
3. Preserve the binding assumption and local, spillover, equilibrium, or external-validity boundary.
4. Offer a policy or managerial implication only if incidence, behavioral response, and relevant welfare margins are actually studied; otherwise frame it as a consideration rather than a prescription.

### Final output check

Verify that abstract, introduction, design, tables, results, and conclusion use the same treatment, estimand, estimate, units, baseline, sample, and uncertainty. Keep assignment distinct from exposure, identification distinct from diagnostics, mechanism distinct from heterogeneity, and local evidence distinct from universal policy claims.
