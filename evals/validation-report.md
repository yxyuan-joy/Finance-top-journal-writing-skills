# Validation Report

Release: **v1.3.1**

Last updated: **2026-08-17**

## What this report establishes

This report records the single current validation summary for the five-skill suite. It evaluates routing, package integrity, observable writing behavior, transfer to unseen papers, and claim-boundary discipline. It does not estimate acceptance probability, certify scientific correctness, or treat a source paper's wording and paragraph order as the only acceptable answer.

No local PDF, MinerU article text, protected corpus artifact, identity-bearing blind-test manifest, or generated model transcript is published here.

## Evaluation layers

### 1. Deterministic package and routing checks

The public harness contains English, Chinese, and mixed-language prompts, colloquial requests, missing specialist terminology, genuine hybrids, cross-skill conflicts, adjacent negatives, and out-of-scope tasks.

Current regression results:

- 29/29 in-scope cases selected the required primary skill at rank 1;
- 29/29 contained the complete required core-plus-specialist set within the declared top-k;
- 60/60 declared adjacent-specialist negatives were excluded;
- 4/4 out-of-scope prompts produced no route;
- 10 behavioral contracts contain 30 positive expectations and 23 hard-failure assertions with no schema errors;
- five skills, their local links, curated evidence sets, and ten synthetic gold cases pass repository validation.

These are in-repository regression results, not estimates of performance on all possible prompts. The deterministic router is a test baseline; it does not replace model or author judgment.

### 2. Isolated synthetic behavioral cases

Ten cases—two per skill—were run with clean agents. Each writer saw only task facts and the task-needed skill references. Assertions, suspected failures, and expected outputs were hidden.

Final result: **10/10 cases passed, 30/30 positive expectations matched, and 0/23 hard failures triggered** after correcting two evaluator false positives and one real missing-placeholder behavior. The versioned public cases remain separate from the saved responses so expectations cannot leak into generation.

### 3. Held-out transfer audit

Eight real papers were reserved outside all five curated portfolios. Coverage included JF, JFE, RFS; all five skills; causal and predictive empirics; pure theory; quantitative models; asset pricing; intermediation; and deliberately difficult hybrids.

Result: **5 Pass / 3 Partial / 0 Fail**. The three Partial cases shared one transferable issue: two evidence logics performed independent central jobs. They led to the current hybrid-routing rule, multi-stage estimand separation, and a clearer distinction between illustrative calibration and models disciplined for counterfactual use.

### 4. Three-round blind paper validation

Fifteen additional papers were selected independently: **JF 5, JFE 5, and RFS 5**. Every identity was disjoint from the repository evidence sets, held-out sets, gold cases, routing cases, and every earlier blind round.

Writers received only independently paraphrased fact packets. Titles, authors, DOI values, and source paths remained sealed until outputs were frozen. Every packet passed a leakage gate of zero exact matches at 12 consecutive English words against the complete source Markdown and PDF text. Comparison with the original paper was bidirectional and functional: the audit asked what each argument component accomplished, not whether the generated prose imitated the source.

| Round | Cases | Blind result | Post-reveal functional comparison | Skill-instruction gaps |
|---|---:|---|---|---:|
| 1 | 6 | No Major or Invalidating defect; all observed issues were locally repairable | No Major or Invalidating defect | 0 |
| 2 | 6 | 4 Robust, 2 Repairable; recurrent execution failures fell materially | 3 Robust, 3 locally Repairable | 0 |
| 3 | 3 | All frozen confirmation gates passed | 3/3 Robust after two minimal, source-supported output repairs | 0 |

No round produced a Major or Invalidating defect. No recurring issue had missing skill instructions as its primary cause. The remaining problems were local output-execution errors—unsupported connective wording, evidence ownership, scope modifiers, or model-assumption roles—and the current skills already instructed against them.

## What improved during iteration

The revisions retained only general controls:

1. keep every substantive bridge supported or visibly inferential;
2. delete evidence that does not change the question, answer, decisive credibility, counterweight, boundary, or contribution;
3. place population, design, model, and welfare conditions next to the first claim they constrain;
4. keep each evidence owner, predicate, quantity, comparison, uncertainty, and status inside one compatible component;
5. verify scope modifiers such as `broader`, `local`, `full`, `only`, and `subsample` against supplied facts;
6. distinguish assumptions that map prices, quantities, conversions, counterfactual closure, and welfare.

Paper topics, institutions, variable names, estimates, titles, identifiers, and source-specific paragraph structures were not converted into generic writing rules.

## Release decision and limits

The evidence supports public use of the suite for drafting, restructuring, and auditing finance manuscripts. It does **not** support the claims that:

- the skills guarantee publication or reproduce a journal's preferred voice;
- corpus frequencies are mandatory paragraph, sentence, citation, or length rules;
- an agent can resolve missing design facts, conflicting analysis outputs, or unverified citations without author input;
- passing a deterministic matcher proves semantic quality;
- a generic writing workflow substitutes for identification, modeling, or domain expertise.

The blind paper rounds assessed the substantive rule set at commit `da2c20ff8f7438c59be6e6873bf3e43a58690fc4`. Release v1.3.0 added public packaging, bilingual documentation, and language-selection behavior without changing the validated claim and evidence logic. Release v1.3.1 keeps those rules unchanged, consolidates maintainer documentation and duplicate assertions, and prevents local cache files from entering an installation. All deterministic checks are rerun on the final release commit.

## Reproduce the public checks

```bash
python3 scripts/validate_repo.py
python3 scripts/run_skill_evals.py
python3 -m unittest discover -s tests -v
```

To grade saved model responses without exposing assertions during generation, follow the [`evaluation harness`](README.md) and use `scripts/run_behavior_evals.py`.
