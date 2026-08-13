# SELF-USE SYNTHETIC TASK

All facts below are invented for testing. Do not add citations, estimators, or results not supplied.

Use `finance-causal-empirical-writing` to audit and rewrite the identification/results narrative for a JF paper.

- Policy: states introduce a guarantee registry in staggered years from 2012 to 2019.
- Unit of treatment: state-year. Unit of observation: small-business loan application.
- Intended estimand: ATT on approval probability during the first two post-adoption years for applicants in adopting states.
- Current TWFE uses never-treated, not-yet-treated, and already-treated states as controls.
- A cohort-time estimator using not-yet-treated states gives +2.4 percentage points, 95% CI [0.5, 4.3]. Baseline approval is 36%.
- Event time −2 is +1.1 percentage points, 95% CI [0.2, 2.0]. The registry was publicly announced about nine months before implementation.
- Application volume rises 4% after announcement; applicant observables are stable, but unobserved borrower composition is unavailable.
- Standard errors are clustered by state; there are 24 treated and 8 never-treated states.
- No spillover test across bordering states is supplied.

The draft says: “Parallel trends is satisfied, and the registry causally raises credit supply by 2.4 percentage points.”

Deliver:

1. A prioritized audit.
2. A rewritten design/results passage.
3. The strongest currently defensible headline sentence.
