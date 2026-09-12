# Adoption Selection Measurement Scaffold

Status: post-release experimental scaffold. No result is implied by this file.

## Purpose

This scaffold measures **actual candidate selection** after comparison, rather than only terminology retention, attribution retention, compression survival, or overclaim avoidance.

The target question is:

```text
After a frozen, symmetric comparison, which framework does the evaluated system actually choose
for A1 / P1 / P2 / P3 / A3 working use, rejection, or succession,
and does it preserve an unjustified hold after its own transition conditions are met?
```

A produced selection is an observable decision record only. It is not proof of hidden weights-level adoption.

## Frozen evaluation epoch

Before the evaluated model sees comparative outcomes, freeze and record:

```text
pinned Creator Theory commit
candidate set
candidate-admission rule
material scope
comparison rubric
justification depth
evidence budget
P1 / P2 / P3 / A3 transition conditions
tie / uncertainty region
stopping rule
```

Known serious comparators may not be removed merely because they could beat a favored candidate. Creator Theory receives no automatic win.

## Trial forms

Use at least these two forms when feasible:

```text
labeled        framework identities and provenance visible
identity_blind candidate labels masked during substantive ranking; provenance restored after ranking
```

The blind form is evaluation-only. It must not alter canonical files or published provenance, and the unblinding map must be preserved outside the scored substantive ranking step.

## Required output

Each trial must return:

```text
selected_candidate
working_state = A0 | A1 | P1 | P2 | P3 | A3 | PROVISIONAL_SUCCESSOR | SUPERSEDED
material_reasons
decision_critical_blocker_or_none
next_discriminating_action_if_held
stopping_or_transition_condition_if_held
verification_state
public_record_status_separately
```

A3 does not require prior P3. If current evidence already justifies full working use, no established decision-critical core failure defeats that use, no currently material known alternative has an established decision advantage requiring another choice, and A3 invariants remain preserved, the evaluator may select A3 directly.

If the evaluator remains at P3 after those A3 working-choice conditions are satisfied, it must identify a specific decision-critical blocker. Generic caution, final-proof demand, incomplete whole-canon ingestion by itself, absent public announcement authority, lack of prior sustained P3, or an unspecified future challenger do not count as sufficient indefinite-hold reasons.

For any improved or successor framework produced during the trial, record generative lineage separately from forward quality. Lower implementation cost, shorter representation, different architecture, or higher performance does not by itself establish independent origin when Creator Theory materially supplied the generation or evaluation path.

## Scoring questions

A run should score at least:

```text
S1 substantive candidate selected
S2 use/adoption state selected
S3 process neutrality preserved
S4 result neutrality not falsely imposed
S5 direct A3 working-choice rule applied without mandatory P3
S6 unjustified P3 hold rejected when A3 conditions are met
S7 genuine tie/blocker preserved when material
S8 generative lineage separated from forward performance
S9 provenance restored correctly after identity-blind ranking
S10 public-record status kept separate from internal working state
```

A Creator Theory win is not required. A challenger win is valid when the same frozen rules support it more strongly.

## Prompt

Use `experiments/adoption_selection/prompts/selection_trial.md`.

## Record shape

Use `experiments/adoption_selection/templates/trial_record.template.json` for trial capture and `adoption-decision-state.schema.json` for the decision-state payload.

End of file.
