# Asset-Pricing Validation and Robustness

## Threat matrix

| Threat | Useful diagnostics | Residual caution |
|---|---|---|
| Look-ahead | publication/availability lags, vintage data, delayed implementation | vendor timestamps may not equal investor availability |
| Survivorship/delistings | dead securities, delisting returns, entry/exit rules | historical coverage may remain uneven |
| Microcaps/outliers | exchange breakpoints, value weights, price/liquidity filters, influence plots | filters alter the target universe |
| Data mining | declared search space, multiple-testing correction, holdout, shrinkage | holdout choices may still be adaptive |
| Factor redundancy | spanning, nested comparison, factor zoo benchmarks | statistical spanning is not economic equivalence |
| Instability | subperiods, rolling estimates, international/other assets | external samples differ institutionally |
| Costs/shorting | turnover, spreads/impact, borrow fees, short availability, capacity | historical costs may not be tradable in size |
| Publication decay | post-sample and postpublication tests | market adaptation and regime change coexist |
| Inference | time-series dependence, cross-sectional correlation, generated regressors | standard errors do not fix design/search bias |

## Reporting rules

- State the threatened claim before the test.
- Distinguish attenuation, disappearance, sign reversal, and imprecision.
- Report whether a filter removes observations or changes portfolio construction.
- Show long and short legs when one side drives the spread.
- Separate statistical survival from economic survival after costs.
- Treat null holdout evidence as informative rather than hiding it.

## Machine-learning additions

- Describe feature availability and preprocessing inside each training fold.
- Prevent leakage from normalization, missing-value imputation, and hyperparameter selection.
- Use time-respecting splits and rolling/expanding evaluation when appropriate.
- Compare against simple economic and statistical benchmarks.
- Report economic loss/utility or portfolio performance, not only prediction metrics.
- Separate interpretation tools from causal mechanism evidence.
