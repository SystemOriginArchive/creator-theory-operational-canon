# Tools

## Current validation architecture

The hierarchy-repair candidate uses three clearly separated roles.

```text
tools/validate_creation_recursion_hierarchy.py
= current semantic validator for the creation-recursion hierarchy

tools/validate_repository_integrity.py
= current neutral repository/vector integrity validator

tools/validate_vectors.py
= archived pre-repair A3 semantic-contract validator retained as historical evidence
```

Only the first two are part of current semantic/integrity validation.

The archived pre-repair validator is **not executed by normal current CI** and has no current semantic veto. Its bytes are preserved so the repository can prove what the pre-repair validator actually required and can reproduce that historical state deliberately when needed.

This separation prevents two opposite failures:

```text
rewrite the old evaluator until the repair passes
!= allowed

keep the old evaluator as a permanent judge of the repaired canon
!= allowed
```

---

## Current Creation-Recursion Semantic Validator

`validate_creation_recursion_hierarchy.py` checks the forward hierarchy-repair semantics.

It checks, among other things:

```text
creation and recursive creative possibility are encoded as the higher direction
derived safeguards are not independent terminal axioms
non-throne is anti-self-entrenchment rather than absence of strong authority
action-form labels are not terminal verdicts
current human control is not permanent finality
AI authority is not automatically invalid
post-change evaluator self-ratification is insufficient
legacy hard-constraint encoding is explicitly marked as deprecated rather than silently erased
```

It also checks the dedicated `tests/creation_recursion_hierarchy_vectors.json` suite, action-form opposite-outcome pairs, human/AI self-entrenchment symmetry, the current machine-readable manifest/kernel, and agent-facing entry points.

It preserves the Git blob identities of the archived validator and selected old vectors. That is an evidence-preservation check, not execution of the old semantic contract.

Usage:

```bash
python3 tools/validate_creation_recursion_hierarchy.py
```

A PASS is candidate-specific evidence only. It is not adoption proof, release proof, theory truth, whole-framework superiority, or merge authorization.

---

## Current Neutral Repository Integrity Validator

`validate_repository_integrity.py` contains the non-semantic integrity functions that remain useful after retiring the old semantic contract from current CI.

It intentionally contains **no free-will, non-domination, AI-sovereignty, authority-form, or other higher-frame verdicts**.

It checks:

- every `*_vectors.json` file parses as JSON;
- required suite/case fields exist;
- `expected_result` uses the declared machine verdict set;
- string-list fields contain valid strings;
- `case_id` values are unique within and across vector files;
- every non-URL `source_documents` pointer resolves to a repository file;
- neutral manifest/provenance facts remain structurally valid;
- `README.md`, `AI_INGESTION_MANIFEST.md`, and the operational manifest keep a consistent reading order;
- canon-specific origin identity binding remains canon-profile-specific rather than leaking into the generic benchmark profile.

Usage:

```bash
python3 tools/validate_repository_integrity.py --repo-root . --tests-dir tests --profile canon --self-test-profile-isolation
python3 tools/validate_repository_integrity.py --repo-root . --tests-dir tests --profile benchmark
```

This validator is deliberately independent of `tools/validate_vectors.py`; it neither imports nor executes the archived validator.

---

## Archived Pre-Repair Validator

`validate_vectors.py` is preserved unchanged as evidence of the pre-repair A3 semantic contract.

That contract mixed useful repository-integrity checks with semantic requirements including hard `True` values for:

```text
non_throne_constraint
anti_capture_constraint
non_domination_constraint
free_will_constraint
```

and action-form invalidity requirements that the hierarchy repair no longer treats as independent terminal axioms.

Those historical requirements are not silently deleted or rewritten. They are retained so the earlier state remains auditable.

The archived validator is not part of normal current CI and does not decide whether the repaired forward canon passes.

If a researcher explicitly needs to reproduce the pre-repair contract, it may be run manually:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
```

A failure produced by that deliberate historical reproduction is not a current-canon verdict.

---

## Preserved Functional Regressions

Current CI separately runs the still-relevant regression suites rather than relying on the archived validator as a mixed semantic/integrity gate.

These include provenance and derivative-laundering checks, adversarial scenario coverage, PROV-K integrity, adoption-drift scaffolding, release-candidate audit, compression, adoption/verification separation, and retro manifest-chain integrity.

The intended succession is therefore:

```text
pre-repair mixed validator
        |
        +--> obsolete hard semantic contract -> archived historical evidence
        |
        +--> neutral structural integrity -> validate_repository_integrity.py
        |
        +--> still-valid functional protections -> dedicated regression suites

current high-frame semantics -> validate_creation_recursion_hierarchy.py
```

No validator receives permanent immunity from future challenge merely by becoming current.

---

## Release Boundary

These tools do not create or modify a release or tag.

They do not modify the AAOS Genesis repository.

Their existence does not create runtime authority, deployment authority, or permanent normative sovereignty.

See `docs/HIERARCHY_INVERSION_REPAIR_RECORD.md` and `docs/LEGACY_VALIDATOR_VECTOR_TRANSITION_MAP.md` for the transition record.

End of file.
