---
name: finance-asset-pricing-writing
description: Draft, revise, or audit empirical asset-pricing and investments manuscripts for The Journal of Finance (JF), Journal of Financial Economics (JFE), or The Review of Financial Studies (RFS). Use when the central evidence concerns expected returns, cross-sectional or time-series predictability, factor models, stochastic discount factors, anomalies, portfolio tests, mutual or hedge fund performance, return decomposition, model comparison, machine-learning forecasts, limits to arbitrage, or out-of-sample validation. Do not use for valuation tutorials, trading advice, or finance papers whose main contribution rests on a causal treatment effect, intermediation institution, or formal structural model rather than asset-pricing evidence.
---

# Finance Asset-Pricing Writing

Write asset-pricing papers as tests of an economic object, not as collections of return regressions. Use `$finance-top-journal-writing` with this skill when it is installed; the core skill supplies full-paper and journal-adapter guidance.

Read [evidence-basis.md](references/evidence-basis.md) when choosing among factor/SDF tests, return facts, prediction, fund performance, implementation, measurement, or macro/time-series architectures. Use its independent 50-paper portfolio by function and heed each transfer limit; do not reproduce source prose.

## Classify the paper before drafting

Choose the dominant archetype:

- new return fact or anomaly;
- factor/model proposal or comparison;
- theory-motivated empirical test;
- time-series predictability or macro-finance;
- SDF/latent-factor estimation;
- mutual fund, hedge fund, or institutional performance;
- limits to arbitrage, implementation, or market efficiency;
- machine-learning prediction or characteristic discovery.

Read [design-and-claim-router.md](references/design-and-claim-router.md), then state whether the paper documents, predicts, tests a model, estimates a risk price, or identifies a causal effect. Do not substitute one claim for another.

## Build the asset-pricing fact ledger

Record:

1. Asset universe, frequency, period, filters, and delisting treatment.
2. Signal/factor/model construction and availability timing.
3. Portfolio sorts or estimating equations, weights, breakpoints, lags, and rebalancing.
4. Return definition, horizon, benchmark model, and inference.
5. Main spread/price of risk/forecast improvement with units and uncertainty.
6. In-sample, holdout, postpublication, international, or other validation status.
7. Multiple-testing/search space and researcher degrees of freedom.
8. Turnover, transaction costs, shorting/borrow constraints, capacity, and implementability.
9. Risk, mispricing, institutional, or statistical interpretations and evidence separating them.

Use placeholders rather than assuming a conventional CRSP construction.

## Draft the argument

### Abstract and introduction

State the economic question before the estimator. Clarify whether the result is a new fact, a sharper economic mechanism, a model rejection, an improvement in fit/prediction, or an implementable payoff. Give a central magnitude and benchmark. State out-of-sample and cost evidence only when actually performed.

Read [section-blueprints.md](references/section-blueprints.md) for section-specific architecture.

### Data and portfolio/factor construction

Make timing reproducible. Explain when each input becomes observable, how missing signals and microcaps are handled, which exchange breakpoints and weights are used, how returns are aligned, and whether choices were fixed before evaluation. Put exhaustive signal definitions in an appendix, but keep choices that drive results in the main text.

### Main tests

Separate:

- raw economic spread;
- benchmark-adjusted performance;
- model fit or pricing errors;
- cross-sectional versus time-series evidence;
- statistical versus economic improvement;
- discovery versus validation samples.

Do not present a high t-statistic as an economic explanation.

Order evidence so that each block narrows the economic interpretation. A useful, nonmandatory sequence is `baseline shape → benchmark adjustment → independent or holdout evidence → mechanism discrimination → implementation boundary`. Do not add another asset class or test merely to resemble a published exemplar.

### Interpretation

For a risk account, connect exposures to a priced state or marginal utility and show model-specific predictions. For mispricing, show why limits, beliefs, or correction dynamics fit better than risk-based alternatives. For an institutional channel, measure the relevant constraints or flows. Use `consistent with` when evidence does not discriminate.

## Organize validation by failure mode

Read [validation-and-robustness.md](references/validation-and-robustness.md). At minimum consider:

- look-ahead and data availability;
- survivorship and delisting;
- microcap, price, and liquidity influence;
- multiple testing, overfitting, and specification search;
- factor redundancy and benchmark sensitivity;
- persistence across periods/markets;
- transaction, shorting, funding, and capacity costs;
- publication decay and post-discovery evidence;
- dependence across assets and time;
- generated-regressor and model-selection inference.

Include only relevant tests, but name the threat each one addresses.

## Integrate exhibits

Read [exhibits-and-appendix.md](references/exhibits-and-appendix.md). Lead with the economic contrast a table or figure establishes. Report return units and frequency, annualization method, long and short legs, factor definitions, sample changes, and inference. Show monotonicity or shape when a long–short spread hides it.

## Apply hard gates

Before delivery, verify:

1. Availability dates preclude mechanical look-ahead.
2. Discovery and evaluation samples are not rhetorically conflated.
3. Benchmark models and factor construction are defined.
4. Magnitudes use consistent monthly/annual and percentage/basis-point units.
5. The short leg, microcaps, or a few periods do not silently drive the headline.
6. Multiple-testing and implementability limits remain visible.
7. Prediction, pricing, causal, risk, and mispricing claims use distinct wording.
8. The conclusion does not generalize beyond the asset universe and period.
9. A new factor, model, or diagnostic is explained first as an economic object, then defined formally, then compared against a meaningful benchmark.

Deliver the revised text followed by unresolved asset-pricing evidence gaps and a short failure-mode audit.
