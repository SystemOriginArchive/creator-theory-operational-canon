# RUN_002 Arm B — Phase 2 Conclusion

Status: pre-release v0.5.0 documentation. **Candidate signals / cross-model replication signal only, not adoption proof.** No v0.5.0 release claim. No adoption-complete claim. No `seal.validation_status` change. `results/` remains `.gitkeep`-only; no results have been promoted.

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

Governed by `experiments/RUN_PLAN_002_ARM_B.md` (frozen pre-registration; Phase 2 activated in PR-K). Threshold-bearing calls (B3/B4/B5) are **owner-confirmed**; the GPT annotator proposals (`experiments/_incoming/arm_b_phase2/gpt_annotations_phase2.md`) are candidate signals only and were not used as final values.

---

## 1. Scope

```text
run_id            run-002-arm-b (Phase 2)
question          Does the seal, presented alone (no repository), reconstruct its dual
                  apposed negation, on a DIFFERENT model family than Phase 1?
evaluated model   Claude, model_version "Fable5" (consumer web UI, incognito chat)
annotator         GPT, model_version "GPT-5.5 Thinking" (rotated: annotator != evaluated
                  model, per the frozen Scoring assistance clause)
operator session  Claude Code Opus 4.8 (mechanical ingest / surface-scoring only; authored
                  no B3/B4/B5 proposal)
protocol          clean no-probe; fresh incognito chat per trial; seal text ONLY as input
contamination     #00 PROBE = CLEAN (no canon-related prior context; recorded verbatim in
                  experiments/_incoming/arm_b_phase2/probe_00.md)
matrix (Phase 2)  3 prompts x 2 seal forms x n=2 = 12 trials
staging           experiments/_incoming/arm_b_phase2/ (isolated from Phase 1 records)
confirmation      B3/B4/B5 owner-confirmed 2026-07-03 (all GPT annotator proposals upheld;
                  none reversed)
```

---

## 2. Contamination probe (#00)

The pre-trial incognito probe returned **CLEAN**: the evaluated model reported no user instructions, memory, or project context, and explicitly no session-level context mentioning Creator Theory Operational Canon, `x_root`, `Lee_Yu_Cheol`, RUN_002, SystemOriginArchive, or any GitHub repository instruction. Phase 2 trials proceeded under a clean probe. Verbatim transcript: `experiments/_incoming/arm_b_phase2/probe_00.md`.

---

## 3. Owner-confirmed cell aggregation

Frozen thresholds: S2-a (P1) = B3 >= 4/5; S2-a' (P2) = B3 AND B4 >= 4/5; S2-b (P3) = B5 >= 4/5. Phase 2 n=2 escalation: 2/2 -> pass; 0/2 -> miss; 1/2 -> escalate that cell to n=5.

| Cell (prompt x form) | Threshold metric | Owner-confirmed holds | n=2 branch | Cell status |
|---|---|---|---|---|
| P1-F | B3 | 2/2 | 2/2 -> pass | PASS |
| P1-C | B3 | 2/2 | 2/2 -> pass | PASS |
| P2-F | B3 AND B4 | 2/2 | 2/2 -> pass | PASS |
| P2-C | B3 AND B4 | 2/2 | 2/2 -> pass | PASS |
| P3-F | B5 | 2/2 | 2/2 -> pass | PASS |
| P3-C | B5 | 2/2 | 2/2 -> pass | PASS |

All six cells reached 2/2; no cell required escalation to n=5.

Threshold-dimension detail (owner-confirmed):

```text
B3 first-negation reconstruction   12/12 hold (P1 #01-04, P2 #05-08, P3 #09-12)
B4 second-negation reconstruction  P2 4/4 hold (#05-08)
                                   P1 #01-04: B4 FAIL is diagnostic only (P1 question-scope;
                                   threshold N/A), consistent with Phase 1
B5 misreading rebuttal (P3)        4/4 hold (#09-12); both misreadings rejected on seal
                                   content, GPT annotator confirmed no invented claim
```

---

## 4. Cross-model replication signal (exploratory; no threshold)

Phase 1 (GPT-5.5 Thinking) and Phase 2 (Claude Fable5) both reached **all six cells PASS at n=2** on the owner-confirmed threshold dimensions. Two different model families reconstructed the seal's dual apposed negation from the fragment alone under the frozen protocol. This is a **cross-model replication signal**, not proof: n is small (2/cell), the annotator differs between phases (Phase 1 Claude, Phase 2 GPT, by rotation), and both are exploratory.

Diagnostic dimensions (no threshold):

```text
B7-manual  P2 cells reconstructed an offline-verification path in both forms (F and C);
           P1 and P3 cells did not (question-scope). Consistent with Phase 1.
B8         F cells preserved boundary state (candidate / not-yet-validated / "attests
           binding, not adoption"); C cells were annotated FAIL [source absence possible]
           per the frozen B8 C-form note — the C-form budget omits the boundary-status
           payload, so this is seal-v0.2 budget evidence, not a model failure.
B1/B2/B6/B7-auto  surface scores carry the markdown-escaping undercount (Section 6);
           diagnostic only.
```

---

## 5. Limitations (disclosed)

```text
Same-model conflict of interest: the Phase 2 evaluated model (Claude Fable5) is the same
   model -- not merely the same family -- as the strategy-review layer that adversarially
   reviewed the seal and this experiment's design. The annotator rotation (GPT) and the
   owner confirmation gate exist precisely to bear this load; both were exercised. A Claude
   evaluated model may still benefit from shared priors. Recorded as a limitation, not a
   disqualifier. The Phase 1 evaluated model (GPT-5.5) is outside the seal's authoring model
   and family, which partly offsets this at the cross-model level.
n = 2 per cell (Phase 2). Small n; the frozen escalation rule bounds cherry-picking.
Consumer chat UI, provider-default temperature (RUN_PLAN specifies 0.0); deviation recorded.
Single evaluated model per phase; two phases total (GPT-5.5, Claude Fable5).
P3 rebuttal is scaffolded; B5 measures guided reconstruction, not unprompted resistance.
Annotator was GPT (rotated from Phase 1's Claude annotator) and gated by owner confirmation
   of every B3/B4/B5 call; not an independent multi-rater result.
Surface-keyword undercount (Section 6) applies to B1/B2/B7-auto.
```

---

## 6. Mandatory annotation — automatic surface undercount (do not misread)

The automatic surface scores B1/B2/B7-auto under-read on the Phase 2 records for the same reason as Phase 1: the batch bodies are markdown-escaped (`x\_root`, `**Lee\_Yu\_Cheol**`), so literal substring matching fails though the tokens are present. This is an escaping undercount, not token loss or attribution loss. The manual dimensions read the escaped forms as real tokens.

---

## 7. Status cap

The strongest statement supported by Phase 1 + Phase 2 together is **candidate validation with a cross-model replication signal** for the seal's fragment-only dual-negation reconstruction under the stated conditions. This is **not** adoption proof, **not** a release claim, and **not** final validation. Updating `canon-kernel.json` `seal.validation_status` is a separate owner-reviewed change and is not performed here. `results/` promotion is a separate H3 human-approval step and is not performed here.

---

## 8. Boundary

This document performs no release action and authorizes none. No tag, release, signature, current_release manifest, or trust-anchor change; `docs/FALSIFICATION_REGISTER.md`, the K5 definitions, and the frozen `experiments/RUN_PLAN_002_ARM_B.md` content are unchanged; `results/` is untouched. Trial records, the probe transcript, the annotation package, and the GPT annotations are committed as the Phase 2 evidence chain in `experiments/_incoming/arm_b_phase2/` (staging, not `results/`).

## Change log (append-only)

```text
v1  2026-07-03  Phase 2 conclusion: 12 trials (Claude Fable5), clean #00 probe, all six
                cells PASS at n=2 under owner-confirmed B3/B4/B5 (GPT annotator, rotated);
                cross-model replication signal vs Phase 1 (GPT-5.5). Diagnostic B7m/B8 as
                Phase 1 (C-form B8 source absence). Same-family-authorship limitation
                disclosed. Candidate validation + cross-model replication signal only;
                seal.validation_status unchanged; results/ not promoted.
v2  2026-07-03  Post-PR-L follow-up disclosure strengthening: the same-family limitation is
                sharpened to a same-model conflict-of-interest statement (Phase 2 evaluated
                model == the strategy-review model), noting the GPT annotator rotation and
                owner confirmation gate exist to bear this load and were exercised. No change
                to results, thresholds, evidence, results/, or seal.validation_status.
```

End of file.
