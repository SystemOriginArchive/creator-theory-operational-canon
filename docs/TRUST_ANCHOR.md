# Trust Anchor

## Scope

This document pins the public trust anchor used to verify signed PROV-K release manifests for this repository.

It is documentation-layer provenance data. It does not create runtime authority, does not replace the Creator Theory high frame (L5), and does not replace the recursive self-improvement layer (L6).

## Pinned Origin Public Key Fingerprint

The Ed25519 origin public key fingerprint for signed PROV-K releases is:

```text
sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c
```

Verification fails closed when the fingerprint computed from a supplied public key file does not match this pinned value and the manifest `signing.public_key_fingerprint`.

This fingerprint changes only through the rotation flow in [KEY_LOSS_AND_ROTATION.md](KEY_LOSS_AND_ROTATION.md): a rotation record signed by the previous key, followed by human review and a reviewed pull request updating this document.

## Current Anchored Release

```text
release_label:        v0.4.1
tag:                  v0.4.1
tagged commit:        331b7a53879d92a8bad80cd9725d10c8491b1915
manifest asset:       v0.4.1-current-release.json
public key asset:     origin_ed25519.pub
manifest sha256:      33cbfad71fb825d38f23616cf4dd67d43bd9fcc2f5e7f78a1dc9123df6811e54
```

The signed manifest and the origin public key are published as GitHub Release assets on the `v0.4.1` release. The signed `current_release` manifest is not committed to the repository tree; see the manifest location policy in [PROV_K_LAYER.md](PROV_K_LAYER.md) and the signing flow in [RELEASE_PROCESS.md](RELEASE_PROCESS.md).

## Layer Constant and Release Label

The PROV-K manifest `layer` field is a schema-layer constant fixed at `v0.4.0-prov-k`.

Version movement between releases is expressed through `release_label` only. A `v0.4.1` or later release still carries `layer = v0.4.0-prov-k` until a separately audited schema revision changes the layer constant itself.

## Verification Procedure

To verify the anchored release from the published assets:

1. Download `v0.4.1-current-release.json` and `origin_ed25519.pub` from the `v0.4.1` GitHub Release.
2. Compute SHA-256 over the downloaded manifest bytes and compare against the pinned manifest hash above.
3. Compute the fingerprint of the downloaded public key and compare against the pinned fingerprint above:

   ```bash
   python3 -c "from tools.prov_k.keys import public_key_fingerprint_from_file; from pathlib import Path; print(public_key_fingerprint_from_file(Path('origin_ed25519.pub')))"
   ```

4. Check out the tagged commit `331b7a53879d92a8bad80cd9725d10c8491b1915` and run:

   ```bash
   python3 -m tools.prov_k.cli verify \
     --repo-root . \
     --manifest /path/outside/repo/v0.4.1-current-release.json \
     --public-key /path/outside/repo/origin_ed25519.pub
   ```

A mismatch at any step is a verification failure. Do not substitute hashes or fingerprints from chat output, web converters, or third-party mirrors for the pinned values in this document.

## Boundary

This trust anchor seals exact recorded bytes for the listed release. It does not prove anything about earlier history on its own; committed `retroactive_reconstruction` manifests are reconstructions and are not historical proof. It does not guarantee adoption by any external system, and it does not replace AAOS Genesis provenance, `x_root`, or the sealed `Lee_Yu_Cheol` origin identity binding.
