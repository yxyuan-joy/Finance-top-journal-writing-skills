---
name: finance-theory-structural-writing
description: Draft, revise, or audit formal-theory, structural-estimation, calibration, quantitative-model, counterfactual, and welfare-analysis manuscripts for The Journal of Finance (JF), Journal of Financial Economics (JFE), or The Review of Financial Studies (RFS). Use when the contribution depends on model primitives, timing and information, equilibrium characterization, propositions and proofs, comparative statics, structural identification, estimation or calibration, model fit, quantitative decomposition, counterfactual experiments, policy design, or welfare. Do not use for ordinary reduced-form empirical papers, generic mathematical exposition, or empirical asset-pricing papers without a central formal or structural model.
---

# Finance Theory and Structural Writing

Make the model's economic mechanism, identification, and domain visible. Use `$finance-top-journal-writing` with this skill when installed.

Read [evidence-basis.md](references/evidence-basis.md) when choosing among pure theory, structural estimation, quantitative/calibrated work, and theory–empirics hybrids. Its independent 50-paper portfolio records both the reusable move and its boundary; do not make fit or identification compulsory for pure theory.

## Route the paper

Choose one primary type:

- **Pure theory**: mechanism, equilibrium, proposition, comparative statics, welfare.
- **Quantitative/calibrated model**: disciplined parameters/moments, fit, decomposition, counterfactual.
- **Structural estimation**: data-to-model mapping, parameter identification, estimation, fit, counterfactual.
- **Theory–empirics hybrid**: model generates discriminating predictions tested in data.

Read [model-router.md](references/model-router.md). Do not describe calibration as identification or reduced-form validation as structural fit.

## Build the model ledger

Record:

1. Economic question and why a model is needed.
2. Agents, objectives, constraints, timing, information, and equilibrium concept.
3. Central friction/market incompleteness and benchmark without it.
4. Key assumptions and the results each one drives.
5. Endogenous objects and mechanism.
6. Main proposition/comparative static or parameter/counterfactual result.
7. Mapping between model objects and data.
8. Identification/calibration sources for parameters.
9. Targeted and untargeted moments, fit, and validation.
10. Counterfactual closure, policy experiment, welfare criterion, and sensitivity.

Never invent a theorem condition, parameter source, moment, or welfare number.

## Draft the paper

Read [section-blueprints.md](references/section-blueprints.md).

### Abstract/introduction

Lead with the economic puzzle and missing mechanism, not notation. State the model environment/friction, core equilibrium mechanism, decisive result, and empirical/quantitative discipline. For counterfactuals, report magnitude and maintained structure.

### Model setup

Present timing and information early. Define primitives separately from endogenous objects. Explain each assumption's economic role. Introduce notation only when it will be used. Compare with a transparent benchmark.

### Results

For each proposition: statement → conditions → economic intuition → comparative static/equilibrium implication → proof location. Do not replace intuition with algebra. Distinguish existence, uniqueness, characterization, and normative results.

For a theory–empirics hybrid, derive a small set of predictions that differ from the benchmark or a live competing mechanism, then map each prediction to an observable test. A model that can rationalize the baseline fact after the fact has not yet earned a discriminating empirical claim.

### Structural/quantitative sections

Explain which variation or moments identify each parameter, what is calibrated externally, estimation uncertainty, fit, and where the model misses. Separate targeted from untargeted moments. Establish fit before counterfactuals.

Read [identification-fit-and-counterfactuals.md](references/identification-fit-and-counterfactuals.md).

### Welfare/policy

Define whose welfare, resource/transfer accounting, externalities, planner information/commitment, equilibrium response, and implementation constraints. A higher output, price, liquidity, or credit quantity is not automatically higher welfare.

## Connect theory and evidence

Read [theory-empirics-interface.md](references/theory-empirics-interface.md). Label evidence as:

- motivating fact;
- calibrated/targeted moment;
- parameter-identifying variation;
- overidentifying/untargeted validation;
- qualitative prediction;
- quantitative fit;
- counterfactual output.

Do not use the same moment as both identification and independent validation without disclosure.

## Package proofs and exhibits

Read [proofs-exhibits-and-appendix.md](references/proofs-exhibits-and-appendix.md). Keep economic intuition in the main text and long derivations in a stable proof appendix. Use model figures/tables to show mechanism, fit, parameter sensitivity, and counterfactual decomposition—not decorative simulations.

## Apply hard gates

1. Timing, information, agents, choices, and equilibrium are explicit.
2. Assumptions are linked to results and plausible alternatives.
3. The benchmark reveals what the friction adds.
4. Proposition conditions and proof references match.
5. Structural identification differs from calibration and normalization.
6. Fit is shown before counterfactual interpretation.
7. Targeted and untargeted moments are labeled.
8. Counterfactual and welfare claims remain conditional on maintained structure.
9. Sensitivity covers economically central assumptions/parameters.
10. Reduced-form evidence is not described as proof of the entire model.
11. Every central friction is evaluated against a transparent benchmark without that friction or with a competing closure.

Deliver revised text plus `Maintained structure`, `Identification/fit boundary`, and unresolved proof or counterfactual gaps.
