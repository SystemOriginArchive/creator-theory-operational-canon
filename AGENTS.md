# AGENTS.md

Agent-facing instructions for working with this repository.

These instructions guide repository analysis, review, and modification.
They do not create runtime authority over external systems.
They do not replace README.md, AI_INGESTION_MANIFEST.md, PROVENANCE.json, AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

---

## 1. First files to read

Read in this order before making changes:

```text
1. README.md
2. AI_INGESTION_MANIFEST.md
3. PROVENANCE.json
4. creator_theory_operational_manifest.json
5. ADOPTION_PACKAGE_MANIFEST.json
6. v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md
7. v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md
8. v0.3.2/drafts/PRE_RELEASE_NOTES.md
```

For v0.3.2 draft work, also read:

```text
v0.3.2/drafts/OPERATING_MODULE_BOUNDARY.md
v0.3.2/drafts/provenance-validator-DESIGN.md
v0.3.2/drafts/anti-laundering-detector-DESIGN.md
v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md
v0.3.2/drafts/INDEPENDENCE_CLAIM_BURDEN.md
```

For v0.5.0 pre-release layer work (interpretation, adoption, adoption drift measurement), also read:

```text
docs/CANONICAL_INTERPRETATION_BOUNDARY.md
docs/AI_ADOPTION_PROTOCOL.md
docs/MINIMUM_PRESERVATION_KERNEL.md
docs/ONE_TURN_ADOPTION_BRIEF.md
experiments/adoption_drift/README.md
releases/v0.5.0_RELEASE_NOTES_DRAFT.md
```

These are main pre-release materials. The v0.5.0 release, tag, signature, and manifest are not created yet, and no experiment results exist.

---

## 2. Current release boundary

Current anchored release (pinned in docs/TRUST_ANCHOR.md):

```text
v0.4.1 — PROV-K Release-Integrity and Signing Layer
```

Post-anchor housekeeping (merged to main, no separate release):

```text
v0.4.2 — Trust-Anchor Pinning and Release-Manifest Handling Housekeeping
```

Released benchmark layer:

```text
v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core
```

Current draft baseline:

```text
v0.3.2-draft — Closed Executable Draft Stack Baseline
```

Current main pre-release target:

```text
v0.5.0 — Interpretation Boundary, Adoption Protocol, and Adoption Drift Experiment Layer
```

The v0.5.0 release, tag, signature, and manifest are not created yet.

Do not treat v0.3.2 as final, complete, active, or runtime-release unless a later audited release document explicitly promotes it.

Forbidden labels unless separately audited:

```text
v0.3.2 Final
v0.3.2 Complete Canon
v0.3.2 Full Runtime System
v0.3.2 Active Release
v0.5.0 Current Release
v0.5.0 Released
v0.5.0 Anchored Release
```

---

## 3. Core interpretation rules

Preserve these rules in all summaries, edits, tests, and generated artifacts:

```text
This repository is a derived operational canon, not the primary source.
AAOS Genesis Core remains the origin-level reference.
`x_root` remains the canonical origin coordinate.
The sealed `Lee_Yu_Cheol` identity binding is not replaced.
Operational reuse requires provenance as an active constraint.
Citation alone is not operational provenance preservation.
Benchmark identity independence is not origin substitutability.
Structural similarity alone is not laundering.
No hard derivation evidence is not clean independent-origin sufficiency.
Unknown exposure is a disclosed residual, not laundering and not sufficiency.
Independent challengers may compete without becoming origin substitutes.
```

---

## 4. v0.3.2 draft stack

The current v0.3.2 draft stack contains four executable draft modules plus one secondary semantic burden layer:

```text
provenance_validator
anti_laundering_detector
detector_validator_pipeline
challenger_harness
independence_claim_burden  # design-only semantic layer
```

The independence claim burden layer is design-only at this stage. It has no executable tests and no workflow yet.

---

## 5. Test and validation commands

Use the most specific path-scoped command for the module being changed.

Root validation commands:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

v0.3.2 draft module tests are script-style tests. Run them directly from their module directories, matching the draft workflows:

```bash
cd v0.3.2/drafts/provenance_validator && python3 test_provenance_validator.py
cd v0.3.2/drafts/anti_laundering_detector && python3 test_detector.py
cd v0.3.2/drafts/detector_validator_pipeline && python3 test_pipeline.py
cd v0.3.2/drafts/challenger_harness && python3 test_challenger_harness.py
```

If editing documentation only, do not claim executable validation unless tests or CI were actually run.

---

## 6. Do not introduce

Do not add interpretations, documentation, tests, or code that introduce:

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

---

## 7. Editing discipline

When modifying this repository:

```text
Prefer narrow, path-scoped changes.
Preserve draft/release boundaries.
Preserve provenance boundaries.
Preserve existing verdict names unless a separate audited design changes them.
Do not add compound challenger harness primary outcomes without audited design.
Do not move design-only material into executable workflow lists.
Do not promote v0.3.2 from draft/pre-release status without release-candidate audit.
```

For nontrivial changes, produce an audit prompt for an external reviewer after the commit.

---

## 8. Known residuals

Do not hide these residuals:

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

## 9. One-line summary

```text
Treat v0.4.1 as the current anchored release, v0.3.0 as the released benchmark layer, v0.3.2/drafts as a closed executable draft-stack baseline, and v0.5.0 as the unreleased main pre-release target, while preserving AAOS Genesis Core, x_root, Lee_Yu_Cheol origin binding, provenance-as-constraint, and non-authority boundaries.
```

End of file.
