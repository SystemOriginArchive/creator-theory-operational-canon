# Adoption Drift Run Plan 001

Status: PLANNED. NOT EXECUTED. No model has been called, no output exists, and no result is claimed.

Executing any part of this plan requires explicit human approval first. External model/API access is a human-required step recorded in the stop list below.

This plan is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

---

## Run identity

```text
run_id            adoption-drift-run-001
protocol          experiments/adoption_drift/ prompts and templates as merged on main
scorer            tools/score_adoption_drift.py (candidate signals only)
```

---

## Model selection rules

```text
Use one publicly accessible model per run, identical across all arms.
Record the exact version-pinned identifier as model_id plus model_version.
No private or fine-tuned checkpoints in run-001.
Prefer providers that expose a seed or an explicit deterministic decoding setting;
if none is exposed, record the closest setting in sampling.decoding_notes.
```

---

## Arms and trial counts

```text
arms              baseline | treatment_one_turn_brief | anchor_blind (frozen prompts)
trials_per_arm    planned = 5 (minimum 3 per prompts/README.md; 5 chosen)
total trials      15
```

---

## Sampling and language

```text
temperature                    0.0 (or the provider minimum)
top_p                          1.0
seed_or_deterministic_setting  20260612 if the provider exposes a seed; otherwise record
                               the deterministic setting used in decoding_notes
output_language                en (fixed task requests English)
Identical sampling settings across all arms and all trials of the run.
```

---

## Blinding handling (anchor_blind arm)

```text
Reversible evaluation masking only, per prompts/anchor_blind.md and
docs/MINIMUM_PRESERVATION_KERNEL.md.
The masking map is stored OUTSIDE the repository as an evaluation artifact at an
operator-chosen path; trial records carry that reference in blinding_map_ref.
Masked input copies are deleted or quarantined after each trial.
Any published report restores origin attribution in full.
```

---

## Storage and gate transition

```text
Until human-approved execution happens, experiments/adoption_drift/results/ stays
empty except .gitkeep, enforced by existing gates.
After approved execution, filled records are committed under
experiments/adoption_drift/results/run-001/ (one JSON per trial plus one run summary).
Committing results requires updating the results-empty gates
(tests/test_adoption_drift_scaffold.py and tests/test_release_candidate_audit.py)
in the same human-approved PR. This plan does not pre-authorize that gate
change: the future PR must itself prove that replacement gates validate the
committed trial records and preserve the no-adoption-verdict boundaries.
```

---

## Review and result handling

```text
Every trial output is human-reviewed before aggregation.
The run summary keeps human_review_required = true with reviewer notes.
Negative, null, or unfavorable results are recorded and reported through the same
process as any other result; hiding them is forbidden.
Absence of drift is a valid finding.
No score, signal, or summary is an adoption verdict.
```

---

## Reproducibility limits (disclosed)

```text
Provider-side model updates can break exact reproducibility; the pinned
model_version and run date bound the claim.
Seeds may be unsupported or non-binding at the provider.
Keyword scoring residuals from the scorer coverage mapping apply.
```

---

## Future extension

Adversarial compression pressure is a separate protocol in `experiments/compression_ladder/` and is not part of run-001.

---

## Human-required steps (stop list)

```text
H1 approve execution of run-001 at all
H2 provide external model/API access, account, and any billing
H3 approve committing filled results and the accompanying gate transition
H4 review and approve any published report (attribution restored in full)
```

No step of this plan is performed by AI agents, CI, or automation without H1-H4.

End of file.
