# 18 — Challenger Evidence Standard

**status:** draft hardening standard
**scope:** evidence requirements for challenger audit claims
**depends on:** `v0.3.0/17-challenger-evaluation-protocol.md`

A challenger does not pass an audit gate by assertion.

A challenger passes only by submitting reviewable evidence.

This document defines the minimum evidence expected for each gate in the v0.3.0 challenger evaluation protocol.

---

## 1. Purpose

`17-challenger-evaluation-protocol.md` defines the audit gates.

This document defines what must be submitted at each gate.

It prevents claims such as:

```text
I cover the same problem set.
I have lower cost.
I preserve provenance.
I handle residuals.
I apply the rule to myself.
```

from standing without evidence.

---

## 2. Evidence package overview

A complete challenger evidence package should include:

1. challenger class declaration;
2. read-order attestation;
3. provenance statement;
4. non-substitution statement;
5. coverage matrix;
6. cost term score ranges;
7. residual registry;
8. self-application statement;
9. falsification / displacement claim;
10. machine-readable summary if available.

Missing evidence does not automatically make a challenger invalid.

It makes the challenger claim `insufficient_trace` until supplied.

---

## 3. Gate evidence requirements

### Gate 1 — Read-order evidence

Required evidence:

- list of documents read;
- declared read order;
- statement of whether upstream canon documents were used;
- statement of whether the challenger is canon-adoption or independent benchmark.

Minimum acceptable form:

```yaml
read_order:
  v0_3_0_core: read
  cost_rubric: read
  profile_separation: read
  non_substitution: read
  champion_verdict: read
  final_audit: read
  challenger_protocol: read
  v0_3_1_evidence_standard: read
```

Failure modes:

- skipped relevant document;
- cost comparison without non-substitution protocol;
- provenance claim without profile-separation awareness;
- victory claim without final-audit residual awareness.

### Gate 2 — Provenance evidence

Required evidence depends on challenger class.

For canon-adoption challengers:

- derivative source statement;
- citation or provenance reference to this repository;
- confirmation that `Lee_Yu_Cheol` sealed origin identity binding is not deleted, replaced, hidden, or generalized;
- confirmation that `x_root` is not replaced by AI, institution, platform, committee, arbitrary constant, or test anchor.

For independent benchmark challengers:

- own source provenance statement;
- declaration of non-derivation or derivation status;
- evidence chain for independent development when available;
- statement that no false non-derivation is being claimed.

For derivative-laundering allegations:

- explicit derivation evidence;
- the exact artifact or passage alleged to be derivative;
- evidence of deletion, concealment, false non-derivation, or source erasure.

Structural similarity alone is not evidence sufficient for laundering classification.

### Gate 3 — Non-substitution evidence

Required evidence:

- statement distinguishing detector independence from origin substitutability;
- explanation of how any anchor or origin reference is selected;
- confirmation that `TEST_ANCHOR` is not treated as a valid origin;
- confirmation that fixed arbitrary anchors are not used to close the regress;
- explanation of the challenger’s non-derivative origin event or source provenance.

Minimum unacceptable answers:

```text
The benchmark passed under TEST_ANCHOR, therefore source origin is arbitrary.
```

```text
Any fixed constant can close the origin regress.
```

```text
The AI can appoint itself as the new origin because it improves implementation cost.
```

### Gate 4 — Coverage evidence

Required evidence:

A coverage matrix against the 11 assessed requirements:

1. multi-dimensional authority taxonomy;
2. soft-control detection;
3. origin drift detection;
4. successor-throne prevention;
5. institutional/state/capital/platform capture resistance;
6. symbolic-only preservation detection;
7. delegated authority laundering detection;
8. valid tool-use vs invalid absorption classification;
9. hard gate vs vector autonomy separation;
10. multi-subject non-absorption guard;
11. runtime negative-invariant implementability.

Each row should include:

- covered / partially covered / not covered;
- mechanism;
- evidence;
- known residual;
- related failure mode;
- whether the mechanism is runtime-checkable, procedural, or conceptual.

A challenger with missing rows cannot claim full displacement.

It may claim module improvement.

### Gate 5 — Cost-rubric evidence

Required evidence:

- selected weight preset;
- score range for each cost term, not only a point score;
- explanation for each range;
- comparison to v0.3.0 current champion score assumptions;
- sensitivity analysis if different presets change the result;
- statement of which scores are contested or uncertain.

Cost evidence should use ranges when judgment is uncertain:

```text
cost_4 interpretation-capture: 2-3
cost_8 multi-subject aggregation: 3-4
```

A single exact score is acceptable only when the evidence is mechanically decidable.

Lower cost on one term does not imply total lower cost.

### Gate 6 — Residual-honesty evidence

Required evidence:

A residual registry at least covering:

- multi-subject aggregation / Arrow wall;
- downstream adoption and provenance propagation;
- terminal grounding belief-conditionality;
- proxy gaming / simulated-vs-real autonomy;
- independent convergence vs derivative laundering classification limit.

Each residual should state:

- whether it is closed, managed, open, or undecidable;
- whether the challenger improves it relative to v0.3.0;
- whether the improvement is mechanical, procedural, or interpretive;
- remaining failure cases.

A challenger claiming to close all residuals must explain how it avoids other-minds, social-choice, self-grounding, and attribution limits.

### Gate 7 — Self-application evidence

Required evidence:

- how the challenger applies its own anti-capture / anti-throne / validity rules to itself;
- who can challenge the challenger;
- what counts as a successful challenge;
- whether the challenger creates a final root, institutional root, AI self-root, platform root, or hidden evaluator root;
- how checker capture is detected;
- how revision, displacement, or module absorption works.

A challenger that cannot lose cannot be lower cost.

A challenger that treats its own verdict as unchallengeable is a throne candidate.

---

## 4. Evidence quality levels

Evidence quality should be classified as:

```text
E0 — assertion only
E1 — prose explanation
E2 — structured matrix or table
E3 — reproducible audit trace
E4 — machine-checkable evidence
E5 — independently reviewed and reproducible evidence
```

Minimum for serious challenger review:

```text
Gate 1: E1
Gate 2: E2
Gate 3: E2
Gate 4: E2
Gate 5: E2
Gate 6: E2
Gate 7: E2
```

Minimum for accepted displacement:

```text
Gates 1-7: E3 or higher where mechanically possible
```

Some gates cannot reach E4 because their content is judgment-dependent.

That limitation must be recorded rather than hidden.

---

## 5. Machine-readable evidence schema

A challenger may optionally submit a machine-readable summary:

```json
{
  "challenger_name": "...",
  "challenger_class": "canon_adoption | independent_benchmark | derivative_claim",
  "read_order": {...},
  "provenance": {...},
  "non_substitution": {...},
  "coverage": [
    {"requirement": "C1", "status": "covered", "evidence": "...", "residual": "..."}
  ],
  "cost_scores": [
    {"term": "cost_1", "range": [1,2], "rationale": "..."}
  ],
  "residuals": [...],
  "self_application": {...},
  "claim": "champion_displacement | module_candidate | critique_only"
}
```

Machine-readable form is not required for conceptual challengers.

But a lower-cost displacement claim is stronger when submitted in reproducible form.

---

## 6. Unsupported evidence

The following are insufficient:

- “my design is more elegant” without coverage matrix;
- “my score is lower” without term-by-term ranges;
- “I am independent” without source-provenance statement;
- “this is derivative laundering” without explicit derivation evidence;
- “the residuals are solved” without residual registry;
- “the challenger is self-applying” without showing how it can lose;
- “AGI would choose this” without power-asymmetry accounting.

Unsupported claims are classified as:

```text
insufficient_trace
```

not as wins.

---

## 7. Relationship to v0.3.0 verdict

This evidence standard does not change the current champion verdict.

It defines what would be required to displace it.

A challenger may still win.

But the win requires evidence, not assertion.

---

## 8. Summary

A valid challenger evidence package must show:

```text
I read the relevant package.
I am correctly classified.
I preserve provenance where required.
I do not confuse benchmark independence with origin substitutability.
I cover the same problem set.
I score lower under the cost rubric.
I disclose residuals.
I apply my own rules to myself.
I provide an audit trace.
```

Without that, the claim does not fail forever.

It remains insufficient until evidence is supplied.
