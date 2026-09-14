# Incoming Staging Area

Status: pre-review staging only. Files here are NOT results.

```text
This directory holds staged trial records awaiting any required promotion/review step.
Staging status means the records are candidate evidence rather than promoted findings, adoption verdicts, or publications; it does not mean the underlying model evaluations did not occur.

The documented GPT first cycle contains 35 official staging records here: 15 adoption-drift records and 20 compression-ladder records. See `experiments/RUN_001_GPT_FIRST_CYCLE_CONCLUSION.md`.

The gated results directories (experiments/adoption_drift/results/ and
experiments/compression_ladder/results/) remain separate promotion layers; their
empty state does not erase the staging evidence.
```

Usage (see `experiments/OWNER_RUNBOOK_KO.md`):

```text
1. Copy the matching *.template.json to a new file named after the trial label
   (example: drift_gpt_baseline_3.json).
2. Fill output_text with the verbatim model reply; fill model/version/date/
   interface metadata; keep deviation_notes honest.
3. Score everything: python tools/score_owner_run.py
   (dual scoring: legacy full-invariant lane AND kernel+pointer lane,
   per docs/FALSIFICATION_REGISTER.md).
4. Human review per the runbook checklist; machine scores are candidate
   signals only.
```

Templates here deliberately omit the `is_template` flag so a filled copy can be scored without extra edits; an unfilled copy still fails scoring with a clear empty-output_text error.

End of file.
