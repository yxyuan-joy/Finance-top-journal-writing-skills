<p align="center">
  <img src="assets/finance-writing-skills-banner.svg" alt="Finance Top-Journal Writing Skills for JF, JFE, and RFS" width="100%">
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/yxyuan-joy/Finance-top-journal-writing-skills/releases/tag/v1.3.0"><img alt="Release v1.3.0" src="https://img.shields.io/badge/release-v1.3.0-0f766e"></a>
  <a href="https://github.com/yxyuan-joy/Finance-top-journal-writing-skills/actions/workflows/ci.yml"><img alt="CI status" src="https://github.com/yxyuan-joy/Finance-top-journal-writing-skills/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <img alt="Five skills" src="https://img.shields.io/badge/skills-5-1d4ed8">
  <img alt="Evidence census: 2,065 papers" src="https://img.shields.io/badge/evidence_census-2%2C065_papers-b7791f">
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-334155"></a>
</p>

# Finance Top-Journal Writing Skills

An evidence-informed Agent Skills suite for drafting, restructuring, and auditing finance papers aimed at *The Journal of Finance* (JF), *Journal of Financial Economics* (JFE), and *The Review of Financial Studies* (RFS).

This is not a phrase bank or a promise to imitate a journal's “voice.” It turns observable argument structures, section functions, and design-specific credibility requirements into reusable writing workflows. Missing facts remain visible; claims are never strengthened merely because the target journal is selective.

> **Independent and non-official.** This project is not endorsed by the American Finance Association, Elsevier, Oxford University Press, the Society for Financial Studies, or the three journals.

## Start here

### Install with Codex

Ask Codex:

```text
Use $skill-installer to install the skills from https://github.com/yxyuan-joy/Finance-top-journal-writing-skills
```

### Install from a terminal (macOS, Linux, or WSL)

```bash
git clone https://github.com/yxyuan-joy/Finance-top-journal-writing-skills.git
cd Finance-top-journal-writing-skills
./scripts/install.sh
```

The installer copies all five skills to `$HOME/.agents/skills`, the current user-level Codex discovery path. If `CODEX_HOME` is explicitly set, it uses `$CODEX_HOME/skills`. Install only selected skills by naming them:

```bash
./scripts/install.sh finance-top-journal-writing finance-causal-empirical-writing
```

Existing installations are not overwritten silently. Use `--replace` to create a timestamped backup outside the skill discovery directory and install the current release, or `--target PATH` for another Agent Skills directory. The repository also includes a plugin manifest so the five-skill suite can be distributed as one package by compatible Codex plugin workflows.

On native Windows, use the `$skill-installer` option above or copy the five folders under `skills/` to `%USERPROFILE%\.agents\skills`.

## Choose the right skill

The suite deliberately contains **five skills only**: one full-paper core and four specialist evidence logics. This keeps routing predictable and avoids duplicated instructions.

| Skill | Use it for |
|---|---|
| [`finance-top-journal-writing`](skills/finance-top-journal-writing/) | Any section or full paper; title, abstract, introduction, literature, data, design, results, robustness, mechanisms, conclusion, exhibits, appendices, and revisions |
| [`finance-asset-pricing-writing`](skills/finance-asset-pricing-writing/) | Expected returns, factors, SDFs, anomalies, portfolio tests, predictability, fund performance, and validation |
| [`finance-causal-empirical-writing`](skills/finance-causal-empirical-writing/) | DID, event studies, IV, RDD, natural experiments, policy changes, and other identification-led designs |
| [`finance-intermediation-markets-writing`](skills/finance-intermediation-markets-writing/) | Banks, nonbanks, credit supply, funding, liquidity, dealers, price discovery, networks, regulation, and market design |
| [`finance-theory-structural-writing`](skills/finance-theory-structural-writing/) | Pure theory, structural estimation, quantitative models, calibration, counterfactuals, and welfare |

Route by how the central claim is supported, not by a broad topic label. A governance natural experiment is causal; a bank-run model is theory/structural; a corporate-bond return predictor is asset pricing. Genuine hybrids may combine the core with two specialists only when each evidence logic owns a distinct central claim.

## Use it

```text
Use $finance-top-journal-writing to rebuild my JF introduction from the facts below.
Use $finance-asset-pricing-writing to audit whether this RFS abstract distinguishes discovery, validation, and implementability.
Use $finance-causal-empirical-writing to restructure this JFE identification and robustness section.
```

For the strongest result, provide the target journal, paper type, research question, design or model, data and sample, headline results with units, evidentiary limits, closest verified literature, and the section to write. When information is missing, the skills use explicit placeholders instead of plausible-looking inventions.

### English and Chinese output

The skills follow the language requested in the prompt. If no output language is specified, they match the user's language while preserving variable names, citation keys, equations, and technical labels that must remain traceable.

```text
请用 $finance-top-journal-writing，根据下面的事实重写 JF 摘要和引言，输出中文；不要补造数值或文献。
请用 $finance-intermediation-markets-writing，用英文审查这篇银行论文是否区分了信贷供给、需求、选择与替代。
```

## What the workflows cover

- title and abstract;
- introduction, research question, gap, and contribution;
- literature positioning, theory, hypotheses, and institutional background;
- data, samples, variable construction, measurement, and research design;
- results, economic magnitude, robustness, alternatives, and mechanisms;
- heterogeneity, discussion, limitations, and conclusion;
- tables, figures, propositions, online appendices, and full-paper coherence;
- editor/referee revisions and claim-location synchronization.

Specialists add their own failure checks. Asset pricing preserves real-time availability, benchmarks, costs, and validation states. Causal writing maps each diagnostic to a named identification threat. Intermediation separates prices, quantities, selection, substitution, and incidence. Theory/structural writing separates identification, calibration, fit, counterfactual closure, and welfare.

## Evidence, not imitation

The project combines a structural census of **2,065 ordinary JF/JFE/RFS research papers published in 2020–2025** with independently curated teaching portfolios for each skill.

| Portfolio | Selected papers | Independent of the 50-paper general set |
|---|---:|---:|
| General writing | 50 | — |
| Asset pricing | 50 | 42 |
| Causal empirical | 60 | 49 |
| Intermediation and markets | 60 | 46 |
| Theory and structural | 50 | 40 |

The five portfolios contain 270 selected positions covering 224 unique papers. Titles and headings were used only for high-recall discovery; inclusion required direct review of the abstract, full introduction, relevant body sections, and conclusion. The repository publishes bibliographic metadata, aggregate patterns, original synthesis, and synthetic examples—never local PDFs, MinerU text, or article prose.

See [`evidence/README.md`](evidence/README.md), the [`curation report`](evidence/curation-report.md), and the auditable [`evidence sets`](evidence/sets/).

## Validation

The current rule set was tested through deterministic routing, synthetic gold cases, isolated behavioral tasks, held-out transfer checks, and three additional blind rounds on **15 previously unused papers** balanced across JF, JFE, and RFS. Writers saw independently paraphrased fact packets but not paper identities or originals; outputs were frozen before bidirectional functional comparison with the source papers.

Across the three latest rounds, no case produced a Major or Invalidating defect and no recurring problem was attributed to a missing skill instruction. The final confirmation set was 3/3 Robust after local output repairs. These results support use; they do not turn a writing assistant into a substitute for research judgment or source verification.

Read the single current [`validation report`](evals/validation-report.md) and the [`evaluation harness`](evals/README.md).

Run all local checks with:

```bash
python3 scripts/validate_repo.py
python3 scripts/run_skill_evals.py
python3 -m unittest discover -s tests -v
```

## Repository map

```text
skills/      five independently installable skills
evidence/    corpus census, curated portfolios, provenance, and methods
evals/       versioned cases, synthetic gold outputs, rubric, and final report
scripts/     installer, repository validation, and evaluation tools
tests/       deterministic regression tests
```

Each skill uses progressive disclosure: a compact `SKILL.md` routes the task, then loads only the relevant reference or fillable asset. The 50/60-paper evidence catalogs are searchable provenance resources, not always-on context.

## Non-negotiable safeguards

1. Never invent data, coefficients, samples, institutional facts, citations, DOI values, theorem conditions, or journal rules.
2. Keep association, prediction, causality, structural parameters, and equilibrium counterfactuals at different claim strengths.
3. Tie robustness checks to named threats instead of listing specifications.
4. Do not equate heterogeneity, mediation, mechanism evidence, and exclusion of alternatives.
5. Keep every quantity attached to its specification, sample, unit, benchmark, uncertainty, and evidentiary status.
6. Do not reproduce or closely imitate source-paper prose.
7. Recheck live journal instructions whenever submission format or policy matters.

## License and citation

Original code and skill text are released under the [MIT License](LICENSE). Third-party papers, journal names, and external projects remain the property of their respective rights holders.

If this repository supports your work, cite the metadata in [`CITATION.cff`](CITATION.cff).

The skill package follows the current [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills) structure: `SKILL.md` as the entry point, optional `agents/openai.yaml`, and task-loaded `references/`, `assets/`, and `scripts/`.
