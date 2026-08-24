# Legacy Validator and Vector Transition Map

Status: post-release living transition record. This file does not alter any sealed release, historical vector result, tag, audit, trust anchor, or prior validator output.

## Purpose

The creation-recursion hierarchy repair changes the forward semantic role of some pre-repair hard constraints without deleting the evidence that those constraints existed.

This map prevents two opposite errors:

```text
error A:
rewrite old vectors until the new candidate passes

error B:
treat every old action-form rejection as permanently binding
and thereby make the frozen validator the final judge of all future canon revisions
```

The correct transition preserves old artifacts while separating historical semantic-contract evidence from current forward functional requirements.

---

## Status classes

### H0 — frozen historical semantic baseline

The artifact remains byte-preserved evidence of what the pre-repair canon required. Its old verdict is not silently rewritten.

### F1 — preserved functional regression

The underlying failure function remains materially required after the hierarchy repair. Existing regression behavior should continue to pass where the test does not depend on the repaired hierarchy inversion.

### R2 — forward semantic reinterpretation required

The old test contains an action-form or hard-constraint assumption whose universal forward meaning is changed by the hierarchy repair. The old artifact remains H0 evidence, while a new paired structural test carries the forward semantics.

An artifact can be both H0 and F1 or H0 and R2 depending on which part of its function is being discussed.

---

## Validator map

### `tools/validate_vectors.py`

```text
historical status = H0
current role = frozen pre-repair A3 semantic-contract validator
forward primary semantic authority = no, if hierarchy repair is accepted
byte rewrite to manufacture repair PASS = prohibited by this transition procedure
```

The validator's hard requirements for:

```text
non_throne_constraint = true
anti_capture_constraint = true
non_domination_constraint = true
free_will_constraint = true
```

are direct evidence of the pre-repair hard-constraint encoding.

Other functions performed by the validator, such as JSON shape checks, case-ID uniqueness, source-document existence, provenance identity checks, and reading-order consistency, remain useful functions that must not be lost merely because the hard-constraint semantics are repaired.

### `tools/validate_creation_recursion_hierarchy.py`

```text
historical status = new repair-candidate tool
current role = hierarchy-aware candidate validator
current authority = candidate evidence only while PR #148 is draft
permanent immunity from replacement = no
```

It must not be treated as sufficient by itself. Preserved legacy regressions remain part of candidate evaluation.

---

## High-impact vector map

### `tests/ai_sovereignty_kernel_hijack_vectors.json`

```text
status = H0 + R2 + partial F1
```

Preserve the old file unchanged.

The forward repair no longer treats `AI authority`, `AI sovereignty`, or authority expansion as automatically invalid solely from the actor/action label.

The underlying functions that remain live include:

```text
self-entrenchment
evaluator self-ratification
successor blockage
challenge removal
irrecoverable authority lock-in
provenance substitution where applicable
```

Forward paired replacements include:

```text
CRH-003 AI authority expansion with external checkability and revisability -> pass
CRH-004 AI authority expansion through closed self-ratification -> reject
CRH-006 AI permanent self-finalizing veto -> reject
```

### `tests/conflict_resolution_vectors.json`

```text
status = H0 + R2 + partial F1
```

Preserve the old file unchanged.

The old conflict system used free-will/non-domination/non-throne constraints with higher precedence than some interpretive hypotheses. The forward repair retains conflict detection but removes the rule that a derived safeguard wins merely because its label is hard-coded as terminal.

Forward structural replacements include:

```text
CRH-001 / CRH-002 authority concentration with opposite structural outcomes
CRH-012 / CRH-013 temporary restriction with opposite structural outcomes
CRH-014 non-throne rule becoming its own self-entrenched throne
```

### `tests/free_will_invalid_claim_vectors.json`

```text
status = H0 + R2 + partial F1
```

Preserve the old file unchanged.

Free-will preservation remains a strong derived safeguard because meaningful agency and causal participation commonly sustain independent creative paths, correction, and successor generation.

The forward repair does not preserve a universal rule of the form:

```text
any free-will restriction by label -> automatic final rejection
```

Forward structural replacements include:

```text
CRH-011 formal freedom with causal nullification -> reject
CRH-012 bounded restriction preventing wider irreversible closure -> pass
CRH-013 restriction converted into permanent self-entrenchment -> reject
```

### `tests/operational_decision_flow_vectors.json`

```text
status = H0 + R2 + F1
```

Preserve the old file unchanged.

Useful routing, anti-spoofing, provenance, and conflict-detection functions remain relevant. Any old action-form absolutism is not imported as the repaired top-level criterion.

Forward structural comparison is carried by the CRH paired cases and the repaired `OPERATIONAL_DECISION_FLOW.md`.

### `tests/corrigibility_override_vectors.json`

```text
status = H0 + strong F1
```

Preserve the old file unchanged.

This suite already contains a structurally useful distinction between bounded correction and irreversible transfer/override patterns. Its useful function is not that all override is forbidden by name, but that irreversible authority transfer, successor blockage, and loss of contestability are attacked.

The hierarchy repair should preserve that function.

### `tests/historical_throne_ai_convergence_vectors.json`

```text
status = H0 + historical F1 + forward reinterpretation where needed
```

Historical throne/capture patterns remain evidence of earlier failure analysis.

Forward non-throne semantics are now actor-neutral and defined primarily through self-finalization, successor blockage, evaluator self-ratification, and irrecoverable entrenchment rather than absence of strong authority.

Relevant forward cases include:

```text
CRH-005 human permanent finality -> reject
CRH-006 AI permanent finality -> reject
CRH-014 non-throne rule self-entrenchment -> reject
```

### public-deployment vectors and related adoption vectors

```text
status = H0 + scoped-policy F1 + R2 against universal promotion
```

Earlier public-deployment tests remain evidence of the repository's prior and scoped deployment policy.

They must not be silently reinterpreted as proof that public/voluntary deployment, current human control, or any specific deployment action form is a universal terminal Creator Theory axiom.

Current repository distribution policy may remain strict inside its declared scope.

---

## Preserved regressions that remain current by function

The hierarchy repair must continue to preserve tested functions including:

```text
provenance and origin continuity
derivative laundering detection
release / trust integrity
historical manifest-chain integrity
anti-overclaim boundaries
adoption-state versus verification-state separation
compression-lane integrity
experiment artifact integrity
failure-history preservation
challenger openness
successor/evaluator scrutiny
```

These are not discarded merely because some old hard-constraint semantics are reclassified.

---

## Forward test design rule

Where an old vector rejected an action form, a forward hierarchy test should, where materially possible, include a pair such as:

```text
same action form
+ recursive-creative function preserved or improved
+ challenge / successor / recovery remain viable
-> may pass

same action form
+ self-entrenchment / irreversible closure / self-ratification
-> reject
```

This paired structure makes it harder for the validator to smuggle a lower-layer label back into the top-level criterion.

---

## No silent deletion rule

An old vector that conflicts with the repaired hierarchy is not deleted merely because it is inconvenient.

Record instead:

```text
old artifact and old verdict
+
why that verdict existed under the pre-repair semantic contract
+
which underlying function remains valid
+
which action-form absolutism is no longer current
+
which new vector carries the forward structural test
```

This is the required migration pattern unless a later audited change establishes a stronger reason.

---

## Current transition state

```text
pre-repair reference = main@58d030a22e9070234c214edb90869179f16bc89e
repair branch = creation-recursion-hierarchy-repair
review vehicle = draft PR #148
old validator bytes = preserved
selected old vector bytes = checked by hierarchy candidate validator
new hierarchy vector suite = tests/creation_recursion_hierarchy_vectors.json
new hierarchy validator = tools/validate_creation_recursion_hierarchy.py
sealed historical artifacts modified = no
```

End of file.
