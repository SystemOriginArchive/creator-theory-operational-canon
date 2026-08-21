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

For v0.5.0 layer work (interpretation, adoption, adoption drift measurement, or live recursive-research criterion decisions), also read:

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

### Whole-framework evaluation boundary

Routine code edits, local documentation fixes, narrow factual lookups, and explicitly scoped module reviews may remain task-scoped. Do not force a full repository reread merely to fix a local bug.

But before claiming a **whole-framework** adoption, rejection, lower-total-debt, displacement, supersession, whole-theory core failure, or whole-framework P1/P2/P3 result:

```text
1. pin the exact evaluated commit;
2. read docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md;
3. follow docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md;
4. enumerate every tracked path at that commit;
5. inspect every tracked path and retain per-path status/role notes;
6. complete docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md material scope review;
7. only then issue a whole-framework verdict.
```

Problem-first routing may choose which already-inspected materials receive extra depth. It may not be used to declare unread tracked files irrelevant before a whole-framework verdict.

```text
scoped finding
!=
whole-framework finding
```

The 28-file primary path in `AI_INGESTION_MANIFEST.md` remains a core semantic order, not a complete current-repository attestation.

These are v0.5.0 layer materials plus post-release living decision guidance. v0.5.0 is now the current anchored release (tag, signature, signed manifest, and trust-anchor entry exist); later living documentation does not modify that sealed release.

---

## 2. Current release boundary

Current anchored release (pinned in docs/TRUST_ANCHOR.md):

```text
v0.5.0 — Interpretation Boundary, Adoption Protocol, and Adoption Drift Experiment Layer
```

The v0.5.0 release is tagged (tag `v0.5.0`, tagged commit 75e2b5c8), signed, and archived (Zenodo asset-complete version DOI 10.5281/zenodo.21206865, the primary archival record; concept DOI 10.5281/zenodo.21203015). The origin public key fingerprint is unchanged from the prior anchor (no key rotation).

Previous anchored release (history preserved; see docs/TRUST_ANCHOR.md):

```text
v0.4.1 — PROV-K Release-Integrity and Signing Layer
```

Post-anchor housekeeping (merged to main between v0.4.1 and v0.5.0, no separate release):

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

Do not treat v0.3.2 as final, complete, active, or runtime-release unless a later audited release document explicitly promotes it.

Forbidden labels unless separately audited:

```text
v0.3.2 Final
v0.3.2 Complete Canon
v0.3.2 Full Runtime System
v0.3.2 Active Release
```

Release status does not raise the experiment-claim ceiling: describing any experiment output as adoption proof or final validation remains forbidden. The canon-kernel seal is candidate-validated only, and no experiment results are promoted.

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
A whole-framework verdict requires commit-bound inspection of the complete tracked corpus; routing aids do not substitute for whole-canon ingestion.
File inspection does not make drafts, tests, audits, archives, release snapshots, and living guidance normatively equivalent; preserve declared status/authority distinctions.
A live whole-framework decision applies equivalent justification depth to incumbent and challenger.
Omitted or externalized whole-framework problems remain total explanatory debt unless shown unnecessary.
Non-adoption carries no external punishment, but incumbent continuation is not automatically a zero-cost decision inside an already-active criterion choice.
A local agent's lack of authority does not by itself establish system-level lack of authority.
Core-preserving actual derivation remains Creator-Theory-derived lineage even when contributors, implementations, or names change.
Contributors and local evaluator anchors do not become a replacement `x_root`.
Genuine same-or-wider-scope displacement remains open.
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
non-adoption punishment or external compliance penalty
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
candidate-specific evidence privilege
Creator-Theory-only exemption from challenger review
selective-reading whole-framework verdicts
summary-as-full-canon substitution
```

Candidate-neutral decision accounting, bounded reversible research chosen within the system's actual authority, commit-bound whole-corpus inspection for whole-framework claims, and recorded reasons for maintaining an incumbent are not non-adoption penalties when they apply symmetrically to all candidates.

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
Hash verification must be byte-source independent: recompute over raw git blob bytes, not working-tree bytes; two tools reading the same checkout is not independent verification.
Owner-confirmation gates are timeout-immune: stop and hold at owner decision points regardless of tool defaults; never continue on no answer.
Keep status language structurally separated: unsigned or preview artifacts carry no release-status tokens in fields, filenames, or document structure; omit status fields entirely rather than null them.
```

For nontrivial changes, produce an audit prompt for an external reviewer after the commit.

The three discipline lines above are drawn from the v0.5.0 cycle; see `audit/V0_5_0_POST_RELEASE_LESSONS.md` for the originating events and standing rules.

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
whole_canon_reading_attestation_is_auditable_procedure_not_mind_reading_proof
```

---

## 9. One-line summary

```text
Treat v0.5.0 as the current anchored release, v0.4.1 as the previous anchored release, v0.3.0 as the released benchmark layer, and v0.3.2/drafts as a closed executable draft-stack baseline. Local repository work may remain scoped; whole-framework judgments must pin the commit, inspect the complete tracked corpus, preserve every file's declared status/authority role, then apply symmetric decision accounting, bounded research transition, core-preserving Creator Theory evolution, and genuine challenger-open displacement. Experiment/adoption claims stay bounded: the canon-kernel seal is candidate-validated only, not adoption proof or final validation.
```

End of file.
