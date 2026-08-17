# Causal Design Router

## Difference-in-differences and event studies

State treatment cohorts, timing, comparison observations, event window, anticipation, estimator, and weighting. Address:

- parallel trends as an identifying assumption, not a pre-trend test result;
- staggered adoption and heterogeneous effects;
- already-treated or never-treated controls;
- treatment reversals/intensity;
- dynamic effects and omitted endpoints;
- clustering level and few-cluster inference;
- spillovers and concurrent policies.

Explain what event-study leads can diagnose and their limited power. Do not write `no significant pre-trends proves parallel trends`.

For staggered adoption, choose the estimand before choosing a named estimator or software command. Record cohort-specific treatment timing, eligible controls at each date, support by cohort and event time, anticipation, treatment reversals, and whether the target is an overall, cohort-time, or event-time average effect. Then verify that the implementation aggregates only comparisons compatible with that estimand and report the weighting/aggregation rule. A fashionable estimator name does not resolve poor overlap, forbidden controls, few clusters, spillovers, or a policy that changes intensity rather than switching on once. If those inputs are missing, provide a bounded design blueprint rather than pretending to select a production-ready estimator.

## Instrumental variables

Define instrument, endogenous treatment, first stage, reduced form, exclusion restriction, independence, monotonicity, and complier population. Report first-stage strength with appropriate diagnostics. Explain why the instrument affects the outcome only through treatment and discuss plausible violations. Interpret the estimate as the relevant local effect unless stronger homogeneity assumptions are justified.

## Regression discontinuity

Define running variable, cutoff, assignment rule, sharp/fuzzy status, bandwidth, polynomial/local method, and estimand at the threshold. Address manipulation, covariate continuity, sorting, other discontinuities, bandwidth sensitivity, functional form, discrete running variables, and local external validity. Do not generalize the local result silently.

## Policy or natural experiment

Name the exact shock, why exposure differs, whether exposure is predetermined, implementation/anticipation, concurrent shocks, and equilibrium response. A policy date alone is not exogenous variation. State whether the design is DID, IV, event time, synthetic control, or another comparison.

## Randomized interventions

State unit and method of randomization, balance, compliance, attrition, interference, analysis population, preregistration, and inference. Separate intent-to-treat from treatment-on-treated. Do not use covariate balance as proof that attrition or interference is harmless.

## Matching/selection-on-observables

State the conditional-independence assumption, overlap, timing of covariates, matching/weighting method, balance, trimming, and sensitivity to unobserved confounding. Avoid causal certainty when selection on unobservables remains plausible.

## Multiple designs

Choose one primary design tied to the headline estimand. A secondary design can either perform a different evidentiary job or estimate a related object under a different assignment process, assumption set, population, or period. For same-claim triangulation, use:

```text
common target claim
→ design-specific estimand and comparison
→ design-specific leading threat
→ convergent or divergent result
→ exact increment in credibility or scope
```

Before synthesis, keep an internal component record for every design, stage, or model block:

- variation or model source;
- outcome or object and its unit;
- estimand;
- population and period;
- maintained assumptions;
- inference or precision;
- evidentiary job in the argument.

Keep first stage, reduced form, IV, dynamics, downstream outcomes, model results, and analogous blocks separately owned even when they appear in the same exhibit or share a source of variation. Do not attach the outcome, unit, sample, baseline, uncertainty, assumptions, or interpretation of one block to another. Do not use stronger identification or precision in one component to upgrade a weaker component.

Keep unlike estimates separate and explain why their signs or magnitudes are comparable before synthesizing them. Several weak designs do not mechanically create one strong causal claim. In the abstract and introduction, retain only the headline evidence and the diagnostic or trade-off that materially changes its credibility or meaning; defer the component record and secondary evidence to the design and results sections.
