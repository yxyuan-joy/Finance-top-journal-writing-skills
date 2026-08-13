---
name: finance-intermediation-markets-writing
description: Draft, revise, or audit financial-intermediation and market-structure manuscripts for The Journal of Finance (JF), Journal of Financial Economics (JFE), or The Review of Financial Studies (RFS). Use when the central claim concerns banks, nonbank intermediaries, credit supply, deposits and funding, balance sheets, collateral, screening and contracting, liquidity, dealer behavior, trading venues, order flow, price discovery, market design, networks, runs, funding fragility, regulation, or institutional market mechanisms. Do not use for generic corporate-finance writing, pure return-factor studies, or theory/structural papers in which institutional evidence is secondary.
---

# Finance Intermediation and Markets Writing

Center the paper on an institutional mechanism connecting agents, constraints, choices, and market outcomes. Use `$finance-top-journal-writing` with this skill when installed.

Use [evidence-basis.md](references/evidence-basis.md) as an optional searchable provenance catalog. Consult it only when a mechanism-specific anchor or provenance check would help; search by subtype/function and read only matching rows rather than loading all 60 papers. It supplies bounded teaching functions, not language to copy.

## Route the mechanism

Choose the primary lane:

- **Intermediation**: bank/nonbank balance sheets, funding, deposits, capital, liquidity transformation, screening, monitoring, contracting, credit supply.
- **Market structure**: dealers, venues, order types, matching, fees, latency, inventory, price discovery, liquidity, execution, market design.
- **Network/fragility**: exposures, runs, fire sales, collateral chains, contagion, amplification, systemic risk.
- **Regulation/policy**: rules change intermediary or trader incentives, constraints, incidence, and equilibrium outcomes.

Read [mechanism-router.md](references/mechanism-router.md). Use at most two lanes and state which is primary.

## Build the institutional fact ledger

Record:

1. Agents, contracts/venues, sequence, and information.
2. Balance-sheet or trading constraint and how it is measured.
3. Decision margin: lending, pricing, screening, inventory, routing, withdrawal, collateral, entry, or another choice.
4. Data granularity, timestamps, identifiers, and linkage.
5. Source of variation or model mechanism.
6. Outcome and incidence across counterparties.
7. Selection, demand, equilibrium, and spillover risks.
8. Main magnitude in institutionally meaningful units.
9. Evidence separating the proposed channel from alternatives.

Do not call a quantity change `credit supply`, `liquidity`, or `price discovery` without showing why the measure captures that object.

## Draft the paper

Read [section-blueprints.md](references/section-blueprints.md).

### Introduction

Open with the institutional friction or market-design tension. Explain why observing equilibrium quantities/prices alone does not reveal the proposed channel. Describe the institution, leverage, main magnitude, incidence, and equilibrium boundary. Compare against the closest mechanism paper.

### Institutional setting

Use a flow or timeline when it clarifies contracts, order handling, settlement, funding, or regulatory implementation. State who observes what and when; identify strategic responses.

### Data and measurement

Explain entity resolution, lender/borrower or trader/venue linkage, timestamp alignment, quote/trade classification, balance-sheet frequency, censoring, and aggregation. Distinguish posted from executed prices, commitments from originations, applications from approvals, and gross from net exposures.

### Design/results

Separate the institutional margin from aggregate equilibrium outcomes. For credit papers, distinguish supply, demand, borrower selection, and composition. For market papers, distinguish liquidity dimensions, information, inventory, and mechanical price effects. For network papers, separate direct exposure from propagation.

When the paper combines facts and a model, give them different jobs: facts establish the institutional object and motivating patterns; the model separates forces or closes a counterfactual; untargeted evidence evaluates whether that closure is credible. Never relabel a model-based decomposition as model-free evidence.

Read [threats-and-validation.md](references/threats-and-validation.md).

## Write mechanisms and policy carefully

- A balance-sheet correlation is not a supply channel without demand/selection evidence.
- A spread change is not automatically improved liquidity or welfare.
- Faster price adjustment is not automatically more informative prices.
- A local lender/venue response may be offset by substitution elsewhere.
- Regulatory incidence may fall on borrowers, depositors, traders, intermediaries, or entry.
- Welfare requires an explicit benchmark and externalities, not just a lower price or higher quantity.

Use `$finance-causal-empirical-writing` if causal identification drives the contribution. Use `$finance-theory-structural-writing` when counterfactual policy or welfare depends on an estimated model.

## Integrate exhibits

Read [exhibits-and-appendix.md](references/exhibits-and-appendix.md). Include institutional maps/timelines only when they clarify the mechanism. Table notes must state aggregation, timing, side of market, units, fixed effects, and inference. Display both quantity and price/margin when their joint movement identifies incidence.

## Apply hard gates

1. The institutional mechanism can be stated as agents → constraint/information → action → outcome.
2. Every central proxy has a construct-validity argument.
3. Credit supply is separated from demand and selection.
4. Liquidity/price discovery labels match measured dimensions.
5. Timing and aggregation do not create mechanical relations.
6. Substitution, spillovers, and equilibrium response remain visible.
7. Policy claims identify incidence and a welfare benchmark or stay descriptive.
8. Local evidence is not generalized to the entire market without support.
9. Price, quantity, selection, and incidence evidence appear together when the channel requires their joint movement.

Deliver the requested text first. Add a compact `Mechanism boundary` and deduplicated institutional-validity risks when they materially constrain the claim; do not emit every internal ledger by default.
