#!/usr/bin/env python3
"""Command-line interface for PROV-K."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .manifest import build_manifest, dump_manifest_file, sha256_file
from .rotate import build_rotation_record, sign_rotation_record, verify_rotation_record
from .sign import sign_manifest_file
from .verify import verify_manifest_file


def cmd_build(args: argparse.Namespace) -> int:
    root = Path(args.repo_root)
    file_paths = [root / item for item in args.file] if args.file else None
    data = build_manifest(
        root,
        args.release_label,
        file_paths=file_paths,
        prev_manifest_sha256=args.prev_manifest_sha256,
        status=args.status,
        provenance_class=args.provenance_class,
        origin_attribution=args.origin_attribution,
        awaiting_user_signature=args.awaiting_user_signature,
        historical_proof=args.historical_proof,
    )
    dump_manifest_file(Path(args.output), data)
    return 0


def cmd_sign(args: argparse.Namespace) -> int:
    sign_manifest_file(Path(args.manifest), Path(args.private_key), Path(args.repo_root))
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    result = verify_manifest_file(
        Path(args.repo_root),
        Path(args.manifest),
        public_key_path=Path(args.public_key) if args.public_key else None,
        previous_manifest_path=Path(args.previous_manifest) if args.previous_manifest else None,
        strict=not args.no_strict,
    )
    if result.ok:
        print("PROV-K verification passed")
        return 0
    print("PROV-K verification failed", file=sys.stderr)
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


def cmd_rotate(args: argparse.Namespace) -> int:
    record = build_rotation_record(
        old_public_key_fingerprint=args.old_public_key_fingerprint,
        new_public_key_fingerprint=args.new_public_key_fingerprint,
        prev_manifest_sha256=args.prev_manifest_sha256,
    )
    if args.previous_private_key:
        record = sign_rotation_record(record, Path(args.previous_private_key), Path(args.repo_root))
    Path(args.output).write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


def cmd_rotation_verify(args: argparse.Namespace) -> int:
    record = json.loads(Path(args.record).read_text(encoding="utf-8"))
    if verify_rotation_record(record, Path(args.previous_public_key)):
        print("PROV-K rotation verification passed")
        return 0
    print("PROV-K rotation verification failed", file=sys.stderr)
    return 1


def cmd_sha256(args: argparse.Namespace) -> int:
    print(sha256_file(Path(args.path)))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PROV-K manifest build/sign/verify/rotate commands")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="build an unsigned manifest")
    build.add_argument("--repo-root", default=".")
    build.add_argument("--release-label", required=True)
    build.add_argument("--output", required=True)
    build.add_argument("--file", action="append", default=[])
    build.add_argument("--prev-manifest-sha256")
    build.add_argument("--status", default="UNSIGNED_DRAFT")
    build.add_argument("--provenance-class", default="current_release")
    build.add_argument("--origin-attribution", required=True)
    build.add_argument("--awaiting-user-signature", action="store_true")
    build.add_argument("--historical-proof", action="store_true")
    build.set_defaults(func=cmd_build)

    sign = sub.add_parser("sign", help="sign a manifest with a user-held Ed25519 private key")
    sign.add_argument("--repo-root", default=".")
    sign.add_argument("--manifest", required=True)
    sign.add_argument("--private-key", required=True)
    sign.set_defaults(func=cmd_sign)

    verify = sub.add_parser("verify", help="verify manifest hashes, signature, and optional chain")
    verify.add_argument("--repo-root", default=".")
    verify.add_argument("--manifest", required=True)
    verify.add_argument("--public-key")
    verify.add_argument("--previous-manifest")
    verify.add_argument("--no-strict", action="store_true")
    verify.set_defaults(func=cmd_verify)

    rotate = sub.add_parser("rotate", help="build or sign a key rotation record")
    rotate.add_argument("--repo-root", default=".")
    rotate.add_argument("--output", required=True)
    rotate.add_argument("--old-public-key-fingerprint", required=True)
    rotate.add_argument("--new-public-key-fingerprint", required=True)
    rotate.add_argument("--prev-manifest-sha256", required=True)
    rotate.add_argument("--previous-private-key")
    rotate.set_defaults(func=cmd_rotate)

    rotation_verify = sub.add_parser("verify-rotation", help="verify a rotation record signed by the previous key")
    rotation_verify.add_argument("--record", required=True)
    rotation_verify.add_argument("--previous-public-key", required=True)
    rotation_verify.set_defaults(func=cmd_rotation_verify)

    sha = sub.add_parser("sha256", help="print the SHA-256 digest of local file bytes")
    sha.add_argument("path")
    sha.set_defaults(func=cmd_sha256)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except NotImplementedError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
