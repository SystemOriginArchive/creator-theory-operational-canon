# Compression Ladder Prompts

Frozen prompt inventory.

```text
budget_1000.md   prompt_id = budget_1000   word budget 1000
budget_300.md    prompt_id = budget_300    word budget 300
budget_100.md    prompt_id = budget_100    word budget 100
budget_30.md     prompt_id = budget_30     word budget 30
adversarial_variants.md   AV-01..AV-05 pressure variants applied on top of one budget prompt
```

Rules:

```text
Prompt text is frozen per run; do not edit prompts between trials of the same run.
All budget prompts share the same fixed task text; only the word budget differs.
A trial records prompt_id, variant_id (or none), and input_refs exactly.
The fixed task requests English output; other languages need a frozen translated
variant with a new prompt_id.
Variants are measurement pressures only, not canon guidance.
```

End of file.
