# Evidence Method

The repository separates **coverage**, **five independent teaching portfolios**, and **held-out validation**.

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

Writing guidance is not based on a random or hash sample. Each skill has a separately curated evidence portfolio:

| Evidence set | Papers | Purpose |
|---|---:|---|
| `general-writing.csv` | 50 | all-section and cross-archetype writing architecture |
| `asset-pricing.csv` | 50 | seven asset-pricing evidence tasks |
| `causal-empirical.csv` | 60 | design, validation, mechanism, and scope across causal methods |
| `intermediation-markets.csv` | 60 | six balanced institution/mechanism families |
| `theory-structural.csv` | 50 | pure theory, structural, quantitative, and hybrid papers |

These are not nested subsets. Relative to the general portfolio, the specialist portfolios contain 42, 49, 46, and 40 papers of their own, respectively. A small overlap is deliberate when one paper teaches both general section craft and a specialist move. See [`sets/overlap-matrix.json`](sets/overlap-matrix.json).

The selection process was:

1. scan the complete 2,065-paper title and structural inventory;
2. construct a high-recall candidate pool for the portfolio's own purpose;
3. reject keyword false positives and papers whose contribution is peripheral to the portfolio;
4. directly review the abstract, full introduction, named body sections, and conclusion for finalists;
5. record one or more transferable writing functions and an explicit transfer limit;
6. balance functions, journals, designs, and counterexamples as a portfolio rather than rank papers by fame.

Every installable skill carries its own generated `references/evidence-basis.md`, so it remains self-contained. The root CSVs are the auditable source of truth. Run `scripts/build_evidence_references.py` after changing a portfolio.

## 3. What selection does not mean

Selection is not a ranking of research quality. Publication, prizes, citations, author reputation, or memorable prose are insufficient. A technically excellent paper may be a weak teaching anchor if its argument is unusually idiosyncratic or its extraction cannot support the named sections.

`selection_tier=section_specific` or `supporting` means only the named function should guide writing. No exemplar licenses copying sentences, length, heading count, topic-specific claims, or a causal/model interpretation stronger than the user's evidence.

## 4. Held-out validation

[`sets/held-out.csv`](sets/held-out.csv) contains 61 portfolio-labeled papers reserved from rule induction. They test whether the skills transfer to new settings, designs, extraction problems, and complex evidence chains. Counterexamples in the 2,065-paper census prevent a frequent pattern from becoming an absolute requirement.

## 5. Reproduce the census locally

```bash
python3 scripts/build_corpus_evidence.py \
  --strict-csv /absolute/path/to/Three_Layer_Assignment_Paper_Strict_1990_2025_v1.csv \
  --output-dir evidence/corpus-census \
  --start-year 2020 \
  --end-year 2025
```

The local source corpus is not included in this repository.

## 6. Copyright boundary

Only article metadata, aggregate counts, original functional synthesis, and synthetic examples are published. JF/JFE/RFS PDFs, MinerU Markdown/JSON, and article prose remain outside the repository. The portfolio files are evidence maps, not text-training datasets.
