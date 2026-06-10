#!/usr/bin/env python3
"""User-run Ed25519 signing helpers for PROV-K manifests."""

from __future__ import annotations

import base64
import copy
from pathlib import Path
from typing import Any

from .keys import public_key_fingerprint_from_key, require_cryptography
from .manifest import load_manifest_file, signing_payload_bytes, utc_now, validate_manifest_data, dump_manifest_file

try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
except Exception:  # pragma: no cover - exercised when dependency is absent.
    serialization = None  # type: ignore[assignment]
    Ed25519PrivateKey = Any  # type: ignore[misc,assignment]


SIGNABLE_MANIFEST_STATUSES = {"SIGNED_RELEASE", "ROTATED_KEY_RELEASE"}


def _inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def refuse_private_key_inside_repo(repo_root: Path, private_key_path: Path) -> None:
    if _inside(private_key_path, repo_root):
        raise ValueError("private key path resolves inside the repository; production signing must use a user-held key outside the repo")


def _load_private_key_bytes(data: bytes) -> Ed25519PrivateKey:
    require_cryptography()
    loaders = (
        ("PEM", serialization.load_pem_private_key),
        ("OpenSSH", serialization.load_ssh_private_key),
    )
    errors: list[str] = []
    for label, loader in loaders:
        try:
            key = loader(data, password=None)
        except (TypeError, ValueError) as exc:
            errors.append(f"{label}: {exc}")
            continue
        if not isinstance(key, Ed25519PrivateKey):
            raise ValueError("private key must be Ed25519")
        return key
    raise ValueError("private key must be PEM or OpenSSH Ed25519; " + "; ".join(errors))


def load_private_key(path: Path) -> Ed25519PrivateKey:
    return _load_private_key_bytes(path.read_bytes())


def sign_manifest_data(
    data: dict[str, Any],
    private_key: Ed25519PrivateKey,
    *,
    declare_release: bool = False,
) -> dict[str, Any]:
    validate_manifest_data(data)
    signed = copy.deepcopy(data)
    status = signed.get("status")
    if status == "UNSIGNED_DRAFT" and declare_release:
        signed["status"] = "SIGNED_RELEASE"
        signed.pop("awaiting_user_signature", None)
    elif status not in SIGNABLE_MANIFEST_STATUSES:
        raise ValueError("manifest status must be SIGNED_RELEASE or ROTATED_KEY_RELEASE before signing")
    public_key = private_key.public_key()
    signed["signing"] = dict(data["signing"])
    signed["signing"]["public_key_fingerprint"] = public_key_fingerprint_from_key(public_key)
    signature = private_key.sign(signing_payload_bytes(signed))
    signed["signature"] = {
        "value": base64.b64encode(signature).decode("ascii"),
        "signed_utc": utc_now(),
    }
    validate_manifest_data(signed)
    return signed


def sign_manifest_file(
    manifest_path: Path,
    private_key_path: Path,
    repo_root: Path,
    *,
    declare_release: bool = False,
) -> dict[str, Any]:
    refuse_private_key_inside_repo(repo_root, private_key_path)
    private_key = load_private_key(private_key_path)
    data = load_manifest_file(manifest_path)
    signed = sign_manifest_data(data, private_key, declare_release=declare_release)
    dump_manifest_file(manifest_path, signed)
    return signed
