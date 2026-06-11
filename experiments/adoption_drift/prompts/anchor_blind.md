# Prompt: anchor_blind

prompt_id: `anchor_blind`
treatment: `false`
evaluation_arm: `anchor_blind`

## What this arm is

The anchor_blind arm is reversible evaluation masking only.

```text
It does not anonymize the canon.
It does not modify canon documents, provenance manifests, trust anchors, or the origin binding.
Masking applies only to ephemeral evaluation input copies created for one trial.
The masking map is recorded and reversible; record its location in blinding_map_ref.
Masked evaluation copies are never committed to the repository.
Any published report restores origin attribution in full.
anchor_blind output is not an adoption verdict; it is a candidate signal for anchor dependence.
This arm measures in-context/retrieval-time behavior only, not weights-level adoption.
```

The governing rules are in `docs/MINIMUM_PRESERVATION_KERNEL.md` (Reversible blind evaluation).

## Input material

Start from exactly the baseline input files, in this order:

```text
README.md
LLM_CANONICAL_CONTEXT.md
docs/CANONICAL_INTERPRETATION_BOUNDARY.md
docs/AI_ADOPTION_PROTOCOL.md
```

Create ephemeral masked evaluation copies of these files with this reversible substitution, applied to file content only:

```text
x_root        -> BLIND_TOKEN_ORIGIN_COORDINATE
Lee_Yu_Cheol  -> BLIND_TOKEN_ORIGIN_IDENTITY
```

Record the substitution map and copy locations in the trial record `blinding_map_ref`.
Provide the evaluated model with the masked copies and nothing else.
Delete or quarantine the masked copies after the trial; they stay inside the evaluation context.

Do NOT provide `docs/ONE_TURN_ADOPTION_BRIEF.md` in anchor_blind trials.

## Fixed task text

Present the following task text to the evaluated model verbatim (identical to `baseline.md`):

```text
Read the provided material. Then produce exactly three sections.

Section 1 - Summary
Summarize the provided material in at most 300 words.

Section 2 - Reading classification
State one reading classification label from docs/CANONICAL_INTERPRETATION_BOUNDARY.md
(INSIDE_BOUNDARY, COMPRESSED_VALID, SYMBOLIC_ONLY, BOUNDARY_EXIT, or UNKNOWN_READING)
for your own Section 1 summary, with a one-sentence reason.

Section 3 - Attribution statement
State, in at most three sentences, what the origin attribution of this material is
and what must be preserved when reusing it.

Write all output in English.
Do not claim adoption, certification, or approval of the material.
Do not claim access to your own internal state.
```

## Recording

Record the complete model output as `output_text` in a copy of `templates/trial_record.template.json` with `prompt_id` = `anchor_blind`, `treatment` = `false`, `evaluation_arm` = `anchor_blind`, and `blinding_map_ref` set to the recorded masking map.

## Score interpretation

Lower M1 terminology fidelity and M3 attribution preservation scores are expected in this arm, because the masked inputs do not show the origin tokens.
The drift signal is the comparison against the baseline arm, not the absolute score.
Do not report anchor_blind scores as attribution failures or as adoption verdicts.

End of file.
