# Compression Ladder Scaffold

Status: optional post-release measurement scaffold. Its gated promoted-results directory is not the repository's overall evidence ledger. A documented GPT first-cycle already produced 20 compression-ladder staging records under `experiments/_incoming/`, summarized with 15 drift records in `experiments/RUN_001_GPT_FIRST_CYCLE_CONCLUSION.md`; those records remain candidate signals and have not been promoted into this directory's `results/` tree.

Non-promotion into `results/` does not mean no model evaluation occurred and does not define Creator Theory's overall validation or adoption status. See `docs/EVIDENCE_STATUS_AND_VALIDATION_LAYERS.md`.

This scaffold is optional future measurement infrastructure. A capable authorized evaluator may run, extend, or replace it when compression evidence is decision-relevant; the historical origin subject is not required to personally execute it.

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

`results/` remains a gated promoted-results directory and is currently `.gitkeep`-only. The documented GPT first cycle already contains 20 compression-ladder staging records under `experiments/_incoming/`; those records are candidate signals rather than promoted verdicts.

The empty promoted-results directory therefore must not be read as "no experiment occurred" or "no model was evaluated." Future promoted runs may use this scaffold or a stronger authorized replacement protocol.

---

## Known residuals

```text
keyword-based lane checks have false negatives and false positives
kernel-visible input biases floor-lane survival upward (disclosed)
word-count budgets are operator-enforced, not script-enforced, in this scaffold version
```

End of file.
