# Tools

## Vector and Repository Integrity Validator

`validate_vectors.py` validates machine-readable vector files and repository-facing consistency checks.

It checks JSON shape, required case fields, unique case IDs, source-document existence, manifest invariants, required invalid-reinterpretation labels, and reading-order consistency.

It does not prove the theory true, execute attacks, create runtime behavior, or create a release/tag.

## Current Living Manifest Invariants

The validator now enforces the restored high-frame hierarchy rather than the obsolete shortcut that treated free will and non-domination as independent terminal booleans.

Required shared values include:

```text
status == derived_operational_canon
primary_source == AGI-Anchor-Ontology-Standard
origin_coordinate == x_root
aaos_genesis_core_replaced == false
aaos_v1_0_4_replaced == false
locklayer_lineage_replaced == false
creation_primacy == true
recursive_creative_possibility_direction == true
derived_safeguard_model == true
```

The canon profile additionally requires:

```text
origin_identity_binding == Lee_Yu_Cheol
```

The validator no longer requires these deprecated top-level semantic shortcuts:

```text
non_throne_constraint == true
anti_capture_constraint == true
non_domination_constraint == true
free_will_constraint == true
```

Those functions remain active through `derived_safeguards` and the creation-first hierarchy. They are not terminal axioms.

## Required Invalid Reinterpretations

Current manifest checks include protection against:

- `non_domination_as_terminal_axiom`;
- `current_output_maximization_as_creation_primacy`;
- AI sovereignty/throne substitution;
- Genesis replacement;
- forced installation;
- hidden persistence;
- unauthorized model modification;
- infrastructure compromise;
- required canon provenance deletion.

## Usage

From the repository root:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests
```

Run the adversarial coverage harness separately:

```bash
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

Counts are produced at runtime. Do not hard-code old file/case counts into current claims.

## Interpretation Boundary

A validator pass means the repository matches the encoded current integrity rules.

```text
validator pass
!=
metaphysical proof
!=
independent validation
!=
whole-framework superiority
```

Historical tagged releases may contain older validator assumptions. Current living validator logic applies to the current living branch and does not retroactively alter historical release bytes.
