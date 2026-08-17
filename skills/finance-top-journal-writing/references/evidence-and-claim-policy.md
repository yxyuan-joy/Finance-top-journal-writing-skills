# Evidence and Claim Policy

## Contents

1. Source hierarchy
2. Fact ledger
3. Claim ladder
4. Citation integrity
5. Missing evidence
6. Bilingual and unit fidelity
7. Copyright and imitation

## 1. Source hierarchy

Use evidence in this order:

1. Author-provided tables, figures, code outputs, model statements, and verified manuscript facts.
2. Final published or accepted-source material explicitly supplied for comparison.
3. Current official journal or publisher instructions for submission requirements.
4. Verified bibliographic sources for literature claims.
5. Clearly labeled inference.

Do not let fluent prose override a conflict among sources. Surface the conflict and preserve the more authoritative record.

For conflicts among author artifacts, use this compact protocol:

1. Record the value, unit, specification, sample, timestamp/version, and source file for every candidate.
2. Prefer a reproducible output tied to the designated final code and data over a manually copied table, slide, screenshot, or prose note.
3. Do not assume that the newest timestamp or most polished exhibit is authoritative; ask which analysis is final when lineage is unclear.
4. Never assemble one claim from pieces of different specifications. The coefficient, uncertainty, sample, baseline, and label must travel together.
5. Keep `[CONFLICT: ...]` in working text until the lineage is resolved, then update every occurrence and cross-reference.

Treat each reported quantity as an atomic evidence bundle. Keep its source or exhibit, specification or model state, sample or population, unit or denominator, uncertainty, comparison or benchmark, and interpretive status linked in the working record whenever applicable. State the subset locally needed to prevent misreading; do not detach, relabel, or recombine a quantity merely to improve flow.

## 2. Build a fact ledger

Before drafting a high-stakes section, record:

| Field | Required content |
|---|---|
| Question | The economic question, not just the regression relation |
| Unit/setting | Who or what is observed, where, and when |
| Data/sample | Sources, period, construction, exclusions, final N |
| Main object | Outcome, treatment/predictor, model object, or equilibrium object |
| Design/model | Variation, estimand, assumptions, or primitives |
| Finding | Sign, magnitude, uncertainty, units, benchmark |
| Scope | Population, period, equilibrium, or maintained assumptions |
| Closest work | Verified papers and exact margin of difference |
| Missing | Facts required before stronger wording is possible |

Keep the ledger separate from polished prose. If two supplied values disagree, mark `[CONFLICT: ...]` and do not choose silently.

## 3. Use the claim ladder

Choose the highest rung the evidence supports:

1. **Document**: `X is higher after Y in this sample.`
2. **Associate**: `X is associated with Y conditional on controls.`
3. **Predict**: `Y predicts X out of sample.`
4. **Identify an effect**: `Y increases X`, conditional on an articulated research design and assumptions.
5. **Distinguish a mechanism**: the evidence separates a channel from plausible alternatives, rather than merely matching one implication.
6. **Quantify a model-implied counterfactual**: the result follows from estimated/calibrated structure with reported fit and sensitivity.

Do not upgrade a claim because the target journal is selective. Downgrade language when the design cannot support the author's requested verb and explain why.

## 4. Protect citation integrity

- Cite only a source that has been provided or verified.
- Use `[CITATION NEEDED: proposition]` instead of inventing an author-year pair.
- Confirm that a cited paper supports the exact sentence, not merely the topic.
- Separate a paper's result from the current paper's interpretation of it.
- Avoid unsupported novelty claims such as `first`, `only`, or `no study`.
- When verified closest sources are supplied, anchor the contribution to the smallest necessary set of papers and identify the exact margin changed. Otherwise use `[VERIFIED CLOSEST-SOURCE COMPARISON NEEDED]`.
- When revising an existing draft, preserve citation keys unless a verified correction is available.

## 5. Handle missing evidence

Use explicit placeholders that state the missing object:

- `[N AND SAMPLE WINDOW NEEDED]`
- `[MAIN ESTIMATE, SE/CI, AND UNITS NEEDED]`
- `[IDENTIFYING ASSUMPTION NEEDS SUPPORT]`
- `[CLOSEST-LITERATURE COMPARISON NEEDED]`
- `[TABLE/FIGURE CROSS-REFERENCE NEEDED]`

Do not fill a placeholder with a plausible-looking number or reference. If the missing fact determines the argument's direction, draft an outline rather than full prose.

Place each limitation, scope condition, or maintained assumption beside the claim it constrains. Do not replace local qualification with repeated end-of-paragraph disclaimer lists.

## 6. Preserve bilingual statistical meaning

Translate the estimand, not only the words. Preserve the supplied sign, unit, denominator, transformation, comparison group, and uncertainty. A reported change or significance label does not by itself reveal whether the source means percent, percentage points, log points, a coefficient scale, economic magnitude, or statistical significance.

When the source is ambiguous, retain the number only in a ledger and use a named placeholder such as `[CONFIRM WHETHER 4.8 IS PERCENT, PERCENTAGE POINTS, OR LOG POINTS]`. Do not convert units, signs, standard errors, confidence intervals, or significance language for fluency. Preserve English variable names and table labels when translating them would break the link to an exhibit.

## 7. Avoid imitation and protected-text reuse

- Extract rhetorical functions and structural patterns, not sentences.
- Never copy long passages from published papers or MinerU text into an output.
- Do not “paraphrase” by swapping a few words while retaining source syntax.
- Use synthetic examples and author-specific facts.
- If the user supplies text for editing, transform only within the requested scope and retain attribution/citations.
