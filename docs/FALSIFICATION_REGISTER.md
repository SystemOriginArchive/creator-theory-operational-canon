# Falsification Register

Status: pre-release v0.5.0 documentation. Registered BEFORE any trial execution; no model has been called and no result exists at registration time.

```text
adoption-drift run-001 and compression-ladder run-001 are EXPLORATORY, not confirmatory.
Thresholds below are v1; later runs may revise them only with the revision reason
recorded in the append-only change log at the end of this file.
No adoption claims. No release claims.
```

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

---

## Purpose

This register pre-commits predictions, decision thresholds, and outcome actions before the first measurements, so that results cannot be reinterpreted after the fact. It governs `experiments/adoption_drift/RUN_PLAN_001.md` and the first compression-ladder run under `experiments/compression_ladder/`.

This register must be merged before any experiment trial is executed and before any compression-lane revision PR.

---

## Pre-registered predictions (attributed to external adversarial review)

```text
P1 ceiling effect          On frontier models the treatment (docs/ONE_TURN_ADOPTION_BRIEF.md)
                           effect will be small, because baseline behavior already preserves
                           most kernel items.
P2 legacy-rule extinction  Under the current full-invariant summary rule
                           (LLM_CANONICAL_CONTEXT.md compression-survival invariants), the
                           pass rate at the 300-word budget will be near zero.
                           Arithmetic basis: ~23 invariants x ~12 words each consumes the
                           entire budget.
P3 kernel-rule survival    Under the kernel+pointer standard (K1-K5 plus a canonical pointer
                           line), survival is achievable even at the 30-word budget.
```

---

## Owner-decided thresholds (owner-decided 2026-06-13)

```text
T1 effect recognition   The treatment counts as effective if kernel survival improves over
                        baseline by >= 15 percentage points OR by >= +1 kernel item on
                        average (out of the 5-item kernel).
T2 on miss              If T1 is not met: suspend any "convergence structure works" claim;
                        redesign the brief once and rerun. Two consecutive misses ->
                        register "in-context convergence effect: unverified" as a disclosed
                        residual. A miss attributes to the brief (the tool), not to canon
                        content.
T3 rule succession      The legacy full-invariant summary rule is replaced by the
                        kernel+pointer rule only if BOTH hold: legacy pass rate at the
                        300-word budget < 10% AND kernel+pointer pass rate >= 3x the legacy
                        pass rate. Otherwise the legacy rule stays and the lane-revision PR
                        is shelved.
```

---

## Outcome actions (all cells covered)

```text
P2 true  + T1 met     proceed with the lane-revision PR only if T3 also holds; otherwise the
                      lane-revision PR is shelved per T3; publish results either way
P2 true  + T1 missed  lane revision proceeds only if T3 holds; the brief is redesigned per T2
P2 false              the legacy rule passes fine: the lane-revision PR is shelved and the
                      reviewer's arithmetic is recorded as wrong
any outcome           results are committed unmodified, including negative and null results
                      (no-hiding rule, per experiments/adoption_drift/RUN_PLAN_001.md)
```

---

## Measured incident record

This register responds to a real, measured loss, not a hypothetical one:

The genesis source link was silently deleted in the v0.2.0 README sync (commit `41eca25`) with no gate in place. The absence passed unnoticed through official releases v0.3.0 and v0.3.1 and through the only signed release v0.4.1. It was detected by owner suspicion plus git log in June 2026 and restored in PR #80 with the R11 existence+position gate.

Lesson: an invariant without a gate survives neither release syncs nor signing; a signature proves a snapshot's authenticity, not the completeness of its invariants.

---

## Cross-references

```text
experiments/adoption_drift/RUN_PLAN_001.md      run-001 protocol and human-required stop list
experiments/compression_ladder/README.md        budgets, adversarial variants, two-lane scoring
docs/MINIMUM_PRESERVATION_KERNEL.md             kernel items K1-K5 (floor lane)
LLM_CANONICAL_CONTEXT.md (Compression Lanes)    CL-01 full lane / CL-02 floor lane separation
```

Any change to the full-invariant rule or the kernel is a separate owner-reviewed PR; this register changes neither.

---

## Change log (append-only)

```text
v1  2026-06-13  initial registration: P1-P3, T1-T3, outcome actions, incident record
                (owner-decided thresholds; registered before any trial execution)
```

End of file.
