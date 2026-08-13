# Architecture Benchmark

Checked: 2026-08-13.

## Purpose and boundary

This audit asked what highly used agent-skill and agent-workflow repositories can teach this project about routing, progressive disclosure, evaluation, maintenance, and release discipline. Stars were used only to widen discovery; they are not evidence that a repository's content is scientifically correct or suitable for finance writing. We independently implemented the useful abstractions and copied no third-party skill prose, templates, or code.

## Projects examined

| Project | Transferable lesson | Deliberately not copied |
|---|---|---|
| [Anthropic Skills](https://github.com/anthropics/skills) | Separate trigger, behavior, and benchmark artifacts; compare a revision against a baseline; keep assertions machine-checkable. | Vendor-specific UI code and any non-redistributable example content. |
| [Superpowers](https://github.com/obra/superpowers) | Exercise skills under pressure with clean agents; retain transcripts and test activation, not only file validity. | Universal mandates, auto-injection hooks, and long process dogma unrelated to a bounded finance-writing task. |
| [Agent Skills by Addy Osmani](https://github.com/addyosmani/agent-skills) | Use layered structural, routing, and behavioral tests; include near-miss and collision cases. | Web-development-specific content and keyword rankings as proof of actual writing quality. |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | State independently testable scenarios and measurable success conditions before implementation. | Its software-development phase structure as a paper-writing workflow. |
| [Agent Skills specification](https://github.com/agentskills/agentskills) | Keep the required entry point small and place detailed resources behind progressive disclosure. | Cross-client assumptions that are not part of the current Codex skill format. |
| [OpenAI Codex](https://github.com/openai/codex) and [OpenAI Plugins](https://github.com/openai/plugins) | Prefer thin client metadata around a portable core and validate installable packages deterministically. | Product internals, unrelated plugins, and repository-wide infrastructure. |
| [gstack](https://github.com/garrytan/gstack) | Checkpoints, explicit evidence gates, and artifact-oriented QA can improve reliability. | Very large prompts and exhaustive workflows for short section-writing requests. |
| [Matt Pocock's skills](https://github.com/mattpocock/skills) | Give each skill a clear ownership boundary and distinguish user invocation from model routing. | Topic-specific material and implicit assumptions about a different client. |
| [Scientific Agent Skills](https://github.com/K-Dense-AI/claude-scientific-skills) | Scientific workflows benefit from provenance, narrow subtask routing, and reusable deterministic utilities. | Breadth-first installation of hundreds of skills and non-finance scientific instructions. |
| [Planning with Files](https://github.com/OthmanAdi/planning-with-files) | Durable state and small progress artifacts help long tasks survive context boundaries. | Mandatory planning files for routine paragraph or abstract edits. |

We also inspected several broad catalogs and official plugin collections to understand discovery and packaging. Catalog size was not treated as a design target: a repository with hundreds of skills can be useful for discovery while being a poor default installation.

## Decisions adopted here

1. **Five clear owners.** One core finance-paper skill and four evidence-logic specialists reduce name collisions and duplicated rules.
2. **Three-layer disclosure.** Frontmatter handles discovery, `SKILL.md` handles routing and the working contract, and references/assets are loaded only for the selected task.
3. **Evidence catalogs are optional indexes.** The 50/60-paper catalogs remain auditable but are searched by subtype/function instead of loaded end to end for every draft.
4. **Three evaluation layers.** Repository validation checks packaging; deterministic routing cases test activation and collisions; behavioral cases define claim-calibration and artifact requirements for model-backed tests.
5. **Baseline-driven revision.** Real user-style v1 outputs were retained outside the repository, diagnosed, and rerun against the revised skills. Word count, references loaded, hard failures, and unresolved friction are recorded.
6. **Single generated source.** Evidence-reference tables are generated from curated CSVs, and `--check` prevents silent drift.
7. **Fail closed on fragile invariants.** Missing frontmatter, broken links, stale generated evidence, invalid eval cases, leaked corpus text, or held-out overlap must fail validation.
8. **No star-driven borrowing.** Licenses and provenance are checked, and only independently expressed architectural ideas enter this repository.

## Patterns rejected

- One skill per section, method, subfield, or journal, which would multiply routing collisions and maintenance work.
- A giant always-loaded prompt or an always-loaded 50/60-paper exemplar table.
- Keyword routing as the sole quality evaluation; correct activation does not establish a good manuscript output.
- Installing a broad skills catalog when the user asked for a focused finance-writing stack.
- Treating hooks or CI as substitutes for scientific judgment.
- Publishing local PDFs, MinerU text, or close paraphrases of articles as examples.

## Release interpretation

A release can pass deterministic checks while still needing human or model-backed writing evaluation. Conversely, a fluent output can fail release if it invents evidence, hides a conflict, turns prediction into causality, treats calibration as identification, or mistakes a production convention for a live submission rule. Both layers are required.
