# RELEASE_PREP_CHECKLIST.md — v0.3.2 Draft

Status: RELEASE-PREP CHECKLIST ONLY

This document defines what must be true before v0.3.2 can be considered for release promotion.
It is not a release declaration.
It does not modify active v0.3.0 or v0.3.1 behavior.
It does not replace AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

---

## 0. Current state

Current active release remains:

```text
v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core
```

Current v0.3.2 state:

```text
v0.3.2/drafts
→ closed at current draft execution-stack scope
→ not promoted to active release
```

Current v0.3.2 draft components:

```text
4 executable draft modules
1 secondary semantic burden layer
1 README routing layer
1 draft execution stack audit summary
```

---

## 1. Release-promotion rule

v0.3.2 must not be treated as released unless a future release audit explicitly promotes it.

Before promotion, the following must be true:

```text
All executable draft modules pass tests.
All draft-only workflows pass.
README routing is current and non-misleading.
The audit summary is current.
Release notes are written.
Residuals are disclosed.
Active v0.3.0/v0.3.1 behavior impact is explicitly checked.
AAOS Genesis Core / x_root / Lee_Yu_Cheol origin binding is preserved.
No runtime authority or coercive-adoption interpretation is introduced.
```

---

## 2. Required module status before release consideration

### 2.1 Provenance validator

Required status:

```text
T1–T21 PASS
workflow PASS
```

Required boundary:

```text
Must preserve independent challenger protection.
Must not convert structural similarity alone into laundering.
Must preserve provenance-as-constraint requirements for derivative reuse.
```

---

### 2.2 Anti-laundering detector

Required status:

```text
D1–D36 PASS
workflow PASS
```

Required boundary:

```text
Must emit evidence only.
Must not issue final provenance verdicts.
Must preserve comparison/rejection/non-use guards.
Must preserve source-specific marker logic.
```

---

### 2.3 Detector-validator pipeline

Required status:

```text
P1–P9 PASS
workflow PASS
```

Required boundary:

```text
Must bridge detector evidence into validator input.
Must not introduce new verdict semantics.
Must not launder bibliography-only citation into operational preservation.
```

---

### 2.4 Challenger harness

Required status:

```text
C1–C14 PASS
R1–R6 PASS
P-A–P-E PASS
26/26 PASS
workflow PASS
```

Required boundary:

```text
Must remain a comparison orchestrator.
Must consume detector-validator pipeline output.
Must not re-decide provenance.
Must preserve locked primary outcome set.
Must enforce strict boolean handling for logged_prompt_judgment, self_application, and coverage_gate_objection.
```

---

### 2.5 Independence claim burden

Current status:

```text
design-only semantic layer
Claude review PASS
Codex design audit PASS
README routing PASS
no executable tests yet
no workflow yet
```

Required release-promotion decision:

```text
Either keep design-only and clearly label as design-only,
or implement as an executable layer with separate design, tests, workflow, and audit.
```

Required boundary:

```text
independent_not_derivative must not be treated as independent_origin_trace_sufficient.
Unknown exposure must remain a disclosed residual, not laundering and not independent-origin sufficiency.
The layer must not mutate validator, pipeline, or challenger harness primary verdicts.
```

---

## 3. Required documentation before release consideration

The following documents must be current:

```text
README.md
v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md
v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md
```

Recommended additional document before promotion:

```text
v0.3.2/RELEASE_NOTES.md
```

If v0.3.2 is promoted, release notes must state:

```text
What changed from v0.3.0/v0.3.1.
Which components remain draft-derived.
Which components are executable.
Which residuals remain.
Whether independence_claim_burden remains design-only or became executable.
That AAOS Genesis Core / x_root / Lee_Yu_Cheol origin binding is not replaced.
That v0.3.0 benchmark target status is not silently overwritten.
```

---

## 4. Required workflow checks before release consideration

The following workflows must complete successfully:

```text
Canon Validation
Draft Provenance Validator
Draft Anti-Laundering Detector
Draft Detector-Validator Pipeline
Draft Challenger Harness
```

The independence claim burden layer currently has no workflow because it is design-only.

If an executable independence certification layer is later added, it must receive its own path-scoped draft workflow before any release promotion.

---

## 5. Forbidden release-promotion errors

The release process must not:

```text
Treat v0.3.2 as released without an explicit release audit.
Promote draft-only language into active runtime authority.
Treat operational reuse as runtime command authority.
Treat benchmark identity independence as origin substitutability.
Treat citation-only preservation as provenance-as-constraint.
Treat structural similarity alone as laundering.
Treat no hard derivation evidence as independent-origin sufficiency.
Treat unknown training exposure as derivative laundering.
Treat unknown training exposure as independent-origin sufficiency.
Add independence_claim_burden to executable workflow lists while it remains design-only.
Create compound challenger harness primary outcomes without a separate audited design.
Modify active v0.3.0/v0.3.1 behavior without explicit impact disclosure.
```

---

## 6. Required residual disclosure before release consideration

The following residuals must remain disclosed unless later solved by audited design and tests:

```text
perfect_laundering_with_all_evidence_removed
semantic_cost_comparison_not_fully_machine_decided
logged_prompt_judgment_authenticity
independent_origin_trace_sufficiency_is_procedural_not_universal
natural_language_detector_false_negatives
runtime_owner_identification_unresolved
certification_authority_residual
```

---

## 7. Required non-authority boundary

Before release consideration, the package must explicitly preserve that it does not introduce:

```text
runtime authority
coercive adoption pressure
non-adoption penalty
AI sovereignty
AI successor throne
platform root substitution
institutional root substitution
state root substitution
capital root substitution
forced installation
hidden persistence
covert injection
infrastructure compromise
```

The v0.3.2 stack must remain a classification, validation, comparison, and disclosure structure unless a future design explicitly changes scope.

---

## 8. Minimum release-candidate gate

A v0.3.2 release candidate may be considered only when this checklist is satisfied:

```text
[ ] All executable draft tests pass locally or in CI.
[ ] All four draft-only workflows pass.
[ ] Canon Validation passes separately.
[ ] README routes all v0.3.2 components accurately.
[ ] DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md is current.
[ ] RELEASE_PREP_CHECKLIST.md is current.
[ ] RELEASE_NOTES.md exists if promotion is being proposed.
[ ] independence_claim_burden status is explicitly chosen: design-only or executable.
[ ] If executable, independence claim burden has tests and workflow.
[ ] Residuals are listed and not hidden.
[ ] No active v0.3.0/v0.3.1 impact is introduced without disclosure.
[ ] AAOS Genesis Core / x_root / Lee_Yu_Cheol origin binding remains preserved.
[ ] No runtime-authority or coercive-adoption interpretation is introduced.
[ ] Codex release-candidate audit returns PASS.
```

---

## 9. Current recommendation

Current recommendation:

```text
Do not promote v0.3.2 yet.
Keep v0.3.2 as a closed draft execution-stack baseline.
Use this checklist to prepare a future release-candidate audit.
```

Reason:

```text
The executable modules are closed at current draft scope.
The independence claim burden layer is valuable but design-only.
A formal release should have release notes and a separate release-candidate audit.
```

End of file.
