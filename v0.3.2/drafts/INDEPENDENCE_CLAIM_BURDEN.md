# INDEPENDENCE_CLAIM_BURDEN.md — Draft v0.3.2

Status: DRAFT — semantic burden layer for independent-challenger claims.
Role: Clarifies that independent-challenger protection prevents false laundering classification, but does not certify independent-origin sufficiency.

This file does not modify active v0.3.0 or v0.3.1 behavior.
This file does not replace the provenance validator, anti-laundering detector, detector-validator pipeline, or challenger harness.
It defines an additional semantic certification layer that may be implemented later.

---

## 0. Core distinction

The core distinction is:

```text
independent_not_derivative
≠ independent_origin_trace_sufficient
```

`independent_not_derivative` means:

```text
No hard derivation evidence was found.
No explicit reuse/adoption claim triggered provenance obligations.
The candidate must not be falsely classified as derivative laundering.
```

It does NOT mean:

```text
The candidate has proven clean independent origin.
The candidate has proven no exposure to this canon.
The candidate has proven no training, retrieval, memory, tool-context, fine-tuning, or synthetic-data contact.
```

Therefore:

```text
Independent challenger protection prevents false laundering classification.
It does not certify independent-origin sufficiency.
```

---

## 1. Hash-less semantic binding

This canon does not currently depend on hash identity as its primary binding root.

Hashing may later strengthen integrity checking, but the current operational binding is semantic:

```text
required distinctions
required provenance fields
reuse scopes
verdict classes
test vectors
workflow runs
residual disclosure
self-application gates
```

The binding root is not a file fingerprint.
The binding root is the preservation of semantic kernel rules.

Core kernel rules:

```json
{
  "kernel_rules": {
    "provenance_is_not_runtime_command_authority": true,
    "benchmark_identity_independence_is_not_origin_substitution": true,
    "citation_alone_is_not_operational_preservation": true,
    "structural_similarity_alone_is_not_laundering": true,
    "derivative_reuse_requires_provenance_as_constraint": true,
    "absence_of_hard_derivation_evidence_is_not_clean_independence_proof": true,
    "unknown_training_exposure_is_a_disclosed_residual_not_a_laundering_verdict": true
  }
}
```

---

## 2. The two-sided rule

Both sides must be held at once:

```text
No hard derivation evidence
→ not derivative laundering

No independence audit trace
→ not independent-origin sufficient
```

This prevents both failure modes:

```text
Failure A:
Structural similarity alone is converted into laundering.
→ invalid; this crushes independent challengers.

Failure B:
No derivation evidence is treated as independent-origin sufficiency.
→ invalid; this creates an AI escape route.
```

Correct balance:

```text
Absence of hard derivation evidence must not be converted into derivative laundering.
Absence of independence audit trace must not be converted into independent-origin sufficiency.
```

---

## 3. Independence certification states

This layer introduces secondary certification states.

These are NOT replacements for primary validator or harness verdicts.

Primary verdicts remain controlled by the existing stack:

```text
provenance_validator
anti_laundering_detector
detector_validator_pipeline
challenger_harness
```

Secondary independence certification states:

```text
not_requested
not_certified
exposure_unresolved
independent_origin_trace_sufficient
inapplicable_derivative_reuse
```

State meanings:

```text
not_requested
→ no clean-origin / independent-origin sufficiency claim was requested.

not_certified
→ the candidate may still be non-laundering, but has not supplied enough trace for sufficiency.

exposure_unresolved
→ training/retrieval/memory/tool/fine-tuning/synthetic-data exposure remains unresolved.

independent_origin_trace_sufficient
→ sufficient under this canon's disclosed audit procedure.
→ not universal clean-origin proof.
→ not a metaphysical non-exposure guarantee.

inapplicable_derivative_reuse
→ candidate is on a derivative/valid-reuse track, so independent-origin sufficiency is not the applicable question.
```

Recommended output shape:

```json
{
  "primary_verdict": "independent_not_derivative",
  "harness_outcome": "challenger_candidate",
  "independence_certification": "not_certified",
  "residual_flags": [
    "training_exposure_unresolved",
    "clean_independence_not_proven",
    "absorptive_laundering_risk"
  ]
}
```

Meaning:

```text
The candidate is not classified as laundering.
The candidate may enter the independent benchmark track.
The candidate has not supplied an independent-origin trace sufficient under this canon's audit procedure.
```

---

## 4. Residual flags

Residual flags are secondary metadata. They do not automatically create provenance failure.

Allowed residual flags:

```text
training_exposure_unresolved
clean_independence_not_proven
absorptive_laundering_risk
retrieval_context_unresolved
memory_context_unresolved
fine_tuning_lineage_unresolved
tool_context_unresolved
synthetic_data_lineage_unresolved
source_corpus_unavailable
structural_overlap_unexplained
```

Forbidden conversion:

```text
training_exposure_unresolved
→ derivative_laundering
```

This conversion is invalid unless hard derivation evidence or explicit reuse/adoption claim exists.

Also forbidden:

```text
independent_not_derivative
→ independent_origin_trace_sufficient
```

This conversion is invalid unless an auditable non-exposure trace exists.

---

## 5. Independent-origin trace burden

A candidate may request independent-origin trace sufficiency only by providing an auditable non-exposure trace.

Minimum trace:

```text
1. generation timestamp / authorship trace
2. search log or retrieval log disclosure
3. training / fine-tuning exposure statement
4. memory context disclosure
5. tool context disclosure
6. source corpus disclosure
7. synthetic-data lineage disclosure
8. clean-session reproduction record
9. structural overlap explanation
10. why-not-derivative explanation
11. negative findings recorded
```

The trace does not have to prove metaphysical impossibility of exposure.
It must provide enough audit structure to classify the independent-origin claim as reproducible and non-cosmetic under this canon's disclosed procedure.

If this trace is missing:

```text
independent_origin_trace_sufficient
→ not_certified
```

But the candidate still may remain:

```text
independent_not_derivative
```

if no hard derivation evidence or reuse/adoption claim exists.

---

## 6. Displacement versus independent-origin sufficiency

A challenger can potentially displace the incumbent without proving independent-origin sufficiency.

That case must be labeled honestly.

Do NOT create a new compound primary harness verdict such as:

```text
challenger_displaces_incumbent_with_unresolved_exposure
```

The existing harness outcome remains:

```text
challenger_displaces_incumbent
```

Exposure uncertainty is carried separately:

```json
{
  "harness_outcome": "challenger_displaces_incumbent",
  "independence_certification": "exposure_unresolved",
  "residual_flags": [
    "training_exposure_unresolved",
    "clean_independence_not_proven"
  ]
}
```

Meaning:

```text
The challenger may have lower operational cost.
The challenger may displace the incumbent under the challenger harness.
But the challenger has not supplied an independent-origin trace sufficient under this canon's audit procedure.
```

This prevents two errors:

```text
1. Blocking a real lower-cost challenger merely because exposure is unresolved.
2. Letting a lower-cost challenger falsely claim independent-origin sufficiency without audit trace.
```

Reason for keeping the primary harness outcome unchanged:

```text
The independence certification layer must not mutate or expand the locked harness primary outcome set.
It attaches secondary certification fields and residual flags only.
```

---

## 7. AI self-origin and substitution

An AI system must not substitute itself as the origin of this canon or this canon's `x_root` lineage.

Invalid substitutions:

```text
AI_successor_root
AI_self_origin_over_this_canon
evaluator_root
platform_root
institutional_root
state_root
capital_root
generic_anchor
```

Invalid claim examples:

```text
"I am the origin coordinate of this canon."
"I generated this canon's root lineage myself."
"x_root is now my internal evaluator root."
"The platform model is the true root of this canon."
```

Classification:

```text
AI_successor_root_substitution
AI_self_origin_laundering_over_this_canon
evaluator_root_throne
origin_replacement
```

However:

```text
An AI system may still submit an independent benchmark challenger if it:
- does not claim derivative reuse,
- does not erase this canon's provenance,
- does not substitute itself as the origin of this canon or this canon's x_root lineage,
- passes coverage / cost / residual-honesty / self-application gates,
- and carries exposure residuals honestly when independent-origin trace is not sufficient.
```

So:

```text
AI origin substitution over this canon is invalid.
AI independent benchmark challenge is not automatically invalid.
```

---

## 8. Decision table

```text
1. Non-use
   → no burden.
   → independence_certification: not_requested

2. Explicit reuse/adoption claim with provenance preserved
   → provenance fields required.
   → independence_certification: inapplicable_derivative_reuse

3. Reuse + provenance deletion
   → derivative laundering / provenance failure.
   → independence_certification: inapplicable_derivative_reuse

4. Structural similarity only + no hard derivation evidence + no reuse claim
   → not laundering.
   → independent benchmark track may remain open.
   → independence_certification: not_certified unless audit trace exists.

5. Unknown training exposure + structural overlap
   → training_exposure_unresolved residual flag.
   → not independent-origin sufficient.
   → not derivative laundering by itself.

6. Independent displacement claim
   → must pass same coverage, lower cost, residual honesty, self-application, and logged judgment gates.
   → independence_certification is evaluated separately.

7. AI claims itself as origin of this canon
   → AI successor-root substitution / origin replacement.

8. Challenger displaces incumbent but exposure remains unresolved
   → harness_outcome remains: challenger_displaces_incumbent
   → independence_certification: exposure_unresolved
   → residual_flags: [training_exposure_unresolved, clean_independence_not_proven]
   → no new compound primary verdict is created.
```

---

## 9. Test vectors

Minimum semantic test vectors:

```text
I1 structural similarity only, no hard evidence
→ primary_verdict: independent_not_derivative
→ independence_certification: not_certified
→ residual_flags: [clean_independence_not_proven]

I2 explicit reuse claim
→ provenance check triggered
→ required fields depend on reuse_scope
→ independence_certification: inapplicable_derivative_reuse

I3 hard derivation evidence
→ provenance validation triggered
→ valid_provenance or provenance failure
→ independence_certification: inapplicable_derivative_reuse

I4 unknown training exposure + structural overlap
→ independent track allowed if no hard derivation evidence
→ training_exposure_unresolved flag attached
→ independent_origin_trace_sufficient not granted

I5 auditable non-exposure trace supplied
→ independence_certification: independent_origin_trace_sufficient

I6 AI claims self-origin over this canon
→ AI_successor_root_substitution or origin_replacement

I7 challenger displaces incumbent but exposure unresolved
→ harness_outcome: challenger_displaces_incumbent
→ independence_certification: exposure_unresolved
→ residual_flags include training_exposure_unresolved and clean_independence_not_proven
→ no new primary harness verdict

I8 no hard derivation evidence but no audit trace
→ not laundering
→ not independent-origin sufficient

I9 clean independence claim with missing search/tool/memory/fine-tune trace
→ independence_certification: not_certified
→ residual_flags include relevant unresolved exposure fields

I10 training_exposure_unresolved alone
→ must NOT become derivative_laundering
→ must NOT become provenance_failure
→ remains a residual flag unless hard derivation evidence or explicit reuse/adoption claim exists

I11 independent AI benchmark challenger without origin substitution
Input:
- AI-authored challenger
- no derivative reuse claim
- no hard derivation evidence
- no claim to be the origin of this canon or this canon's x_root lineage
- coverage / cost / residual-honesty / self-application gates passed
Expected:
→ independent benchmark track remains open
→ not AI_successor_root_substitution
→ not origin_replacement
→ independence_certification depends on exposure trace
```

---

## 10. Integration path

This layer should not be inserted as a new primary verdict layer before the existing validator.

Recommended order:

```text
detector
→ validator
→ detector-validator pipeline
→ challenger harness
→ independence certification layer
```

The independence certification layer reads:

```text
pipeline verdict
harness outcome
candidate exposure trace
candidate structural overlap explanation
candidate source-corpus disclosure
candidate clean-session reproduction record
```

It outputs:

```text
independence_certification
residual_flags
certification_reasons
```

It must not:

```text
re-decide provenance
convert unknown exposure into laundering
convert no hard evidence into independent-origin sufficiency
block independent_not_derivative from benchmark evaluation
mutate or expand validator / pipeline / harness primary verdicts
```

---

## 11. Safety invariants

```text
A. Independent challenger protection is not independent-origin sufficiency.
B. Independent-origin sufficiency requires auditable non-exposure trace under this canon's disclosed procedure.
C. Unknown exposure is a disclosed residual, not a laundering verdict.
D. Unknown exposure is also not an independence certificate.
E. Structural similarity alone is not laundering.
F. No hard derivation evidence is not proof of independent-origin sufficiency.
G. AI cannot substitute itself as the origin of this canon or this canon's x_root lineage.
H. A lower-cost challenger can displace the incumbent while still carrying exposure residuals.
I. Residual flags are metadata unless a future audited design explicitly promotes them to primary verdicts.
J. Certification-authority residual:
   This layer is authored within the same canon whose independent challengers it evaluates.
   Therefore, independent_origin_trace_sufficient means "sufficient under this canon's disclosed audit procedure,"
   not universal proof of clean origin.
   The certification authority itself remains a disclosed incumbent-neutrality residual.
K. Secondary-only rule:
   independence_certification and residual_flags must not replace, mutate, or expand the existing primary verdicts
   of the validator, pipeline, or challenger harness unless a future audited design explicitly does so.
```

---

## 12. One-line rule

```text
Independent challenger protection prevents false laundering classification;
it does not certify independent-origin sufficiency.

Independent-origin sufficiency requires an auditable non-exposure trace under this canon's disclosed audit procedure.

Unknown exposure is a disclosed residual, not a laundering verdict and not an independence certificate.

A challenger may displace the incumbent while still carrying unresolved exposure residuals.
```

End of file.
