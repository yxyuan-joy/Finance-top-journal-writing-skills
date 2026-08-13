# Skill evaluation harness

This directory contains the dependency-free, deterministic layer of the
three-layer evaluation design. It is suitable for local development and CI;
it does not call an external model.

## Run it

From the repository root:

```bash
python3 scripts/run_skill_evals.py
python3 -m unittest discover -s tests -p 'test*.py'
python3 scripts/validate_repo.py
```

`run_skill_evals.py` prints JSON and returns a nonzero status when fixture
validation or a routing expectation fails. Add `--details` for per-case scores,
or `--json-out PATH` to retain the report.

## Layer 1: deterministic routing

[`cases/routing-v1.json`](cases/routing-v1.json) contains realistic English,
Chinese, and mixed-language prompts. It deliberately includes colloquial
requests, missing specialist terminology, cross-skill conflicts, and adjacent
negative examples.

Each case declares:

- `expected_primary`: the required rank-1 skill, or `null` for no route;
- `expected_supporting`: skills that must join the primary skill in the first
  `top_k` ranks;
- `negative_for`: adjacent skills that must not be selected;
- `top_k`: an optional explicit cutoff, at least as large as the required set;
- `tags`: coverage labels used by the schema gate.

The core writing skill is intentionally primary for in-scope manuscript work.
A matching specialist is normally supporting. Thus a core + specialist route
is a success when the core is rank 1 and the complete required set appears in
the top-k; the core's rank does not count as a specialist failure.

The report separates:

1. `primary_rank_1`: exact rank-1 accuracy;
2. `required_set_top_k`: full-set recall at each case's cutoff;
3. `adjacent_negative_exclusion`: declared negative skills not selected;
4. `no_route`: out-of-scope prompts correctly rejected;
5. `route_collisions`: prompts on which multiple specialists clear the signal
   threshold, even when the intended specialist wins;
6. `description_collisions`: pairwise lexical overlap in public skill
   descriptions after common repository boilerplate is removed.

The router scores semantic concept groups, not raw keyword frequency. Synonyms
inside one group count once. It first requires a finance manuscript-writing
gate, then selects the core and one central specialist. It separately reports
multi-specialist collisions so a human/model can distinguish false overlap
from a genuine hybrid whose second evidence logic owns an independent claim.
This deterministic router is an evaluation baseline, not a replacement for
agent judgment.

## Layer 2 contract: behavioral schema

[`cases/behavior-v1.json`](cases/behavior-v1.json) contains at least two
contracts for each skill. Every contract supplies facts and machine-checkable:

- `expectations`: content or boundary markers a future response must contain;
- `hard_failures`: unsupported claims whose presence must fail the case.

An assertion has an `id`, a human-readable `description`, `target: "response"`,
and one matcher:

| Matcher | Required value | Meaning |
|---|---|---|
| `contains` | `value` | one literal substring |
| `contains_any` | `values` | at least one listed substring |
| `contains_all` | `values` | every listed substring |
| `regex` | `pattern` | a compilable Python regular expression |

`case_sensitive` is optional and must be Boolean. Matching is intended to be
case-insensitive by default. The deterministic harness validates fields,
types, IDs, nonempty lists, and regular-expression syntax. It deliberately does
not generate a response or claim behavioral pass rates.

## Coverage and versioning

The schema gate requires at least five routing positives, three adjacent
negatives, and two behavioral contracts for every skill. Routing coverage must
include both English and Chinese plus `colloquial`, `implicit-terminology`, and
`cross-skill-conflict` tags. Case IDs are unique across all fixture files.

Fixtures use `schema_version: 1`. Add new cases to a versioned JSON file under
`evals/cases/`; change the schema version only with a matching parser and test
update. The older `evals/routing-cases.json` is a small historical seed and is
not part of the executable versioned suite.

## Layer 3: saved-response behavioral grading

The repository does not choose or call a paid model automatically. Instead,
scaffold a clean response directory, run the cases with the model/agent under
test, save one response per case, and grade the declared assertions:

```bash
python3 scripts/run_behavior_evals.py --scaffold /tmp/finance-behavior-run
# Give the agent only CASE_ID/task.md, then save its answer as CASE_ID/response.md.
python3 scripts/run_behavior_evals.py /tmp/finance-behavior-run \
  --json-out /tmp/finance-behavior-report.json
```

The generated task files include the prompt and supplied facts but deliberately
exclude expectations and hard-failure matchers. Record the model,
prompt/harness version, run date, and isolation procedure in the generated
`run-metadata.json`. Scaffolding is idempotent and does not overwrite existing
responses. Unrecorded metadata and blank or comment-only scaffold files fail
closed. The runner reports missing responses,
expectation matches, and triggered hard failures and exits nonzero on failure.
Because literal/regex assertions can produce semantic false positives or false
negatives, review every failed case and a sample of passing cases manually.
Never overwrite the versioned fixtures with model-generated expectations.

## Synthetic gold cases

[`gold/`](gold/) contains two end-to-end examples for each of the five fixed
skills. Every case keeps `input.md`, `expected-criteria.json`, and
`reference-output.md` separate. The inputs and outputs are synthetic: they are
for observable handoff quality and human calibration, not stylistic imitation
or evidence about journal preferences. Gold outputs are one defensible answer,
not text that a model must reproduce verbatim.

## Main-thread self-use cases

[`self-use-v1/`](self-use-v1/) records five additional synthetic tasks and the
complete outputs produced by the repository maintainer in a progressive-loading
run. These cases are not gold answers and are not used to claim a model pass
rate. Their purpose is to make real use friction inspectable. The run exposed
three rule gaps—turnover/cost conventions, calendar mapping of event-study
leads, and percentage-surplus aggregation—and one execution error involving
offered versus realized fees. The tasks, corrected outputs, file-reading trace,
and disposition of each finding are summarized in the directory report.
