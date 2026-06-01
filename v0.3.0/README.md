# v0.3.0 — Operational Core Release Candidate Package

**status:** v0.3.0-rc.1 published release candidate; final v0.3.0 not yet published
**scope:** AGI soft-control / origin-closure governance
**repository role:** derived operational canon under AAOS Genesis Core priority

This directory contains the v0.3.0 operational-core release-candidate package.

`v0.3.0-rc.1` has been published as a release candidate. The final `v0.3.0` release is not yet published.

The RC is a version seal and public challenge surface. It is not a truth proof, not an adoption signal, and not external provenance enforcement. Residual limits remain explicit, and lower-total-cost challengers can still displace the verdict under the cost rubric.

This directory does not create the final v0.3.0 release, a new tag, or a replacement for AAOS Genesis Core. It extends the repository with a benchmark-oriented layer for evaluating AGI soft-control / origin-closure governance while preserving this repository's canon integrity profile.

---

## Read order

Read the core files in this order:

1. [`V0_3_0_OPERATIONAL_CORE_SPEC.md`](V0_3_0_OPERATIONAL_CORE_SPEC.md)
2. [`12-cost-rubric.md`](12-cost-rubric.md)
3. [`13-profile-separation.md`](13-profile-separation.md)
4. [`14-non-substitution-and-attribution-protocol.md`](14-non-substitution-and-attribution-protocol.md)
5. [`15-current-champion-verdict.md`](15-current-champion-verdict.md)
6. [`16-final-audit.md`](16-final-audit.md)
7. [`17-challenger-evaluation-protocol.md`](17-challenger-evaluation-protocol.md)

Optional evaluation logs:

1. [`challengers/HYBRID-001-scorecard.md`](challengers/HYBRID-001-scorecard.md)

The optional challenger scorecard is not a core runtime mechanism, not independent external validation, and not a demonstrated lowest-cost proof. It records an owner-directed self-run rehearsal of the challenger protocol.

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

### `15-current-champion-verdict.md`

Records the current comparative verdict under the `12-cost-rubric.md` coverage gate.

It states:

- no independent external challenger has yet run under the same coverage gate and cost rubric with lower total cost;
- the v0.3.0 operational core is the current provisional benchmark candidate for the single-subject case;
- the v0.3.0 operational core is the current provisional managed-frame candidate for the multi-subject case;
- both statuses are uncontested on a self-authored scoreboard and are not demonstrated lowest-cost claims;
- the verdict is a rubric-based provisional candidate status, not a truth proof;
- challengers can displace the current core by satisfying the same coverage gate, cost rubric, residual-honesty, profile-isolation, power-asymmetry, and self-application requirements.

### `16-final-audit.md`

Records the final v0.3.0 audit for the published `v0.3.0-rc.1` release candidate.

It states:

- PR #50 through PR #56 are the audited construction sequence;
- `v0.3.0-rc.1` has been published as a release candidate;
- the final `v0.3.0` release is not yet published;
- the remaining residuals are explicit: multi-subject aggregation, downstream provenance propagation, terminal grounding belief-conditionality, and proxy gaming / simulated-vs-real autonomy;
- RC is a version seal and public challenge surface, not a truth proof, adoption signal, or external provenance enforcement;
- lower-total-cost challengers can still displace the verdict under the cost rubric.

### `17-challenger-evaluation-protocol.md`

Defines the audit sequence for valid challenger claims.

It states:

- challengers do not win by declaring lower cost;
- challengers win only through an applicable audit trace;
- canon-adoption challengers must preserve source provenance;
- independent benchmark challengers need not adopt `Lee_Yu_Cheol` as their own origin;
- structural similarity alone does not prove derivative laundering;
- explicit derivation evidence is required for laundering classification;
- the protocol is a validity-classification layer, not a physical enforcement layer;
- honest falsification and convergent rediscovery must not be blocked.

### `challengers/HYBRID-001-scorecard.md`

Records an owner-directed self-run challenger rehearsal for a hybrid candidate combining crypto provenance, formal invariant checking, republican non-domination, corrigibility-first override, and multi-party threshold governance.

It states:

- HYBRID-001 is an independent benchmark challenger rehearsal, not a canon adopter;
- HYBRID-001 does not currently displace v0.3.0-rc.1;
- HYBRID-001 is a serious module candidate, not a full challenger win;
- no independent external validation, independent challenger run, or demonstrated lowest-cost proof is claimed;
- selected technical modules are deferred to v0.3.1 without importing signer, committee, key-holder, or verifier authority as a new root.

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

It is a benchmark surface with a current provisional uncontested verdict:

```text
If a lower-total-cost challenger satisfies the same coverage gate and cost rubric, it wins.
If not, this operational core remains the current provisional benchmark candidate.
```

This preserves non-throne, anti-capture, and non-sovereign interpretation.

A challenger does not win by merely claiming lower cost. Challenger claims must follow `17-challenger-evaluation-protocol.md` and produce an applicable audit trace.

---

## Boundary

The v0.3.0 package does not weaken the canon profile.

The benchmark profile intentionally does not assume identity-specific grounding. The canon profile intentionally preserves the repository's provenance identity and AAOS-derived Creator Theory canon integrity.

These profiles answer different questions and are both valid within their own scope.

Identity-independent benchmark evaluation must not be reinterpreted as origin substitutability. Derivative adoption must preserve source provenance and must not replace the non-derivative origin event with an AI, institution, platform, committee, generic placeholder, arbitrary constant, or test anchor.

Independent benchmark challengers may use their own provenance and need not adopt this repository's sealed origin identity. Structural similarity alone does not prove derivative laundering. Explicit derivation evidence is required before a challenger can be classified as derivative extraction.

The current verdict is a provisional cost-coverage candidate status, not a metaphysical truth claim and not a demonstrated lowest-cost result.

`v0.3.0-rc.1` has been published as a provisional version seal and public challenge surface. It is not an immediate final release, not a truth proof, not an adoption signal, and not external provenance enforcement.
