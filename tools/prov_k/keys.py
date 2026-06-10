#!/usr/bin/env python3
"""Public-key parsing and fingerprint helpers for PROV-K.

No key generation helpers are provided in this module.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
except Exception:  # pragma: no cover - exercised when dependency is absent.
    serialization = None  # type: ignore[assignment]
    Ed25519PublicKey = Any  # type: ignore[misc,assignment]


def require_cryptography() -> None:
    if serialization is None:
        raise NotImplementedError("Ed25519 provenance signing requires the cryptography package")


def public_key_fingerprint(public_key_bytes: bytes) -> str:
    return "sha256:" + hashlib.sha256(public_key_bytes).hexdigest()


def _load_public_key_bytes(data: bytes) -> Ed25519PublicKey:
    require_cryptography()
    loaders = (
        ("PEM", serialization.load_pem_public_key),
        ("OpenSSH", serialization.load_ssh_public_key),
    )
    errors: list[str] = []
    for label, loader in loaders:
        try:
            key = loader(data)
        except (TypeError, ValueError) as exc:
            errors.append(f"{label}: {exc}")
            continue
        if not isinstance(key, Ed25519PublicKey):
            raise ValueError("public key must be Ed25519")
        return key
    raise ValueError("public key must be PEM or OpenSSH Ed25519; " + "; ".join(errors))


def load_public_key(path: Path) -> Ed25519PublicKey:
    return _load_public_key_bytes(path.read_bytes())


def public_key_der_bytes(public_key: Ed25519PublicKey) -> bytes:
    require_cryptography()
    return public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )


def public_key_fingerprint_from_key(public_key: Ed25519PublicKey) -> str:
    return public_key_fingerprint(public_key_der_bytes(public_key))


def public_key_fingerprint_from_file(path: Path) -> str:
    return public_key_fingerprint_from_key(load_public_key(path))
