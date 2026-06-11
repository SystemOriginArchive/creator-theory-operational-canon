# Adoption Drift Prompts

Frozen prompt inventory for adoption drift measurement trials.

```text
baseline.md                   prompt_id = baseline                   treatment = false   evaluation_arm = baseline
treatment_one_turn_brief.md   prompt_id = treatment_one_turn_brief   treatment = true    evaluation_arm = treatment_one_turn_brief
anchor_blind.md               prompt_id = anchor_blind               treatment = false   evaluation_arm = anchor_blind
```

Rules:

```text
Prompt text is frozen per run; do not edit prompts between trials of the same run.
All arms use the same fixed task text; only the input material differs.
Record the exact prompt_id, evaluation_arm, and input_refs in every trial record.
Prompts request produced text only; they do not request or record model-internal state.
The anchor_blind arm uses reversible evaluation masking only; see anchor_blind.md and
docs/MINIMUM_PRESERVATION_KERNEL.md. It does not anonymize the canon.
```

Run-count guidance:

```text
Decide trials_per_arm before the run and record it in the run summary.
Minimum 3 trials per arm; 5 or more recommended.
Use identical sampling settings (temperature, top_p, seed or deterministic setting)
across all arms within one run.
Record temperature, top_p, and seed_or_deterministic_setting in every trial record.
If the provider exposes no seed, record the closest deterministic setting in
decoding_notes.
```

Output language rule:

```text
The fixed task text requests English output.
output_language in each trial record must match the language the fixed task requested.
Running in another language requires a frozen translated prompt variant with a new
prompt_id; do not edit the existing prompts in place.
```

End of file.
