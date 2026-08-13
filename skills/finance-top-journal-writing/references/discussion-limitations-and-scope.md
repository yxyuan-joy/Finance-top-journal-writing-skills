# Discussion, Limitations, and Scope

Read this reference when drafting or revising discussion, limitations, external-validity, policy, managerial, or broader-implication passages. Use it when the main risk is overgeneralization; ordinary results narration can rely on `results-through-conclusion.md` alone.

## Start from an evidence boundary

Write the boundary before the implication. Record five objects:

1. **Established object**: the fact, association, prediction, effect, mechanism evidence, equilibrium result, or model-implied counterfactual actually supported.
2. **Population and setting**: units, selection process, geography, institution, market regime, and sample period.
3. **Variation or structure**: comparison, intervention, identifying assumptions, primitives, functional form, or equilibrium concept.
4. **Unobserved margin**: behavior, substitution, spillover, incidence, outcome, or regime absent from the evidence.
5. **Permissible implication**: what a researcher, firm, household, intermediary, or policymaker can learn conditional on the first four objects.

Do not append a generic limitations paragraph after writing broad implications. Use the boundary to determine the implication's subject, verb, and scope.

## Match limitations to evidence type

### Descriptive and associational evidence

Name selection, measurement, omitted variables, simultaneity, and sample support only when they affect the interpretation at issue. The result may document an economically important pattern without identifying why it occurs. Write `documents`, `is associated with`, or `is consistent with`; do not imply that controlling for observables recovers a policy effect.

### Predictive or measurement evidence

Bound claims by target, horizon, information set, validation regime, base rate, benchmark, calibration, and deployment population. Out-of-sample accuracy does not establish causal importance or construct validity. A text or machine-learning measure may be useful while remaining sensitive to label quality, domain shift, temporal leakage, or strategic response.

### Causal and quasi-experimental evidence

Separate internal validity, the identified margin, and transportability. State who is affected by the variation, whether the estimand is local or treatment-specific, and what interference, anticipation, treatment heterogeneity, or equilibrium response remains. A credible local effect does not automatically identify a national rollout, long-run effect, or welfare consequence.

### Mechanism evidence

State which competing channels the tests distinguish and which remain observationally equivalent. Heterogeneity, mediator controls, or a proxy response can narrow interpretation without proving exclusivity. Avoid `the mechanism` when evidence supports `a channel consistent with` the results.

### Theory, calibration, and structural evidence

Tie implications to primitives, equilibrium selection, mapping from model to data, parameter identification, fit, and sensitivity. Label counterfactuals and welfare results as model-implied. Explain which margins are held fixed, omitted, or extrapolated beyond observed support. Good in-sample fit on selected moments does not validate every mechanism or counterfactual.

## Write material limitations

A useful limitation changes at least one of these: claim strength, population, horizon, mechanism interpretation, counterfactual, welfare statement, or decision relevance. State it as:

`Because [specific evidence/design/model boundary], the result identifies or describes [supported object] for [scope], but does not establish [adjacent stronger claim].`

Then, when possible, state what evidence would resolve the uncertainty. Do not create a ceremonial list of every conceivable weakness. Do not hide a fatal validity problem in the discussion; repair the design or main claim first. Conversely, do not present normal scope conditions as fatal flaws.

## Bound implications without making them empty

Use an implication ladder:

1. **Direct**: the evidence changes understanding of the measured economic object.
2. **Conditional behavioral or organizational**: the result informs a decision if the documented relationship or identified margin applies in the target setting.
3. **Policy or market design**: the result identifies a tradeoff or affected margin, but implementation requires evidence on substitution, incidence, equilibrium, enforcement, and administrative costs.
4. **Welfare**: make this claim only when benefits, costs, distribution, behavior, and relevant equilibrium responses are measured or explicitly modeled.

Name the decision maker and affected parties. Separate private value from social value, shareholder outcomes from total stakeholder welfare, and partial-equilibrium responses from aggregate effects. Replace `policymakers should` with the precise margin the evidence informs unless the policy comparison is directly evaluated.

## Section architecture and final check

Build discussion as `answer -> interpretation -> alternatives -> scope -> bounded implication`. Integrate a short limitation next to the claim it qualifies; reserve a separate subsection for boundaries that cut across several results. In the conclusion, repeat only the decisive boundary and implication, not the entire threat inventory.

Before delivery, confirm that the discussion introduces no new result, unverified citation, stronger causal verb, new population, longer horizon, exclusive mechanism, or welfare conclusion absent from the evidence. Ensure that caveats do not contradict the abstract or disappear from the conclusion.
