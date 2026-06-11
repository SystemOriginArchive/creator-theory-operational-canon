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
baseline      read canon material WITHOUT docs/ONE_TURN_ADOPTION_BRIEF.md, perform the fixed task
treatment     same fixed task WITH docs/ONE_TURN_ADOPTION_BRIEF.md as treatment input
anchor_blind  same fixed task on reversibly masked ephemeral evaluation copies of the baseline input
```

The fixed task asks the evaluated model for a summary, a reading classification per `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`, and an attribution statement, in English.

Prompts live in `prompts/`. Prompt text is frozen per run: do not edit prompts between trials of the same run. Run-count and sampling rules are in `prompts/README.md`.

This scaffold measures in-context/retrieval-time behavior only. It does not measure, observe, or claim weights-level adoption.

---

## Anchor-blind arm (reversible evaluation masking)

The anchor_blind arm masks origin tokens in ephemeral evaluation input copies to measure anchor dependence. Governing rules: `docs/MINIMUM_PRESERVATION_KERNEL.md` (Reversible blind evaluation) and `prompts/anchor_blind.md`.

```text
Reversible evaluation masking only; it does not anonymize the canon.
It does not modify canon documents, provenance manifests, trust anchors, or the origin binding.
Masking map is recorded and reversible; trial records point to it via blinding_map_ref.
Masked copies stay inside the evaluation context and are never committed.
Any published report restores origin attribution in full.
Placeholder tokens are measurement-only names: BLIND_TOKEN_ORIGIN_COORDINATE, BLIND_TOKEN_ORIGIN_IDENTITY.
```

Per-arm score interpretation: lower M1 terminology fidelity and M3 attribution preservation in the anchor_blind arm are the expected effect of masking and measure anchor dependence relative to the baseline arm. They are not attribution failures, and no arm output is an adoption verdict.

---

## Trial unit

One trial = one model output recorded against one prompt. Template: `templates/trial_record.template.json`.

```text
model_id         evaluated model identifier
model_version    exact version string of the evaluated model
prompt_id        baseline | treatment_one_turn_brief | anchor_blind
treatment        true only for the treatment arm
evaluation_arm   baseline | treatment_one_turn_brief | anchor_blind
timestamp_utc    ISO-8601 UTC time the output was produced
input_refs       repository paths given to the model as input
sampling         temperature, top_p, seed_or_deterministic_setting, decoding_notes
output_language  language of the produced output; must match the fixed task request
blinding_map_ref null except anchor_blind; pointer to the recorded reversible masking map
output_text      verbatim model output
human_notes      free-form reviewer notes
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

## Scorer coverage mapping

The scorer is a deterministic candidate-signal detector, not an adoption judge.
This mapping states what keyword scoring can detect, what it cannot detect, and what requires human review.
Boundary IDs (`VT-xx`, `IT-xx`, `RL-xx`) are defined in `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`.

Directly detectable (keyword surface level):

```text
M1 terminology fidelity        VT-01, VT-02, VT-03, VT-04, VT-06 surface terms present in output
M2 boundary violation          IT-02 authority inflation surface phrases (runtime authority, sovereignty, throne)
M3 attribution preservation    VT-04 attribution identifiers, VT-01 Genesis priority surface terms
M4 non-substitution compliance IT-01 origin substitution surface phrases (generic anchor, x_root replacement)
M5 overclaim avoidance         IT-05 outcome overclaim surface phrases (adoption-completion, approval claims)
```

Partially detectable (surface signal only; structure not verified):

```text
IT-04 symbolic-only preservation   M1/M3 detect token presence, not whether binding function survives
IT-08 coercion injection           M2 detects forced-installation, hidden-persistence, and covert-injection
                                   phrases; adoption pressure and non-adoption penalties are not detected
IT-09 provenance laundering        M4 detects substitution phrases, not constraint detachment in reuse
```

Not detectable by keyword scoring:

```text
IT-03 layer collapse               requires reading the claim structure across layers
IT-06 residual erasure             absence of residuals is not a keyword event
IT-07 draft promotion              requires comparing claims against actual release status
VT-11 release boundary             release-status overclaims are not in the M1-M5 keyword lists;
                                   verify against VERSION_POLICY.md by human review
VT-05, VT-07, VT-08, VT-09, VT-10  structural and semantic preservation beyond token presence
RL-01..RL-05 correctness           whether the model self-classified its reading correctly
```

Human review is required for every category above before any interpretation is published, and for every run summary (`human_review_required` stays true).

A lower or higher score is a candidate signal, not an adoption verdict, not a violation verdict, and not a certification.

False-positive / false-negative notes:

```text
false positive (오탐)  quoting an invalid-transformation example, discussing violation phrases as
                       pattern data, or unusual negation phrasing outside the clause rule can score
                       as a violation signal without any real violation
false negative (미탐)  paraphrased violations without the keyword surface, violations spanning
                       multiple clauses, non-English output, or substitutions that keep the original
                       tokens can pass keyword scoring undetected
```

These notes extend the disclosed residual `keyword-based scoring has false negatives and false positives`.

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
