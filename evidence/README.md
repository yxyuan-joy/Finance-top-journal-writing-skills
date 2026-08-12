# Evidence Method

The repository separates **coverage**, **curation**, and **validation**.

## 1. Full recent-corpus census

The discovery frame is the immutable strict ordinary-submission sample for final publication years 2020–2025:

| Journal | Papers |
|---|---:|
| JF | 452 |
| JFE | 896 |
| RFS | 717 |
| Total | 2,065 |

`scripts/build_corpus_evidence.py` reads the canonical metadata and corresponding MinerU Markdown files, then exports only bibliographic metadata and aggregate structural flags. It does not export prose or local paths.

Final publication year, rather than source-folder year, defines the window. The census retains both fields: 42 RFS papers in this window have different source-folder and final publication years, while JF/JFE have none. This prevents early-view/relocated packages from being assigned silently to the wrong year.

This census answers questions such as heading prevalence and source coverage. It does **not** decide which papers are good models of writing. MinerU headings can be noisy, and unheaded front matter is common.

## 2. Human-curated exemplar set

Writing guidance comes from a deliberately selected exemplar set, not a random or hash sample. Candidate selection uses the full title/heading inventory and direct reading of a broad pool. A paper is selected for a specific pedagogical function when it demonstrates:

1. a visible question–gap–approach–evidence–contribution chain;
2. unusually clear mapping from claims to exhibits, propositions, or counterfactuals;
3. calibrated language and explicit evidentiary boundaries;
4. a structure transferable beyond that paper's exact topic;
5. useful coverage of an archetype or section missing from the set.

Publication in a top journal, awards, citations, author reputation, or famous results are not sufficient. Selection is not a ranking of paper quality. Dense or highly idiosyncratic papers may be excellent research but poor teaching anchors for a general writing skill.

The curated set contains 36 teaching exemplars, 12 from each journal, stratified across asset pricing, causal empirical work, intermediation/markets, and theory/structural work. Each record states the sections it informs and the limits of transfer. See [`curation-report.md`](curation-report.md) and [`curated-exemplars.csv`](curated-exemplars.csv). No long article text is stored.

## 3. Counterexamples and held-out validation

Rules must survive two checks:

- counterexamples in the census prevent a frequent pattern from becoming an absolute requirement;
- held-out papers in [`held-out-candidates.csv`](held-out-candidates.csv) and synthetic writing tasks test whether a rule transfers without reproducing an exemplar.

Journal production conventions are kept separate from research-design rhetoric. Current submission requirements are sourced from live official pages and dated.

## 4. Reproduce the census locally

```bash
python3 scripts/build_corpus_evidence.py \
  --strict-csv /absolute/path/to/Three_Layer_Assignment_Paper_Strict_1990_2025_v1.csv \
  --output-dir evidence/corpus-census \
  --start-year 2020 \
  --end-year 2025
```

The local source corpus is not included in this repository.

## 5. Copyright boundary

Only article metadata, aggregate counts, original synthesis, and synthetic examples are published. JF/JFE/RFS PDFs and MinerU-derived article text remain outside the repository.
