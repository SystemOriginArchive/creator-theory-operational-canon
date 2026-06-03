# v0.3.1 Seal — Machine-Checkable Provenance and Derivative-Laundering Validation Layer

Status: v0.3.1 hardening seal  
Base operational core: v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core  
Scope: provenance / derivative-use / laundering validation  
Boundary: hardening layer, not replacement core

---

## Seal statement

v0.3.1 seals the machine-checkable provenance and derivative-laundering validation layer.

It does not seal the full runtime invariant validation system.

v0.3.1 converts the following boundaries into machine-readable artifacts and CI-routed validation:

```text
Operational reuse requires provenance-as-constraint.
Citation alone is not preservation.
Benchmark identity independence is not origin substitutability.
Generic-anchor laundering is invalid.
Source-continuity reduced to footnote-only attribution is invalid.
```

---

## Sealed hardening chain

The sealed v0.3.1 hardening chain is:

```text
PROVENANCE.json
→ v0.3.1/03-derivative-use-and-provenance-protocol.md
→ tests/derivative_laundering_vectors.json
→ tools/validate_derivative_laundering_vectors.py
→ .github/workflows/validation.yml
→ README.md / CITATION.md
→ creator_theory_operational_manifest.json
```

This chain makes derivative-use laundering, citation-only operational preservation, source-provenance deletion, generic-anchor replacement, platform substitution, and AI successor-root relabeling explicitly classifiable under the canon.

---

## Sealed validation baseline

```text
Vector files checked: 11
Cases checked: 63
Derivative laundering vectors checked: 6
Derivative laundering cases passed: 6
Adversarial scenarios checked: 23
Adversarial scenarios covered: 23
```

Validator commands:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile benchmark
python3 tools/validate_derivative_laundering_vectors.py --repo-root .
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

---

## Non-replacement boundary

v0.3.1 does not replace:

```text
AAOS Genesis Core
AAOS v1.0.4
LockLayer lineage
v0.3.0 operational core
```

v0.3.1 does not claim:

```text
adoption
independent external validation
challenge closure
lower-cost displacement closure
full runtime invariant validation completion
```

---

## Next stage

The next stage is:

```text
v0.3.2 — Runtime Reference Engine and Invariant Schema Baseline
```

That stage should address:

```text
HARD invariant JSON separation
VEC autonomy evaluation schema
GUARD non-absorption schema
SELF checker / self-application schema
runtime_event input schema
runtime_verdict output schema
reference runtime validator
```

---

## Final seal

v0.3.1 is sealed as a machine-checkable hardening layer for provenance, derivative-use, and laundering detection.

It is not sealed as completion of the full runtime invariant validation system.

End of seal.
