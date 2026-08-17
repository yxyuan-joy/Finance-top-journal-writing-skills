# Asset-Pricing Section Blueprints

Use this workflow to turn an evidence ledger into prose. Treat the listed paragraph jobs as functions, not a mandatory paragraph count: combine adjacent jobs for a short paper and split a dense job when the evidence requires it. Draft only after fixing the target claim—documentation, prediction, model evaluation, risk price, mechanism, or implementability.

## Atomic evaluation state

Before drafting, attach a single evaluation-state record to every performance, fit, or prediction number. Retain every applicable field together:

- sample or universe and period;
- discovery-versus-evaluation status;
- estimation mode;
- benchmark;
- gross-versus-net status;
- cost coverage;
- implementation delay; and
- aggregation, netting, and overlap treatment.

Treat these as independent axes. Never use one axis as shorthand for another, silently carry a label across a changed specification, or combine a number with state fields from another result. Preserve the record across prose, exhibits, and sections. If a field is unknown, mark it and narrow or omit the claim; do not guess. In an abstract or introduction, select only numbers whose applicable state can be conveyed without crowding the argument. Omit a secondary number rather than detach it from the information needed to interpret it.

## Sections

[Abstract](#abstract) · [Introduction](#introduction) · [Design](#data-timing-and-empirical-design) · [Results](#results) · [Validation](#validation-and-interpretation) · [Conclusion](#conclusion)

## Abstract

### Content jobs

Select and combine these jobs without imposing a fixed sentence count:

1. **Question and economic object.** Name the expected-return, pricing, forecasting, or investor-decision question without opening on a method or dataset.
2. **Universe and test.** Give the asset universe, period, signal/model, and whether the evaluation is in sample, held out, post-discovery, or live.
3. **Headline result.** Report one central magnitude with frequency, units, uncertainty, and benchmark: for example, a monthly long–short spread, pricing-error reduction, or out-of-sample loss improvement.
4. **Credibility.** Name the validation that most directly addresses the leading failure mode, such as real-time availability, a frozen holdout, international evidence, or realistic costs.
5. **Interpretation and boundary.** State what the result changes and retain the main ambiguity or scope limit.

Do not walk through the fact ledger. Keep only the evidence necessary to identify the headline claim, its comparator, its credibility, and its binding boundary. Route secondary estimates and the rest of their evaluation states to later sections.

### Required facts

Know the sample endpoints, asset filters, construction timing, benchmark, headline estimate, inference, validation status, and implementation assumptions. If any are missing, insert a visible placeholder or remove the unsupported clause.

### Overclaim traps

Do not call an in-sample pattern predictive, a statistical alpha implementable, a model rejection proof of mispricing, or exposure to a factor evidence that the factor is priced. Do not say `out of sample` when tuning touched the evaluation period.

### Exit check

A reader should be able to identify the economic object, test population, magnitude, comparator, validation regime, and claim boundary without consulting the paper.

## Introduction

### Argument jobs

Select and combine only the jobs needed for the paper; they do not prescribe a paragraph count:

1. **Economic tension.** Establish the pricing fact, model disagreement, or investor problem. Explain the consequence of resolving it—do not merely announce another characteristic or factor.
2. **Why the frontier is insufficient.** Identify the closest evidence and its binding limitation: timing, benchmark, search, measurement, economic mechanism, or feasibility. Avoid a broad literature inventory.
3. **Resolution.** Explain the new object, data, model, or test and why it addresses that limitation. Give enough construction timing to make the design credible.
4. **Headline evidence.** Report the smallest sufficient set of main magnitudes in interpretable units, preserving the full applicable evaluation state. Include raw and benchmark-adjusted objects together only when the contrast is necessary to interpret the claim.
5. **Validation.** Present the smallest discriminating set of tests that bears directly on the leading alternative explanation. Explain what each rules down rather than listing robustness checks.
6. **Economic interpretation.** Distinguish risk, mispricing, institutional, and statistical-learning accounts. State the distinctive prediction tested and any live competing account.
7. **Contribution.** State precisely whether the paper changes a known fact, model assessment, mechanism, validation standard, or feasible-investment conclusion. Compare with the closest work by economic function.
8. **Roadmap only if useful.** Include a short map when the paper has an unusual sequence; do not repeat the table of contents mechanically.

Do not serialize construction choices, validation regimes, or implementation assumptions into the introduction. Retain every applicable state field for each selected headline number; achieve brevity by selecting fewer numbers, not by dropping state fields. Route the complete audit trail to design, results, exhibits, or the appendix.

For a factor-extraction, test-asset, or diagnostic methodology paper, add a conceptual bridge before treating construction as an empirical recipe:

```text
economic pricing object
→ recoverability, spanning, or information condition
→ observable failure if that condition is incomplete
→ feasible sample construction
→ holdings/return/factor structure
→ pricing or model-diagnostic tests
```

The bridge may be formal theory or a transparent economic restriction. Its job is to explain why the proposed construction can recover the claimed object and which later tests can reveal missing priced dimensions. Do not place a long mathematical section first merely because the paper introduces a method; use it only when the empirical object would otherwise be uninterpretable.

### Required facts

Complete the contribution test, construction/availability timeline, magnitude benchmark, discovery-versus-evaluation status, main failure mode, and interpretation boundary before drafting.

### Overclaim traps

Novel data are not a contribution by themselves. More factors or a higher t-statistic do not establish better economic explanation. A mechanism proxy that correlates with returns is not mechanism identification. Cross-market replication is not automatically independent if definitions were adapted after observing results.

### Exit check

Every paragraph must advance `question → unresolved limitation → test → evidence → interpretation → contribution`; delete material that only signals familiarity with the literature.

## Data, timing, and empirical design

### Block jobs

1. **Target universe.** Define databases, dates, securities/assets, exchanges, share classes, filters, delistings, missing observations, and the population to which the claim applies.
2. **Information timeline.** For every signal input, record measurement date, vendor release/publication date, revision policy, reporting lag, portfolio-formation date, and first feasible trade date. Distinguish today’s cleaned file from historically available information.
3. **Construction.** Define transformations, winsorization, breakpoints, weights, long and short legs, rebalance frequency, holding horizon, overlapping returns, and treatment of microcaps or illiquid assets.
4. **Estimating object.** Define the return, alpha, price of risk, pricing error, forecast target, loss function, or utility object. Explain benchmark factors/models, fixed choices, standard errors, and dependence.
5. **Discovery and evaluation.** Identify what was searched or tuned, the candidate space, preprocessing, train/validation/test split, stopping rule, and whether entities or networks can leak across splits. Label the evaluation regime precisely: a resampled or rolling temporal exercise, a frozen holdout, a post-discovery/postpublication period, an external market, and live evidence provide different kinds of support. Do not compress all of them into `out of sample`.
6. **Implementation environment.** State turnover, delay, spreads/impact, borrow availability and fees, leverage/funding, capacity, and investability assumptions when strategy language is used.

Use the fillable [real-time, validation, and implementability ledger](../assets/real-time-validation-implementability-ledger.md) before writing this section.

### Overclaim traps

Database timestamps need not equal investor availability. A conventional lag is not evidence that a variable was observable. Value weighting does not by itself eliminate microcap influence. Random cross-validation can leak future regimes or the same firm/network into training and testing. Annualizing a short sample can obscure instability.

### Exit check

An independent researcher should be able to reconstruct the information set, portfolios or estimating equations, benchmark, evaluation split, and reported units without guessing a convention.

## Results

### Evidence-block jobs

1. **Economic shape.** Show portfolio legs, monotonicity, distribution, or response surface before reducing the finding to one spread or coefficient.
2. **Baseline magnitude.** Report the target estimate, units, horizon, standard error or interval, sample size, and economically meaningful comparator.
3. **Benchmark adjustment or model fit.** Separate raw returns from alpha, fit gains from forecast gains, and average pricing errors from economically important misspecification.
4. **Influence and stability.** Diagnose microcaps, short legs, extreme periods, industries, countries, liquidity, alternative weights, and reasonable construction choices. Say whether the result attenuates, disappears, reverses, or becomes imprecise.
5. **Independent validation.** Report frozen-holdout, post-discovery, postpublication, international, other-asset, or live evidence separately from discovery evidence. Preserve null or weaker validation results.
6. **Economic survival.** If feasible-investment language is material, report turnover and cost assumptions, net performance, shorting/capacity limits, and sensitivity to delay.

### Overclaim traps

Do not mix a coefficient from one specification with the sample size, benchmark, or baseline mean from another. Do not present a robustness table as votes for the hypothesis. Statistical survival after factor adjustment is not economic survival after costs. A small average pricing error can coexist with failure on the economically central assets.

### Exit check

Each block should begin with the claim it tests and end with what changed relative to the prior block. Tables and prose must use the same sample, units, model label, and evaluation regime.

## Validation and interpretation

### Paragraph jobs

1. Name the leading failure mode and the diagnostic designed for it.
2. Report the diagnostic result and the part of the headline claim it supports.
3. State the residual threat; no validation should be described as universal proof.
4. For a risk account, connect exposures to a priced state and test model-specific predictions. For mispricing, test belief/constraint and correction dynamics against credible risk alternatives. For an institutional account, measure the operative constraint or flow. For machine learning, separate prediction, feature attribution, and causal mechanism.
5. Reconcile validation failures rather than burying them: narrow the universe, period, mechanism, or implementability claim as required.

### Exit check

The interpretation must be no stronger than the most discriminating evidence, and every robustness exercise must name the threatened claim it addresses.

## Conclusion

### Paragraph jobs

1. Answer the opening economic question with the exact object learned and its target universe.
2. State the evidence that most changes prior understanding, not a full results recap.
3. Preserve the binding boundary—sample, search, benchmark, instability, mechanism ambiguity, or implementation.
4. Give an implication for modeling, measurement, or investor decisions only at the level supported by the design.

### Final output check

Verify that the abstract, introduction, results, and conclusion use the same headline estimate, units, benchmark, validation label, and claim strength. Keep prediction distinct from causality, model rejection from proof of an alternative, and gross statistical payoff from feasible net performance.
