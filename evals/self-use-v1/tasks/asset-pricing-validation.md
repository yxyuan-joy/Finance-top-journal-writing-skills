# SELF-USE SYNTHETIC TASK

All facts below are invented for testing. Do not add citations or facts.

Use `finance-asset-pricing-writing` to draft a results-and-interpretation section for an RFS return-prediction paper.

- Signal: customer-review dispersion measured monthly.
- Universe: U.S. common stocks, 2006–2024; value-weighted deciles using NYSE breakpoints; delisting returns included.
- Reviews posted during month `t` are timestamped, but deletion histories are unavailable.
- Discovery period: 2006–2015. High-minus-low return = 0.52% per month, t = 3.10.
- Validation period: 2016–2020, used repeatedly for feature and lag selection. Return = 0.31%, t = 2.05.
- Final untouched test: 2021–2024. Return = 0.08%, t = 0.62.
- Excluding microcaps in the untouched test: −0.03%, t = −0.20.
- Five-factor alpha in discovery: 0.41% monthly; untouched-test alpha not supplied.
- Turnover = 190% monthly. A simple spread-and-commission estimate is 35 basis points per one-way trade.
- Borrow availability, market impact, and capacity are not measured.

The current draft calls the signal “robust out-of-sample mispricing and a readily implementable anomaly.”

Deliver a 350–500-word results-and-interpretation section plus a four-item evidence-boundary list.
