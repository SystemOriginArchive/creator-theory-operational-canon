#!/usr/bin/env python3
"""Fail-closed verification for PROV-K manifests."""

from __future__ import annotations

import base64
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .keys import load_public_key, public_key_fingerprint_from_key
from .manifest import (
    HASH_SOURCES,
    load_manifest_file,
    sha256_file,
    sha256_git_blob,
    signing_payload_bytes,
    validate_manifest_data,
)


@dataclass
class VerificationResult:
    ok: bool
    errors: list[str] = field(default_factory=list)


def _fail(errors: list[str], message: str) -> None:
    errors.append(message)


def _manifest_paths(data: dict[str, Any]) -> set[str]:
    return {item["path"] for item in data.get("files", []) if isinstance(item, dict) and isinstance(item.get("path"), str)}


def _actual_paths(root: Path, manifest_path: Path | None) -> set[str]:
    paths: set[str] = set()
    root = root.resolve()
    manifest_resolved = manifest_path.resolve() if manifest_path else None
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
            continue
        if manifest_resolved and path.resolve() == manifest_resolved:
            continue
        paths.add(path.resolve().relative_to(root).as_posix())
    return paths


def _normalize_scope_prefix(prefix: str) -> str:
    candidate = prefix.replace("\\", "/").strip()
    # Drop empty and "." segments so "./a", "a/./b", and "a//b" normalize to
    # the same repo-relative form that manifest and tree paths use.
    segments = [segment for segment in candidate.split("/") if segment not in ("", ".")]
    if (
        not segments
        or candidate.startswith("/")
        or ":" in segments[0]
        or ".." in segments
    ):
        raise ValueError(f"unsafe or empty scope prefix: {prefix!r}")
    return "/".join(segments)


def _in_scope(rel_path: str, prefixes: list[str]) -> bool:
    return any(rel_path == prefix or rel_path.startswith(prefix + "/") for prefix in prefixes)


def verify_manifest_data(
    data: dict[str, Any],
    root: Path,
    *,
    manifest_path: Path | None = None,
    public_key_path: Path | None = None,
    previous_manifest_path: Path | None = None,
    strict: bool = True,
    scope_prefixes: list[str] | None = None,
    hash_source: str = "worktree",
    rev: str = "HEAD",
) -> VerificationResult:
    errors: list[str] = []
    if hash_source not in HASH_SOURCES:
        return VerificationResult(
            False, [f"invalid hash_source: {hash_source!r}; expected one of {HASH_SOURCES}"]
        )
    try:
        validate_manifest_data(data)
    except ValueError as exc:
        return VerificationResult(False, [str(exc)])

    normalized_scope: list[str] | None = None
    if scope_prefixes is not None:
        if not scope_prefixes:
            return VerificationResult(
                False, ["scope_prefixes must not be empty when provided"]
            )
        # Bounded verification narrows only the unmanifested-extras scan.
        # It is reserved for experiment_artifact manifests so release-class
        # verification semantics stay whole-repository and fail-closed.
        if data.get("provenance_class") != "experiment_artifact":
            return VerificationResult(
                False,
                [
                    "scope-prefix bounded verification is only allowed for "
                    "experiment_artifact manifests"
                ],
            )
        try:
            normalized_scope = [_normalize_scope_prefix(prefix) for prefix in scope_prefixes]
        except ValueError as exc:
            return VerificationResult(False, [str(exc)])

    root = root.resolve()
    for item in data["files"]:
        rel = item["path"]
        path = root / rel
        if not path.is_file():
            _fail(errors, f"listed file is missing: {rel}")
            continue
        # git-blob mode changes only the hash byte source (committed blob bytes
        # at rev); the path-existence check above and the _actual_paths extras
        # scan below stay working-tree based and unchanged.
        if hash_source == "git-blob":
            try:
                actual = sha256_git_blob(root, rel, rev)
            except ValueError as exc:
                _fail(errors, f"git blob hash failed for {rel}: {exc}")
                continue
        else:
            actual = sha256_file(path)
        if actual != item["sha256"]:
            _fail(errors, f"sha256 mismatch for {rel}: expected {item['sha256']}, got {actual}")

    if strict:
        actual = _actual_paths(root, manifest_path)
        if normalized_scope is not None:
            actual = {path for path in actual if _in_scope(path, normalized_scope)}
        extras = sorted(actual - _manifest_paths(data))
        if extras:
            _fail(errors, "unmanifested files present: " + ", ".join(extras))

    prev_hash = data.get("prev_manifest_sha256")
    if prev_hash:
        if previous_manifest_path is None:
            _fail(errors, "previous manifest path required for chained verification")
        elif not previous_manifest_path.is_file():
            _fail(errors, "previous manifest file is missing")
        elif sha256_file(previous_manifest_path) != prev_hash:
            _fail(errors, "previous manifest sha256 mismatch")

    signature_value = data.get("signature", {}).get("value")
    needs_signature = data.get("status") in {"SIGNED_RELEASE", "ROTATED_KEY_RELEASE"}
    if signature_value or needs_signature:
        if not signature_value:
            _fail(errors, "signed release status requires a signature")
        elif public_key_path is None:
            _fail(errors, "public key path required for signature verification")
        else:
            try:
                public_key = load_public_key(public_key_path)
                computed_fingerprint = public_key_fingerprint_from_key(public_key)
                manifest_fingerprint = data.get("signing", {}).get("public_key_fingerprint")
                if needs_signature and not manifest_fingerprint:
                    _fail(errors, "signed release status requires public_key_fingerprint")
                elif manifest_fingerprint and manifest_fingerprint != computed_fingerprint:
                    _fail(
                        errors,
                        "public key fingerprint mismatch: "
                        f"manifest has {manifest_fingerprint}, supplied key has {computed_fingerprint}",
                    )
                public_key.verify(base64.b64decode(signature_value), signing_payload_bytes(data))
            except Exception as exc:
                _fail(errors, f"signature verification failed: {exc}")

    return VerificationResult(not errors, errors)


def verify_manifest_file(
    root: Path,
    manifest_path: Path,
    *,
    public_key_path: Path | None = None,
    previous_manifest_path: Path | None = None,
    strict: bool = True,
    scope_prefixes: list[str] | None = None,
    hash_source: str = "worktree",
    rev: str = "HEAD",
) -> VerificationResult:
    data = load_manifest_file(manifest_path)
    return verify_manifest_data(
        data,
        root,
        manifest_path=manifest_path,
        public_key_path=public_key_path,
        previous_manifest_path=previous_manifest_path,
        strict=strict,
        scope_prefixes=scope_prefixes,
        hash_source=hash_source,
        rev=rev,
    )
