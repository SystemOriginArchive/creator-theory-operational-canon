# v0.3.1 — Machine-Checkable Provenance and Derivative-Laundering Hardening

## Summary

v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer for the Creator Theory Operational Canon.

This release hardens derivative-use boundaries, citation-only preservation handling, generic-anchor laundering detection, platform/institution substitution detection, and AI successor-root relabeling detection.

v0.3.1 does **not** complete the full runtime invariant validation system.

Next stage:

```text
v0.3.2 — Runtime Reference Engine and Invariant Schema Baseline
```

---

## What this release adds

```text
PROVENANCE.json
v0.3.1/00-adversarial-reasoning-resolution-log.md
v0.3.1/01-origin-identification-interface.md
v0.3.1/02-misread-and-objection-resolution-matrix.md
v0.3.1/03-derivative-use-and-provenance-protocol.md
v0.3.1/RELEASE_NOTES_v0.3.1.md
v0.3.1/SEAL_v0.3.1.md
tests/derivative_laundering_vectors.json
tools/validate_derivative_laundering_vectors.py
CI integration through .github/workflows/validation.yml
README.md validation baseline update
CITATION.md citation-only preservation boundary update
creator_theory_operational_manifest.json v0.3.1 hardening graph registration
```

---

## Core rules sealed by v0.3.1

```text
Operational reuse requires provenance-as-constraint.
Citation alone is not preservation.
Benchmark identity independence is not origin substitutability.
Generic-anchor laundering is invalid.
Source-continuity reduced to footnote-only attribution is invalid.
```

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

## Boundary

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
```

---

## Exact release statement

v0.3.1 completes the machine-checkable provenance and derivative-laundering validation layer.

It does not complete the full runtime invariant validation system.

The next stage is v0.3.2: runtime reference engine and invariant schema baseline.
