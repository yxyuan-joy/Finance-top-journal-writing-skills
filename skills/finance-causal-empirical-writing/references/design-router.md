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

Choose one primary design tied to the headline estimand. Present secondary designs as triangulation only when their assumptions and target populations are explicit; do not imply that several weak designs mechanically create one strong causal claim.
