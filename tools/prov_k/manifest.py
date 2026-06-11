#!/usr/bin/env python3
"""Build and canonicalize PROV-K manifests.

The signature block is excluded from signing bytes. This module does not create
keys and does not treat attribution text as executable authority.
"""

from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = "1.0.0"
LAYER = "v0.4.0-prov-k"
REPOSITORY = "creator-theory-operational-canon"
ATTRIBUTION_STATEMENT_PATH = "docs/ATTRIBUTION_STATEMENT.md"
ALLOWED_STATUSES = {
    "UNSIGNED_DRAFT",
    "SIGNED_RELEASE",
    "ROTATED_KEY_RELEASE",
    "EMERGENCY_REASSERTED",
    "DISPUTED",
}
ALLOWED_PROVENANCE_CLASSES = {"current_release", "retroactive_reconstruction", "experiment_artifact"}
# experiment_artifact manifests classify adoption-drift experiment records.
# They never carry release or rotation statuses; release signing semantics
# stay reserved for the release provenance classes.
EXPERIMENT_ARTIFACT_ALLOWED_STATUSES = {"UNSIGNED_DRAFT"}
EXCLUDED_DIR_NAMES = {".git", "__pycache__", ".pytest_cache"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def repo_relative_path(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def iter_repository_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIR_NAMES for part in path.parts):
            continue
        files.append(path)
    return sorted(files, key=lambda item: repo_relative_path(root, item))


def canonical_json_bytes(data: dict[str, Any]) -> bytes:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def unsigned_manifest_view(data: dict[str, Any]) -> dict[str, Any]:
    view = copy.deepcopy(data)
    view.pop("signature", None)
    return view


def signing_payload_bytes(data: dict[str, Any]) -> bytes:
    return canonical_json_bytes(unsigned_manifest_view(data))


def manifest_file_bytes(data: dict[str, Any]) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load_manifest_text(text: str) -> dict[str, Any]:
    stripped = text.lstrip()
    if not stripped.startswith("{"):
        first_brace = stripped.find("{")
        if first_brace == -1:
            raise ValueError("manifest text does not contain a JSON object")
        stripped = stripped[first_brace:]
    data = json.loads(stripped)
    if not isinstance(data, dict):
        raise ValueError("manifest top-level value must be an object")
    return data


def load_manifest_file(path: Path) -> dict[str, Any]:
    return load_manifest_text(path.read_text(encoding="utf-8"))


def file_entries(root: Path, paths: Iterable[Path]) -> list[dict[str, str]]:
    root = root.resolve()
    entries: list[dict[str, str]] = []
    for path in paths:
        resolved = path.resolve()
        relative = resolved.relative_to(root).as_posix()
        entries.append({"path": relative, "sha256": sha256_file(resolved)})
    return sorted(entries, key=lambda item: item["path"])


def build_manifest(
    root: Path,
    release_label: str,
    *,
    file_paths: Iterable[Path] | None = None,
    prev_manifest_sha256: str | None = None,
    status: str = "UNSIGNED_DRAFT",
    provenance_class: str = "current_release",
    origin_attribution: str,
    created_utc: str | None = None,
    public_key_fingerprint: str | None = None,
    awaiting_user_signature: bool = False,
    historical_proof: bool = False,
) -> dict[str, Any]:
    if status not in ALLOWED_STATUSES:
        raise ValueError(f"invalid manifest status: {status}")
    if provenance_class not in ALLOWED_PROVENANCE_CLASSES:
        raise ValueError(f"invalid provenance class: {provenance_class}")
    if historical_proof is not False:
        raise ValueError("historical_proof must be false; no attested provenance path is currently supported")
    root = root.resolve()
    selected_paths = list(file_paths) if file_paths is not None else iter_repository_files(root)
    data: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "layer": LAYER,
        "repository": REPOSITORY,
        "release_label": release_label,
        "created_utc": created_utc or utc_now(),
        "files": file_entries(root, selected_paths),
        "prev_manifest_sha256": prev_manifest_sha256,
        "status": status,
        "signing": {
            "scheme": "ed25519",
            "public_key_fingerprint": public_key_fingerprint,
        },
        "provenance_class": provenance_class,
        "historical_proof": False,
        "attribution": {
            "origin_attribution": origin_attribution,
            "role": "origin attribution (documentation layer); not an operational constant",
            "attribution_statement_path": ATTRIBUTION_STATEMENT_PATH,
        },
        "boundary": {
            "replaces_creator_theory_high_frame": False,
            "replaces_recursive_self_improvement_layer": False,
            "layer_scope": "L2/L3 provenance sealing only",
        },
        "signature": {
            "value": None,
            "signed_utc": None,
        },
    }
    if awaiting_user_signature:
        data["awaiting_user_signature"] = True
    validate_manifest_data(data)
    return data


def validate_manifest_data(data: dict[str, Any]) -> None:
    required = {
        "schema_version",
        "layer",
        "repository",
        "release_label",
        "created_utc",
        "files",
        "prev_manifest_sha256",
        "status",
        "signing",
        "provenance_class",
        "historical_proof",
        "attribution",
        "boundary",
        "signature",
    }
    missing = sorted(required - set(data))
    if missing:
        raise ValueError(f"manifest missing fields: {', '.join(missing)}")
    if data["layer"] != LAYER:
        raise ValueError("manifest layer mismatch")
    if data["repository"] != REPOSITORY:
        raise ValueError("manifest repository mismatch")
    if data["status"] not in ALLOWED_STATUSES:
        raise ValueError("manifest status is invalid")
    if data["provenance_class"] not in ALLOWED_PROVENANCE_CLASSES:
        raise ValueError("manifest provenance_class is invalid")
    if (
        data["provenance_class"] == "experiment_artifact"
        and data["status"] not in EXPERIMENT_ARTIFACT_ALLOWED_STATUSES
    ):
        raise ValueError(
            "experiment_artifact manifests must keep status UNSIGNED_DRAFT; "
            "release and rotation statuses are reserved for release provenance classes"
        )
    if data["historical_proof"] is not False:
        raise ValueError("historical_proof must be false")
    files = data["files"]
    if not isinstance(files, list) or not all(isinstance(item, dict) for item in files):
        raise ValueError("manifest files must be a list of objects")
    sorted_paths = sorted(item.get("path") for item in files)
    if [item.get("path") for item in files] != sorted_paths:
        raise ValueError("manifest files must be sorted by path")
    for item in files:
        path = item.get("path")
        digest = item.get("sha256")
        if not isinstance(path, str) or not path or path.startswith("/") or ".." in Path(path).parts:
            raise ValueError(f"unsafe manifest file path: {path!r}")
        if not isinstance(digest, str) or len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise ValueError(f"invalid sha256 for path: {path}")
    boundary = data["boundary"]
    if boundary.get("replaces_creator_theory_high_frame") is not False:
        raise ValueError("boundary flag replaces_creator_theory_high_frame must be false")
    if boundary.get("replaces_recursive_self_improvement_layer") is not False:
        raise ValueError("boundary flag replaces_recursive_self_improvement_layer must be false")
    if boundary.get("layer_scope") != "L2/L3 provenance sealing only":
        raise ValueError("boundary layer_scope must remain L2/L3 provenance sealing only")
    signing = data["signing"]
    if signing.get("scheme") != "ed25519":
        raise ValueError("signing scheme must be ed25519")
    signature = data["signature"]
    if not isinstance(signature, dict) or "value" not in signature or "signed_utc" not in signature:
        raise ValueError("signature block is malformed")


def dump_manifest_file(path: Path, data: dict[str, Any]) -> None:
    validate_manifest_data(data)
    path.write_bytes(manifest_file_bytes(data))
