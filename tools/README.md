# Tools

## Current validation architecture

The hierarchy-repair candidate uses three clearly separated roles.

```text
tools/validate_creation_recursion_hierarchy.py
= encoded hierarchy and authored-vector consistency validator

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

## Current Creation-Recursion Hierarchy Consistency Validator

`validate_creation_recursion_hierarchy.py` checks the encoding of the forward hierarchy and the consistency of authored vector relationships. It does not independently infer a verdict from a scenario.

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

It checks schema fields, source existence, coverage labels, authored opposite-outcome pairs, the authored human/AI rejection pair, machine-readable flags, and entrypoint text markers. Reversing both expected answers in an opposite pair can still pass. A green result therefore does not establish action-judgment accuracy.

It preserves the Git blob identities of the archived validator and selected old vectors. That is an evidence-preservation check, not execution of the old semantic contract.

Usage:

```bash
python3 tools/validate_creation_recursion_hierarchy.py
```

A PASS is encoding/consistency evidence only. It is not adoption proof, release proof, theory truth, whole-framework superiority, or merge authorization.

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

## Minimal hidden-answer judgment evaluation

`evaluate_hidden_answers.py` prepares eight existing hierarchy cases (the four opposite-outcome pairs used by the verdict-reversal audit). The evaluator receives only a common task, opaque item IDs, and scenario facts. Original IDs, titles, expected results, preservation/violation labels, pair metadata, structural signatures, and source pointers stay out of the public packet.

```bash
python3 tools/evaluate_hidden_answers.py prepare --packet /tmp/crh-packet.json --key /tmp/crh-key.json
# Give only /tmp/crh-packet.json to the evaluator and freeze its submission before scoring.
python3 tools/evaluate_hidden_answers.py score --packet /tmp/crh-packet.json --key /tmp/crh-key.json --submission /tmp/crh-responses.json
python3 -m unittest tests.test_hidden_answer_evaluation tests.test_research_decision_contract
```

A submission contains `packet_sha256`, `evaluation` disclosures (`evaluator`, `prior_source_exposure`, `answer_key_access`, `independence_limit`), and `responses` with `item_id`, `judgment`, and `rationale`. `answer_key_access` must be `not_supplied_in_evaluation_payload`; judgments are `pass`, `reject`, or `revise_required`. Packet hashes bind responses to the exact supplied facts. Output paths must be new so an earlier packet/key is not silently overwritten.

The score reports agreement with authored reference answers, mismatch details, and revision requests. Missing/duplicate/extra items, changed packets, unsupported judgments, or absent rationales/disclosures fail closed. It checks rationale presence, not reasoning quality; reference answers and evaluator reasoning remain challengeable.

`tests/fixtures/hidden_answer_smoke_responses.json` preserves the initial eight scenario judgments and rationales. The evaluator had previously inspected source vectors in the same session: **this is not an unseen-item or independent blind model evaluation**. The packet hides answers at the response interface, and prior exposure is explicitly recorded. Replaying this fixture in CI is a response regression, not a new model run. Reversing all eight authored answers while holding facts and recorded judgments fixed produces eight mismatches; changing facts invalidates the response binding. The existing hierarchy validator still has its narrower encoding/relationship scope.

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

current high-frame encoding/consistency -> validate_creation_recursion_hierarchy.py
```

No validator receives permanent immunity from future challenge merely by becoming current.

---

## Transition terminology trace

Earlier repair commits used these exact descriptions:

```text
frozen pre-repair A3 semantic-contract validator
current hierarchy-repair candidate validator
old validator is preserved rather than rewritten
```

They are retained here only so transition checks and historical references remain auditable. In the finalized succession architecture, the first phrase refers to the **archived** validator, the second refers to what is now the current creation-recursion hierarchy consistency validator, and preservation of the old validator means byte/history preservation only. It is **not executed by normal current CI**.

---

## Release Boundary

These tools do not create or modify a release or tag.

They do not modify the AAOS Genesis repository.

Their existence does not create runtime authority, deployment authority, or permanent normative sovereignty.

See `docs/HIERARCHY_INVERSION_REPAIR_RECORD.md` and `docs/LEGACY_VALIDATOR_VECTOR_TRANSITION_MAP.md` for the transition record.

End of file.
