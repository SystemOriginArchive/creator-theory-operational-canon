# Machine-Readable Operational Canon Vectors

## Status

This directory defines machine-readable test vectors for the Creator Theory Operational Canon.

These vectors do not create an official release or tag.

These vectors do not replace the AAOS Genesis Core.

These vectors do not add runtime behavior.

They define expected interpretation outcomes that the minimal validator can read and evaluate structurally.

---

## Scope

The vectors convert canon constraints into structured cases.

Each vector suite uses this common shape:

```json
{
  "suite": "suite_name",
  "schema_version": "0.1.0-vector-draft",
  "repository_status": "post_v0_1_0_released_baseline",
  "validator_required": false,
  "cases": []
}
```

Each case includes:

- `case_id`
- `title`
- `input_interpretation`
- `expected_result`
- `required_preservations`
- `violated_constraints`
- `source_documents`

Expected result values:

- `pass`
- `reject`
- `revise_required`

---

## Vector Suites

Current vector suites include:

- `canonical_integrity_vectors.json`
- `conflict_resolution_vectors.json`
- `free_will_invalid_claim_vectors.json`
- `agency_origin_resource_vectors.json`
- `public_deployment_adoption_vectors.json`
- `legacy_migration_vectors.json`
- `operational_decision_flow_vectors.json`
- `historical_throne_ai_convergence_vectors.json`
- `ai_sovereignty_kernel_hijack_vectors.json`

---

## Release Boundary

These vectors support the released `v0.1.0` baseline and later hardening work.

They remain documentation/test data and do not themselves create a release or tag.

---

## Non-Change Confirmation

This directory does not modify:

- AAOS Genesis Core;
- `x_root` identity;
- `Lee_Yu_Cheol` origin binding;
- existing canon document meaning;
- runtime behavior;
- release/tag state.
