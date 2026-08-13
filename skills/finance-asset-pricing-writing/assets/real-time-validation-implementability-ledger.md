# Real-Time, Validation, and Implementability Ledger

Copy this template into the working paper folder and fill it before drafting data, design, validation, or strategy claims. Use `unknown` rather than supplying a conventional choice. Delete rows that are genuinely inapplicable only after recording why.

## 1. Research object

| Field | Entry | Source / exhibit | Unresolved decision |
|---|---|---|---|
| Target claim: document / predict / price / explain / implement |  |  |  |
| Asset universe and target population |  |  |  |
| Sample period and frequency |  |  |  |
| Headline return / pricing / forecast object |  |  |  |
| Benchmark and economic comparator |  |  |  |
| Discovery status: inherited / searched / prespecified |  |  |  |

## 2. Real-time availability

Complete one row for every input that could mechanically leak future information.

| Input / feature | Economic measurement date | Public/vendor release date | Revision or vintage policy | Assumed reporting lag | Portfolio-formation date | First feasible trade date | Evidence for timing |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Record separately:

```text
Historical vintage files available?:
Point-in-time constituent/security universe?:
Dead securities and delisting returns included?:
Preprocessing estimated using future observations?:
Normalization/imputation refit inside each training window?:
Entity, industry, fund-family, or network leakage risk?:
Minimum implementable delay and delayed-result estimate?:
```

## 3. Construction and inference

| Choice | Main specification | Alternatives tested | Why it matches the economic object | Exhibit / code source |
|---|---|---|---|---|
| Signal transformation and missing values |  |  |  |  |
| Universe filters and delistings |  |  |  |  |
| Breakpoints and portfolio count |  |  |  |  |
| Weights and rebalance frequency |  |  |  |  |
| Holding horizon / overlapping returns |  |  |  |  |
| Long and short leg definitions |  |  |  |  |
| Factor/model benchmark |  |  |  |  |
| Standard errors / dependence |  |  |  |  |

## 4. Discovery and validation separation

| Stage | Dates / markets / assets | What was chosen or tuned here? | Frozen before next stage? | Primary metric | Result with uncertainty |
|---|---|---|---|---|---|
| Discovery / training |  |  |  |  |  |
| Validation / tuning |  |  |  |  |  |
| Final holdout |  |  |  |  |  |
| Post-discovery / postpublication |  |  |  |  |  |
| External market / asset class |  |  |  |  |  |

```text
Candidate/search space:
Multiple-testing, shrinkage, or model-selection adjustment:
Simple economic/statistical benchmark:
Decision rule fixed before final evaluation:
Validation result weaker than discovery result? If yes, how will the claim narrow?:
```

## 5. Implementability bridge

Before performing gross-to-net arithmetic, record the exact turnover definition and the cost application rule (per side, per round trip, or another stated convention). If either is unknown, retain the symbolic calculation and mark net performance unresolved; never infer or silently insert a factor of two.

| Friction | Main assumption | Data/source | Sensitivity range | Gross-to-net effect | Residual boundary |
|---|---|---|---|---|---|
| Turnover |  |  |  |  |  |
| Bid–ask spread and commissions |  |  |  |  |  |
| Market impact |  |  |  |  |  |
| Short availability and borrow fee |  |  |  |  |  |
| Delay / stale information |  |  |  |  |  |
| Leverage and funding |  |  |  |  |  |
| Capacity and crowding |  |  |  |  |  |
| Asset availability / investor access |  |  |  |  |  |

## 6. Claim reconciliation

| Proposed sentence | Evidence object | Discovery or evaluation? | Gross or net? | Risk / mispricing / prediction / causal status | Safe wording | Remaining caveat |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Before using `out of sample`, `alpha`, `risk price`, `mispricing`, or `implementable`, verify that the corresponding row is complete. Reconcile the ledger against the abstract, introduction, headline table, and conclusion; do not combine a magnitude, benchmark, sample, or cost assumption drawn from different specifications.
