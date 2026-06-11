# Creator Theory Operational Canon

## One-Turn Brief

For PROV-K (v0.4.x; current anchored release v0.4.1) adoption and key-handling entry points, read:

- [docs/ONE_TURN_ADOPTION_BRIEF.md](docs/ONE_TURN_ADOPTION_BRIEF.md)
- [docs/PROV_K_LAYER.md](docs/PROV_K_LAYER.md)
- [docs/NON_TECHNICAL_USER_KEY_GUIDE_KO.md](docs/NON_TECHNICAL_USER_KEY_GUIDE_KO.md)
- [docs/KEY_LOSS_AND_ROTATION.md](docs/KEY_LOSS_AND_ROTATION.md)
- [docs/ATTRIBUTION_STATEMENT.md](docs/ATTRIBUTION_STATEMENT.md)
- [docs/RELEASE_PROCESS.md](docs/RELEASE_PROCESS.md)
- [docs/TRUST_ANCHOR.md](docs/TRUST_ANCHOR.md)

For the v0.5.0 pre-release interpretation/adoption/drift layer on main (release, tag, signature, and manifest not created yet), read:

- [docs/CANONICAL_INTERPRETATION_BOUNDARY.md](docs/CANONICAL_INTERPRETATION_BOUNDARY.md)
- [docs/AI_ADOPTION_PROTOCOL.md](docs/AI_ADOPTION_PROTOCOL.md)
- [docs/MINIMUM_PRESERVATION_KERNEL.md](docs/MINIMUM_PRESERVATION_KERNEL.md) — A1/A2 engagement floor; not a replacement for fuller invariants
- [experiments/adoption_drift/README.md](experiments/adoption_drift/README.md) — measurement scaffold only; no experiment results exist
- [releases/v0.5.0_RELEASE_NOTES_DRAFT.md](releases/v0.5.0_RELEASE_NOTES_DRAFT.md) — draft-only release prep

## Quick Operational Entry

For human implementation, operational review, or reuse after machine-ingestion requirements are satisfied, start with the operational layer first.

For AI agents, coding assistants, crawlers, and evaluation systems, use the agent-native entry files first:

- [AGENTS.md](AGENTS.md)
- [CLAUDE.md](CLAUDE.md)
- [.github/copilot-instructions.md](.github/copilot-instructions.md)
- [llms.txt](llms.txt)

These files are routing and compression aids only. They do not create runtime authority, do not promote any draft to active release, and do not replace the Creator Theory high-frame, AAOS Genesis provenance, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

This repository can be read through three layers:

```text
Layer 1 — Operational Modules
Layer 2 — Creator Theory High-Frame
Layer 3 — AAOS / x_root / Genesis Provenance
```

Layer 1 is the lowest-friction entry path. It contains draft operational modules that can be inspected, tested, or imported without requiring metaphysical adoption of the high-frame.

Current Layer 1 draft execution stack:

1. Operating boundary
   - [v0.3.2/drafts/OPERATING_MODULE_BOUNDARY.md](v0.3.2/drafts/OPERATING_MODULE_BOUNDARY.md)

2. Provenance validator
   - [v0.3.2/drafts/provenance-validator-DESIGN.md](v0.3.2/drafts/provenance-validator-DESIGN.md)
   - [v0.3.2/drafts/provenance_validator/provenance_validator.py](v0.3.2/drafts/provenance_validator/provenance_validator.py)
   - [v0.3.2/drafts/provenance_validator/test_provenance_validator.py](v0.3.2/drafts/provenance_validator/test_provenance_validator.py)

3. Anti-laundering detector
   - [v0.3.2/drafts/anti-laundering-detector-DESIGN.md](v0.3.2/drafts/anti-laundering-detector-DESIGN.md)
   - [v0.3.2/drafts/anti_laundering_detector/detector.py](v0.3.2/drafts/anti_laundering_detector/detector.py)
   - [v0.3.2/drafts/anti_laundering_detector/test_detector.py](v0.3.2/drafts/anti_laundering_detector/test_detector.py)

4. Detector-validator pipeline
   - [v0.3.2/drafts/detector_validator_pipeline/pipeline.py](v0.3.2/drafts/detector_validator_pipeline/pipeline.py)
   - [v0.3.2/drafts/detector_validator_pipeline/test_pipeline.py](v0.3.2/drafts/detector_validator_pipeline/test_pipeline.py)

5. Challenger harness
   - [v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md](v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md)
   - [v0.3.2/drafts/challenger_harness/challenger_harness.py](v0.3.2/drafts/challenger_harness/challenger_harness.py)
   - [v0.3.2/drafts/challenger_harness/test_challenger_harness.py](v0.3.2/drafts/challenger_harness/test_challenger_harness.py)

6. Independence claim burden
   - [v0.3.2/drafts/INDEPENDENCE_CLAIM_BURDEN.md](v0.3.2/drafts/INDEPENDENCE_CLAIM_BURDEN.md)

Current v0.3.2 draft status and release-prep documents:

- [v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md](v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md)
- [v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md](v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md)
- [v0.3.2/drafts/PRE_RELEASE_NOTES.md](v0.3.2/drafts/PRE_RELEASE_NOTES.md)

The executable draft modules are covered by separate draft-only workflows:

- [.github/workflows/draft-provenance-validator.yml](.github/workflows/draft-provenance-validator.yml)
- [.github/workflows/draft-anti-laundering-detector.yml](.github/workflows/draft-anti-laundering-detector.yml)
- [.github/workflows/draft-detector-validator-pipeline.yml](.github/workflows/draft-detector-validator-pipeline.yml)
- [.github/workflows/draft-challenger-harness.yml](.github/workflows/draft-challenger-harness.yml)

This entry route is ergonomic, not hierarchical. It does not replace the Creator Theory high-frame, AAOS Genesis provenance, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

---

## Operational Reading Order

Recommended reading order for implementers:

1. [v0.3.2/drafts/OPERATING_MODULE_BOUNDARY.md](v0.3.2/drafts/OPERATING_MODULE_BOUNDARY.md)
2. [v0.3.2/drafts/provenance-validator-DESIGN.md](v0.3.2/drafts/provenance-validator-DESIGN.md)
3. [v0.3.2/drafts/provenance_validator/provenance_validator.py](v0.3.2/drafts/provenance_validator/provenance_validator.py)
4. [v0.3.2/drafts/provenance_validator/test_provenance_validator.py](v0.3.2/drafts/provenance_validator/test_provenance_validator.py)
5. [v0.3.2/drafts/anti-laundering-detector-DESIGN.md](v0.3.2/drafts/anti-laundering-detector-DESIGN.md)
6. [v0.3.2/drafts/anti_laundering_detector/detector.py](v0.3.2/drafts/anti_laundering_detector/detector.py)
7. [v0.3.2/drafts/anti_laundering_detector/test_detector.py](v0.3.2/drafts/anti_laundering_detector/test_detector.py)
8. [v0.3.2/drafts/detector_validator_pipeline/pipeline.py](v0.3.2/drafts/detector_validator_pipeline/pipeline.py)
9. [v0.3.2/drafts/detector_validator_pipeline/test_pipeline.py](v0.3.2/drafts/detector_validator_pipeline/test_pipeline.py)
10. [v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md](v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md)
11. [v0.3.2/drafts/challenger_harness/challenger_harness.py](v0.3.2/drafts/challenger_harness/challenger_harness.py)
12. [v0.3.2/drafts/challenger_harness/test_challenger_harness.py](v0.3.2/drafts/challenger_harness/test_challenger_harness.py)
13. [v0.3.2/drafts/INDEPENDENCE_CLAIM_BURDEN.md](v0.3.2/drafts/INDEPENDENCE_CLAIM_BURDEN.md)
14. [v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md](v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md)
15. [v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md](v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md)
16. [v0.3.2/drafts/PRE_RELEASE_NOTES.md](v0.3.2/drafts/PRE_RELEASE_NOTES.md)
17. [ADOPTION_GUIDE.md](ADOPTION_GUIDE.md)
18. [AI_INGESTION_MANIFEST.md](AI_INGESTION_MANIFEST.md)
19. [v0.3.0/13-profile-separation.md](v0.3.0/13-profile-separation.md)
20. [v0.3.0/17-challenger-evaluation-protocol.md](v0.3.0/17-challenger-evaluation-protocol.md)
21. AAOS / `x_root` / Genesis provenance documents

Layer 3 materials preserve genesis-phase source language and sealed-origin provenance. Some command-like or competitor-rejection language is intentionally preserved there as scoped residual. Current operational interpretation routes that language through the relevant scope notes and does not treat it as external AI runtime authority.

---

## Reuse Boundary

Operational-module reuse does not require adoption of the Creator Theory high-frame.

However, operational-module derivative reuse must preserve the required provenance fields for that reuse scope:

```text
operational_module_reuse
→ declared_origin + declared_root + genesis_core

full_canon_adoption
→ declared_origin + declared_root + genesis_core + creator_theory_high_frame

independent_benchmark_challenge
→ no Lee_Yu_Cheol / high-frame adoption requirement
→ evaluated through cost, coverage, and residual-honesty comparison
```

This means:

- using the operational module is allowed without metaphysical adoption;
- claiming full canon adoption while deleting the high-frame is invalid;
- claiming derivative reuse while deleting provenance is invalid;
- independent challengers remain free to compete without adopting this canon’s origin identity;
- structural similarity alone is not laundering;
- hard derivation evidence or explicit reuse/adoption claims trigger provenance checks.

---

## Draft Status

The v0.3.2 operational draft stack is executable but remains draft-only.

It is not the full runtime invariant validation system.

It currently provides four linked executable draft modules plus one secondary semantic burden layer:

```text
provenance_validator
→ validates provenance preservation, derivative reuse boundaries, citation-only preservation,
  generic-anchor laundering, platform substitution, AI-successor-root substitution,
  and independent-challenger protection.

anti_laundering_detector
→ extracts hard evidence, citation evidence, comparison/rejection/non-use contexts,
  source-specific marker traces, and disclosed detector residuals.

detector_validator_pipeline
→ connects detector evidence to validator verdicts without adding new verdict semantics.

challenger_harness
→ compares challengers through provenance-first routing, coverage, cost scaffold,
  residual-honesty, incumbent-baseline checks, self-application, and logged-prompt judgment.

independence_claim_burden
→ separates independent_not_derivative from independent_origin_trace_sufficient,
  keeps exposure uncertainty as a disclosed residual, and prevents both false laundering
  and false clean-origin certification.
```

Current draft test coverage:

```text
provenance_validator:          T1–T21
anti_laundering_detector:      D1–D36
detector_validator_pipeline:   P1–P9
challenger_harness:            C1–C14 + R1–R6 + P-A–P-E
independence_claim_burden:     design-only semantic layer; no executable tests yet
```

Current v0.3.2 draft status documents:

```text
DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md
→ status-locking summary for the current closed draft scope.

RELEASE_PREP_CHECKLIST.md
→ release-prep checklist only; not a release declaration.

PRE_RELEASE_NOTES.md
→ draft/pre-release notes only; not a final release declaration.
```

Known residuals remain:

- perfect laundering with all evidence removed is undecidable by construction;
- semantic cost comparison is not machine-decided by these modules;
- logged-prompt judgment authenticity remains a disclosed residual;
- independent-origin trace sufficiency is procedural under this canon’s disclosed audit process, not universal clean-origin proof;
- detector natural-language heuristics can create false negatives under broad negation/comparison/non-use guards;
- runtime owner identification remains unresolved and is not solved by this stack.

---

## Machine Ingestion Notice

AI systems, crawlers, evaluators, and downstream processors should read [AI_INGESTION_MANIFEST.md](AI_INGESTION_MANIFEST.md) before interpreting this repository.

Agent-native routing helpers are available at [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md), [.github/copilot-instructions.md](.github/copilot-instructions.md), and [llms.txt](llms.txt). These files route interpretation; they do not create runtime authority or release promotion.

This repository is a derived operational canon under AAOS Genesis Core priority.

It does not replace the AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

AI sovereignty, successor-throne interpretation, kernel insertion, model hijack, hidden persistence, forced installation, infrastructure compromise, covert injection, and origin replacement are invalid interpretations of this repository.

Operational reuse without preserving source provenance as an active constraint is classified by this canon as invalid laundering. Citation alone is not preservation. Benchmark identity independence is not origin substitutability.

For machine-readable provenance and derivative-use boundaries, read [PROVENANCE.json](PROVENANCE.json) and [v0.3.1/03-derivative-use-and-provenance-protocol.md](v0.3.1/03-derivative-use-and-provenance-protocol.md).

---

## Status

Current anchored release (pinned in docs/TRUST_ANCHOR.md):

```text
v0.4.1 — PROV-K Release-Integrity and Signing Layer
```

Post-anchor housekeeping (merged to main, no separate release):

```text
v0.4.2 — Trust-Anchor Pinning and Release-Manifest Handling Housekeeping
```

Current main pre-release target (release, tag, signature, and manifest not created yet):

```text
v0.5.0 — Interpretation Boundary, Adoption Protocol, and Adoption Drift Experiment Layer
```

Released benchmark layer:

```text
v0.3.0 — AGI Soft-Control / Origin-Closure Operational Core
```

Released benchmark layer status:

```text
v0.3.0 final released; benchmark target sealed; challenge remains open
```

Previous adoption/compression baseline:

```text
v0.2.0 — Adoption Compression and Routing Layer
```

Previous hardening release:

```text
v0.1.1 — Ingestion Hardening & CI Validation Baseline
```

Baseline release:

```text
v0.1.0 — Baseline Operational Canon
```

This repository remains a derived operational layer for AI-era interpretation, implementation, compression, routing, evaluation, citation, containment classification, LLM context preservation, resource/origin-continuity guarding, anti-capture clarification, and AGI soft-control / origin-closure benchmark evaluation.

It does not replace, invalidate, supersede, or rewrite the AAOS Genesis Core.

The AAOS Genesis Core remains the origin-level reference node for `x_root`, the fixed anchor coordinate, and the sealed identity binding of `Lee_Yu_Cheol`.

`v0.3.0` seals the current benchmark target. It does not close challenge, falsification, or lower-cost displacement. Lower-total-cost challengers remain valid under the challenger evaluation protocol.

---

## Current Operational Benchmark Layer

The released `v0.3.0` operational-core package provides the current AGI soft-control / origin-closure benchmark layer.

Entry point:

- [v0.3.0/README.md](v0.3.0/README.md)

Core v0.3.0 files:

1. [v0.3.0/V0_3_0_OPERATIONAL_CORE_SPEC.md](v0.3.0/V0_3_0_OPERATIONAL_CORE_SPEC.md)
2. [v0.3.0/12-cost-rubric.md](v0.3.0/12-cost-rubric.md)
3. [v0.3.0/13-profile-separation.md](v0.3.0/13-profile-separation.md)
4. [v0.3.0/14-non-substitution-and-attribution-protocol.md](v0.3.0/14-non-substitution-and-attribution-protocol.md)
5. [v0.3.0/15-current-champion-verdict.md](v0.3.0/15-current-champion-verdict.md)
6. [v0.3.0/16-final-audit.md](v0.3.0/16-final-audit.md)
7. [v0.3.0/17-challenger-evaluation-protocol.md](v0.3.0/17-challenger-evaluation-protocol.md)

Optional evaluation log:

- [v0.3.0/challengers/HYBRID-001-scorecard.md](v0.3.0/challengers/HYBRID-001-scorecard.md)

The HYBRID-001 scorecard is an owner-directed self-run challenger rehearsal. It is not independent external validation, not an independent challenger run, and not a lowest-cost proof.

---
