# Curated Writing-Evidence Report

Checked: 2026-08-13.

## What was selected

The public set contains 36 deliberately selected teaching exemplars: 12 each from JF, JFE, and RFS. Every exemplar is attached to a specific writing function and a transfer limit in [`curated-exemplars.csv`](curated-exemplars.csv). A paper can be excellent research yet unsuitable as a general writing model.

The set is not a ranking and is not random. It balances four evidence logics used by the five skills:

- asset pricing and investments;
- causal empirical finance;
- intermediation and market structure;
- theory, structural estimation, and quantitative models.

Company finance, household finance, FinTech, policy, and behavioral papers enter through these evidence logics rather than becoming overlapping skills.

## Selection funnel

| Journal | Strict census | Discovery and comparison | Selected |
|---|---:|---|---:|
| JF | 452 | All titles, abstracts, and structures scanned; 37-paper cross-archetype pool; 12 finalists deeply read | 12 |
| JFE | 896 | All records scanned; 500 broad structural/archetype candidates; 34 high-potential papers deeply read | 12 |
| RFS | 717 | All records and headings scanned; 24 targeted candidates deeply read | 12 |

Deep reading covered the abstract, full introduction, relevant design/model/results/mechanism section, and conclusion. The final portfolio also received an independent metadata-and-teaching-function audit, with targeted first-page PDF checks across all three production formats. Selection used the rubric in [`curation-rubric.md`](curation-rubric.md). It did not use citations, prizes, author reputation, or a hash/random draw.

## Portfolio rules

An exemplar entered the set only for a named function, such as estimand separation, competition among mechanisms, threat-driven validation, model-to-data mapping, or a prediction-to-test bridge. The selector then asked:

1. Is the question–approach–evidence–claim chain visible?
2. Does the evidence order teach a reusable reasoning move rather than a topic-specific trick?
3. Are causal, predictive, descriptive, and model-implied claims calibrated?
4. Does the paper add an archetype or section function missing from the portfolio?
5. What would be misleading if a user copied this paper too literally?

`selection_tier=section_specific` means that only the named functions are recommended as anchors. It is not a lower judgment of research quality.

## Counterexamples and held-out cases

[`held-out-candidates.csv`](held-out-candidates.csv) retains strong papers that were deliberately excluded because their extraction was damaged, the exposition was unusually specialized, the structure duplicated another anchor, or the paper is more useful as a generalization test. These cases prevent the skills from learning that more headings, more robustness tables, or a memorable phrase automatically imply better writing.

## Metadata corrections and date boundary

- `10.1093/rfs/hhaf045` is officially titled *Π-CAPM: The Classical CAPM with Probability Weighting and Skewed Assets*. The local OCR rendered Π as `5`; the public curated record uses the verified OUP title.
- `10.1093/rfs/hhad095` has canonical year 2024 but sits in a 2023 source folder. The census uses the canonical year and retains source-folder year separately.
- `10.1093/rfs/hhaf080` was a strong intermediation candidate. The local canonical table places it in 2025, while the current OUP page reports online publication in 2025 and a July 2026 print issue. It is not in the 36-paper core set; `10.1093/rfs/hhaa119` is used instead so the selected portfolio stays within print years 2020–2025.

The full census still follows the local canonical publication-year field. For article-level historical claims, verify online-first and print-issue dates on the publisher page.

## Copyright boundary

The repository stores bibliographic metadata and original functional synthesis only. It does not store article prose, PDFs, or MinerU-derived full text. Writing skills must learn rhetorical functions, not reproduce or lightly paraphrase an exemplar.
