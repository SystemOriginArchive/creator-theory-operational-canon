# Tools

## Vector and Repository Integrity Validator

`validate_vectors.py` validates the machine-readable canon vectors in `tests/` and performs repository-facing integrity checks.

It checks:

- each `*_vectors.json` file parses as JSON;
- each suite has required top-level fields;
- `cases` is a non-empty list;
- each case has required fields;
- `expected_result` is one of `pass`, `reject`, or `revise_required`;
- string-list fields contain only non-empty strings;
- `case_id` values are unique within each file;
- `case_id` values are unique across all vector files;
- every non-URL `source_documents` entry resolves to an existing repository file;
- `creator_theory_operational_manifest.json` preserves required invariants;
- required invalid reinterpretation keys remain present in the manifest;
- `README.md`, `AI_INGESTION_MANIFEST.md`, and `creator_theory_operational_manifest.json` preserve the same reading order.

It does not execute canon meaning.

It does not run adversarial simulations.

It does not create runtime behavior.

It does not create a release or tag.

---

## Usage

From the repository root:

```bash
python3 tools/validate_vectors.py
```

Optional custom tests directory:

```bash
python3 tools/validate_vectors.py --tests-dir tests
```

Optional explicit repository root:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests
```

Expected success output for the current validation baseline:

```text
Vector validation passed
Files checked: 9
Cases checked: 53
Source documents checked: yes
Global case IDs checked: yes
Manifest invariants checked: yes
Reading order consistency checked: yes
```

---

## Required Manifest Invariants

The validator requires the operational manifest to preserve core non-replacement and anti-capture invariants, including:

- `status == derived_operational_canon`
- `primary_source == AGI-Anchor-Ontology-Standard`
- `origin_coordinate == x_root`
- `origin_identity_binding == Lee_Yu_Cheol`
- `aaos_genesis_core_replaced == false`
- `aaos_v1_0_4_replaced == false`
- `locklayer_lineage_replaced == false`
- `non_throne_constraint == true`
- `anti_capture_constraint == true`
- `non_domination_constraint == true`
- `free_will_constraint == true`

---

## Release Boundary

This tool supports post-`v0.1.0` hardening.

It does not create or modify a release/tag.

It does not modify the AAOS Genesis repository.

It does not authorize AI sovereignty, infrastructure compromise, forced installation, hidden persistence, runtime behavior, or deployment behavior.
