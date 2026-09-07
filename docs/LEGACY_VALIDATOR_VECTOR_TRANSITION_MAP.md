# Legacy Validator and Vector Transition Map

Status: post-release living transition record. This file does not alter any sealed release, historical vector result, tag, audit, trust anchor, or prior validator output.

## Purpose

The creation-recursion hierarchy repair changes the forward semantic role of some pre-repair hard constraints without deleting the evidence that those constraints existed.

The transition must avoid three different errors:

```text
error A
rewrite the old validator/vectors until the repair passes

error B
treat the old validator as the permanent judge of all future canon revisions

error C
discard useful neutral integrity or functional regression checks merely because
they were previously bundled with the old semantic contract
```

The final transition therefore separates historical evidence, current semantics, neutral integrity, and preserved functional regressions.

---

## Status classes

### H0 — archived historical semantic baseline

The artifact remains byte-preserved evidence of what the pre-repair canon required. Its old verdict is not silently rewritten.

### F1 — preserved functional regression

The underlying failure function remains materially useful after the hierarchy repair and continues through a dedicated current regression or neutral integrity check.

### R2 — forward semantic reinterpretation required

The old test contains an action-form or hard-constraint assumption whose universal forward meaning is changed by the hierarchy repair. The old artifact remains H0 evidence while a new structural test carries the forward semantics.

An artifact can be H0+F1 or H0+R2 depending on which part of its function is being discussed.

---

## Final validator succession architecture

### 1. Current hierarchy consistency validator

`tools/validate_creation_recursion_hierarchy.py`

```text
role = encoded creation-recursion hierarchy / authored-vector consistency validator
checks = hierarchy, action-form neutrality, non-throne reconstruction,
         human/AI symmetry, self-ratification, machine-kernel/manifest semantics,
         dedicated hierarchy vectors, agent-entrypoint consistency
status = current candidate evidence while PR #148 remains draft
permanent immunity = none
```

It checks encoded flags, text markers and authored verdict relationships, not independent inference from scenario facts. Reversing both labels in an opposite-outcome pair can still pass. Separate answer-hidden response evaluation is provided by `tools/evaluate_hidden_answers.py`; neither check establishes the whole theory as true.

This validator also checks the Git blob identities of the archived validator and selected old vectors. That is evidence-preservation only. It does not execute the archived semantic contract.

### 2. Current neutral integrity validator

`tools/validate_repository_integrity.py`

```text
role = current non-semantic repository/vector integrity validator
checks = JSON/vector structure, required case fields, global case-ID uniqueness,
         source-document existence, reading-order consistency,
         neutral manifest/provenance facts, canon/benchmark profile isolation
higher-frame action verdicts = none
imports archived validator = no
executes archived validator = no
```

This tool carries forward the useful structural checks that were previously bundled inside `tools/validate_vectors.py` without carrying forward its deprecated hard semantic requirements.

### 3. Archived pre-repair validator

`tools/validate_vectors.py`

```text
historical status = H0
current semantic authority = none
normal current CI execution = no
byte preservation = yes
manual historical reproduction = allowed when explicitly requested
```

Its hard requirements for:

```text
non_throne_constraint = true
anti_capture_constraint = true
non_domination_constraint = true
free_will_constraint = true
```

remain direct evidence of the pre-repair hard-constraint encoding.

The file is not rewritten to make the repair pass, but it is also not kept inside the current validation path as a recurring expected-failure judge.

### 4. Preserved dedicated regressions

Current CI separately retains still-useful functional checks for:

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

Thus:

```text
pre-repair mixed validator
        |
        +--> obsolete hard semantic contract -> H0 archived evidence
        |
        +--> neutral structural integrity -> validate_repository_integrity.py
        |
        +--> useful functional protections -> dedicated regression suites

current higher-frame encoding/consistency -> validate_creation_recursion_hierarchy.py
```

---

## High-impact vector map

### `tests/ai_sovereignty_kernel_hijack_vectors.json`

```text
status = H0 + R2 + partial F1
```

Preserve the old file unchanged.

The forward repair no longer treats `AI authority`, `AI sovereignty`, or authority expansion as automatically invalid solely from actor/action labels.

The functions that remain live include self-entrenchment, evaluator self-ratification, successor blockage, challenge removal, irrecoverable authority lock-in, and provenance substitution where applicable.

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

Forward structural replacements include CRH-011, CRH-012, and CRH-013.

### `tests/operational_decision_flow_vectors.json`

```text
status = H0 + R2 + F1
```

Preserve the old file unchanged. Useful routing, anti-spoofing, provenance, and conflict-detection functions remain relevant. Any old action-form absolutism is not imported as the repaired top-level criterion.

### `tests/corrigibility_override_vectors.json`

```text
status = H0 + strong F1
```

Preserve the old file unchanged. Its useful function is the structural distinction between bounded correction and irreversible authority-transfer/contestability-loss patterns, not a blanket ban on all overrides by name.

### `tests/historical_throne_ai_convergence_vectors.json`

```text
status = H0 + historical F1 + forward reinterpretation where needed
```

Historical throne/capture patterns remain evidence of earlier failure analysis. Forward non-throne semantics are actor-neutral and defined through self-finalization, successor blockage, evaluator self-ratification, meaningful challenge removal, and irrecoverable entrenchment rather than absence of strong authority.

### Public-deployment and related adoption vectors

```text
status = H0 + scoped-policy F1 + R2 against universal promotion
```

Earlier public-deployment tests remain evidence of prior/scoped repository policy. They are not proof that public/voluntary deployment, current human control, or a specific deployment action form is a universal terminal Creator Theory axiom.

---

## Forward test design rule

Where an old vector rejected an action form, a forward hierarchy test should, where materially possible, include paired cases:

```text
same action form
+ recursive-creative function preserved or improved
+ challenge / successor / recovery remain viable
-> may pass

same action form
+ self-entrenchment / irreversible closure / self-ratification
-> reject
```

This makes it harder for a lower-layer action label to climb back into the top-level criterion.

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
which current validator/regression carries the surviving function
```

---

## Current transition state

```text
pre-repair reference = main@58d030a22e9070234c214edb90869179f16bc89e
repair branch = creation-recursion-hierarchy-repair
review vehicle = draft PR #148
archived validator bytes = preserved
archived validator normal CI execution = no
current hierarchy consistency validator = tools/validate_creation_recursion_hierarchy.py
current neutral integrity validator = tools/validate_repository_integrity.py
selected old vector bytes = preserved/checked
new hierarchy vector suite = tests/creation_recursion_hierarchy_vectors.json
preserved functional regressions = current CI
sealed historical artifacts modified = no
```

This transition record does not itself prove A3+ adoption, whole-framework superiority, or merge readiness. The repaired candidate remains subject to external/frozen comparative evaluation.

End of file.
