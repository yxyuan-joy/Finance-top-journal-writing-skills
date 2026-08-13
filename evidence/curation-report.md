# Independent Writing-Evidence Portfolios

Checked: 2026-08-13.

## Release decision

The five skills are supported by five independent, manually curated portfolios containing 270 set memberships and 224 unique papers. The general skill uses exactly 50 papers. Every specialist has its own 50- or 60-paper evidence base and is not a slice of the general 50.

| Portfolio | JF | JFE | RFS | Total | Overlap with general | Outside general |
|---|---:|---:|---:|---:|---:|---:|
| General writing | 17 | 17 | 16 | 50 | 50 | 0 |
| Asset pricing | 16 | 18 | 16 | 50 | 8 | 42 |
| Causal empirical | 20 | 20 | 20 | 60 | 11 | 49 |
| Intermediation/markets | 20 | 20 | 20 | 60 | 14 | 46 |
| Theory/structural | 17 | 17 | 16 | 50 | 10 | 40 |

Pairwise overlap among specialists is also low; the highest specialist-to-specialist intersection is seven papers. Machine-readable counts and Jaccard coefficients are in [`sets/overlap-matrix.json`](sets/overlap-matrix.json).

## Independent curation work

- **General writing (50):** deliberately balanced across journals and section functions, including abstracts, introductions, contribution positioning, measurement, institutional background, design/model exposition, results, robustness, mechanism, limitations, conclusion, and full evidence chains. It combines prior deep-read anchors with 14 additional papers selected to fill missing functions; it is not a journal-by-year sample.
- **Asset pricing (50):** 775 high-recall candidates, 83 structural-review candidates, 68 four-section deep reads, and 50 finalists. Coverage: factor/SDF/model tests, return facts/anomalies, ML/prediction, fund performance, market efficiency/implementation, theory/measurement, and time-series/macro.
- **Causal empirical (60):** 785 design/causal candidates; all 60 finalists reviewed across abstract/introduction, design, validation/robustness, mechanism/boundaries, and conclusion. The final set is 20 papers per journal and spans IV, DID/event study, RDD/RKD, RCT, threshold/bunching, and multi-design work.
- **Intermediation/markets (60):** 414 high-recall candidates; all 60 finalists reviewed at section level. Bank/nonbank credit supply and dealer/venue/order-flow work each receive 12 papers; deposits/funding, screening/contracting, networks/runs, and regulation/FinTech/market design each receive nine.
- **Theory/structural (50):** 1,241 high-recall candidates and 911 stricter review entries; all 50 finalists reviewed across the relevant model, discipline, fit/validation, counterfactual/welfare, and conclusion sections. The set contains 21 structural, 12 quantitative/calibrated, nine theory–empirics hybrid, and eight pure-theory papers.

Candidate-pool counts are discovery counts, not claims that every candidate was suitable. Titles and headings never caused automatic inclusion. Every public record states its teaching function and its transfer boundary.

## Portfolio rules

An exemplar enters a portfolio only for a named function, such as estimand separation, competition among mechanisms, threat-driven validation, model-to-data mapping, prediction-to-test bridges, or a concise limitations-aware conclusion. The selector asks:

1. Is the question–approach–evidence–claim chain visible?
2. Does the evidence order teach a reusable reasoning move?
3. Are causal, predictive, descriptive, and model-implied claims calibrated?
4. Does the paper add a missing archetype or section function?
5. What would become misleading if a user copied it too literally?

`section_specific` and `supporting` are scope labels, not judgments of research quality.

## Held-out and metadata boundaries

The public held-out file contains 61 portfolio-labeled cases. It includes complex but strong papers, overlapping architectures, and known extraction or date-boundary challenges. Notable metadata cautions include RFS papers whose canonical final year differs from the source folder, JFE accepted-manuscript/preproof wrappers, and the local OCR rendering of `Π-CAPM` as `5-CAPM`. Public titles and years use the strict canonical inventory plus documented official corrections.

## Copyright boundary

The repository stores bibliographic metadata and original functional synthesis only. It does not publish article prose, PDFs, MinerU Markdown, or JSON. Skills must learn rhetorical functions, not reproduce or lightly paraphrase an exemplar.
