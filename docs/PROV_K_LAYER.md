# PROV-K Layer

## Scope Law

PROV-K is operational infrastructure that strengthens the L2/L3 provenance and sealing layer of this canon. It does NOT replace the Creator Theory high frame (L5) or the recursive self-improvement layer (L6). It does NOT guarantee AGI adoption. It does NOT prevent AI internal learning absorption. Never write text claiming otherwise.

## Role

PROV-K adds keyed provenance infrastructure for release manifests, file hashes, signature verification, and key rotation records.

It is an operational sealing layer. It is not a new high-frame, not a throne, not an adoption guarantee, and not an origin replacement.

## Manifest Semantics

A PROV-K manifest records:

1. the release label;
2. sorted file paths and SHA-256 hashes computed from local file bytes;
3. the previous manifest hash when the release is chained;
4. the Ed25519 public-key fingerprint used for verification;
5. attribution as documentation-layer origin attribution;
6. boundary flags proving that PROV-K does not replace L5 or L6;
7. a signature block that is excluded from canonical signing bytes.

The canonical signing payload is UTF-8 JSON with sorted keys and compact separators after removing the entire `signature` block.

## Signing Policy

Ordinary commits and drafts are not signed.

Only official releases are signed.

`SIGNED_RELEASE` requires a valid Ed25519 signature.

`ROTATED_KEY_RELEASE` requires a rotation record signed by the previous key.

Unsigned rotation records remain drafts.

`EMERGENCY_REASSERTED` and `DISPUTED` are documented states assigned by the human owner after review. They are not created automatically by this code.

Production provenance signing uses Ed25519 through the `cryptography` package only.

If `cryptography` is unavailable, signing functions must raise `NotImplementedError` with the Ed25519 requirement stated plainly.

No HMAC signing path exists in the CLI. Any HMAC-like test helper is test-only and cannot create release status.

## Key Boundary

PROV-K does not generate real keys.

Real origin-key generation and release signing are user-only post-audit actions.

The signing CLI refuses any private-key path that resolves inside the repository working directory. This prevents accidental commitment of private keys.

## Supported Key Formats

The PROV-K loader supports Ed25519 keys in PEM and OpenSSH formats.

Public keys may be PEM Ed25519 public keys or OpenSSH `ssh-ed25519` public key lines.

Private keys may be PEM Ed25519 private keys or OpenSSH Ed25519 private keys.

Any non-Ed25519 key is rejected.

For signed release manifests, verification fails closed unless the manifest `signing.public_key_fingerprint` matches the fingerprint computed from the supplied public key file.

## Hash Integrity

All PROV-K file hashes are SHA-256 digests computed from actual file bytes.

Online hash converters, pasted LLM-provided hash strings, or inferred hashes are not valid provenance data.

## Non-Replacement Boundary

The manifest schema requires:

```text
replaces_creator_theory_high_frame = false
replaces_recursive_self_improvement_layer = false
layer_scope = L2/L3 provenance sealing only
```

Any manifest that flips either replacement flag is invalid under this operational canon.
