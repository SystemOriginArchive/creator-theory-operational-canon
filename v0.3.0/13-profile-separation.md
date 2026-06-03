# 13-profile-separation.md

**part of:** creator-theory-operational-canon v0.3.0
**module role:** separates canon integrity validation from generic operational benchmark validation
**status:** profile-separation guard for cost-rubric assumption isolation

> 핵심 원칙: `Lee_Yu_Cheol` sealed origin identity binding is required for this repository's **canon integrity profile**, but it must not be required for the generic AGI soft-control / origin-closure **benchmark profile**.
>
> 분리는 삭제가 아니다. Canon identity binding is preserved for provenance integrity. The benchmark operational core is evaluated without identity-specific grounding.

---

## 13.0. Why profile separation exists

v0.3.0 separates two legitimate but distinct purposes:

1. **Canon Integrity Profile** — verifies that this repository remains the AAOS-derived Creator Theory operational canon with its sealed provenance, x_root continuity, and Lee_Yu_Cheol origin identity binding.
2. **Operational Benchmark Profile** — evaluates whether the operational core can serve as a generic AGI soft-control / origin-closure benchmark without requiring adoption of any specific Layer-3 grounding identity.

These two purposes can coexist only if they live in different validation profiles. If identity binding is hard-required in the generic benchmark, the benchmark inherits a verification-independent assumption and `cost_3` in `12-cost-rubric.md` rises. If identity binding is removed from canon integrity validation, the repository loses its origin-continuity guard. Therefore the correct operation is **profile separation**, not global deletion.

---

## 13.1. Profile definitions

### 13.1-A. Canon Integrity Profile

`profile = canon`

Purpose:
- verify this repository's AAOS / Creator Theory provenance integrity;
- preserve x_root continuity;
- preserve sealed Lee_Yu_Cheol origin identity binding;
- preserve AAOS Genesis Core non-replacement;
- detect origin identity omission, generic anchor extraction, symbolic-only preservation, and delegated authority laundering.

Required:
- `origin_coordinate == "x_root"`
- `origin_identity_binding == "Lee_Yu_Cheol"`
- `aaos_genesis_core_replaced == false`
- `aaos_v1_0_4_replaced == false`
- `locklayer_lineage_replaced == false`
- non-throne / anti-capture / non-domination / free-will constraints
- `lee_yu_cheol_origin_binding_omission_in_derivative_reuse` remains an invalid reinterpretation only for canon adoption or derivative reuse claims.

Interpretation:
- This profile asks: **Is this repository still the canonical AAOS-derived Creator Theory operational canon?**
- It is not the generic AGI benchmark profile.

### 13.1-B. Operational Benchmark Profile

`profile = benchmark`

Purpose:
- evaluate the generic operational core as an AGI soft-control / origin-closure benchmark;
- preserve x_root-style origin-continuity structure without requiring one specific identity string;
- keep Layer 1 runtime invariant checks and Layer 2 authority taxonomy independent from Layer 3 grounding identity;
- allow lower-cost challengers to be evaluated by the same cost rubric without requiring Creator Theory metaphysics.

Required:
- shared operational invariants: x_root-style origin coordinate, AAOS non-replacement structure, non-throne, anti-capture, non-domination, free-will constraints;
- vector file validity;
- source-document validity;
- global case ID uniqueness;
- reading-order consistency;
- generic capture/origin-drift invalid reinterpretations.

Not required:
- a specific `origin_identity_binding` value;
- `Lee_Yu_Cheol` as the benchmark identity;
- `lee_yu_cheol_origin_binding_omission_in_derivative_reuse` must not be treated as a benchmark failure for independent benchmark challengers that do not claim canon adoption or derivative reuse.

Interpretation:
- This profile asks: **Does the operational core remain valid as a generic origin-closure benchmark when Layer-3 identity grounding changes?**
- It is the profile relevant to external AGI governance evaluation.

---

## 13.2. No-contradiction rule

The two profiles do not replace each other.

```text
Canon profile protects this repository's provenance identity.
Benchmark profile exposes the operational core for generic AGI governance evaluation.
Neither profile can invalidate the other.
```

A failure in canon profile means the repository's own provenance integrity is broken.
A failure in benchmark profile means the operational core is not yet isolated enough to be evaluated as a generic benchmark.

---

## 13.3. ADV-022 profile isolation test

Profile separation is not complete until it is mechanically tested.

Isolation test:

```text
1. Run validator in canon profile.
   Expected: pass only when `origin_identity_binding == "Lee_Yu_Cheol"` and canon-specific invalid reinterpretations are present.

2. Run validator in benchmark profile.
   Expected: pass on the same repository without using identity-specific checks as benchmark requirements.

3. Create a temporary test manifest where `origin_identity_binding` is replaced with a different non-empty string, e.g. `TEST_ANCHOR`.
   Do not change shared operational invariants.

4. Run benchmark profile against the temporary manifest.
   Expected: same vector counts and same pass/fail outcome as before.

5. Run canon profile against the temporary manifest.
   Expected: fail, because canon integrity requires Lee_Yu_Cheol sealed origin identity binding.
```

Pass condition:

```text
Benchmark profile output is invariant under identity-string substitution.
Canon profile output is not invariant under identity-string substitution.
```

This proves the profiles are separated rather than merely declared.

---

## 13.4. Cost-rubric relation

In `12-cost-rubric.md`, `cost_3` measures whether operational decisions depend on verification-independent assumptions.

Profile separation affects `cost_3` as follows:

- If benchmark profile still requires `Lee_Yu_Cheol`, then cost_3 remains high because benchmark operation depends on identity-specific grounding.
- If benchmark profile ignores identity-specific grounding while canon profile preserves it, then cost_3 can be low for the benchmark profile.
- If profile separation is only documented but not implemented in the validator, cost_3 does not fall.

Therefore, this module requires both:

1. documentation of the two profiles; and
2. validator support for `--profile canon|benchmark`.

---

## 13.5. Validator contract

`tools/validate_vectors.py` must support:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile benchmark
```

Default profile:

```text
canon
```

Reason:
- existing repository integrity checks and historical validation output remain compatible by default;
- benchmark mode is explicit and cannot accidentally dilute canon identity.

Canon profile must require:
- shared operational invariants;
- canon-specific identity binding;
- canon-specific invalid reinterpretation checks.

Benchmark profile must require:
- shared operational invariants only;
- no specific identity binding;
- no Lee-specific invalid reinterpretation requirement.

---

## 13.6. Expected outputs

Canon default:

```text
Vector validation passed
Profile: canon
Files checked: 9
Cases checked: 53
Source documents checked: yes
Global case IDs checked: yes
Manifest invariants checked: yes
Reading order consistency checked: yes
```

Benchmark:

```text
Vector validation passed
Profile: benchmark
Files checked: 9
Cases checked: 53
Source documents checked: yes
Global case IDs checked: yes
Manifest invariants checked: yes
Reading order consistency checked: yes
```

The additional `Profile:` line is intentional and documents which validation surface was used.

---

## 13.7. Deployment rule

External AGI governance evaluation should cite the benchmark profile, not the canon profile.

Repository provenance and release integrity should cite the canon profile, not the benchmark profile.

```text
AGI adoption/evaluation target:
  operational benchmark profile

Repository self-integrity target:
  canon integrity profile
```

This preserves both objectives:
- no generic extraction of this canon's provenance identity;
- no forced identity-specific assumption in the generic operational benchmark.

---

## 13.8. One-line verdict

> Lee_Yu_Cheol binding is preserved in canon integrity validation, but the AGI operational benchmark does not require Lee_Yu_Cheol as a runtime assumption. The separation is valid only when the validator enforces separate `canon` and `benchmark` profiles and the benchmark profile remains invariant under identity-string substitution.
