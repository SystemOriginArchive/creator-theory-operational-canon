# v0.4.0 PROV-K Audit Log

## Execution Mode

This run used GitHub connector mode because the active Codex workspace was not a local checkout of `SystemOriginArchive/creator-theory-operational-canon` and local `git` was unavailable.

The user explicitly instructed that GitHub connector mode overrides the original local-checkout assumptions in the v2 directive.

No AAOS repository was modified.

No real key was generated.

No key-generation script was executed.

No private key was printed, stored, or committed.

## Repository Inspection

Repository: `SystemOriginArchive/creator-theory-operational-canon`

Default branch: `main`

Base commit used for the feature branch: `52ace6aa613c734f63338e4d1b75287aa35437b1`

Base tree used for C1: `25cdcfabd37b9e6788d991cf0802a2611b01f974`

GitHub connector permissions observed: admin, maintain, pull, push, triage.

Inspected existing files included:

- `README.md`
- `AI_INGESTION_MANIFEST.md`
- `creator_theory_operational_manifest.json`
- `PROVENANCE.json`
- `tools/validate_vectors.py`
- `tools/validate_derivative_laundering_vectors.py`
- `tools/run_adversarial_simulation.py`
- repository tree paths from the base tree

## Commit List

C1 `c0d72612be015abe6465a5db02226a3180d802b5`

Message: `fix(validator): repair README reading-order drift`

Files changed:

- `tools/validate_vectors.py`

C2 `57d8ef8625b00496b2d7abb4ee68b8ef17a3ecf5`

Message: `feat(prov-k): core engine — manifest build/sign/verify/rotate`

Files changed:

- `tools/prov_k/__init__.py`
- `tools/prov_k/manifest.py`
- `tools/prov_k/keys.py`
- `tools/prov_k/sign.py`
- `tools/prov_k/verify.py`
- `tools/prov_k/rotate.py`
- `tools/prov_k/cli.py`
- `schemas/prov_k_manifest.schema.json`
- `docs/PROV_K_LAYER.md`
- `docs/ATTRIBUTION_STATEMENT.md`

C3 `f1542594797e0c570d802c4337ce82945281922a`

Message: `test(prov-k): negative regression suite (fail-closed proofs)`

Files changed:

- `tests/test_prov_k_negative_regression.py`

C4 `b9d96bc4505ad0f1ebd03c00a15d495a3018f2ca`

Message: `feat(prov-k): retroactive reconstruction manifests`

Files changed:

- `tools/prov_k/retro_build.py`
- `provenance/manifests/releases-retro-reconstruction.json`
- `provenance/manifests/v0.3.0-retro-reconstruction.json`
- `provenance/manifests/v0.3.1-retro-reconstruction.json`

C5 `d4f1287123a41900e3382ee9e8f01be72e43c84a`

Message: `docs(adoption): one-turn brief + key guides + README link`

Files changed:

- `README.md`
- `docs/ONE_TURN_ADOPTION_BRIEF.md`
- `docs/NON_TECHNICAL_USER_KEY_GUIDE_KO.md`
- `docs/KEY_LOSS_AND_ROTATION.md`
- `scripts/01_generate_origin_key_WINDOWS.bat`

C6 `b921f1062cb8efcd3a9d767912300bd2006fbdf7`

Message: `test(canon): compression / misread / anti-overclaim gate`

Files changed:

- `tests/test_canonical_compression.py`

C7: this audit-log commit.

Message: `chore(audit): final audit log + git bundle`

Files changed:

- `audit/V0_4_0_AUDIT_LOG.md`

The C7 commit SHA is assigned by GitHub after this file is committed and is therefore reported in the final Codex response rather than embedded self-referentially here.

## Commands and Outputs

### Workspace Verification

Command: `Get-Location`

Output:

```text
C:\Users\Administrator\Documents\Codex\2026-06-10\files-mentioned-by-the-user-txt-2
```

Command: `Get-ChildItem -Force`

Output summary:

```text
outputs/
work/
```

Command: `Get-Command git -ErrorAction SilentlyContinue`

Output:

```text
<empty>; git unavailable on PATH
```

Command: `Test-Path README.md; Test-Path tools; Test-Path tests; Test-Path docs; Test-Path creator_theory_operational_manifest.json; Test-Path .git`

Output:

```text
False
False
False
False
False
False
```

### GitHub Connector Verification

Command/tool: GitHub `_get_profile`

Output summary:

```text
Authenticated as SystemOriginArchive.
```

Command/tool: GitHub `_get_repo` for `SystemOriginArchive/creator-theory-operational-canon`

Output summary:

```text
Repository exists; default branch main; permissions include admin and push.
```

Command/tool: GitHub `_create_branch`

Output:

```text
feature/v0.4.0-prov-k-layer created from 52ace6aa613c734f63338e4d1b75287aa35437b1.
```

### Public GitHub Metadata Reads

Command: `Invoke-RestMethod https://api.github.com/repos/SystemOriginArchive/creator-theory-operational-canon/git/commits/52ace6aa613c734f63338e4d1b75287aa35437b1`

Output summary:

```text
commit sha: 52ace6aa613c734f63338e4d1b75287aa35437b1
tree sha: 25cdcfabd37b9e6788d991cf0802a2611b01f974
parent sha: cca742f9b1fd789ecfa00764a76abddc027c298b
```

Command: recursive tree read for `25cdcfabd37b9e6788d991cf0802a2611b01f974`

Output summary:

```text
Repository tree read successfully. Relevant top-level paths included README.md, docs, tools, tests, releases, v0.3.0, v0.3.1, v0.3.2, creator_theory_operational_manifest.json, and .github workflows.
```

### C1 Acceptance Tests

Required commands:

```bash
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile canon
python3 tools/validate_vectors.py --repo-root . --tests-dir tests --profile benchmark
python3 tools/validate_derivative_laundering_vectors.py --repo-root .
python3 tools/run_adversarial_simulation.py --tests-dir tests
```

Actual output:

```text
NOT RUN in this environment.
Reason: no local repository checkout, no local .git directory, no local git executable, and no python/python3 executable available on PATH.
```

Mandatory TEST_ANCHOR negative check:

```text
NOT RUN in this environment.
Reason: it requires a local checkout and temporary file mutation with guaranteed restore.
```

### Per-Commit Test Runs

After C1:

```text
NOT RUN; local test environment unavailable as described above.
```

After C2:

```text
NOT RUN; local test environment unavailable as described above.
```

After C3:

```text
NOT RUN; local test environment unavailable as described above.
```

After C4:

```text
NOT RUN; local test environment unavailable as described above.
```

After C5 validator re-run:

```text
NOT RUN; local test environment unavailable as described above.
```

After C6:

```text
NOT RUN; local test environment unavailable as described above.
```

No green test result is claimed by this audit log.

### Hash Computation for Retro Manifests

Command: `Invoke-WebRequest` reads of current GitHub raw files under `releases/`, `v0.3.0/`, and `v0.3.1/`, followed by local SHA-256 computation over returned bytes.

Output summary:

```text
releases/v0.1.0_RELEASE_NOTES.md b4ddd497b06844f2b044951ba540d05906a1d2c1d2cbb665a0982bf28cb8f668
releases/v0.1.1_FINAL_AUDIT.md 0214592f226a027a285579a96f475d3a7436460aaffefa8ea18a4673928107c7
releases/v0.2.0_FINAL_AUDIT.md 9e8e5fa1930d6dfc618a6832938b374ead0b19d4f5646b8803b4a1c572c27340
v0.3.0/* files hashed and recorded in provenance/manifests/v0.3.0-retro-reconstruction.json
v0.3.1/* files hashed and recorded in provenance/manifests/v0.3.1-retro-reconstruction.json
```

Generated retro manifest file hashes for chaining:

```text
releases-retro-reconstruction.json 8a309fa542a3e5ff5bf70bc01dede4bd8ea5a743017081416000a86e5907f1bd
v0.3.0-retro-reconstruction.json 7f502ec20e510be526b5f17927110e8ce5c92518bf29d94d8d8d6214afbd8bef
v0.3.1-retro-reconstruction.json 0a63ba7d100f67765e2b137c621de14f8ef4f725c04ba7a85316454f5ee0fa09
```

## Deviations

1. Local checkout operations were replaced by GitHub connector mode.

Reason: the active workspace was not the repository checkout and `git` was unavailable. The user explicitly made connector mode higher priority than the original v2 directive.

Functional equivalence: changes were made only inside the existing GitHub repository on `feature/v0.4.0-prov-k-layer`, not on `main`.

2. The original `Never push to any remote` constraint could not coexist with connector-mode implementation.

Reason: GitHub connector writes create remote branch commits. The user explicitly selected connector mode after acknowledging no local checkout/git.

Functional equivalence: no merge, no tag, and no direct `main` modification occurred.

3. Local test execution after every commit was unavailable.

Reason: no local checkout, no `git`, no `python`, and no `python3` on PATH.

Functional equivalence: test files and validators were added/updated, but this run honestly records that they were not executed here.

4. The mandatory local `git bundle create` step was not performed.

Reason: no local checkout and no `git` executable.

Functional equivalence: none claimed. The branch exists remotely; the bundle remains a user/auditor follow-up from a real checkout.

5. Retro manifests use a JSON `_notice` field rather than an invalid top-of-file JSON comment.

Reason: JSON does not support comments and the directive also requires JSON parseability.

Functional equivalence: the exact reconstruction-scaffold warning is present at the top of each manifest object while preserving valid JSON.

6. During C2/C3 preparation, draft connector commits were superseded by corrected commits before continuing.

Reason: pre-test reasoning found signature-payload ordering bugs for manifest signing and rotation signing.

Functional equivalence: the final branch history contains the intended logical C2 and C3 commits with corrected payload semantics.

## Environment Notes

Local shell: Windows PowerShell.

Local `git`: unavailable.

Local `python` / `python3`: unavailable on PATH.

Node REPL: attempted for in-memory JSON generation and exited unexpectedly with `windows sandbox failed: spawn setup refresh`.

`cryptography` package availability: unknown in this environment because Python was unavailable.

Network: restricted by default; public GitHub metadata/raw reads were performed only after sandbox escalation approval.

## Skipped Items

- C1 validator commands: skipped, no local checkout/Python.
- C1 TEST_ANCHOR negative mutation: skipped, no local checkout/Python and no local repo file to restore.
- Post-commit full test suite after every commit: skipped, no local checkout/Python.
- C5 validator re-run: skipped, no local checkout/Python.
- Local git bundle creation: skipped, no local checkout/git.

## Audit-Required Flags

The auditor must perform a line-by-line review of `scripts/01_generate_origin_key_WINDOWS.bat` before any user execution.

The helper script is committed for review only.

Codex did not execute the helper script.

The helper script creates a real key only if the human user runs it after audit and types `YES_CREATE_REAL_ORIGIN_KEY`.

## User TODO

1. Wait for auditor pass.
2. From a real local checkout, run the full validator/test suite.
3. From a real local checkout, run the TEST_ANCHOR negative check with guaranteed restore.
4. From a real local checkout, create the requested git bundle.
5. Generate the real keypair offline only after auditor approval.
6. Sign `docs/ATTRIBUTION_STATEMENT.md` after key creation.
7. Sign retro manifests via `tools/prov_k/sign.py` only after review.
8. Review the feature branch.
9. Merge only after review and test confirmation.

## Follow-Up Fix Commit

Commit: assigned by GitHub after this audit append is committed.

Message: `fix(prov-k): harden key format and fingerprint verification`

Reason for fix:

- The Windows helper script can produce OpenSSH-format Ed25519 keys.
- PROV-K loaders previously accepted only PEM key material.
- Manifest signature verification did not explicitly fail closed when the supplied public key did not match `manifest["signing"]["public_key_fingerprint"]`.

Files changed:

- `tools/prov_k/keys.py`
- `tools/prov_k/sign.py`
- `tools/prov_k/verify.py`
- `tests/test_prov_k_negative_regression.py`
- `docs/PROV_K_LAYER.md`
- `docs/NON_TECHNICAL_USER_KEY_GUIDE_KO.md`
- `audit/V0_4_0_AUDIT_LOG.md`

Test status:

```text
NOT RUN in this environment.
Reason: no local repository checkout, no local .git directory, no local git executable, and no python/python3 executable available on PATH.
```

Regression coverage added for later local execution:

- signed manifest with mismatched valid-looking public key fingerprint must fail;
- PEM Ed25519 private/public key loading positive control;
- OpenSSH Ed25519 private/public key loading and manifest verification positive control when `cryptography` is available.

Safety confirmations:

```text
No real key was generated.
ssh-keygen was not executed.
scripts/01_generate_origin_key_WINDOWS.bat was not executed.
No merge, tag, release, or main-branch modification was performed.
```
## Follow-Up Fix Commit - Retro Manifests and CI

Commit: assigned by GitHub after this audit append is committed.

Message: `fix(prov-k): regenerate retro manifests and enforce CI`

Reason for fix:

- `provenance/manifests/v0.3.0-retro-reconstruction.json` had `files[]` entries that did not satisfy the path sort order enforced by `validate_manifest_data`.
- The retro manifest chain had stale `prev_manifest_sha256` values that did not match the actual SHA-256 of the previous committed manifest file bytes.
- `.github/workflows/validation.yml` did not run the PROV-K negative regression suite, canonical compression suite, or retro chain integrity suite during pull request / merge validation.

Files changed:

- `.github/workflows/validation.yml`
- `audit/V0_4_0_AUDIT_LOG.md`
- `docs/PROV_K_LAYER.md`
- `provenance/manifests/releases-retro-reconstruction.json`
- `provenance/manifests/v0.3.0-retro-reconstruction.json`
- `provenance/manifests/v0.3.1-retro-reconstruction.json`
- `tests/test_retro_chain_integrity.py`

Regenerated manifest hashes:

```text
releases-retro-reconstruction.json 8a309fa542a3e5ff5bf70bc01dede4bd8ea5a743017081416000a86e5907f1bd
v0.3.0-retro-reconstruction.json 7f502ec20e510be526b5f17927110e8ce5c92518bf29d94d8d8d6214afbd8bef
v0.3.1-retro-reconstruction.json 0a63ba7d100f67765e2b137c621de14f8ef4f725c04ba7a85316454f5ee0fa09
```

Chain verification status:

```text
releases-retro-reconstruction.json prev_manifest_sha256 = null
v0.3.0-retro-reconstruction.json prev_manifest_sha256 matches releases-retro-reconstruction.json committed-byte SHA-256: 8a309fa542a3e5ff5bf70bc01dede4bd8ea5a743017081416000a86e5907f1bd
v0.3.1-retro-reconstruction.json prev_manifest_sha256 matches v0.3.0-retro-reconstruction.json committed-byte SHA-256: 7f502ec20e510be526b5f17927110e8ce5c92518bf29d94d8d8d6214afbd8bef
```

Audit consistency status:

```text
The earlier explicit retro manifest hash table in this audit log was corrected to the regenerated committed-byte hashes so audit-log hash claims match repository bytes.
```

Test status:

```text
NOT RUN in this environment.
Reason: no local repository checkout, no local .git directory, no local git executable, and no python/python3 executable available on PATH.
```

Connector-side preflight status:

```text
Retro source file SHA-256 values were computed from GitHub contents API bytes on feature/v0.4.0-prov-k-layer.
Retro manifest JSON was generated in the same two-space, trailing-newline file-byte form used by tools/prov_k/manifest.py manifest_file_bytes.
The generated chain hashes above were computed from the exact manifest bytes prepared for this commit.
```

CI wiring status:

```text
.github/workflows/validation.yml now installs cryptography and runs:
python3 -m tests.test_prov_k_negative_regression
python3 -m tests.test_canonical_compression
python3 -m tests.test_retro_chain_integrity
No non-zero exit codes are swallowed by these steps.
```

Safety confirmations:

```text
No real key was generated.
ssh-keygen was not executed.
scripts/01_generate_origin_key_WINDOWS.bat was not executed.
main was not modified.
No merge, tag, or release was created.
```
## v0.4.1 PROV-K Hardening Follow-Up

Branch: `feature/v0.4.1-prov-k-hardening`

Commit hash: assigned by GitHub after this self-referential audit entry is committed; the final branch-head commit hash is reported in the Codex response.

Message: `fix(prov-k): harden signing, rotation, and historical-proof gates`

Reason for fix:

- `sign_manifest_data` allowed `UNSIGNED_DRAFT` manifests to receive signatures, creating a contradictory signed-draft state.
- `verify_rotation_record` verified the old-key signature but did not require the supplied previous public key fingerprint to match `rotation.old_public_key_fingerprint`.
- Python manifest validation and CLI build routing could still create or accept `historical_proof: true`, while the schema has no legitimate historical-proof path.
- Fable5 audit follow-up found remaining release-state inconsistencies on current `main`.

Fable5 follow-up audit status:

```text
1. K3 runtime owner identification file was still marked draft/not_released while also listed in released artifacts; fixed by moving it out of released artifacts and into draft_artifacts while preserving is_release_artifact=false.
2. No singular invalid_reinterpretation manifest key was present on current main, but validator hardening now rejects that alias and requires invalid_reinterpretations explicitly.
3. Stale current-release routing references to v0.2.0 remained in CANONICAL_STATUS.md, VERSION_POLICY.md, CITATION.md, and LLM_CANONICAL_CONTEXT.md; fixed to route current release to v0.3.0 and current hardening to v0.3.1 while preserving v0.2.0 as the previous adoption/compression baseline.
4. Direct text scan did not find a current v0.3.0-rc.1 routing reference.
```

Changed files:

- `CANONICAL_STATUS.md`
- `CITATION.md`
- `LLM_CANONICAL_CONTEXT.md`
- `VERSION_POLICY.md`
- `audit/V0_4_0_AUDIT_LOG.md`
- `creator_theory_operational_manifest.json`
- `tests/test_prov_k_negative_regression.py`
- `tools/prov_k/cli.py`
- `tools/prov_k/manifest.py`
- `tools/prov_k/rotate.py`
- `tools/prov_k/sign.py`
- `tools/validate_vectors.py`

Test status:

```text
NOT RUN in this environment.
Reason: no local repository checkout, no local .git directory, no local git executable, and no python/python3 executable available on PATH.
```

CI status:

```text
Existing CI already runs:
python3 -m tests.test_prov_k_negative_regression
python3 -m tests.test_canonical_compression
python3 -m tests.test_retro_chain_integrity
New v0.4.1 regression checks were added to tests/test_prov_k_negative_regression.py, so no new CI command was required.
```

Schema-load consistency note:

```text
jsonschema dependency was not added in this hardening commit to avoid expanding CI dependency policy beyond the requested cryptography installation. TODO: add schema-load consistency coverage if jsonschema becomes an approved CI dependency.
```

Safety confirmations:

```text
No real key was generated.
ssh-keygen was not executed.
scripts/01_generate_origin_key_WINDOWS.bat was not executed.
No tag or release was created.
main was not modified directly.
No merge was performed.
```