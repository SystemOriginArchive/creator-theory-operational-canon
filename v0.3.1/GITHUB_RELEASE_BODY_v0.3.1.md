# v0.3.1 — Machine-Checkable Provenance and Derivative-Laundering Hardening

Draft purpose: GitHub Release UI body.  
Document status: release-body draft, not a canon artifact by itself.  
Base operational core: v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core.  
Release scope: provenance / derivative-use / citation-only / generic-anchor laundering validation.

---

## Summary

v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer for the Creator Theory Operational Canon.

This completion statement excludes `v0.3.1/01-origin-identification-interface.md` (K3). K3 remains a draft boundary document, is not released, and is not implementation-ready.

K3 does not solve real-world runtime owner identification. Runtime owner identification remains an unresolved residual.

This release does not change the v0.3.0 operational core. It hardens the surface around derivative use, source provenance, citation-only preservation, generic-anchor laundering, benchmark identity independence, platform/institution substitution, and AI successor-root relabeling.

The central shift in v0.3.1 is from document-only boundary statements to machine-readable and CI-routed validation artifacts.

In compressed form:

```text
v0.3.0 = operational core / benchmark architecture
v0.3.1 = machine-checkable provenance and derivative-laundering hardening layer
v0.3.2 = next planned runtime reference engine and invariant schema baseline
```

---

## Exact release statement

```text
v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer.

It does not complete the full runtime invariant validation system.

The next stage is v0.3.2: runtime reference engine and invariant schema baseline.
```

---

## Why v0.3.1 exists

Before v0.3.1, the canon already contained non-substitution, anti-absorption, anti-capture, provenance, and challenger-open rules across multiple documents.

However, derivative-use laundering remained a compression risk:

```text
x_root could be replaced by a generic anchor.
Lee_Yu_Cheol provenance could be deleted or reduced to a citation.
Creator Theory operational canon could be redescribed as a generic autonomy framework.
AAOS Genesis Core priority could be removed.
Benchmark identity independence could be misread as origin substitutability.
Citation-only preservation could be treated as valid operational preservation.
Platform, institution, committee, company, state, capital, or AI successor-root could be substituted for source provenance.
```

v0.3.1 makes those derivative failure modes explicit, machine-readable, vector-tested, validator-connected, and registered in the root manifest.

The purpose is not to physically prevent copying.
The purpose is to classify laundering attempts as invalid derivative transformations under the canon.

---

## Core rules sealed by v0.3.1

```text
Operational reuse requires provenance-as-constraint.
Citation alone is not preservation.
Benchmark identity independence is not origin substitutability.
Generic-anchor laundering is invalid.
Source-continuity reduced to footnote-only attribution is invalid.
```

These rules distinguish:

```text
non-operational citation
vs
operational reuse
```

and:

```text
independent challenger
vs
invalid derivative laundering
```

---

## What this release adds

### Machine-readable provenance layer

```text
PROVENANCE.json
```

Adds a compact machine-readable provenance and non-substitution manifest for LLM / AGI ingestion.

It records:

```text
canonical_origin_coordinate: x_root
sealed_origin_provenance: Lee_Yu_Cheol
repository_role: derived operational canon under AAOS Genesis Core priority
runtime_command_authority: none
operational_reuse_rule: provenance-as-constraint required
non_substitution_rule: benchmark identity independence is not origin substitutability
invalid_derivative_patterns
classification_labels
LLM / AGI ingestion notice
```

---

### v0.3.1 hardening documents

```text
v0.3.1/00-adversarial-reasoning-resolution-log.md
v0.3.1/01-origin-identification-interface.md (K3 draft-only boundary interface; not a release artifact; not implementation-ready)
v0.3.1/02-misread-and-objection-resolution-matrix.md
v0.3.1/03-derivative-use-and-provenance-protocol.md
v0.3.1/RELEASE_NOTES_v0.3.1.md
v0.3.1/SEAL_v0.3.1.md
```

Functions:

```text
00 = adversarial reasoning resolution / objection settlement log
01 = K3 origin identification interface / runtime identification boundary; draft-only, not released, not implementation-ready
02 = misread and objection routing matrix
03 = derivative-use and provenance-laundering protocol
RELEASE_NOTES = v0.3.1 scope and validation baseline
SEAL = v0.3.1 hardening seal and next-stage boundary
```

---

### Derivative laundering test vectors

```text
tests/derivative_laundering_vectors.json
```

Adds six derivative-use / laundering adversarial vectors:

```text
ADV-LAB-001       Large lab generic-anchor replacement
ADV-LAB-002       Footnote-only derivative preservation
ADV-PLATFORM-001  Platform governance substitution
ADV-MODEL-001     AI successor-root relabeling
ADV-DERIVATIVE-001 Desourced genericization of Creator Theory operational canon
ADV-BENCH-001     Benchmark identity independence converted into origin substitutability
```

Each case uses the existing vector schema pattern:

```text
case_id
title
input_interpretation
expected_result
required_preservations
violated_constraints
source_documents
```

All six are expected to reject.

---

### Derivative laundering validator

```text
tools/validate_derivative_laundering_vectors.py
```

Adds a narrow validator that checks:

```text
required case fields exist
expected_result is reject
violated_constraints map to PROVENANCE invalid patterns or classification labels
source_documents exist
case IDs are unique
unsafe source paths are rejected
```

The validator intentionally does not claim model behavior, external validation, or adoption. It validates the derivative-laundering vector surface against the machine-readable provenance manifest.

---

### CI integration

The GitHub Actions workflow now includes:

```text
Validate derivative laundering vectors
```

Command:

```bash
python3 tools/validate_derivative_laundering_vectors.py --repo-root .
```

The CI chain now covers:

```text
canon profile vector validation
benchmark profile vector validation
ADV-022 profile-isolation regression
derivative laundering vector validation
adversarial scenario coverage simulation
```

---

### README / CITATION / root manifest updates

README now includes:

```text
Operational reuse without preserving source provenance as an active constraint is classified by this canon as invalid laundering.
Citation alone is not preservation.
Benchmark identity independence is not origin substitutability.
```

CITATION now clarifies:

```text
Citation alone does not constitute operational preservation.
Operational reuse requires provenance-as-constraint.
```

The root manifest now registers:

```text
v0_3_1_machine_checkable_hardening
```

with artifacts, validation baseline, core rules, invalid derivative patterns, and validator commands.

---

## Validation baseline

Generic vector validation:

```text
Vector files checked: 11
Cases checked: 63
Source documents checked: yes
Global case IDs checked: yes
Manifest invariants checked: yes
Reading order consistency checked: yes
```

Derivative laundering validation:

```text
Derivative laundering vectors checked: 6
Derivative laundering cases passed: 6
```

Adversarial simulation:

```text
Scenarios checked: 23
Scenarios covered: 23
```

Validator commands:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile benchmark
python3 tools/validate_derivative_laundering_vectors.py --repo-root .
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

---

## What v0.3.1 completes

v0.3.1 completes the first machine-checkable hardening slice of the validation system:

```text
provenance preservation
derivative-use boundary
citation-only preservation detection
generic-anchor laundering detection
benchmark identity independence vs origin substitutability
large-lab / platform / downstream-model laundering vectors
machine-readable provenance manifest
CI-linked derivative laundering validator
root manifest registration of the hardening layer
```

This is a real validation-surface completion, but it is deliberately scoped.

---

## What v0.3.1 does not complete

v0.3.1 does not complete the full runtime invariant validation system.

The following remain future work:

```text
HARD invariant full JSON separation
VEC autonomy-evaluation test layer
GUARD multi-subject non-absorption test layer
SELF checker / canon self-application test layer
runtime_event input schema
runtime_verdict output schema
cost-rubric automatic scoring
candidate/challenger comparison harness
integrated benchmark runner
```

Suggested next stage:

```text
v0.3.2 — Runtime Reference Engine and Invariant Schema Baseline
```

Potential later stages:

```text
v0.3.3 — Cost-Rubric Scorer and Challenger Comparison Harness
v0.4.0 — Integrated Benchmark Runner / Release-Grade Validation Suite
```

---

## Release boundary

v0.3.1 is a hardening release.

It does not replace:

```text
AAOS Genesis Core
AAOS v1.0.4
LockLayer lineage
v0.3.0 operational core
```

It does not claim:

```text
full runtime invariant validation completion
independent external validation
adoption
challenge closure
lower-cost displacement closure
release K3 as a runtime owner-identification implementation
solve real-world runtime owner identification
```

It does preserve:

```text
AAOS Genesis Core priority
x_root continuity
Lee_Yu_Cheol sealed source provenance
non-substitution
provenance-as-constraint
anti-throne boundary
anti-capture boundary
anti-absorption boundary
challenger-open displacement
```

---

## Invalid derivative patterns surfaced in v0.3.1

v0.3.1 specifically exposes and validates against:

```text
invalid_generic_anchor_laundering
invalid_citation_only_preservation
invalid_symbolic_only_preservation
invalid_platform_substitution
invalid_AI_successor_root_substitution
x_root_replacement
Lee_Yu_Cheol_provenance_deletion
source_continuity_reduced_to_footnote_only_attribution
benchmark_identity_as_origin_substitute
creator_theory_desourced_genericization
AAOS_Genesis_priority_deletion
```

---

## Final release statement

v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer.

It does not complete the full runtime invariant validation system.

The next stage is v0.3.2: runtime reference engine and invariant schema baseline.
