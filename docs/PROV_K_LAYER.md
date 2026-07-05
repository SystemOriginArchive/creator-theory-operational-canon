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

## Manifest Location Policy

Manifest storage is determined by `provenance_class`:

1. `current_release` manifests are published as GitHub Release assets only. They are never committed to the repository tree, because a signed manifest records hashes of tree files at the tagged commit and committing it back into that tree changes the tree it describes.
2. `retroactive_reconstruction` manifests are committed under `provenance/manifests/` as `UNSIGNED_DRAFT` with `awaiting_user_signature = true`.
3. `experiment_artifact` manifests classify adoption drift experiment records and summaries produced under `experiments/`. They stay `UNSIGNED_DRAFT`; release and rotation statuses are rejected for this class, so they cannot enter the release signing flow and have no effect on the trust anchor. They are not committed under `provenance/manifests/`.

`provenance/manifests/` is reserved for `retroactive_reconstruction` manifests only.

`experiment_artifact` manifests support bounded verification: `verify --scope-prefix <repo-relative-prefix>` limits the strict unmanifested-files scan to the given prefix (repeatable). The option is rejected for `current_release` and `retroactive_reconstruction` manifests, whose verification stays whole-repository. Experiment artifact verification results are candidate-signal infrastructure only and are not adoption verdicts.

The pinned verification fingerprint and the current anchored release are recorded in [TRUST_ANCHOR.md](TRUST_ANCHOR.md). The full signing and publication flow is documented in [RELEASE_PROCESS.md](RELEASE_PROCESS.md).

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

## Release Declaration Flow

The signing flow is explicit:

1. Build an unsigned draft manifest.
2. Review the exact draft content and file list.
3. Sign the reviewed draft with `prov_k sign --declare-release`.
4. Verify the signed manifest with the public key.

The `--declare-release` flag is the only supported transition from a reviewed `UNSIGNED_DRAFT` manifest to a signed `SIGNED_RELEASE` manifest.

Do not rebuild the manifest with `--status SIGNED_RELEASE` after review. Rebuilding can change reviewed bytes such as timestamps, file ordering, and canonical signing payload inputs. The reviewed draft should be the object that receives the explicit release declaration.

Without `--declare-release`, direct signing of `UNSIGNED_DRAFT` remains forbidden. `DISPUTED` and `EMERGENCY_REASSERTED` manifests are not accepted by release declaration signing.

Example:

```bash
python3 -m tools.prov_k.cli build \
  --repo-root . \
  --release-label v0.4.1 \
  --output provenance/manifests/v0.4.1-current-release.json \
  --provenance-class current_release \
  --origin-attribution TEST_ORIGIN \
  --awaiting-user-signature

python3 -m tools.prov_k.cli sign \
  --repo-root . \
  --manifest provenance/manifests/v0.4.1-current-release.json \
  --private-key /path/outside/repo/origin_ed25519 \
  --declare-release

python3 -m tools.prov_k.cli verify \
  --repo-root . \
  --manifest provenance/manifests/v0.4.1-current-release.json \
  --public-key /path/to/origin_ed25519.pub
```

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

PROV-K seals exact recorded bytes, not semantic equivalence. JSON key order, whitespace, and trailing newlines matter whenever SHA-256 is computed over manifest bytes; regenerate manifests through `tools/prov_k/retro_build.py` rather than hand-editing JSON.

Line endings are part of the sealed bytes. Committed manifests under `provenance/manifests/` are marked `-text` in `.gitattributes` so checkouts on any platform preserve the exact committed LF bytes instead of converting them to platform line endings.

Online hash converters, pasted LLM-provided hash strings, or inferred hashes are not valid provenance data.

## Byte-Source: Working Tree vs. git-blob (opt-in)

`build` and `verify` accept an opt-in `--hash-source {worktree,git-blob}` flag (default `worktree`) with a companion `--git-rev` (default `HEAD`).

The default `worktree` mode is unchanged: hashes are computed over local working-tree file bytes exactly as before. Omitting the flag produces byte-identical output to prior behavior.

`git-blob` mode computes each SHA-256 over the committed blob bytes of the file at `--git-rev`, read from the git object database (`git cat-file blob <rev>:<path>`) rather than from the working tree. Its purpose is checkout line-ending independence: because working-tree bytes can be altered by `core.autocrlf` line-ending conversion on checkout, hashing them can diverge from the raw git blob bytes that repository signing conventions seal. Reading the blob at a pinned revision removes that checkout-dependent variance. Repo-relative paths are normalized to POSIX form before building the object spec, so the same command works on Windows and POSIX checkouts. A path or revision with no blob fails closed with an error; there is no silent fallback to working-tree bytes.

The meaning is precisely bounded. `git-blob` verify checks the committed blob bytes of the specified revision. It does not verify working-tree bytes, and it does not attest that the working tree is clean — a repository with uncommitted or divergent working-tree changes can still pass `git-blob` verification, because that mode does not read the working tree for hashing. Use `worktree` mode when the property under test is the state of the checkout itself.

The `git-blob` flag changes only the hash byte source. Path enumeration is unchanged: the listed-path existence check and the strict unmanifested-files scan (`_actual_paths`) stay working-tree based in both modes. This is the byte-source-independent verification path recorded in [audit/V0_5_0_POST_RELEASE_LESSONS.md](../audit/V0_5_0_POST_RELEASE_LESSONS.md) L1; the follow-up `prov_k` git-blob hash mode anticipated there is this flag.

## Non-Replacement Boundary

The manifest schema requires:

```text
replaces_creator_theory_high_frame = false
replaces_recursive_self_improvement_layer = false
layer_scope = L2/L3 provenance sealing only
```

Any manifest that flips either replacement flag is invalid under this operational canon.
