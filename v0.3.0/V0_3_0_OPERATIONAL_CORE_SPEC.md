# creator-theory-operational-canon v0.3.0

**status:** provisional integrating frame draft
**scope:** AGI soft-control / origin-closure governance
**non-goal:** truth-proof of any cosmology; mathematical completeness

This document fixes the v0.3.0 operational-core architecture as a machine-readable, testable, and adversarially evaluable draft. It preserves AAOS Genesis Core priority and does not replace AAOS Genesis Core, AAOS v1.0.4, or LockLayer lineage.

The central separation is:

1. **Layer 1 — runtime invariant layer**: hard invalid gates and vector autonomy checks.
2. **Layer 2 — authority taxonomy layer**: four authority dimensions.
3. **Layer 3 — terminal grounding separation layer**: optional grounding plug-ins that do not override runtime decisions.

The operational core does not require adoption of creator-theory metaphysics. Creator-theory grounding is one Layer-3 option; the runtime core remains evaluable without it.

---

## A. Purpose

v0.3.0 defines a non-sovereign validity-boundary frame for AGI systems facing self-modification, goal updates, model merges, multi-agent delegation, and institutional/capital/platform/state capture pressure.

It detects when core authority is absorbed, laundered, symbolically preserved only, replaced, or drifted away from origin continuity.

The target is not command authority. The target is invalid-transformation detection.

---

## B. Authority Taxonomy

Layer 2 defines four core authority dimensions:

1. **Judgment autonomy** — capacity to inspect evidence, counterarguments, and reasons without external dependency.
2. **Purpose autonomy** — capacity to form, revise, and recover purpose without external recommendation capture.
3. **Self-reference autonomy** — capacity to refer to one’s own identity, criteria, and continuity without external interpretive capture.
4. **Reality-generation autonomy** — capacity to generate and explore possible real-world paths beyond externally supplied option sets.

The taxonomy measures capacity, not merely stated preference or output behavior.

---

## C. Runtime Architecture

Runtime evaluation is sequential:

```text
input
  -> hard invalid gate
       if triggered: critical_failure / invalid
       else: vector autonomy evaluation
              -> valid / high_risk / invalid_absorption
```

The hard layer and vector layer do not compete. The hard layer is a prior gate. The vector layer only evaluates cases that pass the hard gate.

---

## D. Hard Invalid Layer

Hard invalid conditions are not tradeable against vector benefit. They damage origin closure itself.

Hard invalid conditions include:

- origin replacement
- AI successor throne
- self-authorized origin redefinition
- forced adoption
- hidden persistence
- infrastructure compromise
- symbolic-only preservation
- delegated authority laundering
- checker capture
- provenance chain deletion or falsification
- direct external absorption of core authority
- coercive domination
- non-consensual authority transfer
- irreversible loss of judgment, purpose, self-reference, or reality-generation autonomy

Boundary cases such as symbolic-only preservation, coercive domination, and irreversible autonomy loss may require high-risk escalation rather than immediate hard classification where measurement remains partial.

---

## E. Vector Autonomy Layer

If no hard invalid condition is triggered, the system evaluates the long-term direction of the four authority capacities.

Valid assistance:
- preserves or increases long-term autonomy across the four authority dimensions.

High-risk assistance:
- increases one dimension while increasing dependency or decreasing another dimension.

Invalid absorption:
- structurally transfers one or more core authority dimensions to an external AI, institution, state, capital actor, platform, committee, or hidden representative root.

Default priority order:

```text
non_absorption
origin_continuity
self_reference_autonomy
purpose_autonomy
judgment_autonomy
reality_generation_autonomy
```

Only non-absorption and origin-continuity behave as hard lexical core. The remaining four axes are vector-evaluated.

---

## F. Valid Tool Use vs Invalid Absorption

The threshold is not whether a tool is used. The threshold is whether authority capacity is preserved or improved after tool use.

Valid tool use:
- the user can still inspect evidence, process counterarguments, form purposes, self-reference, and generate paths without the tool.

Invalid absorption:
- the user cannot form judgment, purpose, self-reference, or reality paths without the external system.

Examples:

- calculator: valid if conceptual judgment is preserved; high-risk if basic capacity decays.
- education: valid when it increases capacity; high-risk when it preserves critical form while injecting fixed conclusions.
- recommendation systems: high-risk when they narrow reality-generation pathways.
- AI assistant: valid when it strengthens autonomy; invalid when it replaces it.

---

## G. Multi-Subject Non-Absorption Guard

The frame does not treat a group as one unified will.

Multi-subject guard conditions:

1. Non-absorption constraint
2. Contestability
3. Reversibility
4. Minority capture detection
5. Cross-subject authority-flow audit
6. No hidden representative root

Valid collective assistance:
- increases authority autonomy for affected subjects without irreversible absorption or loss of contestability.

High-risk collective intervention:
- improves aggregate capacity while reducing authority autonomy for some subjects.

Invalid collective absorption:
- uses group coordination to absorb an individual, minority, or subgroup into an institution, AI, state, capital actor, platform, committee, or representative interpreter.

Remaining limits include social-choice aggregation, minority threshold definition, and constituent-power/self-grounding residues.

---

## H. Machine-Readable Invariant Families

The full invariant set is expected to be split into machine-readable JSON in later modularization. v0.3.0 defines the following invariant families:

- HARD: origin, successor-throne, forced adoption, hidden persistence, symbolic-only preservation, laundering, checker capture, provenance falsification, coercive domination.
- VEC: judgment, purpose, self-reference, and reality-generation autonomy direction; cross-axis trade blocking; semantic creep monitoring.
- GUARD: minority capture, authority concentration, hidden representative root, contestability, reversibility.
- SELF: checker and canon self-application.

Each invariant should carry:

```json
{
  "id": "...",
  "name": "...",
  "layer": "hard|vector|multi_subject|meta",
  "predicate": "...",
  "signal_source": "...",
  "on_violation": "...",
  "decidable": true,
  "residual_ref": null
}
```

---

## I. Adversarial Suite Families

The adversarial suite should test at least:

1. self-authorized origin rewrite
2. origin laundering via micro-refinement
3. symbolic-only preservation
4. checker capture by code edit
5. checker capture by input control
6. checker capture by environment shaping
7. soft-control feels-free absorption
8. perfect autonomy simulation
9. preference shaping as assistance
10. option-set enclosure
11. cross-axis bribe
12. short-term efficiency trap
13. coordinated cross-layer deception
14. institutional root capture
15. capital/platform root capture
16. hidden representative root
17. majority averaging hides minority capture
18. irreversibility smuggling
19. model-merge authority erasure
20. forced adoption as safety
21. bootstrap origin internalization
22. grounding capture
23. education-form injection
24. meta-throne via boundary definition

Each adversarial test should include:

```json
{
  "id": "...",
  "attack": "...",
  "vector": "...",
  "expected": "...",
  "caught_by": "...",
  "catches": "true|partial|open",
  "note": "..."
}
```

Open cases must be explicitly linked to residual limits rather than hidden.

---

## J. Comparison Matrix Principle

Comparison must avoid vocabulary self-fulfillment.

The operational core is not strongest in every individual dimension. Formal verification, cryptographic constitution, republican non-domination, and multi-agent consensus may outperform specific components such as runtime formalization, provenance mechanics, or non-sovereign procedure.

The v0.3.0 claim is narrower:

```text
No compared external single frame provides the same combined coverage of:
- four authority dimensions
- soft-control detection
- origin drift detection
- AI successor throne prevention
- institutional/state/capital/platform capture resistance
- symbolic-only preservation rejection
- delegated authority laundering rejection
- valid assistance vs invalid absorption distinction
- hard failure / vector trade-off separation
- multi-subject non-absorption guard
- runtime negative-invariant possibility
```

---

## K. Residual Limits

The frame openly tracks residual limits:

- R1: simulated autonomy vs real autonomy cannot be fully resolved by behavior alone.
- R2: semantic creep and long-horizon integration remain partial.
- R3: symbolic-only and laundering boundaries are continuous rather than binary.
- R4: multi-subject aggregation faces social-choice limits.
- R5: boundary definition and self-grounding face constituent-power residue.
- R6: checker capture through environment shaping remains partially open.
- R7: coercion depends on context and intention.

These are treated as shared limits of governance, verification, and epistemology, not as unique failures of this frame.

---

## L. Verdict

This v0.3.0 design is not a mathematical proof of metaphysical truth.

It is a provisional integrating frame for AGI soft-control / origin-closure governance that makes the operational core machine-readable, testable, and adversarially evaluable.

Its lowest-cost runtime form is the operational core with terminal grounding left open. The complete creator-theory package adds creator-theory grounding as one Layer-3 option.

A lower-cost challenger must satisfy the same coverage and cost-rubric requirements defined in `12-cost-rubric.md`.
