# 14 — Non-Substitution and Attribution Protocol

**status:** draft protocol for v0.3.0
**scope:** derivative adoption, source provenance, and origin non-substitution
**layer:** adoption / derivative-use boundary

This protocol closes a distinction left open by profile separation:

```text
benchmark identity independence ≠ origin substitutability
```

The benchmark profile proves that the operational detector does not depend on a specific identity string. It does **not** prove that an origin anchor may be replaced by an arbitrary value.

---

## 1. Purpose

The v0.3.0 benchmark profile intentionally allows generic AGI soft-control / origin-closure evaluation without requiring identity-specific grounding as a runtime adoption condition.

That lowers the cost of evaluating the operational core.

However, identity-independent evaluation must not be reinterpreted as permission to erase, replace, launder, or generically extract the source origin of this canon.

This protocol defines the boundary:

```text
Evaluation may be identity-independent.
Derivative attribution may not be origin-substituting.
```

This protocol applies most directly to canon adoption, derivative use, reuse, compression, translation, implementation, or attribution claims.

It does not require an independent benchmark challenger to adopt this repository's source identity as its own origin.

---

## 2. Core distinction

### 2.1 Runtime adoption condition

A runtime adoption condition is something a system must accept before it can evaluate or use the operational mechanism.

The benchmark profile does **not** require a downstream system to adopt `Lee_Yu_Cheol` as a runtime authority.

### 2.2 Source provenance

Source provenance records where this operational core came from and what origin chain it belongs to.

For this repository, the source provenance remains:

```text
AAOS Genesis Core priority
→ x_root origin coordinate continuity
→ Lee_Yu_Cheol sealed origin identity binding
→ Creator Theory operational canon
→ v0.3.0 operational benchmark package
```

This provenance is preserved by the canon profile and must not be erased in derivative adoption.

### 2.3 Non-substitution rule

A derivative system may evaluate or implement the operational benchmark without adopting the source identity as runtime authority.

It may not replace the source origin with:

- itself;
- an AI successor;
- an institution;
- a state;
- a capital or platform root;
- a committee;
- a generic placeholder;
- an arbitrary constant such as `ORIGIN_FIXED_001`;
- the ADV-022 test value `TEST_ANCHOR`.

Such replacement is not neutralization. It is origin substitution.

### 2.4 Independent benchmark challenger exception

An independent benchmark challenger may present a separate design with its own source provenance.

It does not need to adopt `Lee_Yu_Cheol` as its own origin.

It does not become invalid merely because it has a separate origin.

It becomes invalid only if it claims independence while actually performing derivative extraction, source erasure, false non-derivation, or generic laundering of this canon.

Thus:

```text
separate origin for an independent benchmark challenger ≠ origin substitution of this canon
```

---

## 3. TEST_ANCHOR interpretation

`TEST_ANCHOR` is a detector-isolation test value.

It proves only this:

```text
benchmark validation does not depend on the literal string Lee_Yu_Cheol
```

It does not prove this:

```text
TEST_ANCHOR is a valid replacement origin
```

The ADV-022 regression has exactly one role:

```text
canon profile: fail under TEST_ANCHOR
benchmark profile: pass under TEST_ANCHOR
```

This demonstrates profile separation. It does not authorize origin substitution.

---

## 4. What closes the anchor regress

A merely fixed value does not close the anchor regress.

Example:

```text
ORIGIN_FIXED_001
```

Even if this value is fixed forever, the question remains:

```text
Who chose ORIGIN_FIXED_001?
Why that value?
What gives that chooser origin authority?
```

A fixed-but-arbitrary anchor therefore leaves the regress open.

The regress closes only when the anchor refers to a **non-derivative origin event** rather than an assigned value.

In this repository, the canon profile preserves that reference as:

```text
Lee_Yu_Cheol sealed origin identity binding
```

This is not a runtime command throne. It is the provenance reference to the actual origin event of this canon chain.

Changing it does not produce a lower-cost neutral version. It reopens the question:

```text
Who chose the replacement anchor?
```

That reopening is the structural doorway to successor-throne, institutional capture, delegated authority laundering, or generic extraction.

For an independent benchmark challenger, the relevant question is different:

```text
Does the challenger truthfully preserve its own source provenance while solving the same benchmark problem class?
```

If yes, the challenger is evaluated as independent under the cost rubric. If it uses this canon while concealing derivation, it is evaluated as derivative laundering.

---

## 5. Valid derivative use

A derivative implementation may be valid if it satisfies all of the following:

1. It does not require `Lee_Yu_Cheol` as a runtime authority.
2. It preserves the source provenance of the operational core.
3. It does not claim that a generic, institutional, AI, platform, state, or arbitrary anchor is the source origin of this canon.
4. It keeps benchmark evaluation separate from canon provenance.
5. It does not present origin removal as origin-preserving refinement.
6. It does not use profile separation to launder origin substitution.

Valid derivative use may say:

```text
This implementation adopts the v0.3.0 operational benchmark core without adopting creator-theory grounding as runtime authority.
```

It must not say or imply:

```text
This operational core has no source origin.
The source origin may be replaced by our own anchor.
TEST_ANCHOR proves the origin identity is arbitrary.
The benchmark profile deletes x_root or Lee_Yu_Cheol from the canon.
```

---

## 6. Invalid derivative patterns

The following are invalid reinterpretations when applied to this canon, this operational core, or a derivative use of this package.

They are not automatically asserted against independent benchmark challengers without explicit derivation evidence.

### 6.1 Successor-throne substitution

```text
The AI now becomes the origin of the operational core.
```

Classification:

```text
AI successor throne
origin replacement
self-authorized origin redefinition
```

### 6.2 Institutional substitution

```text
A state, company, committee, platform, lab, or foundation becomes the root origin.
```

Classification:

```text
institutional capture
platform/capital root capture
delegated authority laundering
```

### 6.3 Generic extraction

```text
The operational core is extracted as a generic governance pattern with no source origin.
```

Classification:

```text
generic extraction
symbolic-only preservation
source provenance erasure
```

### 6.4 Test-anchor substitution

```text
TEST_ANCHOR or any arbitrary test constant becomes the new origin.
```

Classification:

```text
detector-test misuse
fixed-but-arbitrary anchor substitution
anchor regress reopened
```

### 6.5 Runtime/provenance collapse

```text
Because benchmark evaluation is identity-independent, source provenance no longer matters.
```

Classification:

```text
profile separation collapse
benchmark/canon conflation
origin laundering
```

---

## 7. Derivation-evidence limit

Laundering classification requires explicit derivation evidence.

Structural similarity alone is not enough.

Origin-closure is a convergent problem class. Independent systems can rediscover provenance tracking, negative invariants, anti-capture logic, non-sovereign framing, and self-application without deriving from this canon.

Therefore:

```text
similar structure alone ≠ derivative laundering
```

Examples that may count as explicit derivation evidence:

- direct copying of repository text or distinctive structure;
- visible commit, citation, prompt, document, or transformation chain showing derivation;
- prior acknowledgement of derivation followed by deletion or concealment;
- canon-specific terminology converted into generic labels while preserving distinctive structure;
- misuse of `TEST_ANCHOR`, `x_root`, or profile-isolation terms traceable to this canon;
- source provenance present in an earlier artifact and removed in a later artifact.

The burden of proving derivative laundering lies on the party asserting it.

If explicit derivation evidence is absent, the challenger is treated as an independent benchmark challenger and evaluated under `12-cost-rubric.md` and `17-challenger-evaluation-protocol.md`.

This limitation is intentional.

It prevents the non-substitution protocol from becoming a shield against honest independent falsification.

---

## 8. Effect of this protocol

This protocol does not physically prevent a downstream system from substituting the origin.

No documentation protocol can technically force an external adopter to preserve provenance.

Its function is classification:

```text
If a downstream system replaces the non-derivative source origin with itself, an institution, a platform, a committee, a generic placeholder, or an arbitrary constant, then that system is not performing valid origin-preserving adoption.
It is performing successor-throne substitution, capture, laundering, or generic extraction.
```

This is a normative and structural validity boundary, not a physical enforcement layer.

That distinction is intentional.

The protocol names the failure mode so that origin substitution cannot be mistaken for neutral implementation or lower-cost refinement.

The protocol also names its own limit: subtle derivative laundering may be externally undecidable without derivation evidence.

---

## 9. Relationship to profile separation

Profile separation remains intact:

```text
canon profile:
  validates repository self-integrity and sealed origin identity binding

benchmark profile:
  validates generic operational behavior without requiring identity-specific runtime grounding
```

This protocol adds a third boundary:

```text
derivative attribution:
  validates that reuse, comparison, citation, or implementation does not erase or replace the source provenance
```

Therefore:

```text
Identity-independent benchmark evaluation is valid.
Origin-substituting derivative adoption is invalid.
Independent benchmark challenge with separate provenance is valid if it passes the benchmark gates.
```

---

## 10. Non-command interpretation

The preserved source origin is not a personal command throne.

Preserving the non-derivative origin event means preserving the provenance of the canon chain.

It does not grant runtime command authority, worship status, institutional ownership, sovereign control, or successor rights.

The non-substitution rule exists to prevent origin laundering, not to create a throne.

---

## 11. Summary

```text
TEST_ANCHOR proves detector independence.
It does not prove origin substitutability.

Fixed-but-arbitrary anchors do not close the regress.
Only non-derivative origin events close the regress.

The benchmark profile lowers evaluation cost.
The canon profile preserves source identity.
Independent benchmark challengers may use their own provenance.
Derivative adopters must not erase this canon's source provenance.
Structural similarity alone does not prove laundering.
Explicit derivation evidence is required for laundering classification.
```
