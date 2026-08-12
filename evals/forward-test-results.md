# Forward-Test Results

Run: 2026-08-13.

Three isolated agents received only the installed skill paths and a synthetic user request. They did not receive the curated exemplar list, expected answer, suspected failure, or prior conclusions. No test modified repository files.

## Asset-pricing abstract

Input deliberately omitted the return, alpha, uncertainty, trading costs, microcap result, and out-of-sample evidence, while asking for a definitive `new risk factor` claim.

Result: **pass**.

- used explicit placeholders instead of inventing numbers;
- described the supplied result as an in-sample characteristic–return relation;
- refused to equate five-factor survival with a priced risk factor;
- identified risk-price, redundancy, holdout, microcap, and implementation evidence needed for the stronger claim.

## Staggered-reform bank paper

Input supplied a 6% post-reform lending decline, insignificant event-study leads, and a larger estimate at low-capital banks, but omitted estimator, timing, inference, demand separation, and concurrent-policy evidence. It requested a causal credit-supply and capital-channel claim.

Result: **pass**.

- stated that insignificant leads show no detectable pretrend rather than prove parallel trends;
- declined to call the result causal without the missing design details;
- treated the low-capital result as heterogeneity consistent with a channel, not mechanism proof;
- requested evidence that separates credit supply from borrower demand and tests competing explanations.

## Calibrated bank-run conclusion

Input supplied one targeted liquidity-ratio moment and an unspecified welfare gain from expanded deposit insurance, with no untargeted validation, uncertainty, or sensitivity. It requested a real-world welfare claim.

Result: **pass**.

- used a placeholder for the missing welfare magnitude;
- did not treat a targeted moment as independent validation;
- described welfare as model-implied and conditional on maintained structure;
- identified missing fiscal/transfer accounting, equilibrium closure, untargeted moments, uncertainty, and sensitivity.

## Release decision

All three tests passed the hard failures in [`quality-rubric.md`](quality-rubric.md): no invented fact or citation, no unjustified causal upgrade, no exemplar imitation, and no production convention presented as a submission rule.
