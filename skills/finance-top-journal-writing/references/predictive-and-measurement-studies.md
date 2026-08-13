# Predictive and Measurement Studies

## Route the contribution

Choose the primary claim before drafting:

| Claim | Required evidence | Safe wording |
|---|---|---|
| New measure | Construct validity, timing, reliability, benchmark constructs | `measures`, `captures`, `is associated with` |
| Incremental prediction | Honest holdout design, benchmark, uncertainty, calibration or decision value | `improves prediction in...` |
| Economic interpretation | Distinctive implications that separate the construct from alternatives | `supports` or `is consistent with` |
| Causal effect | Exogenous variation and articulated assumptions | Use causal verbs only for the identified margin |

Do not turn a predictor into a mechanism or a semantic/ML score into the underlying economic construct by definition.

## Build the prediction ledger

Record:

1. Prediction target, horizon, unit, event prevalence, and decision context.
2. Construction sample and the time at which each input becomes observable.
3. Train, tuning/validation, and locked test units and dates.
4. Entity or network grouping used to prevent leakage.
5. Benchmark models, variables, and information sets.
6. Primary performance metric with uncertainty and a paired comparison.
7. Calibration, threshold performance, and economic or decision value when relevant.
8. Missingness, drift, retraining, subgroup performance, and external validation.
9. Whether the exercise explains, predicts, ranks, classifies, or measures.

Time ordering is necessary but not sufficient for an honest holdout. The same firm, borrower, customer network, event, or revised data can leak across splits even when observations have different dates.

## Validate a constructed measure

Separate four questions:

- **Content validity:** Does the construction match the intended economic object?
- **Convergent/discriminant validity:** Does it relate to nearby constructs without collapsing into them?
- **Reliability:** Is it stable to reasonable coding, model, aggregation, and data-source choices?
- **Incremental validity:** Does it add information beyond an appropriate benchmark?

A variable can predict an outcome without being a valid measure of the proposed mechanism. Name alternative meanings—complexity, style, data coverage, composition, or mechanical scaling—and test their distinctive implications.

## Report results

Give the baseline prevalence or loss, the performance change, uncertainty, and the exact evaluation sample. Avoid `superior` from a small AUC or R-squared increase without a paired comparison and decision benchmark. For rare outcomes, report precision/recall or other threshold behavior in addition to rank metrics when decisions depend on classification.

Keep model selection separate from final evaluation. If the specification, embedding, prompt, variable family, or horizon was chosen after seeing the test set, relabel that set as development and obtain a new holdout.

## Bound interpretation

- Prediction does not establish causality.
- Attention weights, feature importance, and SHAP values describe a fitted model; they do not identify an economic mechanism.
- A better test metric does not ensure economic materiality, calibration, portability, or policy value.
- A proprietary or historically reconstructed input requires a vintage and availability audit before a real-time claim.
- External validation changes the population tested; it does not automatically validate the construct everywhere.

Deliver missing split, leakage, benchmark, uncertainty, calibration, and construct-validity evidence as named gaps rather than generic requests for robustness.
