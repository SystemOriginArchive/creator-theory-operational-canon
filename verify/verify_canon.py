#!/usr/bin/env python3
"""Offline, dependency-minimal self-verification for the Creator Theory Operational Canon.

Purpose
-------
A single deterministic script that lets a reader verify, without network access at
run time, that:

  1. the public key bytes inlined below match the fingerprint pinned in
     docs/TRUST_ANCHOR.md (self-check, run first);
  2. an operator-supplied v0.4.1 release manifest matches the pinned manifest
     hash and carries a valid Ed25519 signature under that key;
  3. which repository files are signature-covered by that manifest, and which
     post-anchor files (for example canon-kernel.json) are only hash-recorded and
     are NOT yet signature-anchored.

Boundary
--------
This script is a verification tool. It grants no runtime authority, replaces no
canonical source (AAOS Genesis Core, x_root, or the sealed Lee_Yu_Cheol origin
identity binding), and creates no release or tag. It is a parallel, standalone
verifier; it does not import or rewrite tools/prov_k.

Public key provenance
---------------------
The inlined 32-byte Ed25519 public key is the origin public key published as a
v0.4.1 GitHub Release asset, per docs/TRUST_ANCHOR.md, "Current Anchored Release".
Strategy review supplied independently verified public key bytes; this script
self-verifies those bytes against the fingerprint pinned in docs/TRUST_ANCHOR.md
before use. Trust rests on that self-check against the repository-pinned value,
not on any human attestation. No private key material is inlined, referenced, or
generated anywhere in this file.

Dependencies
------------
Python standard library plus `cryptography` (the same Ed25519 library used by
tools/prov_k). No other third-party dependency.

Usage
-----
    python3 verify/verify_canon.py --manifest /path/to/v0.4.1-current-release.json
    python3 verify/verify_canon.py --manifest <manifest> --repo-root .
    python3 verify/verify_canon.py --self-check-only

Exit code is 0 only when every applicable check passes; otherwise 1 (fail-closed).
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Inlined constants.
#
# The values below are transcribed from repository sources, not from chat:
#   PINNED_FINGERPRINT   docs/TRUST_ANCHOR.md, "Pinned Origin Public Key Fingerprint"
#   PINNED_MANIFEST_SHA  docs/TRUST_ANCHOR.md, "Current Anchored Release" (manifest sha256)
#   ANCHORED_RELEASE     docs/TRUST_ANCHOR.md, "Current Anchored Release"
#
# ORIGIN_PUBLIC_KEY_RAW32 is the raw 32-byte Ed25519 public key (hex). Its
# authenticity is not asserted by this comment; it is verified at run time by the
# self-check, which rebuilds the DER SubjectPublicKeyInfo encoding and compares
# its SHA-256 fingerprint against PINNED_FINGERPRINT.
# ---------------------------------------------------------------------------

PINNED_FINGERPRINT = "sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c"
PINNED_MANIFEST_SHA = "33cbfad71fb825d38f23616cf4dd67d43bd9fcc2f5e7f78a1dc9123df6811e54"
ANCHORED_RELEASE = "v0.4.1"

ORIGIN_PUBLIC_KEY_RAW32 = "d1bbcbd48e84c66b7af7310e416b6eaa283057065c0a57e241564ae8a4f4c73c"

# DER SubjectPublicKeyInfo prefix for an Ed25519 public key: the fixed 12-byte
# header (algorithm id 1.3.101.112) followed by the raw 32-byte key. Assembled
# with the standard library only so the fingerprint computation does not depend
# on the cryptography package.
ED25519_SPKI_DER_PREFIX = bytes.fromhex("302a300506032b6570032100")

# Files added after the v0.4.1 signing event are not covered by the anchored
# signature. They are hash-recorded here, never labeled signature-covered. The
# authoritative coverage set is read from the manifest's files[] list at run
# time; this list only decides which recorded-but-unsigned files to report on.
POST_ANCHOR_RECORDED_FILES = [
    "canon-kernel.json",
    "SELF_ANCHORING_PROTOCOL.md",
    "DECISION_INDEX.md",
    "SUCCESSOR_HANDOVER_PROTOCOL.md",
    "PRECEDENT_LEDGER.md",
]


def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _der_from_raw32(raw32_hex: str) -> bytes:
    raw = bytes.fromhex(raw32_hex)
    if len(raw) != 32:
        raise ValueError(f"raw public key must be 32 bytes, got {len(raw)}")
    return ED25519_SPKI_DER_PREFIX + raw


def _fingerprint_from_raw32(raw32_hex: str) -> str:
    # Mirrors tools/prov_k/keys.py: fingerprint == "sha256:" + sha256(DER SPKI).
    return "sha256:" + _sha256_hex(_der_from_raw32(raw32_hex))


def _signing_payload_bytes(manifest: dict) -> bytes:
    # Faithful copy of tools/prov_k/manifest.py:signing_payload_bytes.
    # The signature block is excluded; the remaining object is serialized as
    # canonical JSON (UTF-8, sorted keys, compact separators). Not imported, so
    # this verifier stays standalone.
    view = copy.deepcopy(manifest)
    view.pop("signature", None)
    return json.dumps(view, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _emit(results: list[tuple[str, str]], status: str, message: str) -> None:
    results.append((status, message))
    print(f"[{status}] {message}")


def run_self_check(results: list[tuple[str, str]]) -> bool:
    """Rebuild the fingerprint from the inlined key and compare to the pin."""
    try:
        computed = _fingerprint_from_raw32(ORIGIN_PUBLIC_KEY_RAW32)
    except ValueError as exc:
        _emit(results, "FAIL", f"self-check: cannot build key fingerprint: {exc}")
        return False
    if computed == PINNED_FINGERPRINT:
        _emit(results, "PASS", "self-check: inlined public key matches the fingerprint pinned in docs/TRUST_ANCHOR.md")
        return True
    _emit(
        results,
        "FAIL",
        f"self-check: inlined public key fingerprint {computed} does not match pinned {PINNED_FINGERPRINT}",
    )
    return False


def verify_manifest(manifest_path: Path, results: list[tuple[str, str]]) -> dict | None:
    # Every gate is evaluated (no early return on a failed gate) so that a
    # tampered manifest shows exactly which independent gates catch it -- both
    # the whole-file hash pin and the Ed25519 signature. The overall result is
    # still fail-closed: any FAIL makes the script exit non-zero.
    raw = manifest_path.read_bytes()
    manifest_sha = _sha256_hex(raw)
    if manifest_sha == PINNED_MANIFEST_SHA:
        _emit(results, "PASS", f"manifest sha256 matches the pinned value for release {ANCHORED_RELEASE}")
    else:
        _emit(results, "FAIL", f"manifest sha256 {manifest_sha} does not match pinned {PINNED_MANIFEST_SHA}")

    try:
        manifest = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        _emit(results, "FAIL", f"manifest is not valid JSON: {exc}")
        return None

    manifest_fp = manifest.get("signing", {}).get("public_key_fingerprint")
    if manifest_fp == PINNED_FINGERPRINT:
        _emit(results, "PASS", "manifest signing fingerprint matches the pinned fingerprint")
    else:
        _emit(results, "FAIL", f"manifest signing fingerprint {manifest_fp} does not match pinned {PINNED_FINGERPRINT}")

    signature_value = manifest.get("signature", {}).get("value")
    if not signature_value:
        _emit(results, "FAIL", "manifest carries no signature value")
        return manifest

    try:
        import base64

        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

        public_key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(ORIGIN_PUBLIC_KEY_RAW32))
        public_key.verify(base64.b64decode(signature_value), _signing_payload_bytes(manifest))
    except ImportError as exc:
        _emit(results, "FAIL", f"cryptography package required for signature verification: {exc}")
        return manifest
    except Exception as exc:  # signature failure is fail-closed
        _emit(results, "FAIL", f"Ed25519 signature verification failed: {exc}")
        return manifest

    _emit(results, "PASS", "Ed25519 signature over the manifest is valid under the pinned key")
    return manifest


def report_coverage(manifest: dict, repo_root: Path | None, results: list[tuple[str, str]]) -> None:
    """Separate signature-covered files from post-anchor recorded-only files."""
    covered = {
        item["path"]: item["sha256"]
        for item in manifest.get("files", [])
        if isinstance(item, dict) and isinstance(item.get("path"), str)
    }
    print("")
    print(f"--- signature coverage (authoritative set read from manifest files[]: {len(covered)} files) ---")

    for rel in POST_ANCHOR_RECORDED_FILES:
        if rel in covered:
            # Would only happen once a later signed release absorbs the file.
            print(f"[COVERED]  {rel}: present in the signed manifest (signature-covered)")
            continue
        if repo_root is not None:
            path = repo_root / rel
            if path.is_file():
                digest = _sha256_hex(path.read_bytes())
                print(f"[RECORDED] {rel}: sha256 {digest} - recorded, not yet signature-anchored (pending next signed release)")
            else:
                print(f"[RECORDED] {rel}: not present in working tree - nothing to record")
        else:
            print(f"[RECORDED] {rel}: recorded, not yet signature-anchored (pending next signed release) [--repo-root not given; hash not computed]")

    print("Note: RECORDED is a coverage status, not a signature verdict. Only manifest-listed files are signature-covered.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline canon self-verification (fail-closed).")
    parser.add_argument("--manifest", type=Path, help="path to the v0.4.1 signed release manifest asset")
    parser.add_argument("--repo-root", type=Path, default=None, help="repository root, to hash post-anchor recorded files")
    parser.add_argument("--self-check-only", action="store_true", help="run only the inlined-key self-check")
    args = parser.parse_args(argv)

    results: list[tuple[str, str]] = []

    # The self-check always runs first and is a hard gate.
    if not run_self_check(results):
        print("")
        print("RESULT: FAIL")
        return 1

    if args.self_check_only:
        print("")
        print("RESULT: PASS (self-check only)")
        return 0

    if args.manifest is None:
        _emit(results, "FAIL", "no --manifest supplied; download the v0.4.1 manifest asset per docs/TRUST_ANCHOR.md")
        print("")
        print("RESULT: FAIL")
        return 1

    if not args.manifest.is_file():
        _emit(results, "FAIL", f"manifest file not found: {args.manifest}")
        print("")
        print("RESULT: FAIL")
        return 1

    manifest = verify_manifest(args.manifest, results)
    failed = any(status == "FAIL" for status, _ in results)

    # Coverage is only meaningful for an authentic, fully verified manifest.
    if manifest is not None and not failed:
        report_coverage(manifest, args.repo_root, results)
        failed = any(status == "FAIL" for status, _ in results)
    elif failed:
        print("")
        print("(signature coverage report skipped: manifest did not fully verify)")
    print("")
    print("RESULT:", "FAIL" if failed else "PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
