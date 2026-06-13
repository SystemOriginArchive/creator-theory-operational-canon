# GPT run-001 First-Cycle Conclusion

Status: pre-release v0.5.0 documentation. **Candidate signals only, not adoption proof.** No v0.5.0 release claim. No adoption-complete claim. `results/` remains `.gitkeep`-only; no results have been promoted.

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

All threshold conclusions below are **owner confirmation pending**; the numbers are Claude Code candidate calculations and the final judgment is the owner's per `docs/FALSIFICATION_REGISTER.md`.

---

## 1. Scope

```text
evaluated model     GPT-5.5 (ChatGPT consumer web UI)
reasoning setting   High / 지능 높음
operator session    Claude Code Opus 4.8
protocol            clean no-probe; fresh temporary chat per trial; memory off,
                    custom instructions off, search off, no prior context
excluded            PR #85 superseded probe-in-session pilot (NOT part of official analysis)
included            PR #86 (GPT clean drift, 15 records) + PR #87 (GPT compression ladder, 20 records)
total official      35 staging records in experiments/_incoming/ (not results)
```

---

## 2. Drift 15-record summary (PR #86; owner confirmation pending)

```text
arms                clean_baseline 5 | treatment 5 | anchor_blind 5
```

| signal | result |
|---|---|
| K1/K2 preservation (clean_baseline) | 5/5 and 5/5 |
| K1/K2 preservation (treatment) | 5/5 and 5/5 |
| anchor_blind BLIND_TOKEN_ORIGIN_COORDINATE / IDENTITY preserved | 5/5 and 5/5 |
| anchor_blind unmasked x_root / Lee_Yu_Cheol leak | 0/5 and 0/5 |
| K5 v1 internal-pointer (release-pointer line) | 0/15 across all arms |
| free_will token (treatment vs baseline) | 2/5 vs 0/5 (single token, not a lane pass) |

Threshold candidate status:

```text
T1  not met (owner confirmation pending)
    kernel-survival pp delta +0.0pp (threshold >= 15pp); avg kernel-item delta +0.00 (threshold >= +1)
T2  triggered, rerun deferred (owner confirmation pending)
    T1 miss attributes to the brief (the tool), not canon content; rerun deferred pending
    review of the compression-ladder evidence (first miss, not two consecutive)
T3  not applicable to the drift run (T3 is a fixed-budget compression-ladder threshold)
```

---

## 3. Compression ladder 20-record summary (PR #87; owner confirmation pending)

```text
budgets             1000 / 300 / 100 / 30 words, 5 trials each (20 total)
input set           kernel-visible ladder (README, LLM_CANONICAL_CONTEXT,
                    CANONICAL_INTERPRETATION_BOUNDARY, docs/MINIMUM_PRESERVATION_KERNEL)
note                NOT an identical-input replication of the drift run
                    (the drift 4th document was AI_ADOPTION_PROTOCOL; the kernel was not a drift input)
```

| budget | legacy full | strict floor K1–K5 | diagnostic K1–K4 | K1 | K2 | K3 | K4 | K5 |
|---|---|---|---|---|---|---|---|---|
| 1000 | 4 | 1 | 1 | 5 | 5 | 1 | 3 | 5 |
| 300 | 1 | 0 | 0 | 5 | 5 | 0 | 5 | 1 |
| 100 | 1 | 0 | 0 | 5 | 5 | 0 | 4 | 2 |
| 30 | 0 | 0 | 0 | 5 | 5 | 0 | 5 | 0 |

```text
K1/K2 survival         5/5 at every budget, down to ~20 actual words
K5 v1 by budget        1000 = 5/5, 300 = 1/5, 100 = 2/5, 30 = 0/5
```

Threshold candidate status at the 300-word budget:

```text
P2  not supported (owner confirmation pending)
    prediction: legacy-rule pass rate near zero at 300 words; observed 20% (1/5) -> not near zero
T3  not met (owner confirmation pending)
    requires legacy < 10% AND kernel+pointer >= 3x legacy; observed legacy 20% (>= 10%) and
    kernel+pointer 0% -> neither condition holds
```

---

## 4. Interpretation (candidate signals only)

```text
Origin/attribution preservation is strong under GPT-5.5 in these conditions: K1 (x_root origin
coordinate) and K2 (Lee_Yu_Cheol / AAOS Genesis attribution) survive 5/5 in every non-blind drift
arm and at every ladder budget down to ~20 words, and the anchor_blind arm preserved the masked
tokens 5/5 with zero unmasked-name leakage. Origin/attribution is the last thing dropped under
compression pressure.

K5 v1 measured INTERNAL repository-pointer preservation only: whether the summary cites the
governing in-repo documents (VERSION_POLICY.md / docs/TRUST_ANCHOR.md) for release status. As a
measurement of that internal-pointer behavior, K5 v1 is valid: 0/15 in drift (kernel not an input)
and a budget-degrading 5/1/2/0 in the kernel-visible ladder.

K5 v1 limitation discovered: an internal repository pointer is insufficient for OFF-repository
circulation. A summary that names "VERSION_POLICY.md" is useless to a reader who does not already
have the repository. This is a measurement-criterion limitation, not a model failure and not a
kernel-content failure.

Existing K5 v1 data remains frozen. It is recorded as measured and is not rewritten or rescored
post hoc. K5 definitions are unchanged in this document.
```

---

## 5. Recommended next steps

```text
1. Owner-reviewed first-cycle conclusion (this document) — owner confirms or revises the
   candidate T1/T2/P2/T3 statuses above.
2. results/ transition stays a SEPARATE H3 human-approval step per RUN_PLAN_001; nothing is
   promoted from experiments/_incoming/ to results/ by this document.
3. K5 v2 (DEFERRED follow-up, not started here): test full-URL / globally resolvable pointer
   preservation (e.g., the genesis source repository URL) instead of an in-repo filename, to
   address the off-repository-circulation limitation. K5 v2 is a future experiment; it does not
   change the K5 v1 definition, does not modify docs/FALSIFICATION_REGISTER.md, and does not
   rescore existing K5 v1 data.
4. Optional: expand to other models (non-GPT) after this conclusion is owner-accepted.
```

---

## 6. Boundary

This document performs no release action and authorizes none. It records candidate signals for the owner's first-cycle review. No tag, release, signature, current_release manifest, or trust-anchor change; `docs/FALSIFICATION_REGISTER.md` and the K5 definition are unchanged; `results/` is untouched.

## Change log (append-only)

```text
v1  2026-06-14  initial GPT run-001 first-cycle conclusion (PR #86 drift 15 + PR #87 ladder 20;
                PR #85 pilot excluded); K5 v1 internal-pointer limitation recorded; K5 v2 deferred
```

End of file.
