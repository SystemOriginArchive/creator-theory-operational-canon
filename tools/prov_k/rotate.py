#!/usr/bin/env python3
"""Key-rotation records for PROV-K."""

from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Any

from .keys import load_public_key, public_key_fingerprint_from_key
from .manifest import canonical_json_bytes, utc_now
from .sign import load_private_key, refuse_private_key_inside_repo


def build_rotation_record(
    *,
    old_public_key_fingerprint: str,
    new_public_key_fingerprint: str,
    prev_manifest_sha256: str,
    created_utc: str | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "layer": "v0.4.0-prov-k",
        "record_type": "key_rotation",
        "created_utc": created_utc or utc_now(),
        "status": "UNSIGNED_DRAFT",
        "rotation": {
            "old_public_key_fingerprint": old_public_key_fingerprint,
            "new_public_key_fingerprint": new_public_key_fingerprint,
            "prev_manifest_sha256": prev_manifest_sha256,
            "previous_key_signature": None,
            "signed_utc": None,
        },
    }


def rotation_payload_bytes(record: dict[str, Any]) -> bytes:
    view = json.loads(json.dumps(record))
    view["rotation"] = dict(view["rotation"])
    view["rotation"].pop("previous_key_signature", None)
    view["rotation"].pop("signed_utc", None)
    return canonical_json_bytes(view)


def sign_rotation_record(record: dict[str, Any], previous_private_key_path: Path, repo_root: Path) -> dict[str, Any]:
    refuse_private_key_inside_repo(repo_root, previous_private_key_path)
    private_key = load_private_key(previous_private_key_path)
    signed = json.loads(json.dumps(record))
    signed["status"] = "ROTATED_KEY_RELEASE"
    signed["rotation"] = dict(signed["rotation"])
    signature = private_key.sign(rotation_payload_bytes(signed))
    signed["rotation"]["previous_key_signature"] = base64.b64encode(signature).decode("ascii")
    signed["rotation"]["signed_utc"] = utc_now()
    return signed


def verify_rotation_record(record: dict[str, Any], previous_public_key_path: Path) -> bool:
    rotation = record.get("rotation", {})
    signature = rotation.get("previous_key_signature")
    if not signature or record.get("status") != "ROTATED_KEY_RELEASE":
        return False
    declared_old_fingerprint = rotation.get("old_public_key_fingerprint")
    if not declared_old_fingerprint:
        return False
    public_key = load_public_key(previous_public_key_path)
    if public_key_fingerprint_from_key(public_key) != declared_old_fingerprint:
        return False
    try:
        public_key.verify(base64.b64decode(signature), rotation_payload_bytes(record))
        return True
    except Exception:
        return False
