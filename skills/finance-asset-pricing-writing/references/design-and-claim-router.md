# Asset-Pricing Design and Claim Router

## Route by target claim

| Target claim | Minimum evidence | Safe framing |
|---|---|---|
| New return fact | Reproducible construction, magnitude, uncertainty, influential-observation analysis | `documents` |
| Predictability | Real-time timing, holdout evaluation, benchmark forecasts, economic loss/utility | `predicts` |
| Factor/model performance | Pricing errors, fit, redundancy, competing models, economically motivated tests | `prices/explains within...` |
| Risk mechanism | Priced-state exposure, model-specific cross-sectional/time-series predictions | `supports a risk-based account` |
| Mispricing mechanism | Belief/constraint proxies, correction dynamics, rejected risk alternatives | `is consistent with / supports mispricing` |
| Fund skill | Appropriate benchmark, holdings/returns timing, persistence, fees, selection and incubation | `evidence of performance/skill conditional on...` |
| Implementable strategy | Realistic costs, shorting, turnover, capacity, delay, live/holdout evidence | `implementable under stated assumptions` |
| Causal channel | Exogenous variation plus causal assumptions and validation | Use causal language only for that channel |

## Contribution test

Complete:

```text
Existing frontier:
Unresolved economic question:
Why existing tests cannot resolve it:
New asset/data/model/test:
Main magnitude relative to benchmark:
What interpretation changes:
Validation that makes the change credible:
Scope and remaining ambiguity:
```

Do not claim contribution from another characteristic, factor, or machine-learning model unless it changes an economic conclusion or validation standard.

## Hybrid routing

- Use `$finance-causal-empirical-writing` when an exogenous shock identifies how an institution changes prices/returns.
- Use `$finance-intermediation-markets-writing` when dealer balance sheets, funding, trading protocols, or price discovery are the central mechanism.
- Use `$finance-theory-structural-writing` when equilibrium primitives, structural parameters, or counterfactual welfare carry the contribution.

Keep one primary logic. Explain how secondary modules support rather than redefine the paper.
