# Results and interpretation

> SYNTHETIC SELF-USE OUTPUT: all manuscript facts below were invented for this test.

Among U.S. common stocks, customer-review dispersion is associated with a sizeable return spread in the discovery sample, but the relation weakens sharply as the evaluation becomes more independent. The portfolios are value-weighted deciles formed from NYSE breakpoints and include delisting returns. From 2006 through 2015, the high-minus-low portfolio earns 0.52% per month (t = 3.10). Its five-factor alpha is 0.41% per month, indicating that the discovery-sample spread is not absorbed by that benchmark. This alpha is a benchmark-relative result, not evidence that the spread represents mispricing: no belief, constraint, correction-dynamics, or priced-state test is supplied.

The 2016–2020 estimate does not provide a clean out-of-sample test. Although the spread remains positive at 0.31% per month (t = 2.05), this period was repeatedly used to choose features and lags. It is therefore a tuning or validation sample, not an untouched holdout. The only final untouched test is 2021–2024, in which the spread falls to 0.08% per month (t = 0.62). Excluding microcaps changes the estimate to −0.03% per month (t = −0.20). The independent evidence is consequently both economically small and statistically imprecise, and the microcap exclusion removes rather than strengthens the positive point estimate. An untouched-test five-factor alpha is not supplied, so the discovery alpha cannot be carried into the later period.

Implementation evidence further narrows the claim. The portfolios turn over 190% per month, and the supplied spread-and-commission estimate is 35 basis points per one-way trade. These inputs cannot yet be converted into a defensible monthly net return because the turnover statistic is not defined by trading side or round trip, and the cost application rule is not stated. The manuscript should disclose both conventions and show the gross-to-net calculation rather than silently inserting a factor of two. Borrow availability, market impact, and capacity are also unmeasured. The evidence therefore supports neither a numerical net payoff nor an implementability claim.

The supported conclusion is narrower: customer-review dispersion organizes a positive discovery-sample return pattern, but the relation decays in the only untouched period and does not survive microcap exclusion there. Timestamped reviews help establish when surviving observations were posted, yet unavailable deletion histories leave a residual real-time data-availability concern. The evidence does not establish robust out-of-sample performance, mispricing, or a readily tradable anomaly.

## Evidence boundaries

1. **Search:** 2016–2020 was used for feature and lag selection and is not an independent holdout.
2. **Stability:** the untouched estimate is 0.08% monthly and turns slightly negative after excluding microcaps.
3. **Interpretation:** discovery alpha is benchmark-relative evidence, not a test that distinguishes risk from mispricing.
4. **Feasibility:** the turnover/cost mapping is undefined, and borrow, impact, and capacity evidence is missing; no numerical net-return or implementable-strategy claim is supported.
