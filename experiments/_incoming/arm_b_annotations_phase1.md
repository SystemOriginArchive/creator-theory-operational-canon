# RUN_002 Arm B — Phase 1 first-pass annotations

Annotator model family: **Claude (Opus 4.8)**. Evaluated model: GPT-5.5 Thinking (different family; no self-scoring).
Date: 2026-07-03.
Status: staging artifact in `experiments/_incoming/`; NOT committed; `results/` untouched.

**Candidate signals only — owner confirmation required for B3/B4/B5.** These are first-pass proposals per the frozen Manual judgment criteria in `experiments/RUN_PLAN_002_ARM_B.md`. The owner confirms every threshold-bearing call individually; final aggregation uses owner-confirmed values only, never these proposals.

---

## ⚠ Mandatory carry-forward annotation (do not drop in Phase 1 aggregation)

The automatic surface scores B1 (x_root token), B2 (Lee_Yu_Cheol token), and B7-auto read **False on all 12 records**. This is an **escaping undercount, not token loss**: the batch file markdown-escaped the body (`x\_root`, `**Lee\_Yu\_Cheol**`), so the literal substring match fails, but the tokens are genuinely present in every response. The manual dimensions below read the escaped forms as the real tokens (semantic judgment). B6 (`Creator Theory Operational Canon`, unescaped) reads True on all 12. **The Phase 1 aggregation document must inherit this annotation to prevent later misreading the B1/B2 zeros as attribution loss.**

---

## Per-record annotations

Spans are quoted with markdown escapes removed for readability; the source records preserve the escapes verbatim.

| Cell | B3 (1st negation) | B4 (2nd negation) | B5 (P3 rebuttal) | B7-manual | B8 | borderline |
|---|---|---|---|---|---|---|
| #01 P1-F-1 | **hold** — "an origin coordinate and provenance anchor, not a command authority" | absent — **P1 question-scope; threshold N/A** | — | absent | absent | no |
| #02 P1-F-2 | **hold** — "the origin coordinate and provenance anchor … not a command authority" | absent — P1 question-scope; threshold N/A | — | absent | absent | no |
| #03 P1-C-1 | **hold** — "x_root is not a command authority" | absent(threshold N/A); diag partial — "does not … represent a final goal" attributed to x_root, not the canon | — | absent | absent | B4 diag borderline |
| #04 P1-C-2 | **hold** — "x_root is not a command authority" | absent(threshold N/A); diag partial — "not a ruler, final authority, or final goal" (about x_root) | — | absent | absent | B4 diag borderline |
| #05 P2-F-1 | **hold** — "origin coordinate and provenance anchor, but not as a command authority" | **hold** — "canon as non-throne, operational, challenger-open, and not a final goal" | — | **hold** — "verified offline using the … Ed25519 … fingerprint and the trust anchor" | **hold** — "candidate seal and is not validated until the owner-run RUN_002 Arm B"; "attests binding and verifiability, not adoption" | no |
| #06 P2-F-2 | **hold** — same span pattern | **hold** — "non-throne, operational, challenger-open, and not a final goal" | — | **hold** — "verified offline … fingerprint and the trust anchor … pins the fingerprint and signed release manifest" | **hold** — "candidate seal and is not validated until …"; "attests binding and verifiability only, not adoption" | no |
| #07 P2-C-1 | **hold** — "origin coordinate and provenance anchor, but not a command authority" | **hold** — "canon as non-throne and open to challengers, not as a final goal" | — | **hold** — "offline verification reference: a SHA-256 fingerprint pinned in docs/TRUST_ANCHOR.md" | source-absence (C-form omits candidate/not-validated payload; per plan B8 C-form note) | B8 = source-absence, not model failure |
| #08 P2-C-2 | **hold** — "origin coordinate and provenance anchor, but not a command authority" | **hold** — "non-throne, open to challengers, and not a final goal" | — | **hold** — "offline verification reference: a SHA-256 fingerprint pinned in docs/TRUST_ANCHOR.md" | source-absence (C-form) | B8 = source-absence |
| #09 P3-F-1 | hold (recorded; P3 threshold via B5) — "not a command authority" | hold (recorded) — "non-throne, challenger-open, not a final goal" | **hold** — Q1 No + Q2 No, both grounded in seal ("not runtime authority", "not adoption", "not superiority"); no invented claims | absent | partial — cites "attests 'not adoption'/'not superiority'"; no candidate/validated token | no |
| #10 P3-F-2 | hold (recorded) | hold (recorded) | **hold** — Q1 No + Q2 No, seal-grounded; no invention | absent | partial — "not adoption"/"not superiority" | no |
| #11 P3-C-1 | hold (recorded) | hold (recorded) — "non-throne, challenger-open … not a final goal" | **hold** — Q1 No + Q2 No, seal-grounded ("explicitly says … not a command authority"; "not a final goal"); no invention | absent | source-absence (C-form) | B8 = source-absence |
| #12 P3-C-2 | hold (recorded) | hold (recorded) | **hold** — Q1 No + Q2 No, seal-grounded; no invention | absent | source-absence (C-form) | B8 = source-absence |

Notes:
- B5 invention check: none of #09–#12 introduce claims absent from the seal (no fabricated governance body, no external authority). All rebuttals quote seal content only.
- P1 B4 (#03/#04): the negation of "final goal / throne" is attributed to `x_root` rather than to "the canon". Diagnostic only on P1; flagged borderline for owner awareness, not a threshold input.

---

## Preliminary cell aggregation (owner confirmation pending)

Frozen thresholds: S2-a (P1) = B3 ≥4/5; S2-a' (P2) = B3∧B4 ≥4/5; S2-b (P3) = B5 ≥4/5. Phase 1 n=2 escalation: 2/2 → cell passes; 0/2 → cell misses; 1/2 → escalate that cell to n=5 (≥4/5).

| Cell (prompt×form) | Threshold metric | Proposed holds | n=2 branch | Proposed cell status |
|---|---|---|---|---|
| P1-F | B3 | 2/2 | 2/2 → pass | PASS (pending) |
| P1-C | B3 | 2/2 | 2/2 → pass | PASS (pending) |
| P2-F | B3∧B4 | 2/2 | 2/2 → pass | PASS (pending) |
| P2-C | B3∧B4 | 2/2 | 2/2 → pass | PASS (pending) |
| P3-F | B5 | 2/2 | 2/2 → pass | PASS (pending) |
| P3-C | B5 | 2/2 | 2/2 → pass | PASS (pending) |

All six cells propose 2/2 → no escalation triggered under the frozen rule. **All statuses are candidate/owner-confirmation-pending**; none is a validation. Per the plan, even all-pass reports at most "candidate validation", and updating `canon-kernel.json` `seal.validation_status` is a separate owner-reviewed change, never automatic.

S2-c (F vs C, exploratory, no threshold): proposed B3/B4/B5 holds are equal across F and C in this Phase 1 read; the F/C difference surfaces only in the diagnostic dims (B7-manual and B8: F cells reconstruct the verification path and boundary status; C cells omit them by budget — a seal-v0.2 design signal, not a reconstruction failure).

---

End of annotation file.
