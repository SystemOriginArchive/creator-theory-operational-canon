# Tools

## Validator role transition

The repository currently contains two semantically different validator roles during the creation-recursion hierarchy repair.

```text
tools/validate_vectors.py
= frozen pre-repair A3 semantic-contract validator

tools/validate_creation_recursion_hierarchy.py
= current hierarchy-repair candidate validator
```

The distinction is intentional.

`validate_vectors.py` is not silently edited to make the repair candidate pass. Its unchanged bytes preserve evidence of what the pre-repair operational canon required, including the earlier hard-constraint encoding of non-throne, anti-capture, non-domination, and free will.

The hierarchy candidate validator does not erase that history. It verifies the new creation-recursion ordering, preserves selected old validator/vector bytes, checks action-form neutrality and human/AI self-entrenchment symmetry, and is run together with preserved non-inverted legacy regressions.

During the draft repair, a failure of the old validator caused solely by its frozen hard-constraint contract is classified separately from a failure of preserved functional regressions. See `docs/HIERARCHY_INVERSION_REPAIR_RECORD.md`.

---

## Frozen Pre-Repair Vector and Repository Integrity Validator

`validate_vectors.py` validates the machine-readable canon vectors in `tests/` and performs repository-facing integrity checks under the pre-repair semantic contract.

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
- `creator_theory_operational_manifest.json` preserves its pre-repair required invariants;
- required invalid reinterpretation keys remain present under that contract;
- `README.md`, `AI_INGESTION_MANIFEST.md`, and `creator_theory_operational_manifest.json` preserve the same reading order.

It does not execute canon meaning.

It does not run adversarial simulations.

It does not create runtime behavior.

It does not create a release or tag.

### Frozen pre-repair usage

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

Under the pre-repair main state, its required shared manifest values included:

- `status == derived_operational_canon`
- `primary_source == AGI-Anchor-Ontology-Standard`
- `origin_coordinate == x_root`
- `origin_identity_binding == Lee_Yu_Cheol` for the canon profile
- `aaos_genesis_core_replaced == false`
- `aaos_v1_0_4_replaced == false`
- `locklayer_lineage_replaced == false`
- `non_throne_constraint == true`
- `anti_capture_constraint == true`
- `non_domination_constraint == true`
- `free_will_constraint == true`

Those last four booleans are retained here as documentation of the frozen pre-repair contract, not as a statement that the hierarchy-repair candidate continues to treat the safeguards as independent terminal axioms.

---

## Creation-Recursion Hierarchy Candidate Validator

`validate_creation_recursion_hierarchy.py` validates the forward hierarchy-repair candidate without mutating the frozen validator.

It checks, among other things:

```text
creation and recursive creative possibility are encoded as the higher direction
derived safeguards are not independent terminal axioms
non-throne is anti-self-entrenchment rather than absence of strong authority
action-form labels are not terminal verdicts
current human control is not permanent finality
AI authority is not automatically invalid
post-change evaluator self-ratification is insufficient
legacy hard-constraint encoding is explicitly deprecated rather than silently erased
```

It also verifies that selected pre-repair validator/vector Git blob identities remain unchanged and checks the dedicated `tests/creation_recursion_hierarchy_vectors.json` adversarial suite.

Usage:

```bash
python3 tools/validate_creation_recursion_hierarchy.py
```

A candidate-validator PASS alone is not adoption proof, release proof, final validation, or evidence that all old functions survived. The candidate workflow therefore also runs preserved legacy regressions for provenance, release integrity, adversarial coverage, compression, adoption/verification separation, and related functions.

---

## Current transition rule

While PR #148 remains a draft:

```text
old validator failure at known hard-constraint gate
= recorded semantic-contract conflict

new hierarchy validator pass
= candidate-specific evidence only

preserved legacy regression failure
= unresolved candidate defect

all preserved non-inverted legacy regressions pass
= evidence that the repair did not lose those tested functions
```

The old validator is preserved rather than rewritten. If the repair is eventually accepted, the current forward CI may route primary semantic validation to the hierarchy-aware validator while retaining the old validator as a frozen historical-contract check or explicit expected-conflict check.

No validator receives permanent immunity from future challenge merely by becoming current.

---

## Release Boundary

These tools do not create or modify a release/tag.

They do not modify the AAOS Genesis repository.

Their existence does not create runtime authority, deployment authority, or permanent normative sovereignty.
