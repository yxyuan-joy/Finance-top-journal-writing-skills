# Intermediation and Markets Section Blueprints

Use this workflow for bank, nonbank, credit, market-structure, network, and regulatory papers. Select only the modules the paper actually supports. Before drafting, fix one primary mechanism chain and complete the relevant rows of the [mechanism–incidence map](../assets/mechanism-incidence-map.md). The map is an internal control document; deliver it only when requested.

## Drafting sequence

1. Write the institutional object in one sentence: agent → constraint, information, or rule → decision → market outcome.
2. Fix the unit, timing, comparison, and measured price/quantity objects.
3. Rank evidence by function, then draft from that ranking rather than narrating tables in numerical order.
4. Remove claims that require an unfilled map cell.

For a hybrid empirical intermediation paper, separate three evidence levels before drafting:

```text
institutional and descriptive evidence: what the intermediary, contract, or venue does
→ identified intermediary response: how entry, supply, pricing, or substitution changes
→ counterparty outcome: what happens to borrowers, traders, firms, or the market
```

The levels may use different units, comparisons, estimands, and selection assumptions. Agreement across them can build a mechanism chain, but evidence at one level does not inherit the causal strength of another. If several shocks support the same response, synthesize them by their different assumptions and populations rather than inventing separate contributions.

## Abstract

**Function.** Compress the institutional mechanism and evidence into a self-contained claim. A useful five-sentence order is: institutional tension; setting and design/model; behavioral response; price, quantity, or incidence magnitude; interpretation and boundary. Use fewer sentences when they perform the same jobs.

**Required evidence.** Name the agents, decision margin, variation or model discipline, market, and estimand. Report the headline magnitude with unit and benchmark. If the mechanism depends on joint movement, state both price and quantity, or quantity and selection. Say whether the result is local, short-run, partial-equilibrium, or model-dependent.

**Common overclaims.** Do not turn lower lending into tighter supply without demand or selection evidence; a narrower spread into higher welfare; faster price response into better price discovery; a regulatory exposure into compliance; or a model decomposition into model-free causality. Avoid listing every robustness check.

**Output gate.** A reader can identify who changes what, relative to which counterfactual, by how much, and why the evidence favors the stated channel. Every number has a unit. The final sentence does not travel beyond the paper's equilibrium or welfare support.

## Introduction

**Function.** Make the contribution legible before institutional detail. Build paragraphs around distinct jobs:

1. State the economically consequential institutional tension.
2. Explain the inference problem: observed equilibrium prices and quantities can reflect multiple sides or channels.
3. Introduce the setting, data granularity, and source of leverage.
4. State the central behavioral result and magnitude.
5. Explain the evidence that separates the proposed mechanism from the closest alternative.
6. Present substitution, real effects, propagation, incidence, or model-based equilibrium implications.
7. Position the exact object learned relative to the nearest mechanism and design papers.
8. End with one boundary when local evidence, measurement, or maintained structure limits the claim.

**Required evidence.** Support the headline with the same specification and population used later. Preview the decisive diagnostic. For hybrid papers, separate what empirical variation establishes from what the model supplies.

**Common overclaims.** Do not use a broad social problem as a substitute for a specific research question. Do not claim to identify supply, information, contagion, or welfare merely because the result is consistent with it. Avoid contribution lists based only on a new country, dataset, or shock.

**Output gate.** Each paragraph has one job, the main estimate appears once with stable units, and the novelty claim names the object or mechanism changed. Removing the proposed mechanism would make the evidence order visibly different.

## Institutional setting

**Function.** Give readers the minimum institutional model needed to evaluate measurement and behavior. Explain agents, contracts or venue, timing, information, cash/security/data flows, constraints, enforcement, and feasible outside options. Use a timeline or flow diagram when readers otherwise must retain more than two bilateral links or stages.

**Required evidence.** Document who observes and chooses what; effective versus announcement dates; eligibility and enforcement; pricing and nonprice terms; reporting lags; and avoidance or substitution opportunities. Distinguish institutional facts from interpretation.

**Common overclaims.** Formal rules need not equal actual exposure or compliance. Contract authority need not imply exercised discretion. Gross contractual links need not measure net economic exposure.

**Output gate.** A reader can reconstruct treatment or exposure timing, identify both sides of the transaction, and name at least one strategic response without consulting later regressions.

## Data, measurement, and design

**Function.** Show that the dataset observes the mechanism at the right unit and time, then connect variation to the intended estimand or model object.

**Required evidence.** State observation level, coverage, frequency, entity linkage, timestamp precision, reporting lag, inclusion rules, censoring, aggregation, weighting, and external coverage. Define whether measures are applications, approvals, commitments, originations, drawdowns, quotes, orders, trades, posted terms, executed terms, gross exposure, or net exposure. Validate central proxies against an institutional benchmark. For reduced-form designs, define assignment, comparison units, timing, fixed effects, inference, anticipation, and spillovers. For structural or quantitative designs, separate observed facts from model-imposed decomposition.

**Common overclaims.** Aggregated lending can confound borrower demand and lender supply. Observed borrowers or executed trades can hide selection. Clock mismatch can manufacture price response. Balance-sheet frequency can be too coarse for event timing. A proxy's convenient availability is not construct validity.

**Output gate.** Every central variable maps to a decision or outcome in the mechanism chain; sample construction can be reproduced; timing respects information availability; and the design states which alternative comparisons remain possible.

## Results

**Function.** Accumulate evidence in causal or mechanism order, not in the order regressions were run. A typical sequence is:

1. Validate exposure, constraint, information, or rule implementation.
2. Establish the response at the relevant decision margin.
3. Report the corresponding price and quantity, contract, execution, or balance-sheet effects.
4. Examine selection and composition.
5. Distinguish supply from demand, information from inventory, or common exposure from propagation.
6. Measure substitution across lenders, products, venues, instruments, or time.
7. Trace incidence, real outcomes, stability, or aggregate response.
8. Present welfare or policy only if the design or model supports it.

**Required evidence.** For each main exhibit, state the question, comparison, magnitude, uncertainty, benchmark, and implication for one live alternative. Keep denominators, samples, units, and specification lineage stable. Report informative nulls. Interpret informative price–quantity movement jointly.

**Common overclaims.** Heterogeneity is not automatically mechanism evidence; an interaction can reflect composition. A lender-level response need not reduce borrower-level credit if substitution is strong. Common asset losses are not contagion. A spread measure does not represent every liquidity dimension. Downstream correlations are not real effects without credible timing and comparison.

**Output gate.** Each subsection changes belief about a named link in the mechanism chain. No table is included only because it is statistically significant. The last sentence of each subsection says what the result establishes and what it does not.

## Mechanism, substitution, and incidence

**Function.** Close the loop between local behavior and economic consequence. Organize the section as proposed channel → discriminating implication → evidence → remaining alternative. Use the map to make price, quantity, selection, substitution, and incidence jointly visible.

**Required evidence.** State which side initially responds, who can substitute, where activity migrates, which parties bear price or nonprice changes, and whether the estimate is gross, net, local, or aggregate. For network papers, separate direct exposure, behavioral response, propagation, and feedback. For policy papers, distinguish implementation, avoidance, incidence, externalities, and equilibrium adjustment.

**Common overclaims.** A pattern merely compatible with a channel does not identify it. Mediation based on an endogenous intermediate outcome does not by itself quantify a causal mechanism. Local gains do not establish aggregate gains, and redistribution does not establish welfare improvement.

**Output gate.** At least one credible alternative faces a discriminating test; substitution is measured or explicitly left open; winners and losers are named; and welfare language has a stated benchmark, externality, and maintained equilibrium structure.

## Conclusion

**Function.** Answer the research question without replaying the paper. Use three moves: the institutional object learned; the decisive mechanism or incidence evidence; the boundary and implication.

**Required evidence.** Reuse no magnitude that differs from the abstract or main results. Identify the population, market, and horizon. If a model closes equilibrium or welfare, label the implication conditional on that structure.

**Common overclaims.** Avoid universal policy prescriptions, new causal verbs, or new mechanisms. Do not turn absence of detected substitution into absence of substitution, or short-run incidence into steady-state welfare.

**Output gate.** Every sentence is supported earlier, no new result appears, and the final implication remains valid after appending the paper's most important identification, measurement, or equilibrium qualifier.

## Whole-paper output gate

Before delivery, confirm that the same mechanism vocabulary, unit, sample, horizon, and specification travel across abstract, introduction, exhibits, and conclusion. Confirm that price, quantity, selection, substitution, and incidence are either supported, marked not applicable, or explicitly left unresolved—never silently omitted when central to the claim.
