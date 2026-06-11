# Release Process

## Scope

This document describes the human-owner process for declaring, signing, publishing, and anchoring a signed PROV-K release.

Release signing is a user-only post-audit action. AI agents, CI jobs, and repository automation do not generate keys, do not touch private keys, and do not sign releases. The PROV-K boundary rules in [PROV_K_LAYER.md](PROV_K_LAYER.md) apply throughout.

## Manifest Location Policy

Manifest storage is determined by `provenance_class`:

```text
current_release            -> GitHub Release asset only; never committed to the repository tree
retroactive_reconstruction -> committed under provenance/manifests/ as UNSIGNED_DRAFT
```

Rationale for keeping the signed `current_release` manifest out of the tree: the manifest records SHA-256 hashes of repository files at the tagged commit. Committing the signed manifest back into the same tree changes the tree it describes and creates drift between the reviewed signed bytes and the committed bytes. The release asset is the single canonical copy.

`provenance/manifests/` is reserved for `retroactive_reconstruction` manifests only. These remain `UNSIGNED_DRAFT` with `awaiting_user_signature = true` and are regenerated only through `tools/prov_k/retro_build.py`, never by hand-editing JSON.

## Layer Constant and Release Label

The manifest `layer` field stays fixed at `v0.4.0-prov-k`. New releases move the `release_label` only. Do not bump the layer constant as part of an ordinary release.

## Signing Flow

The flow is explicit and review-gated:

1. **Build an unsigned draft** at the commit intended for release:

   ```bash
   python3 -m tools.prov_k.cli build \
     --repo-root . \
     --release-label vX.Y.Z \
     --output /path/outside/repo/vX.Y.Z-current-release.json \
     --provenance-class current_release \
     --origin-attribution Lee_Yu_Cheol \
     --awaiting-user-signature
   ```

   Write the draft to a path outside the repository tree so the build does not alter the tree being sealed.

2. **Review the exact draft bytes**: release label, file list, hashes, attribution, boundary flags.

3. **Sign the reviewed draft** with `--declare-release`. This is the only supported transition from a reviewed `UNSIGNED_DRAFT` to `SIGNED_RELEASE`:

   ```bash
   python3 -m tools.prov_k.cli sign \
     --repo-root . \
     --manifest /path/outside/repo/vX.Y.Z-current-release.json \
     --private-key /path/outside/repo/origin_ed25519 \
     --declare-release
   ```

   The private key must resolve outside the repository working directory; the CLI refuses inside-repo private-key paths. Do not rebuild the manifest after review, and do not edit the signed JSON by hand.

4. **Verify the signed manifest** against the public key and the pinned fingerprint in [TRUST_ANCHOR.md](TRUST_ANCHOR.md):

   ```bash
   python3 -m tools.prov_k.cli verify \
     --repo-root . \
     --manifest /path/outside/repo/vX.Y.Z-current-release.json \
     --public-key /path/to/origin_ed25519.pub
   ```

5. **Tag the release commit** (`vX.Y.Z`) and create the GitHub Release for that tag.

6. **Upload release assets**: the signed manifest (`vX.Y.Z-current-release.json`) and the origin public key (`origin_ed25519.pub`). Do not commit the signed manifest to the repository tree.

7. **Anchor the release** in a follow-up reviewed pull request that updates [TRUST_ANCHOR.md](TRUST_ANCHOR.md) with the release label, tagged commit, asset names, manifest SHA-256, and (unchanged unless rotated) public key fingerprint.

## Prohibitions

```text
No private key inside the repository tree.
No signing by AI agents, CI, or automation.
No --status SIGNED_RELEASE rebuilds after review; use sign --declare-release on the reviewed draft.
No hand-editing of manifest JSON; regenerate retro manifests via tools/prov_k/retro_build.py.
No committing current_release manifests under provenance/manifests/.
No HMAC signing path; production signing is Ed25519 via the cryptography package only.
```

## Completed Reference

The `v0.4.1` release followed this process. Its anchored values (tag commit, asset names, manifest SHA-256, key fingerprint) are pinned in [TRUST_ANCHOR.md](TRUST_ANCHOR.md). No additional signing, tagging, or asset upload remains outstanding for `v0.4.1`.
