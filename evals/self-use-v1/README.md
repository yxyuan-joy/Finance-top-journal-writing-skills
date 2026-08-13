# Maintainer self-use run v1

- Run date: 2026-08-13
- Scope: all five fixed skills
- Operator: repository maintainer in the primary task thread
- Status: completed, manually reviewed, and corrected

This directory records a direct self-use run rather than a delegated agent
test. Five synthetic tasks were frozen before the operator opened the task's
skill references. The operator then drafted each complete response, inspected
the result against the supplied facts, and changed repository rules only when
the run exposed a transferable failure. No local paper text, PDF, MinerU
output, or protected workspace directory was used.

## Test protocol

1. Write and freeze one previously unseen synthetic task for each fixed skill.
2. Load only the target `SKILL.md` and references needed for that task.
3. Draft the requested artifact without reading gold answers or behavioral
   assertions.
4. Audit every supplied number, unit, design label, and evidence boundary.
5. Separate a rule gap from an operator error or a stylistic preference.
6. Correct the response, patch only transferable gaps, and add regression
   contracts for those gaps.

The tasks and corrected complete responses are in [`tasks/`](tasks/) and
[`outputs/`](outputs/). These are examples of one defensible execution, not
gold prose and not evidence of a general model pass rate.

## Progressive-loading trace

| Case | Skill and references read | Full evidence catalog read? | Outcome |
|---|---|---:|---|
| Core literature positioning | core `SKILL.md`; literature synthesis; introduction/positioning; evidence-and-claim policy | No | Claim and citation-status boundaries held |
| Asset-pricing validation | AP `SKILL.md`; section blueprints; validation; implementability ledger | No | One arithmetic-convention gap found |
| Causal repair | causal `SKILL.md`; section blueprints; design router; threats | No | One event-time mapping gap found |
| Intermediation incidence | intermediation `SKILL.md`; section blueprints; threats; mechanism-incidence map | No | One operator error found; existing rule already covered it |
| Theory counterfactual | theory `SKILL.md`; section blueprints; identification/fit/counterfactuals; welfare matrix | No | One aggregation-disclosure gap found |

The AP and intermediation ledgers were useful for whole-chain audits but heavier
than needed for a short paragraph. Their `SKILL.md` files already say not to load
or emit the whole template for narrow edits, so this was recorded as operator
over-reading rather than a reason to add more files.

## Findings and disposition

| Finding | First-pass behavior | Classification | Repository disposition |
|---|---|---|---|
| Undefined turnover convention | The AP draft converted 190% turnover and a 35-bp one-way cost into 1.33% monthly costs by silently inserting a factor of two. | Transferable rule gap | Net-return arithmetic now requires the turnover definition and per-side/round-trip cost rule; a behavioral regression case was added. |
| Event-time lead versus announcement | The causal draft said event time −2 might be announcement anticipation even though only a nine-month announcement lead was supplied and the bin's calendar span was unknown. | Transferable rule gap | Leads must be mapped into calendar time and overlap the documented anticipation window before receiving that interpretation; a regression case was added. |
| Group surplus percentages | The theory draft correctly refused to add the figures, but the previous workflow did not explicitly demand denominators and an aggregation formula. | Transferable audit gap | Welfare guidance and the matrix now require bases and aggregation rules; a regression case was added. |
| Offered versus realized fees | The intermediation draft briefly stated that approved borrowers faced lower fees when only offered fees were supplied. | Operator error | The response was corrected. No new rule was needed because the existing skill already distinguishes posted/offered from executed terms. |
| Journal adapter over-loading | A JFE label in a bounded literature task did not change the substantive positioning prose. | Progressive-disclosure friction | The core skill now loads the journal adapter for formatting, organization, or near-final adaptation—not merely because a journal name appears. |

## Manual outcome

After correction, all five outputs satisfy their requested deliverables and
retain the central evidence boundaries:

- descriptive literature evidence is not made causal and title-only metadata
  is not used substantively;
- discovery, tuning, and untouched asset-pricing samples remain distinct, with
  no unsupported net return, mispricing, or implementability claim;
- staggered-DID comparisons, adverse pre-movement, composition, spillovers,
  and state-cluster inference remain visible;
- offered prices, approvals, selection, substitution, real effects, incidence,
  and welfare are not collapsed into one policy verdict;
- estimated and calibrated parameters, targeted and untargeted fit,
  out-of-support counterfactuals, redistribution, uncertainty, and omitted
  welfare margins retain distinct labels.

The run did not justify another skill, another evidence portfolio, or more
journal personas. Its useful changes are narrow execution guards plus three
behavioral regressions.
