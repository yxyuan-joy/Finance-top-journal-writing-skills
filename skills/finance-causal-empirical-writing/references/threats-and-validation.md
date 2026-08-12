# Identification Threats and Validation

## Threat-to-test matrix

Complete before drafting:

| Threat | Design-specific reason | Evidence/test | Result | What it alleviates | What remains |
|---|---|---|---|---|---|
| Nonparallel trends / selection |  |  |  |  |  |
| Anticipation / timing |  |  |  |  |  |
| Concurrent shocks |  |  |  |  |  |
| Weak first stage / compliance |  |  |  |  |  |
| Manipulation / sorting |  |  |  |  |  |
| Spillovers / interference |  |  |  |  |  |
| Composition / attrition |  |  |  |  |  |
| Measurement change |  |  |  |  |  |
| Inference / dependence |  |  |  |  |  |
| External validity |  |  |  |  |  |

## Writing diagnostics accurately

- `The estimates are stable when...` is narrower than `the result is robust`.
- A null placebo can reduce concern about that placebo outcome/time/group; it does not validate all assumptions.
- Covariate balance is descriptive and may be underpowered.
- Pre-trend estimates reveal detectable differences, not the truth of parallel counterfactual trends.
- Alternative bandwidths/specifications address sensitivity, not unobserved confounding.
- Clustering choices address sampling dependence, not design bias.

## Economic magnitude

Report the effect in original units, relative to the untreated/pre-treatment mean or economically meaningful distribution, and for the target estimand. Avoid scaling by a baseline mean near zero. For nonlinear models, clarify whether reported objects are coefficients, marginal effects, elasticities, or percentage changes.

## Negative and null evidence

State confidence intervals and economically relevant bounds when a null matters. Do not equate nonsignificance with zero, no effect, or equivalence unless an equivalence/noninferiority framework supports it.
