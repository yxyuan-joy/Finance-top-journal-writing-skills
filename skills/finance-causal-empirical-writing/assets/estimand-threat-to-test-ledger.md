# Estimand and Threat-to-Test Ledger

Copy this template into the working paper folder before drafting identification claims. Fill missing cells with `unknown`; an empty cell is not an identifying assumption. Keep separate rows for distinct treatment stages, estimands, or designs.

## 1. Causal object

| Field | Entry | Source / exhibit | Unresolved decision |
|---|---|---|---|
| Economic question |  |  |  |
| Assignment / intervention |  |  |  |
| Economically relevant exposure |  |  |  |
| Outcome and horizon |  |  |  |
| Unit of assignment |  |  |  |
| Unit of observation |  |  |  |
| Target population and period |  |  |  |
| Treatment contrast |  |  |  |
| Counterfactual comparison |  |  |  |
| Estimand: ITT / ATT / LATE / local / dynamic / other |  |  |  |
| Weighting across units, cohorts, or event time |  |  |  |

Write the target sentence:

```text
For [target population], the design estimates [estimand] of [treatment contrast]
on [outcome over horizon], using [identifying comparison], under [main assumption].
```

## 2. Treatment chain

| Link | Variable and unit | Variation used | Estimand at this link | Assumption | Estimate / uncertainty | Interpretation limit |
|---|---|---|---|---|---|---|
| Assignment → take-up |  |  |  |  |  |  |
| Take-up → exposure/intensity |  |  |  |  |  |  |
| Exposure → main outcome |  |  |  |  |  |  |
| Main outcome → downstream consequence |  |  |  |  |  |  |

Do not relabel an assignment effect as an exposure effect. Record whether each reported result is ITT, first stage, reduced form, IV/TOT, mediation, or a descriptive downstream association.

## 3. Assignment and timing

```text
Eligibility measurement date:
Announcement date:
Anticipation window:
Event-time-bin to calendar-time mapping:
Lead/lag bins that actually overlap the announcement or anticipation window:
Assignment / treatment dates:
Implementation and compliance dates:
Outcome measurement window:
Treatment reversals or intensity changes:
Concurrent policies or shocks:
Potential spillover units or markets:
Comparison observations eligible at each date:
```

## 4. Threat-to-test map

Rank threats by their ability to overturn the headline causal interpretation. A test earns space only if its result changes what can be claimed.

| Priority | Threat and setting-specific reason | Threatened estimand/claim | Diagnostic or design response | Result with uncertainty | What it alleviates | What remains | Claim change if adverse | Exhibit |
|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |

Consider, when relevant:

- differential trends, selection, or endogenous timing;
- anticipation, treatment reversal, or changing intensity;
- concurrent policies and shocks;
- weak first stage, noncompliance, or exclusion restriction;
- sorting/manipulation at eligibility or a cutoff;
- spillovers, interference, displacement, or equilibrium response;
- attrition, composition, linkage, or measurement change;
- few clusters, serial/spatial/network dependence, or generated regressors;
- heterogeneous effects, support, and estimator weighting;
- local-population and external-validity limits.

## 5. Main estimate reconciliation

| Specification / exhibit | Estimand | Sample and N | Estimate | Units | SE / CI | Baseline / benchmark | Horizon | Weighting | Causal wording allowed |
|---|---|---|---|---|---|---|---|---|---|
| Headline |  |  |  |  |  |  |  |  |  |
| Preferred sensitivity |  |  |  |  |  |  |  |  |  |
| Abstract value |  |  |  |  |  |  |  |  |  |

## 6. Mechanism boundary

| Proposed channel | Distinctive prediction | Live alternative | Evidence type: intermediate / timing / cross-section / competing test / heterogeneity / mediation | Does assignment identify this quantity? | Safe wording | Residual ambiguity |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 7. Final claim boundary

```text
Strongest supported causal sentence:
Most important maintained assumption:
Diagnostic with greatest identifying value:
Residual interference/equilibrium concern:
Population, setting, and horizon limit:
Evidence that would force a weaker claim:
Policy implication supported directly:
Policy implication that remains speculative:
```

Reconcile this ledger against the abstract, introduction, design equation, headline table, results prose, and conclusion. Never combine the coefficient from one specification with the N, baseline, uncertainty, horizon, or estimand from another.
