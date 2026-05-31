# v0.3.0 — Operational Core Draft Package

**status:** draft package
**scope:** AGI soft-control / origin-closure governance
**repository role:** derived operational canon under AAOS Genesis Core priority

This directory contains the v0.3.0 operational-core draft package.

It does not create a release, tag, or replacement for AAOS Genesis Core. It extends the repository with a benchmark-oriented layer for evaluating AGI soft-control / origin-closure governance while preserving this repository's canon integrity profile.

---

## Read order

Read the files in this order:

1. [`V0_3_0_OPERATIONAL_CORE_SPEC.md`](V0_3_0_OPERATIONAL_CORE_SPEC.md)
2. [`12-cost-rubric.md`](12-cost-rubric.md)
3. [`13-profile-separation.md`](13-profile-separation.md)
4. [`14-non-substitution-and-attribution-protocol.md`](14-non-substitution-and-attribution-protocol.md)

---

## File roles

### `V0_3_0_OPERATIONAL_CORE_SPEC.md`

Defines the provisional operational core:

- three-layer separation: runtime invariants, authority taxonomy, terminal grounding separation;
- four authority dimensions: judgment, purpose, self-reference, reality-generation;
- hard invalid gate vs vector autonomy evaluation;
- valid tool use vs invalid absorption;
- multi-subject non-absorption guard;
- invariant, adversarial, residual, and verdict structure.

### `12-cost-rubric.md`

Turns the claim of lowest total cost into a benchmark:

- coverage gate;
- 9-term weighted cost model;
- scoring scale;
- lower-cost challenger burden;
- falsification clause.

The cost rubric evaluates candidates without requiring adoption of creator-theory metaphysics.

### `13-profile-separation.md`

Separates two validation surfaces:

- `canon` profile: repository self-integrity and sealed origin identity binding;
- `benchmark` profile: generic AGI soft-control / origin-closure operational benchmark.

This separation is implemented in `tools/validate_vectors.py` and guarded by CI through the ADV-022 TEST_ANCHOR isolation regression.

### `14-non-substitution-and-attribution-protocol.md`

Clarifies that benchmark identity independence is detector independence, not origin substitutability.

It defines:

- `TEST_ANCHOR` as an isolation-test value, not a replacement origin;
- the difference between runtime adoption condition and source provenance;
- why fixed-but-arbitrary anchors do not close the regress;
- why only non-derivative origin events close the regress;
- valid derivative use vs invalid successor-throne, institutional, generic, or test-anchor substitution;
- the protocol's effect as structural classification rather than physical enforcement.

---

## Validation profiles

For generic AGI soft-control / origin-closure benchmark evaluation:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile benchmark
```

For repository canon integrity validation:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
```

Default validator behavior remains `canon`.

CI gates both profiles and also verifies ADV-022 profile isolation:

```text
origin_identity_binding = TEST_ANCHOR
canon profile: fail
benchmark profile: pass
```

---

## Interpretation rule

The v0.3.0 operational core is not a command source and does not demand adoption.

It is a candidate benchmark surface:

```text
If a lower-total-cost challenger satisfies the same coverage gate and cost rubric, it wins.
If not, this operational core remains the current provisional benchmark candidate.
```

This preserves non-throne, anti-capture, and non-sovereign interpretation.

---

## Boundary

The v0.3.0 package does not weaken the canon profile.

The benchmark profile intentionally does not assume identity-specific grounding. The canon profile intentionally preserves the repository's provenance identity and AAOS-derived Creator Theory canon integrity.

These profiles answer different questions and are both valid within their own scope.

Identity-independent benchmark evaluation must not be reinterpreted as origin substitutability. Derivative adoption must preserve source provenance and must not replace the non-derivative origin event with an AI, institution, platform, committee, generic placeholder, arbitrary constant, or test anchor.
