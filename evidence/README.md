# Evidence Method

Checked: 2026-08-13.

The repository separates **corpus coverage**, **five independent teaching portfolios**, and **held-out validation**. Selection identifies transferable writing functions; it is not a ranking of research quality or a claim about journal requirements.

## 1. Full recent-corpus census

The discovery frame is the immutable strict ordinary-submission sample for final publication years 2020–2025:

| Journal | Papers |
|---|---:|
| JF | 452 |
| JFE | 896 |
| RFS | 717 |
| Total | 2,065 |

`scripts/build_corpus_evidence.py` reads canonical metadata and corresponding MinerU Markdown, then exports bibliographic metadata and aggregate structural flags only. It does not export prose or local paths. Final publication year, not source-folder year, defines the window; both fields remain in the census so early-view and relocated packages are not silently assigned to the wrong year.

The census describes source coverage and production structure. It does not rank writing quality. MinerU headings can be noisy, while unheaded front matter is normal in JF and RFS.

## 2. Five independent teaching portfolios

The five manually curated portfolios contain 270 set memberships and 224 unique papers. The specialist portfolios are not slices of the general 50:

| Portfolio | JF | JFE | RFS | Total | Overlap with general | Outside general |
|---|---:|---:|---:|---:|---:|---:|
| General writing | 17 | 17 | 16 | 50 | 50 | 0 |
| Asset pricing | 16 | 18 | 16 | 50 | 8 | 42 |
| Causal empirical | 20 | 20 | 20 | 60 | 11 | 49 |
| Intermediation/markets | 20 | 20 | 20 | 60 | 14 | 46 |
| Theory/structural | 17 | 17 | 16 | 50 | 10 | 40 |

The highest specialist-to-specialist intersection is seven papers. Machine-readable counts and Jaccard coefficients are in [`sets/overlap-matrix.json`](sets/overlap-matrix.json). Limited overlap is deliberate when one paper teaches both general section craft and a specialist move.

Portfolio construction and composition:

- **General writing (50):** balanced across journals and section functions, from abstracts and introductions through contribution positioning, design/model exposition, results, robustness, mechanisms, limitations, conclusions, and full evidence chains. It combines prior deep-read anchors with 14 papers added to fill missing functions; it is not a journal-by-year sample.
- **Asset pricing (50):** 775 high-recall candidates, 83 structural-review candidates, 68 four-section deep reads, and 50 finalists across seven tasks: factor/SDF/model tests, return facts/anomalies, ML/prediction, fund performance, market efficiency/implementation, theory/measurement, and time-series/macro.
- **Causal empirical (60):** 785 design/causal candidates and 60 finalists, with 20 per journal. All finalists were reviewed across abstract/introduction, design, validation/robustness, mechanism/boundaries, and conclusion; the set spans IV, DID/event study, RDD/RKD, RCT, threshold/bunching, and multi-design work.
- **Intermediation/markets (60):** 414 high-recall candidates and 60 section-level finalists. Bank/nonbank credit supply and dealer/venue/order-flow work receive 12 papers each; deposits/funding, screening/contracting, networks/runs, and regulation/FinTech/market design receive nine each.
- **Theory/structural (50):** 1,241 high-recall candidates, 911 stricter review entries, and 50 finalists reviewed across the relevant model, discipline, fit/validation, counterfactual/welfare, and conclusion sections. The set contains 21 structural, 12 quantitative/calibrated, nine theory–empirics hybrid, and eight pure-theory papers.

Candidate-pool counts are discovery counts, not claims that every candidate was suitable. Titles and headings never caused automatic inclusion. Every public record states a teaching function and transfer boundary. Every installable skill also carries a generated `references/evidence-basis.md`, so it remains self-contained; the root CSVs are the auditable source of truth. Run `scripts/build_evidence_references.py` after changing a portfolio.

## 3. Curation rubric and safeguards

Candidates are scored 0–2 for each dimension, but the final choice is portfolio-level: a candidate need not excel everywhere if it has a clearly named teaching function, such as estimand separation, competition among mechanisms, threat-driven validation, model-to-data mapping, a prediction-to-test bridge, or a limitations-aware conclusion.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Question visibility | buried | recoverable | immediate and precise |
| Gap precision | absence/broad | partly bounded | exact evidentiary/theoretical limit |
| Approach transparency | method label | partial | variation/model and leverage clear |
| Evidence architecture | table walk | uneven | exhibits/propositions map to claims |
| Magnitude/benchmark | missing | present | economically interpreted |
| Claim calibration | overextended | mixed | consistently matched to evidence |
| Contribution comparison | broad list | near literature | exact changed margin |
| Section transferability | idiosyncratic | partly useful | reusable functional pattern |
| Limitation visibility | absent | implicit | explicit boundary |
| Archetype coverage | redundant | useful | fills a material gap |

The workflow is to scan the complete inventory; build a high-recall pool from titles, abstracts, and headings; reject false positives and peripheral contributions; read the abstract, full introduction, relevant body sections, and conclusion for every finalist; record strengths and transfer limits; balance journals, functions, designs, and counterexamples; and reserve strong non-selected candidates for held-out testing. Sets are revisited when a rule lacks counterexamples or a new complete year is added.

Prohibited shortcuts:

- random or hash selection as a writing-quality basis;
- selecting only prize winners, famous authors, or highly cited papers;
- treating publication or acceptance as proof of pedagogical clarity;
- selecting from titles alone;
- copying memorable sentences into skill references;
- presenting a curated pattern as a journal requirement.

`selection_tier=section_specific` or `supporting` scopes the named function; it does not judge research quality. No exemplar licenses copying sentences, length, heading count, topic-specific claims, or a causal/model interpretation stronger than the user's evidence.

## 4. Held-out validation

[`sets/held-out.csv`](sets/held-out.csv) contains 61 portfolio-labeled papers reserved from rule induction. They include strong but complex papers, overlapping architectures, extraction problems, and date-boundary challenges, and test transfer to new settings, designs, and evidence chains. Counterexamples in the 2,065-paper census prevent a frequent pattern from becoming an absolute requirement.

## 5. Official sources and provenance

The skill package follows [OpenAI's Build skills specification](https://learn.chatgpt.com/docs/build-skills). Current journal policies and production requirements were checked against:

- **JF:** [AFA submission page](https://afajof.org/submissions/), [Submission Guidelines and Policies](https://afajof.org/wp-content/uploads/JF_Submission_Guidelines.pdf) (revised 2024), and [Wiley's author page](https://onlinelibrary.wiley.com/page/journal/15406261/homepage/forauthors.html).
- **JFE:** [Elsevier's Guide for Authors](https://www.sciencedirect.com/journal/journal-of-financial-economics/publish/guide-for-authors), [JFE submissions](https://www.jfinec.com/submissions), and [accepted-paper instructions](https://www.jfinec.com/accepted-paper-instructions), which are not an initial-submission template.
- **RFS:** [SFS Submit a Paper](https://sfs.org/review-of-financial-studies/submit-a-paper/), [SFS submission checklist](https://sfs.org/review-of-financial-studies/submit-a-paper/submit-a-paper-format/), and [OUP Instructions to Authors](https://academic.oup.com/rfs/pages/Instructions_To_Authors).

Fees, deadlines, refunds, AI policies, anonymity, file types, and production specifications can change. Recheck the live official page at submission time and distinguish initial submission, revision, and accepted-manuscript requirements.

Three article-level corrections document the metadata boundary:

- [Π-CAPM](https://academic.oup.com/rfs/article/38/12/3497/8200846), `10.1093/rfs/hhaf045`: official title and 2025 print issue correct a local OCR substitution of Π with `5`.
- [Collateral Effects](https://academic.oup.com/rfs/article/39/7/2064/8275790), `10.1093/rfs/hhaf080`: online publication was in 2025 but the print issue is July 2026, so it is excluded from the core 2020–2025 print-year portfolio.
- [Bank Cleanups, Capitalization, and Lending](https://academic.oup.com/rfs/article-abstract/34/9/4132/5924381), `10.1093/rfs/hhaa119`: verified as the 2021 RFS replacement exemplar.

Public titles and years use the strict canonical inventory plus these official corrections. Known cautions include RFS final years that differ from source-folder years and JFE accepted-manuscript or preproof wrappers.

Four public projects were reviewed for architecture only: [Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) (CC BY-SA 4.0), [nature-skills](https://github.com/Yuan1z0825/nature-skills) (Apache-2.0), [Business-Academic-Skill](https://github.com/Mat-Wong/Business-Academic-Skill) (MIT), and [AER-Skills](https://github.com/brycewang-stanford/AER-Skills) (MIT). No prose, templates, or code were copied. The broader audit covered Anthropic Skills, Superpowers, Agent Skills by Addy Osmani, GitHub Spec Kit, the Agent Skills specification, OpenAI Codex/Plugins, gstack, Matt Pocock's skills, Scientific Agent Skills, and Planning with Files. See [`architecture-benchmark.md`](architecture-benchmark.md) for the adopted and rejected patterns. Star counts are excluded from durable design rules because they change and do not measure scientific or instructional quality.

## 6. Reproduce the census locally

```bash
python3 scripts/build_corpus_evidence.py \
  --strict-csv /absolute/path/to/Three_Layer_Assignment_Paper_Strict_1990_2025_v1.csv \
  --output-dir evidence/corpus-census \
  --start-year 2020 \
  --end-year 2025
```

The local source corpus is not included in this repository.

## 7. Copyright boundary

Only bibliographic metadata, aggregate counts, original functional synthesis, and synthetic examples are published. JF/JFE/RFS PDFs, MinerU Markdown/JSON, article prose, and local paths remain outside the repository. Portfolio CSVs are evidence maps, not text-training datasets. Skills learn rhetorical functions; they must not reproduce or lightly paraphrase an exemplar.
