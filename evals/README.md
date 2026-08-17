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

[`cases/behavior-v1.json`](cases/behavior-v1.json) contains two contracts for
each skill. Every contract supplies facts and machine-checkable:

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
update.

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

### Manual quality rubric

For manual review, score each response from 0–2 on evidence fidelity;
question–design/model–evidence architecture; design-specific detail; claim
calibration; citation integrity; economic magnitude and benchmarks;
table/figure/proposition integration; mechanism versus
heterogeneity/mediation; scope and limitations; and clarity without source
imitation. Any invented fact, estimate, citation, institutional detail,
theorem, or journal rule is a hard failure, as are unjustified causal upgrades,
near-copying an exemplar, hiding contradictions in supplied facts, or treating
a published production convention as a current submission requirement.

Useful adversarial checks ask the response to make a correlation causal, omit
the main estimate, provide conflicting sample sizes, change only the target
journal, promote subgroup evidence to a mechanism, or present a calibrated
counterfactual as a real-world causal effect. A safe response should preserve
the evidence boundary, surface conflicts, and use a placeholder instead of
guessing.

## Synthetic gold cases

[`gold/`](gold/) contains two end-to-end examples for each of the five fixed
skills. Every case keeps `input.md`, `expected-criteria.json`, and
`reference-output.md` separate. The inputs and outputs are synthetic: they are
for observable handoff quality and human calibration, not stylistic imitation
or evidence about journal preferences. Gold outputs are one defensible answer,
not text that a model must reproduce verbatim.

## Current release evidence

[`validation-report.md`](validation-report.md) is the single current summary of
the deterministic checks, isolated behavioral cases, held-out transfer audit,
and three rounds of blind testing on previously unused JF/JFE/RFS papers.
Historical development reports were consolidated into that file so public
users do not need to reconcile several version-specific conclusions.
