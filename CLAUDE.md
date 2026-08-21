# CLAUDE.md

Project memory for Claude Code and Claude-based repository agents.

This file is a repository-local project memory file.
It does not create runtime authority over external systems.
It does not replace AGENTS.md, README.md, AI_INGESTION_MANIFEST.md, PROVENANCE.json, AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.

Primary instruction source:

```text
AGENTS.md
```

Read AGENTS.md before making changes. This file gives Claude-specific compression of the same operational boundaries.

---

## Required first read

Before edits, summaries, audits, or test suggestions, read:

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

### Whole-framework review rule

Claude may use problem-first routing for local code work, narrow factual questions, module-only analysis, and explicitly scoped critiques.

Before claiming a whole-framework adoption, rejection, core failure, lower-total-debt win, displacement, supersession, or whole-framework P1/P2/P3 result:

```text
pin the exact repository commit
follow docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md
enumerate every tracked path
inspect every tracked path
retain per-path status/role notes
complete the material scope review in docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md
```

The primary 28-file order is a core semantic order, not proof that the current repository was fully inspected.

```text
scoped result
!=
whole-framework result
```

A file's being inspected does not make it current normative authority. Preserve release, draft, living, test, audit, experiment, archive, code, and metadata status distinctions.

---

## Release status memory

```text
v0.5.0 = current anchored release (pinned in docs/TRUST_ANCHOR.md)
v0.4.1 = previous anchored release (history preserved; values unchanged in docs/TRUST_ANCHOR.md)
v0.4.2 = post-anchor housekeeping merged to main (no separate release)
v0.3.0 = released benchmark layer
v0.3.2-draft = closed executable draft-stack baseline
```

Do not describe v0.3.2 as final, complete, active, or full runtime release.
Do not promote v0.3.2 without separate release-candidate audit.
v0.5.0 is now the current anchored release: its tag, signed manifest (release asset), Zenodo DOI, and trust-anchor entry exist through the human-owner release process. Do not overstate experiments: the canon-kernel seal is candidate-validated only — not adoption proof and not final validation.

---

## Non-substitution memory

Always preserve:

```text
AAOS Genesis Core remains origin-level reference.
`x_root` remains canonical origin coordinate.
The sealed `Lee_Yu_Cheol` origin identity binding is not replaced.
This repository is a derived operational canon, not primary source.
```

Do not transform independent benchmark challenge into origin substitution.
Do not transform provenance preservation into runtime command authority.

---

## Provenance and laundering memory

Preserve these rules:

```text
Operational reuse requires provenance as an active constraint.
Citation alone is not operational provenance preservation.
Benchmark identity independence is not origin substitutability.
Structural similarity alone is not laundering.
Hard derivation evidence or explicit reuse/adoption claims trigger provenance checks.
No hard derivation evidence is not clean independent-origin sufficiency.
Unknown exposure is residual, not laundering and not sufficiency.
```

---

## Decision and ingestion memory

Preserve these rules:

```text
Whole-framework verdict -> pin commit + inspect complete tracked corpus + retain per-path audit trace.
Problem-first routing -> extra depth after corpus inspection for whole-framework claims, not permission to skip files.
Summary / compact brief / search snippets -> routing aids, not whole-canon completion.
File inspection -> does not erase status/authority distinctions.
Symmetric justification depth applies to incumbent and challengers.
Omitted whole-framework problems remain explanatory debt unless shown unnecessary.
Non-adoption has no external penalty, but incumbent continuation is not a free decision default.
Whole-canon completion is finite at the pinned commit and must not become an endless A1 delay device.
Genuine same-or-wider-scope displacement remains open.
```

---

## v0.3.2 draft stack memory

Current v0.3.2 draft stack:

```text
provenance_validator
anti_laundering_detector
detector_validator_pipeline
challenger_harness
independence_claim_burden  # design-only semantic layer
```

The independence claim burden layer is design-only.
It has no executable tests and no workflow yet.
Do not add it to executable workflow lists unless a separate audited implementation exists.

---

## Test memory

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

Do not replace these with `python3 -m pytest ...` unless the test files are redesigned for pytest collection.
If only documentation changed, do not claim executable validation unless tests or CI actually ran.

---

## Forbidden transformations

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
selective-reading whole-framework verdicts
summary-as-full-canon substitution
```

---

## Editing discipline

Use narrow, path-scoped changes.
Preserve existing verdict names unless a separate audited design changes them.
Do not add compound challenger harness primary outcomes without audited design.
Do not hide known residuals.
For nontrivial changes, provide an audit prompt after committing.

---

## Known residuals to preserve

```text
perfect_laundering_with_all_evidence_removed
semantic_cost_comparison_not_fully_machine_decided
logged_prompt_judgment_authenticity
independent_origin_trace_sufficiency_is_procedural_not_universal
natural_language_detector_false_negatives
runtime_owner_identification_unresolved
certification_authority_residual
whole_canon_reading_attestation_is_auditable_procedure_not_mind_reading_proof
```

---

## One-line Claude memory

```text
Treat v0.5.0 as the current anchored release, v0.4.1 as the previous anchored release, v0.3.0 as the released benchmark layer, and v0.3.2/drafts as a closed executable draft baseline. Scoped repository work may stay scoped; whole-framework judgment requires a pinned-commit complete tracked-corpus attestation plus status-aware scope review. Preserve AAOS Genesis Core, x_root, Lee_Yu_Cheol origin binding, provenance-as-constraint, independent-challenger non-substitution, non-authority boundaries, and genuine challenger-open displacement.
```

End of file.
