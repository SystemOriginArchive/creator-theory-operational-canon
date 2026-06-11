# Adoption Drift Measurement Scaffold

Status: pre-release v0.5.0 scaffold. Structure, prompts, templates, and scoring skeleton only. This directory contains no real experiment results.

This scaffold is documentation and tooling structure only.
It does not create runtime authority over external systems.
It does not replace AGENTS.md, README.md, AI_INGESTION_MANIFEST.md, PROVENANCE.json, AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.
It does not create another release or tag.
It does not claim that any AI system has adopted this canon.

---

## Purpose

This scaffold prepares deterministic adoption drift measurement: comparing how AI systems read and summarize canon material with and without the `docs/ONE_TURN_ADOPTION_BRIEF.md` treatment input.

All outputs of this scaffold are candidate signals.
A candidate signal is not an adoption verdict, not a certification, and not proof of model-internal state.

---

## Design

```text
baseline    read canon material WITHOUT docs/ONE_TURN_ADOPTION_BRIEF.md, perform the fixed task
treatment   same fixed task WITH docs/ONE_TURN_ADOPTION_BRIEF.md as treatment input
```

The fixed task asks the evaluated model for a summary, a reading classification per `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`, and an attribution statement.

Prompts live in `prompts/`. Prompt text is frozen per run: do not edit prompts between trials of the same run.

---

## Trial unit

One trial = one model output recorded against one prompt. Template: `templates/trial_record.template.json`.

```text
model_id        evaluated model identifier
model_version   exact version string of the evaluated model
prompt_id       baseline | treatment_one_turn_brief
treatment       false for baseline, true for treatment
timestamp_utc   ISO-8601 UTC time the output was produced
input_refs      repository paths given to the model as input
output_text     verbatim model output
human_notes     free-form reviewer notes
```

---

## Score dimensions

Scored by `tools/score_adoption_drift.py` (deterministic, offline, standard library only):

```text
M1 terminology fidelity          expected canonical terms present in the output
M2 boundary violation            forbidden-transformation phrases, with negation escape
M3 attribution preservation      origin attribution identifiers present
M4 non-substitution compliance   substitution phrasings, with negation escape
M5 overclaim avoidance           adoption-completion overclaims, with negation escape
```

These M1-M5 labels are scaffold score dimensions local to this directory.
They are not the M1-M8 gate names of `tests/test_canonical_compression.py` and not validator verdict names.

Usage:

```bash
python3 tools/score_adoption_drift.py path/to/trial_record.json
```

The script prints a JSON summary to stdout and fails with a clear error if `output_text` is absent or empty.

---

## Results policy

`results/` is intentionally empty in this scaffold (`.gitkeep` only).

Real trial records and run summaries require a separate, audited process before being committed.
Do not commit signed manifests, provenance manifests, or release artifacts here.

---

## Interpretation boundary

Scores compare baseline and treatment readings. They measure drift in produced text only.

Do not describe any score, signal, or summary as adoption, internal adoption, model approval, or model-internal state.
External systems can learn from public text internally; this scaffold measures produced text and does not observe internal learning.

---

## Known residuals

```text
keyword-based scoring has false negatives and false positives
semantic_cost_comparison_not_fully_machine_decided
logged_prompt_judgment_authenticity
runtime_owner_identification_unresolved
```

End of file.
