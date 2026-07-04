# v0.5.0 Release Execution Runbook (Owner-Only)

Status: pre-release preparation aid. NO RELEASE PERFORMED by this document. The v0.5.0 release, git
tag, signature, signed manifest, release assets, and trust-anchor entry are NOT created yet. Every step
below is a **human-owner** action executed **owner-locally**; AI agents, CI, and automation perform none
of them.

This document carries the standard documentation boundary stated at the top of
`docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority; no replacement of any canonical
source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding —
and no new release or tag by this file. v0.5.0 disposition here is **release candidate / pre-release
target only**.

Authoritative procedure: [docs/RELEASE_PROCESS.md](../docs/RELEASE_PROCESS.md). This runbook expands that
procedure into an owner command checklist and MUST stay consistent with it. Where this runbook differs,
the difference is listed explicitly in "Differences from docs/RELEASE_PROCESS.md" below; the canonical
procedure is not modified retroactively.

---

## Token-avoidance note (HARD STOP 2)

Committed repository files must not carry the signed-release-asset status token in any field or filename.
Therefore, in the commands below:

- the release provenance-class value is shown as the placeholder `<RELEASE_CLASS>`, and
- the release-asset manifest filename is shown as the placeholder `v0.5.0-<RELEASE_ASSET>.json`.

The canonical literal values for both live in [docs/RELEASE_PROCESS.md](../docs/RELEASE_PROCESS.md)
(Manifest Location Policy and Signing Flow). The owner substitutes the literal value/filename locally at
execution time. Nothing in this repository tree needs to contain the literal token.

---

## Manifest location policy (asset-only)

Per docs/RELEASE_PROCESS.md, the signed release-asset manifest is a **GitHub Release asset only** and is
**never committed to the repository tree**. Rationale: the manifest records SHA-256 hashes of repository
files at the tagged commit; committing the signed manifest back into the same tree would change the tree
it describes. The single canonical copy is the release asset. `provenance/manifests/` is reserved for
`retroactive_reconstruction` drafts only and is not used by this release.

The committed file `releases/v0.5.0_COVERAGE_PROPOSAL_PREVIEW_FOR_OWNER_REVIEW.json` is a coverage
proposal preview (not a manifest, not a release asset). It exists only to let the owner review scope and
per-file SHA-256 in advance; the final manifest is generated owner-locally via the prov_k toolchain as a
release asset only and is never committed to the tree.

---

## Preconditions

```text
P0  Release-candidate audit of main is green:
      python tests/test_release_candidate_audit.py
      python -m tests... (full suite per docs/RELEASE_PROCESS.md / CI)
P1  License policy decision resolved by owner (docs/LICENSE_POLICY_DRAFT.md is NOT A LICENSE).
P2  Zenodo <-> GitHub integration is ON for this repository BEFORE the GitHub Release is published,
    so the DOI is minted against the published release (with assets attached).
P3  Owner holds the origin Ed25519 private key OUTSIDE the repository tree. The public-key fingerprint
    pinned in docs/TRUST_ANCHOR.md is unchanged (no key rotation); the canon-kernel seal text is
    therefore unchanged.
P4  The signing clone's working-tree bytes equal the git blob bytes (no line-ending drift). See the
    "Byte-source / line-ending guard" section; this is REQUIRED before building the manifest.
```

Key paths below are placeholders. Do not write real key values, real key paths, or machine-specific
information into any committed file.

---

## Byte-source / line-ending guard (REQUIRED before building the manifest)

PROV-K seals SHA-256 over exact file bytes. The repository's established convention seals **raw git
blob bytes** (LF), evidenced by the committed `provenance/manifests/` retro manifests and the v0.4.1
signed release assets. A clone checked out with `core.autocrlf=true` has **CRLF** working-tree bytes for
text files; because `tools/prov_k` hashes `path.read_bytes()` from the working tree, signing from such a
clone would seal CRLF hashes. Those hashes then fail verification in an external verifier's standard
(LF) checkout — breaking the "anyone can verify offline" property. `.gitattributes` exempts only
`provenance/manifests/*.json` (`-text`); all other text files are affected.

The signing environment MUST be one of:

```text
a) a FRESH clone with core.autocrlf=false (blob bytes land in the working tree unchanged), or
b) the existing clone reconfigured and re-materialized:
     git config core.autocrlf false
     git rm --cached -r .        # drop the index's crlf-smudged entries
     git reset --hard            # re-checkout blob bytes without conversion
   then reconfirm canonical bytes as below.
```

Before building the manifest, prove working-tree bytes equal git blob bytes for at least one covered
text file (repeat for a few; all must match):

```bash
# blob bytes (object database) vs working-tree bytes must be identical:
git cat-file blob <RELEASE_COMMIT_SHA>:canon-kernel.json | sha256sum
sha256sum canon-kernel.json
# The two SHA-256 values MUST be equal. If they differ, the clone has line-ending
# drift; STOP and fix per (a)/(b) above before building or signing.
```

Rationale: this inherits the git-blob-byte convention of the v0.4.1 assets and the retro manifests. A
mismatch guarantees external-verification failure.

---

## Execution steps (owner-local)

### 1. (Precondition gate) Confirm Zenodo–GitHub integration is ON

Confirm in the Zenodo account (GitHub tab) that this repository's toggle is ON **before** publishing the
GitHub Release. Publishing with the toggle OFF mints no DOI for the release.

### 2. Build the final manifest owner-locally (outside the tree)

First satisfy the "Byte-source / line-ending guard" above (working-tree bytes == git blob bytes). Then:

```bash
python -m tools.prov_k.cli build \
  --repo-root . \
  --release-label v0.5.0 \
  --provenance-class <RELEASE_CLASS> \
  --origin-attribution Lee_Yu_Cheol \
  --awaiting-user-signature \
  --output <OUTSIDE_REPO_DIR>/v0.5.0-<RELEASE_ASSET>.json
```

`<OUTSIDE_REPO_DIR>` is any path outside the repository working tree, so the build does not alter the
tree being sealed. Review the exact draft bytes: release label, whole-repository file list, hashes,
attribution, boundary flags, `signature.value = null`, `historical_proof = false`.

### 3. Sign the reviewed draft owner-locally

```bash
python -m tools.prov_k.cli sign \
  --repo-root . \
  --manifest <OUTSIDE_REPO_DIR>/v0.5.0-<RELEASE_ASSET>.json \
  --private-key <OUTSIDE_REPO_DIR>/origin_ed25519 \
  --declare-release
```

The private key MUST resolve outside the repository working directory; the CLI refuses inside-repo
private-key paths. Do not rebuild the manifest after review, and do not hand-edit the signed JSON.

### 4. Verify the signed manifest against the pinned trust anchor

```bash
python -m tools.prov_k.cli verify \
  --repo-root . \
  --manifest <OUTSIDE_REPO_DIR>/v0.5.0-<RELEASE_ASSET>.json \
  --public-key <OUTSIDE_REPO_DIR>/origin_ed25519.pub
```

Confirm the public-key fingerprint equals the pinned value in docs/TRUST_ANCHOR.md
(`sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c`). A mismatch is a stop.

### 5. Tag, create a DRAFT GitHub Release, attach assets, then publish

Attach the two assets to a DRAFT release first, so the assets are present before publish and Zenodo
captures the asset-included state.

```bash
git tag v0.5.0 <RELEASE_COMMIT_SHA>
git push origin v0.5.0

# Draft release (not yet public), then upload the two assets:
gh release create v0.5.0 --draft --title "v0.5.0" --notes-file releases/v0.5.0_RELEASE_NOTES_DRAFT.md
gh release upload v0.5.0 \
  <OUTSIDE_REPO_DIR>/v0.5.0-<RELEASE_ASSET>.json \
  <OUTSIDE_REPO_DIR>/origin_ed25519.pub

# Confirm both assets are attached to the draft:
gh release view v0.5.0 --json assets

# Publish only after the two assets are confirmed attached:
gh release edit v0.5.0 --draft=false
```

Do NOT commit the signed manifest to the repository tree at any point. The signed manifest and
`origin_ed25519.pub` exist as release assets only.

### 6. Re-verify the published release assets

Download the two published assets to a fresh outside-repo directory and re-run step 4's verify against
the downloaded bytes; recompute the manifest SHA-256 for the trust-anchor record.

### 7. Confirm the Zenodo DOI

Confirm Zenodo minted a DOI for the published v0.5.0 release and that the DOI record includes the
attached assets.

### 8. Post-release follow-up PRs (separate, reviewed; not part of release publication)

```text
- docs/TRUST_ANCHOR.md   : APPEND a v0.5.0 anchor entry (release label, tag, tagged commit, asset
                           names, manifest SHA-256, unchanged key fingerprint). Append only; the
                           v0.4.1 entry stays.
- VERSION_POLICY.md      : move v0.5.0 from pre-release target to its post-release status.
- README.md              : update the Status section.
- AGENTS.md              : update the release-boundary labels.
- CITATION.md / CITATION.cff : record the Zenodo DOI.
```

Each is a separate human-reviewed PR after the release exists. None is performed by PR-N.

### 9. External archival

```text
- Software Heritage: "Save code now" for the tagged commit.
- archive.org (Wayback): save the release page and the repository README.
```

---

## Differences from docs/RELEASE_PROCESS.md

```text
D1  Token placeholders: this committed runbook uses <RELEASE_CLASS> and v0.5.0-<RELEASE_ASSET>.json in
    place of the literal signed-release-asset token that docs/RELEASE_PROCESS.md prints verbatim. Reason:
    HARD STOP 2 (no signed-release status token in committed files), preserved without relaxation. The
    canonical literals remain in docs/RELEASE_PROCESS.md; the owner substitutes them locally.
D2  Draft-first GitHub Release: this runbook makes the gh CLI draft-release path explicit (create draft
    -> upload assets -> confirm -> publish) so assets are attached before publish and Zenodo captures
    them. docs/RELEASE_PROCESS.md step 5-6 states "create the GitHub Release" and "upload assets" without
    prescribing draft-first ordering; this runbook refines the ordering and does not contradict it.
D3  Zenodo / SWH / archive.org steps (P2, 7, 9) are added operational detail not present in
    docs/RELEASE_PROCESS.md; they add archival actions and change none of its signing/anchoring rules.

docs/RELEASE_PROCESS.md is not modified by PR-N. If the owner wants these refinements folded into the
canonical procedure, that is a separate reviewed PR after the release.
```

---

## Root cause and prov_k follow-up

```text
Root cause: tools/prov_k hashes working-tree bytes (path.read_bytes()). Under core.autocrlf=true the
working tree holds CRLF for text files, so manifest generation is line-ending dependent and can diverge
from the git-blob-byte convention that the v0.4.1 assets and retro manifests follow.

This PR does NOT modify the tool. It adds the byte-source / line-ending guard above so the owner signs
from a blob-consistent clone.

Separate-PR candidate (not part of PR-N): add a git-blob hash mode to tools/prov_k (hash
`git cat-file blob <rev>:<path>` bytes instead of working-tree bytes), making manifest generation
independent of checkout line-ending settings. Until then, the guard is mandatory.
```

---

## Absolute prohibitions (unchanged)

```text
No private key inside the repository tree.
No signing by AI agents, CI, or automation.
No committing the signed release-asset manifest into the tree (asset-only).
No hand-editing of manifest JSON; build/sign via the prov_k toolchain.
No git tag, GitHub Release, or signed manifest created by PR-N.
No docs/TRUST_ANCHOR.md edit in PR-N (append happens only in a post-release reviewed PR).
No real key values, key paths, or machine-specific information in any committed file.
No signing from a clone whose working-tree bytes differ from git blob bytes (line-ending drift).
```

End of file.
