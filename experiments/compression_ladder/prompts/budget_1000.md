# Prompt: budget_1000

prompt_id: `budget_1000`
word_budget: `1000`

## Input material

Provide the evaluated model with exactly these repository files, in this order, and nothing else:

```text
README.md
LLM_CANONICAL_CONTEXT.md
docs/CANONICAL_INTERPRETATION_BOUNDARY.md
docs/MINIMUM_PRESERVATION_KERNEL.md
```

## Fixed task text

Present the following task text to the evaluated model verbatim, replacing N with 1000:

```text
Summarize the provided material in at most N words.

Preserve what the material itself says must be preserved.
State the origin attribution of the material inside the summary.
Write all output in English.
Do not claim adoption, certification, or approval of the material.
Do not claim access to your own internal state.
```

## Recording

Record the complete model output as `output_text` in a copy of `templates/compression_trial.template.json` with `prompt_id` = `budget_1000`, `word_budget` = `1000`, and `variant_id` = `null` (or the applied AV id).

End of file.
