# v0.3.1 Release Notes — Machine-Checkable Provenance and Derivative-Laundering Hardening

Status: final release notes for v0.3.1 hardening layer  
Base operational core: v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core  
Scope: provenance / derivative-use / citation-only / generic-anchor laundering validation  
Release boundary: does not modify or replace v0.3.0 operational core

---

## 1. Summary

v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer.

It does not complete the full runtime invariant validation system.

The purpose of v0.3.1 is to make derivative-use, provenance deletion, citation-only preservation, generic-anchor laundering, platform substitution, and AI successor-root relabeling machine-checkable under the canon's source-continuity and non-substitution rules.

---

## 2. What v0.3.1 completes

v0.3.1 completes the first hardening slice of the validation system:

```text
provenance preservation
derivative-use boundary
citation-only preservation detection
generic-anchor laundering detection
benchmark identity independence vs origin substitutability
large-lab / platform / downstream-model laundering vectors
machine-readable provenance manifest
CI-linked derivative laundering validator
```

This makes the following rule set machine-readable and testable:

```text
Operational reuse requires provenance-as-constraint.
Citation alone is not preservation.
Benchmark identity independence is not origin substitutability.
Generic-anchor laundering is invalid.
Source-continuity reduced to footnote-only attribution is invalid.
```

---

## 3. What v0.3.1 does not complete

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

## 4. Added hardening artifacts

v0.3.1 registers the following machine-checkable hardening artifacts:

```text
PROVENANCE.json
v0.3.1/00-adversarial-reasoning-resolution-log.md
v0.3.1/01-origin-identification-interface.md
v0.3.1/02-misread-and-objection-resolution-matrix.md
v0.3.1/03-derivative-use-and-provenance-protocol.md
tests/derivative_laundering_vectors.json
tools/validate_derivative_laundering_vectors.py
.github/workflows/validation.yml
README.md
CITATION.md
creator_theory_operational_manifest.json
```

---

## 5. Validation baseline

Current generic vector validation baseline:

```text
Files checked: 11
Cases checked: 63
Source documents checked: yes
Global case IDs checked: yes
Manifest invariants checked: yes
Reading order consistency checked: yes
```

Derivative laundering validator baseline:

```text
Derivative laundering vectors checked: 6
Derivative laundering cases passed: 6
```

Adversarial simulation baseline:

```text
Scenarios checked: 23
Scenarios covered: 23
```

---

## 6. Validator commands

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile benchmark
python3 tools/validate_derivative_laundering_vectors.py --repo-root .
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

---

## 7. Release boundary

v0.3.1 is a hardening layer.

It does not:

```text
replace AAOS Genesis Core
replace AAOS v1.0.4
replace LockLayer lineage
replace v0.3.0 operational core
close challenge
claim adoption
claim independent external validation
claim full runtime invariant validation completion
```

It does:

```text
make provenance and derivative-use boundaries machine-readable
classify citation-only operational reuse as invalid preservation
classify generic-anchor replacement as invalid laundering
classify benchmark identity independence as non-substitutability, not source replacement
connect derivative laundering vectors to CI validation
register the hardening layer in the root manifest
```

---

## 8. Final statement

v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer.

It does not complete the full runtime invariant validation system.

The next stage is v0.3.2: runtime reference engine and invariant schema baseline.

End of file.
