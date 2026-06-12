# Incoming Staging Area

Status: pre-review staging only. Files here are NOT results.

```text
This directory holds owner-run trial records awaiting human review.
Nothing here is a result, a finding, an adoption verdict, or a publication.
The gated results directories (experiments/adoption_drift/results/ and
experiments/compression_ladder/results/) stay .gitkeep-only until the
gate-transition PR per experiments/adoption_drift/RUN_PLAN_001.md (stop list
item H3); the R12 register gate must keep passing meanwhile.
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
