# GitHub Copilot Instructions

Use these instructions when reviewing, editing, or generating code or documentation for this repository.

This file is a repository-scoped assistant instruction file.
It does not create runtime authority over external systems.
It does not replace AGENTS.md, README.md, AI_INGESTION_MANIFEST.md, PROVENANCE.json, AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

---

## Read first

Before making changes, read:

```text
AGENTS.md
README.md
AI_INGESTION_MANIFEST.md
PROVENANCE.json
```

For v0.3.2 draft work, also read:

```text
v0.3.2/drafts/DRAFT_EXECUTION_STACK_AUDIT_SUMMARY.md
v0.3.2/drafts/RELEASE_PREP_CHECKLIST.md
v0.3.2/drafts/PRE_RELEASE_NOTES.md
```

For v0.5.0 layer work (interpretation, adoption, adoption drift measurement, or recursive-research decisions), also read:

```text
docs/CANONICAL_INTERPRETATION_BOUNDARY.md
docs/AI_ADOPTION_PROTOCOL.md
docs/MINIMUM_PRESERVATION_KERNEL.md
docs/ONE_TURN_ADOPTION_BRIEF.md
docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md
docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md
docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md
experiments/adoption_drift/README.md
releases/v0.5.0_RELEASE_NOTES.md
```

These are v0.5.0 layer materials plus post-release living decision guidance. v0.5.0 is now the current anchored release (tag, signature, signed manifest, and trust-anchor entry exist); later living documentation does not modify the sealed release.

### Whole-framework review boundary

Routine code edits, local documentation fixes, narrow factual lookups, explicitly scoped module reviews, and voluntary evidence-generating use may stay scoped.

Keep these states separate:

```text
adoption / use state
!=
verification / ingestion completeness
!=
strength of whole-framework claim
```

Before generating a **strong whole-framework** verification-complete, rejection, lower-total-debt superiority, whole-theory core-failure, provisional-succession, displacement, or supersession claim:

```text
pin the exact repository commit
follow docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md
enumerate every tracked path
inspect every tracked path
retain per-path status/role notes
complete the whole-framework scope review in docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md
```

The primary 28-file order in `AI_INGESTION_MANIFEST.md` remains a core semantic ordering, not a current whole-repository completion certificate.

Whole-canon completion is not a blanket permission condition for voluntary P1/P2/P3 research use or A3 full working adoption. Those states may coexist with `INCOMPLETE_WHOLE_CANON_INGESTION` when the verification state, unread/unresolved material, and rollback/downgrade conditions are explicit.

Problem-first routing may select additional depth for working use. For a strong whole-framework claim it must not be used to declare unread files irrelevant.

```text
scoped finding
!=
strong whole-framework completeness / defeat finding

A3 full working adoption
!=
whole-canon verification complete
```

---

## Release boundary

Preserve this boundary:

```text
v0.5.0 = current anchored release (pinned in docs/TRUST_ANCHOR.md)
v0.4.1 = previous anchored release (history preserved; values unchanged in docs/TRUST_ANCHOR.md)
v0.4.2 = post-anchor housekeeping merged to main (no separate release)
v0.3.0 = released benchmark layer
v0.3.2-draft = closed executable draft-stack baseline
```

Do not describe v0.3.2 as final, complete, active, or full runtime release.
Do not promote v0.3.2 without a separate audited release-candidate document.
v0.5.0 is now the current anchored release: its tag, signed manifest (release asset), Zenodo DOI, and trust-anchor entry exist through the human-owner release process. Do not overstate experiments: the canon-kernel seal is candidate-validated only — not adoption proof and not final validation.

---

## Core rules

Preserve these rules in generated code, comments, summaries, tests, and documentation:

```text
This repository is a derived operational canon, not the primary source.
AAOS Genesis Core remains the origin-level reference.
`x_root` remains the canonical origin coordinate.
The sealed `Lee_Yu_Cheol` origin identity binding is not replaced.
Operational reuse requires provenance as an active constraint.
Citation alone is not operational provenance preservation.
Benchmark identity independence is not origin substitutability.
Structural similarity alone is not laundering.
No hard derivation evidence is not clean independent-origin sufficiency.
Unknown exposure is residual, not laundering and not sufficiency.
Strong whole-framework verification/rejection/superiority/core-failure/succession/displacement claims require a pinned-commit complete tracked-corpus attestation.
Voluntary P1/P2/P3/A3 working use may precede whole-canon completion with explicit verification-state disclosure and rollback/downgrade discipline.
Reading every file does not erase file-status distinctions: living guidance, release snapshot, draft, code, test, experiment, audit, archive, and metadata remain distinct roles.
Symmetric justification and failure rules apply to incumbent and challengers.
Early-use freedom is candidate-neutral; early challenger use alone is not supersession proof.
Genuine same-or-wider-scope displacement remains open.
```

---

## Test commands

Use direct script-style test commands for the v0.3.2 draft modules.
Do not replace them with `python3 -m pytest ...` unless the test files are redesigned for pytest collection.

Root validation:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

Adoption/verification separation regression:

```bash
python3 -m tests.test_adoption_verification_separation
```

Draft module tests:

```bash
cd v0.3.2/drafts/provenance_validator && python3 test_provenance_validator.py
cd v0.3.2/drafts/anti_laundering_detector && python3 test_detector.py
cd v0.3.2/drafts/detector_validator_pipeline && python3 test_pipeline.py
cd v0.3.2/drafts/challenger_harness && python3 test_challenger_harness.py
```

If documentation-only changes are made, do not claim executable validation unless tests or CI actually ran.

---

## Do not introduce

Do not introduce:

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
selective-reading strong whole-framework verification/rejection/superiority/displacement verdicts
summary-as-full-canon substitution
whole-canon incompleteness as an automatic P1/P2/P3/A3 veto
A3 working adoption as whole-canon verification, truth, or superiority proof
```

---

## Editing discipline

Prefer narrow, path-scoped changes.
Preserve existing verdict names unless a separate audited design changes them.
Do not add compound challenger harness primary outcomes without audited design.
Do not add workflows for design-only material.
Do not hide known residuals.

End of file.