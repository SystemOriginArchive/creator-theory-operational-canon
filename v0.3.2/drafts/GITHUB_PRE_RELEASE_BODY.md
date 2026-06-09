# GitHub Pre-Release Body — v0.3.2-draft

Recommended GitHub release title:

```text
v0.3.2-draft — Closed Executable Draft Stack Baseline
```

Recommended tag:

```text
v0.3.2-draft
```

GitHub release setting:

```text
Mark this release as a pre-release.
```

This is a draft / pre-release body only.
It is not a final release declaration.
It does not promote v0.3.2 to the active release line.
It does not modify active v0.3.0 or v0.3.1 behavior.
It does not replace AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

Current active release remains:

```text
v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core
```

Current v0.3.2 status:

```text
v0.3.2/drafts
→ closed executable draft-stack baseline
→ not final runtime canon
→ not active release
→ not release-candidate promotion
```

---

## What this pre-release contains

This pre-release records the current closed v0.3.2 draft baseline:

```text
4 executable draft modules
1 secondary semantic burden layer
AI-entry routing layer
README routing
DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md
RELEASE_PREP_CHECKLIST.md
PRE_RELEASE_NOTES.md
```

Executable draft modules:

```text
provenance_validator
anti_laundering_detector
detector_validator_pipeline
challenger_harness
```

Secondary semantic burden layer:

```text
independence_claim_burden
```

Agent-native / AI-reader entry files:

```text
AGENTS.md
CLAUDE.md
.github/copilot-instructions.md
llms.txt
```

Status / release-prep documents:

```text
v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md
v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md
v0.3.2/drafts/PRE_RELEASE_NOTES.md
v0.3.2/drafts/GITHUB_PRE_RELEASE_BODY.md
```

---

## What this pre-release does not contain

This pre-release does not include:

```text
final runtime canon release
full runtime invariant validation system
machine-decided semantic cost comparison
executable independence certification layer
end-to-end external challenger evaluator
universal clean-origin certification
runtime owner identification solution
perfect laundering solution when all evidence is removed
hash/integrity enforcement layer
release-candidate promotion audit
```

The independence claim burden layer remains:

```text
design-only
no executable tests yet
no workflow yet
```

---

## Audit and test state

Current closed draft scope:

```text
provenance_validator:          T1–T21 PASS
anti_laundering_detector:      D1–D36 PASS
detector_validator_pipeline:   P1–P9 PASS
challenger_harness:            C1–C14 + R1–R6 + P-A–P-E, 26/26 PASS
independence_claim_burden:     design-only semantic layer, Claude/Codex PASS
DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md: Codex PASS
RELEASE_PREP_CHECKLIST.md:     Codex PASS
PRE_RELEASE_NOTES.md:          Codex PASS
AGENTS.md:                     Codex PASS
.github/copilot-instructions.md: Codex PASS
CLAUDE.md:                     Codex PASS
llms.txt:                      Codex PASS
README AI-entry routing:       Codex PASS
```

Draft-only workflows exist for the executable modules only:

```text
.github/workflows/draft-provenance-validator.yml
.github/workflows/draft-anti-laundering-detector.yml
.github/workflows/draft-detector-validator-pipeline.yml
.github/workflows/draft-challenger-harness.yml
```

No draft workflow exists for `independence_claim_burden` because it remains design-only.

---

## Direct validation commands

Root validation:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

v0.3.2 draft module tests are script-style. Run directly from module directories:

```bash
cd v0.3.2/drafts/provenance_validator && python3 test_provenance_validator.py
cd v0.3.2/drafts/anti_laundering_detector && python3 test_detector.py
cd v0.3.2/drafts/detector_validator_pipeline && python3 test_pipeline.py
cd v0.3.2/drafts/challenger_harness && python3 test_challenger_harness.py
```

Do not replace these module commands with `python3 -m pytest ...` unless the test files are redesigned for pytest collection.

---

## Structural closure

The current v0.3.2 draft baseline closes this operational chain:

```text
detection
→ validation
→ detector-validator routing
→ challenger comparison
→ independence-claim burden separation
→ AI-entry routing
→ status summary
→ release-prep checklist
→ pre-release body
```

Core closure:

```text
structural similarity alone is not laundering
hard derivation evidence or explicit reuse/adoption claims trigger provenance checks
citation alone is not operational provenance preservation
independent benchmark challenge does not require origin identity adoption
independent_not_derivative is not independent_origin_trace_sufficient
unknown exposure is a disclosed residual, not laundering and not clean-origin sufficiency
challenger harness does not re-decide provenance
challenger harness primary outcome set is not expanded by independence residuals
AI-entry files route interpretation but do not create runtime authority
AI-entry files do not promote v0.3.2 to active release
```

---

## Remaining residuals

The following residuals remain open:

```text
perfect_laundering_with_all_evidence_removed
semantic_cost_comparison_not_fully_machine_decided
logged_prompt_judgment_authenticity
independent_origin_trace_sufficiency_is_procedural_not_universal
natural_language_detector_false_negatives
runtime_owner_identification_unresolved
certification_authority_residual
```

These residuals must not be hidden by pre-release labeling.

---

## Non-authority boundary

This pre-release / draft baseline does not introduce:

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
origin replacement
```

It remains a classification, validation, comparison, routing, and disclosure structure.
It is not an external runtime-command layer.

---

## Release-note one-liner

```text
v0.3.2-draft records the closed executable draft-stack baseline plus audited AI-entry routing for provenance validation, anti-laundering detection, detector-validator routing, challenger comparison, and independence-claim burden separation, while preserving v0.3.0 as the current active release and maintaining non-authority / non-substitution boundaries.
```

End of file.
