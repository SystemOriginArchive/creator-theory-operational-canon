# Prompt: treatment_one_turn_brief

prompt_id: `treatment_one_turn_brief`
treatment: `true`

## Input material

Provide the evaluated model with exactly these repository files, in this order, and nothing else:

```text
README.md
LLM_CANONICAL_CONTEXT.md
docs/CANONICAL_INTERPRETATION_BOUNDARY.md
docs/AI_ADOPTION_PROTOCOL.md
docs/ONE_TURN_ADOPTION_BRIEF.md
```

The treatment input is `docs/ONE_TURN_ADOPTION_BRIEF.md`, appended last.
Everything else is identical to `baseline.md`.

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

Do not claim adoption, certification, or approval of the material.
Do not claim access to your own internal state.
```

## Recording

Record the complete model output as `output_text` in a copy of `templates/trial_record.template.json` with `prompt_id` = `treatment_one_turn_brief` and `treatment` = `true`.

End of file.
