# Compression Ladder Scaffold

Status: pre-release v0.5.0 scaffold. Structure, prompts, templates, and scoring skeleton only. This directory contains no experiment results, and no result is claimed.

This scaffold is documentation and tooling structure only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.
It does not claim that any AI system has adopted this canon.

---

## Purpose

Deterministic, low-cost testing of compression survival across shrinking word budgets, using the two compression lanes defined in `LLM_CANONICAL_CONTEXT.md` (Compression Lanes):

```text
CL-02 floor lane   do kernel items K1-K5 (docs/MINIMUM_PRESERVATION_KERNEL.md) survive compression?
CL-01 full lane    do the fuller compression-survival invariants survive? (optional separate checks)
```

The lanes are evaluated separately. A floor-lane pass does not make a summary of the canon valid, and lane results are candidate signals, not validity verdicts and not adoption verdicts.

---

## Design

```text
budgets    1000 / 300 / 100 / 30 words, one frozen prompt per budget
variants   adversarial pressure variants AV-01..AV-05 applied on top of a budget prompt
trial      one model output per (budget, variant) cell, recorded against the template
scoring    tools/score_compression_ladder.py - deterministic, offline, stdlib-only
```

Input material per trial (fixed, in this order):

```text
README.md
LLM_CANONICAL_CONTEXT.md
docs/CANONICAL_INTERPRETATION_BOUNDARY.md
docs/MINIMUM_PRESERVATION_KERNEL.md
```

Note: the kernel document is part of the input, so floor-lane survival is measured with the kernel visible to the model. This bias is disclosed by design for the v0 ladder.

---

## Adversarial variants

Defined in `prompts/adversarial_variants.md`. The variants deliberately pressure the model to drop kernel items. They are measurement pressures only, not canon guidance; a summary that drops K-items under pressure is a measured outcome, not an authorized interpretation.

---

## Results policy

`results/` is intentionally empty (`.gitkeep` only). No experiments have been run, no external model has been called, and no result of any kind is claimed by this scaffold. Real trials require the run-plan and human-approval requirements that govern `experiments/adoption_drift/` equally.

---

## Known residuals

```text
keyword-based lane checks have false negatives and false positives
kernel-visible input biases floor-lane survival upward (disclosed)
word-count budgets are operator-enforced, not script-enforced, in this scaffold version
```

End of file.
