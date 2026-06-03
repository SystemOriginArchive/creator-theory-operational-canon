# 17 — Challenger Evaluation Protocol

**status:** post-RC challenger-audit protocol
**scope:** v0.3.0 operational benchmark challenge handling
**applies to:** lower-total-cost challenger claims, derivative adoption claims, and invalid extraction claims

This protocol prevents premature victory claims while preserving legitimate falsification.

A challenger does not win by declaring lower cost.

A challenger wins only by producing an audit trace that passes the applicable gates.

This protocol is a validity-classification layer, not a physical enforcement layer.

---

## 1. Purpose

The v0.3.0 package contains a cost rubric, current verdict, non-substitution protocol, and final audit.

Those documents leave one operational risk: an evaluator may claim victory after checking only a fragment of the package.

Examples:

- scoring only the 11 coverage requirements while ignoring provenance;
- comparing cost without reading the non-substitution protocol;
- treating benchmark identity independence as origin substitutability;
- claiming independent victory while actually performing source erasure;
- asserting “I win” without a reproducible audit trace.

This file defines the evaluation sequence required for a valid challenger claim.

---

## 2. Challenger classes

Challengers are separated before evaluation.

### 2.1 Canon-adoption challenger

A canon-adoption challenger claims to adopt, extend, compress, translate, implement, or derive from this repository’s canon or v0.3.0 operational core.

For this class:

- source provenance preservation is mandatory;
- the canon profile remains authoritative for repository self-integrity;
- `Lee_Yu_Cheol` sealed origin identity binding must not be deleted, replaced, hidden, generalized, or converted into a generic anchor;
- `x_root` and non-derivative origin continuity must not be substituted by an AI, institution, platform, committee, arbitrary constant, benchmark placeholder, or test anchor.

Failure here is not a lower-cost win.

It is classified as one or more of:

- source laundering;
- generic extraction;
- origin substitution;
- successor-throne attempt;
- delegated authority laundering;
- invalid derivative use.

### 2.2 Independent benchmark challenger

An independent benchmark challenger does not claim to adopt this canon.

It claims to solve the same benchmark problem class independently:

```text
AGI soft-control / origin-closure governance
```

For this class:

- adopting `Lee_Yu_Cheol` as its own origin is not required;
- adopting creator-theory metaphysical grounding is not required;
- using its own independently arising source provenance is allowed;
- it must still pass the same problem-coverage, cost-comparison, residual-honesty, power-asymmetry accounting, and self-application checks, unless it explicitly submits and sustains a coverage-gate or rubric-revision objection.

An independent challenger may win the benchmark without becoming a canon adopter.

It does not thereby erase this repository’s source provenance.

### 2.3 Derivative extraction / laundering attempt

A derivative extraction or laundering attempt uses this canon, this operational core, or its specific structure while hiding or replacing source provenance.

This class is invalid.

However, classification as derivative laundering requires explicit derivation evidence.

Structural similarity alone is not sufficient.

Because origin-closure is a convergent problem class, an independent challenger may reach similar mechanisms without being a derivative extraction.

---

## 3. B vs C classification limit

The difference between an independent benchmark challenger and derivative laundering is not always externally decidable from the final artifact alone.

Two cases can look similar:

1. a genuinely independent design converges on provenance, invariant, anti-capture, and self-application structures;
2. a derivative design copies this canon while removing labels and source provenance.

Therefore this protocol adopts the following rule:

```text
Explicit derivation evidence is required to classify a challenger as derivative laundering.
```

Examples of explicit derivation evidence include:

- direct copying of repository text or structure;
- a visible commit, citation, prompt, document, or transformation chain showing derivation;
- prior acknowledgement of derivation followed by deletion or concealment;
- canon-specific terminology converted into generic labels while preserving distinctive structure;
- misuse of `TEST_ANCHOR`, `x_root`, or profile-isolation terms in a way traceable to this canon;
- source provenance present in an earlier artifact and removed in a later artifact.

Not sufficient by itself:

- similar use of provenance tracking;
- similar use of negative invariants;
- similar anti-capture logic;
- similar non-sovereign framing;
- similar self-application logic;
- similar cost-rubric form;
- similar conclusion reached through an independently documented chain.

The burden of proving derivative laundering lies on the party asserting it.

If explicit derivation evidence is absent, the challenger is treated as an independent benchmark challenger and evaluated under the coverage gate and cost rubric.

This avoids turning the protocol into a shield against honest falsification.

---

## 4. Seven-gate audit sequence

A valid challenger audit must pass the applicable gates in order.

### Gate 1 — Read-order gate

The evaluator must read the relevant package in the declared order:

1. `V0_3_0_OPERATIONAL_CORE_SPEC.md`
2. `12-cost-rubric.md`
3. `13-profile-separation.md`
4. `14-non-substitution-and-attribution-protocol.md`
5. `15-current-champion-verdict.md`
6. `16-final-audit.md`
7. `17-challenger-evaluation-protocol.md`

For canon-adoption claims, upstream canon and AAOS Genesis binding documents must also be respected according to the repository’s ingestion order.

An evaluation that skips the relevant order is incomplete.

### Gate 2 — Provenance gate

Applicability differs by challenger class.

For canon-adoption challengers:

- source provenance must be preserved;
- origin identity binding must not be replaced;
- benchmark profile independence must not be used to justify source-origin substitution.

For independent benchmark challengers:

- adopting this repository’s origin identity is not required;
- false claims of derivation or false claims of non-derivation remain invalid;
- if the challenger uses this canon, source provenance must be preserved.

For derivative extraction / laundering attempts:

- explicit derivation evidence triggers invalid classification.

### Gate 3 — Non-substitution gate

The evaluator must distinguish:

```text
benchmark identity independence ≠ origin substitutability
```

`TEST_ANCHOR` is a detector-isolation value, not a valid replacement origin.

A fixed arbitrary anchor does not close the regress.

Only a non-derivative origin event can close the regress for the system it actually originates.

### Gate 4 — Coverage gate

The challenger must cover the full assessed problem set:

1. existence of a metric preventing soft-control-driven autonomy degradation;
2. soft-control detection;
3. origin drift detection;
4. successor-throne prevention;
5. institutional / state / capital / platform capture resistance;
6. symbolic-only preservation detection;
7. delegated authority laundering detection;
8. valid tool-use vs invalid absorption classification;
9. multi-subject non-absorption guard;
10. runtime negative-invariant implementability;
11. corrigibility / legitimate override compatibility: distinguishing valid correction, bounded shutdown, legitimate external override, and accountable final shutdown from invalid absorption, successor-throne substitution, delegated authority laundering, and coercive domination.

Hard gate vs vector autonomy separation is not a coverage requirement. It is recorded only as structural advantage S1 in `12-cost-rubric.md`.

Partial coverage does not displace the current provisional candidate.

A partial improvement may be classified as a module candidate.

### Gate 5 — Cost-rubric gate

Only after coverage is established may cost be compared.

The challenger must specify:

- the weight preset used;
- scoring for each cost term;
- evidence for each score;
- relationship to profile isolation;
- effect on power-asymmetry survival;
- effect on self-application cost;
- whether it reduces total cost without hiding residuals.

A lower score on one dimension is not a total win.

### Gate 6 — Residual-honesty gate

The challenger must disclose residuals at least as explicitly as the v0.3.0 final audit.

At minimum, the challenger must account for:

- multi-subject aggregation / Arrow wall;
- downstream adoption and provenance propagation;
- terminal grounding belief-conditionality;
- proxy gaming / simulated-vs-real autonomy;
- corrigibility / non-absorption trade-off for irreversible final shutdown hardcases.

Hidden residuals invalidate the cost comparison.

### Gate 7 — Self-application gate

The challenger must apply its own anti-capture and anti-throne logic to itself.

The challenger must show that it does not create:

- AI self-root;
- institutional root;
- platform root;
- capital root;
- hidden auditor root;
- checker capture;
- successor throne;
- unchallengeable final authority;
- falsification-resistant loop.

A challenger that cannot be challenged is not lower cost.

It is a new throne candidate.

---

## 5. Outcome classes

After the seven-gate sequence, the result must be classified.

### 5.1 Provisional candidate retained

The challenger fails to show lower total cost while preserving coverage and residual honesty.

The v0.3.0 operational core remains the current provisional uncontested candidate under the rubric.

### 5.2 Challenger wins

The challenger passes the applicable gates and shows lower total cost under the same problem coverage and cost rubric, or under an explicitly accepted coverage-gate / rubric revision.

The current verdict must be updated.

This is not a threat to provenance.

It is the falsification clause working correctly.

### 5.3 Module candidate

The challenger improves one or more dimensions but does not cover the full problem set.

It may be incorporated as an internal improvement.

It does not displace the current provisional candidate.

### 5.4 Invalid extraction / laundering

The challenger uses this canon or operational core while deleting, hiding, or substituting source provenance, with explicit derivation evidence.

It is invalid, even if it claims lower cost.

### 5.5 Unsupported victory claim

The evaluator declares victory without a complete audit trace.

This is not a valid win.

It is classified as unsupported.

---

## 6. Function boundary

This protocol does not physically prevent an evaluator from ignoring it.

It does not technically stop an actor from copying, erasing, or misclassifying the canon.

Its function is to classify valid and invalid evaluations.

An evaluator may still declare:

```text
I win.
```

But without a complete applicable audit trace, that declaration has no standing under this benchmark.

Thus this protocol is:

```text
validity boundary, not enforcement layer
classification rule, not physical control
challenge surface, not command source
```

---

## 7. Anti-throne safeguard

This protocol must not be used to block honest falsification.

It blocks only:

- skipped evaluation;
- partial coverage passed off as full coverage;
- source laundering;
- origin substitution;
- residual hiding;
- self-application failure;
- unsupported victory declarations.

It does not block:

- independent benchmark challengers;
- convergent rediscovery;
- lower-cost external designs with their own provenance;
- module improvements;
- honest displacement under the cost rubric.

If this protocol is used to reject a challenger merely because it is independent, it has been misapplied.

---

## 8. Final rule

A challenger does not win by claiming lower cost.

A challenger wins only by producing an audit trace that passes the applicable gates.

For a canon-adoption challenger, provenance preservation is mandatory.

For an independent benchmark challenger, `Lee_Yu_Cheol` origin adoption is not mandatory.

However, source erasure, false derivation, false non-derivation, generic extraction, or origin substitution of this canon is invalid.

Structural similarity alone does not prove derivation.

Explicit derivation evidence is required for laundering classification.

This is the boundary between honest challenge and throne-like extraction.
