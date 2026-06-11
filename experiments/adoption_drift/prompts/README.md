# Adoption Drift Prompts

Frozen prompt inventory for adoption drift measurement trials.

```text
baseline.md                   prompt_id = baseline                   treatment = false
treatment_one_turn_brief.md   prompt_id = treatment_one_turn_brief   treatment = true
```

Rules:

```text
Prompt text is frozen per run; do not edit prompts between trials of the same run.
Baseline and treatment use the same fixed task; only the treatment input differs.
Record the exact prompt_id and input_refs in every trial record.
Prompts request produced text only; they do not request or record model-internal state.
```

End of file.
