# Manual and Held-Out Test Report

Run date: 2026-08-13.

## Scope

This report records model-backed and source-backed checks that cannot be reduced to repository validation. Raw synthetic prompts, complete outputs, and per-task run records were retained outside the public repository under `/tmp` during development; the repository publishes the method, aggregate results, and failure modes rather than bulky transcripts. No local PDF, MinerU article text, or protected corpus artifact is published.

The evaluation had four parts:

1. **v1 blind use:** 17 user-style writing tasks executed by isolated agents that saw the installed skills and task facts but not expected answers, suspected defects, or prior evaluation conclusions.
2. **v2 matched rerun:** five high-information general/causal tasks rerun on the same raw prompts after revision, again without access to v1 outputs or intended fixes.
3. **v2 specialist rerun:** bounded asset-pricing, market-microstructure, and quantitative-model tasks rerun on the revised specialists.
4. **Real held-out transfer:** eight papers reserved outside every curated portfolio inspected at the abstract, full-introduction, named-body-section, and conclusion level.

The v1 versus v2 comparison is a previous-skill baseline, not a no-skill randomized experiment. Timing came from isolated run windows and is descriptive; model/token billing was unavailable. Claims below therefore focus on observable output length, files read, hard scientific boundaries, and transfer coverage.

## v1 blind-use coverage and diagnosis

The 17 tasks covered:

- JF abstract/introduction, JFE introduction, RFS results/conclusion, and uncertain journal targeting;
- incomplete staggered DID, mechanism overclaim, conflicting analysis artifacts, and Chinese notes with ambiguous units;
- asset-pricing discovery, model testing, real-time timing, data mining, holdout decay, and implementability;
- bank credit supply versus demand/selection/substitution, microstructure dimensions, regulation, incidence, and welfare;
- pure theory, structural estimation, calibration, counterfactual support, equilibrium multiplicity, and welfare accounting.

The skills consistently prevented invented data/citations, unsupported causal upgrades, alpha-as-mispricing, subgroup-as-mechanism, targeted-moments-as-validation, counterfactual-as-treatment-effect, silent number reconciliation, percent/percentage-point mixing, and model-component-as-social-welfare claims.

Observed v1 weaknesses were concrete rather than stylistic:

1. bounded section tasks often opened the full 50/60-paper evidence catalogs;
2. the core and specialist output contracts repeated the same gaps in several ledgers;
3. a prediction paper lacked explicit holdout, entity leakage, benchmark, calibration, and construct-validity routing;
4. journal adapters could format papers but not support a confident targeting recommendation;
5. material conflicts lacked a compact lineage protocol;
6. bilingual statistical ambiguity had no dedicated rule;
7. staggered-DID guidance named threats without an estimand-first implementation boundary;
8. the draft linter falsely treated `first month` as novelty and bounded negative causal statements as positive causal claims.

These failures directly produced the v2 changes; none was inferred from star counts or copied from an exemplar project.

## Matched v1–v2 results

Five prompts were rerun: predictive JFE introduction, uncertain journal fit, incomplete staggered DID, conflicting table/output packages, and Chinese notes. All five v2 outputs retained the v1 scientific safety boundaries. The full evidence catalogs were opened zero times in v2.

| Task | v1 words | v2 words | Change |
|---|---:|---:|---:|
| Predictive JFE introduction | 1,190 | 655 | -45% |
| Uncertain journal fit | 866 | 567 | -35% |
| Incomplete staggered DID | 1,864 | 889 | -52% |
| Conflicting artifacts | 1,644 | 816 | -50% |
| Chinese notes only | 2,073 | 1,238 | -40% |
| **Total** | **7,637** | **4,165** | **-45%** |

V2 task outputs ranged from 567 to 1,238 words (median 816). The decline is not presented as quality by itself: the important result is that outputs became shorter while still (a) refusing unsupported causal/mechanism/welfare claims, (b) preserving ambiguous `4.8` units, (c) keeping incompatible coefficient/SE/N/baseline packages together, and (d) marking journal choice as low-confidence when closest papers were unverified.

The predictive task used the new prediction/measurement reference and explicitly surfaced train/validation/test units, entity/time leakage, paired uncertainty for the AUC gain, calibration, decision value, and construct validity. The journal-fit task separated fit from formatting and returned a provisional first choice plus reversal conditions. The staggered-DID task selected a cohort-time estimand before asking for a named estimator. The conflict task applied a source-lineage hierarchy without assuming that the largest or most polished estimate was final. The bilingual task retained the unresolved unit rather than converting it for fluency.

Remaining friction is real. When the main magnitude or design is missing, safe prose must still contain placeholders and cannot be submission-ready. Study-specific design problems—such as migration, multi-government exposure, spillovers, or policy overlap—cannot be solved by a generic writing skill. The deterministic linter remains a review prompt, not a scientific grader.

Three additional v2 specialist reruns produced an RFS asset-pricing abstract (139 words), a JF microstructure results section plus boundary (302 words), and a JF quantitative-model abstract plus maintained-structure boundary (211 words). None opened an evidence catalog end to end. All three retained the decisive limits: discovery/holdout decay and costs did not become an attention anomaly or implementable strategy; mixed spread/depth/price-discovery measures did not become uniform market-quality or welfare improvement; and a conditional run-risk counterfactual did not become an optimum, elimination result, or social-welfare estimate.

## Real held-out transfer

Eight papers were selected from the globally disjoint held-out pool; none had informed the curated portfolios. Coverage was JF/JFE/RFS = 3/3/2 and included all five skills, causal and predictive empirics, pure theory, calibrated/quantitative models, asset pricing, intermediation, and three deliberately difficult hybrids.

Result: **5 Pass / 3 Partial / 0 Fail**.

The five passes required no new architecture. The three partial cases were not section-template failures: each needed two evidence logics with independent jobs—asset pricing plus causal identification, causal identification plus a calibrated model, or intermediation shocks plus priced-risk tests. This finding changed the router from a mechanical one-specialist ceiling to one primary specialist by default plus one narrowly owned auxiliary specialist for genuine hybrids. It also added multi-stage estimand guidance and separated illustrative calibration from models disciplined for counterfactual use.

## Deterministic evaluation layer

The public harness supplements, rather than replaces, the manual tests:

- 33 routing prompts in English, Chinese, and mixed language;
- 29/29 primary rank-1 decisions;
- 29/29 complete core-plus-specialist sets within the declared top-k;
- 60/60 adjacent negative selections excluded;
- 4/4 out-of-scope prompts rejected;
- 10 behavioral contracts, 30 positive expectations, and 23 hard-failure assertions with zero schema errors.

The router explicitly reports cross-specialist collisions. Its 100% result is an in-repository regression score on declared cases, not an estimate of performance on all possible user prompts. The behavioral contracts currently validate schema; actual model behavior is evidenced by the blind tasks above and should continue to be rerun when rules change.

## Release decision

Release is supported because packaging, generated evidence, routing cases, behavioral schemas, and unit tests pass; v2 matched reruns preserve scientific hard boundaries with substantially less context/output overhead; and eight real held-out papers produced no core-architecture failure. The main residual risk is hybrid routing and study-specific scientific judgment, which the skill now surfaces rather than claiming to automate.
