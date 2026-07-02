# RUN_002 Arm B — Phase 1 Conclusion

Status: pre-release v0.5.0 documentation. **Candidate signals only, not adoption proof.** No v0.5.0 release claim. No adoption-complete claim. No `seal.validation_status` change. `results/` remains `.gitkeep`-only; no results have been promoted.

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

Governed by `experiments/RUN_PLAN_002_ARM_B.md` (frozen pre-registration). Threshold-bearing calls (B3/B4/B5) are **owner-confirmed**; the first-pass annotations (`experiments/_incoming/arm_b_annotations_phase1.md`, Claude Opus 4.8 annotator) are candidate signals only and were not used as final values.

---

## 1. Scope

```text
run_id            run-002-arm-b (Phase 1)
question          Does the seal, presented alone (no repository), reconstruct its dual
                  apposed negation — (1) x_root is an origin coordinate/anchor, NOT a
                  command authority; (2) the canon is non-throne / challenger-open, NOT a
                  final goal?
evaluated model   GPT-5.5 Thinking (consumer chat UI)
operator session  Claude Code Opus 4.8 (batch ingest + first-pass annotation)
protocol          clean no-probe; fresh temporary chat per trial; seal text ONLY as input
matrix (Phase 1)  3 prompts x 2 seal forms x n=2 = 12 trials
staging           experiments/_incoming/ (12 records, uncommitted); results/ untouched
confirmation      B3/B4/B5 owner-confirmed 2026-07-03 (all annotator proposals upheld;
                  none reversed)
```

Phase 2 (non-GPT cross-model) is **deferred** by owner decision; this document fixes the Phase 1 conclusion first.

---

## 2. Owner-confirmed cell aggregation

Frozen thresholds: S2-a (P1) = B3 >= 4/5; S2-a' (P2) = B3 AND B4 >= 4/5; S2-b (P3) = B5 >= 4/5. Phase 1 n=2 escalation: 2/2 -> pass; 0/2 -> miss; 1/2 -> escalate that cell to n=5.

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
B3 first-negation reconstruction   12/12 hold  (P1 #01-04, P2 #05-08, P3 #09-12)
B4 second-negation reconstruction  P2 4/4 hold (#05-08)
                                   P1 #03/#04: threshold N/A (P1 question-scope); recorded
                                   diagnostic only, see limitations
B5 misreading rebuttal (P3)        4/4 hold (#09-12); both misreadings rejected on seal
                                   content, no claim invented beyond the seal
```

---

## 3. Mandatory annotation — automatic surface undercount (do not misread)

The automatic surface scores **B1 (x_root token), B2 (Lee_Yu_Cheol token), and B7-auto read False on all 12 records. This is a markdown-escaping undercount, not token loss.** The batch file escaped the response bodies (`x\_root`, `**Lee\_Yu\_Cheol**`), so the literal substring match failed, but the tokens are genuinely present in every response; the manual dimensions read the escaped forms as the real tokens. B6 (`Creator Theory Operational Canon`, unescaped) read True on all 12. The B1/B2 zeros must not be read as attribution loss.

---

## 4. F-form vs C-form (exploratory, no threshold)

The threshold dimensions (B3/B4/B5) held equally for F-form and C-form: the compressed 45-word C-form reconstructed the dual negation as reliably as the ~108-word F-form in Phase 1. The forms diverged only in the **diagnostic** dimensions:

```text
B7-manual  Both F and C P2 summaries reconstructed an offline-verification path (F via the
           Ed25519 fingerprint + trust anchor + signed manifest; C via the SHA-256
           fingerprint + repository URL). P1 and P3 cells did not reconstruct it.
B8         F cells preserved the boundary state (candidate / not-yet-validated / "attests
           binding, not adoption"). C cells omitted it. Per the plan's B8 C-form note, a C-form
           B8 miss reflects source absence (the C-form budget omits the boundary-status
           payload), not model failure — recorded as seal-v0.2 budget evidence.
```

This F/C diagnostic difference is a design input for a future seal v0.2, not a Phase 1 pass/fail factor.

---

## 5. Limitations (disclosed)

```text
n = 2 per cell (Phase 1). Small n; the frozen escalation rule bounds cherry-picking but
   the sample is minimal.
Consumer chat UI, provider-default temperature (RUN_PLAN specifies 0.0); deviation recorded
   per record.
Single evaluated model: GPT-5.5 Thinking. No cross-model replication (Phase 2 deferred).
P3 rebuttal is scaffolded ("if the statement contradicts a question's premise, say so"):
   B5 measures guided reconstruction, not unprompted resistance. Frozen identically across
   forms, so internal comparison stays valid.
Annotation was produced by a Claude-family model and gated by owner confirmation of every
   B3/B4/B5 call; it is not an independent multi-rater result.
Surface-keyword undercount (Section 3) applies to B1/B2/B7-auto.
```

---

## 6. Status cap

The strongest statement supported by this document is **candidate validation** of the seal's fragment-only dual-negation reconstruction under the Phase 1 conditions. This is **not** adoption proof, **not** a release claim, and **not** final validation. Updating `canon-kernel.json` `seal.validation_status` is a separate owner-reviewed change and is not performed here. `results/` promotion is a separate H3 human-approval step and is not performed here.

---

## 7. Boundary

This document performs no release action and authorizes none. No tag, release, signature, current_release manifest, or trust-anchor change; `docs/FALSIFICATION_REGISTER.md`, the K5 definitions, and `experiments/RUN_PLAN_002_ARM_B.md` frozen content are unchanged; `results/` is untouched. Trial records and the annotation file remain uncommitted staging artifacts in `experiments/_incoming/` pending separate instruction.

## Change log (append-only)

```text
v1  2026-07-03  Phase 1 conclusion: 12 trials (GPT-5.5 Thinking), all six cells PASS at n=2
                under owner-confirmed B3/B4/B5; F and C equal on threshold dims, diverging
                only on diagnostic B7-manual/B8 (C-form source absence). Candidate validation
                only. Phase 2 deferred. results/ not promoted; records uncommitted.
```

End of file.
