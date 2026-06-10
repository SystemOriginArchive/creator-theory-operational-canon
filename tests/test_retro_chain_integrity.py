#!/usr/bin/env python3
"""Retroactive reconstruction manifest chain integrity tests."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Callable

from tools.prov_k.manifest import validate_manifest_data

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = ROOT / "provenance" / "manifests"
MANIFEST_ORDER = [
    MANIFEST_DIR / "releases-retro-reconstruction.json",
    MANIFEST_DIR / "v0.3.0-retro-reconstruction.json",
    MANIFEST_DIR / "v0.3.1-retro-reconstruction.json",
]
AUDIT_LOG = ROOT / "audit" / "V0_4_0_AUDIT_LOG.md"
TABLE_MARKERS = (
    "Generated retro manifest file hashes for chaining:",
    "Regenerated manifest hashes:",
)
CHECKED = 0
PASSED = 0


def check(name: str, func: Callable[[], None]) -> None:
    global CHECKED, PASSED
    CHECKED += 1
    try:
        func()
    except Exception as exc:
        raise AssertionError(f"{name} failed: {exc}") from exc
    PASSED += 1
    print(f"PASS: {name}")


def read_json(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    assert isinstance(data, dict), f"{path} must contain a JSON object"
    return data


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retro_manifest_paths() -> list[Path]:
    paths = sorted(MANIFEST_DIR.glob("*retro-reconstruction.json"))
    assert paths, "no committed retro reconstruction manifests found"
    return paths


def test_all_committed_retro_manifests_validate_and_sort_files() -> None:
    for path in retro_manifest_paths():
        data = read_json(path)
        validate_manifest_data(data)
        files = data.get("files")
        assert isinstance(files, list), f"{path} files must be a list"
        file_paths = [item.get("path") for item in files if isinstance(item, dict)]
        assert file_paths == sorted(file_paths), f"{path} files[] is not sorted by path"


def test_retro_manifest_chain_uses_committed_file_bytes() -> None:
    previous_hash: str | None = None
    for path in MANIFEST_ORDER:
        data = read_json(path)
        assert data.get("prev_manifest_sha256") == previous_hash, (
            f"{path.name} prev_manifest_sha256 does not match previous committed manifest bytes"
        )
        previous_hash = sha256_file(path)


def explicit_audit_hash_claims(text: str) -> list[tuple[str, str]]:
    claims: list[tuple[str, str]] = []
    for marker in TABLE_MARKERS:
        pattern = re.compile(re.escape(marker) + r"\n\n```text\n(?P<body>.*?)\n```", re.S)
        for match in pattern.finditer(text):
            for raw_line in match.group("body").splitlines():
                parts = raw_line.strip().split()
                if len(parts) != 2:
                    continue
                name, digest = parts
                if name.endswith("retro-reconstruction.json") and re.fullmatch(r"[0-9a-f]{64}", digest):
                    claims.append((name, digest))
    return claims


def test_audit_log_explicit_hash_tables_match_committed_bytes() -> None:
    if not AUDIT_LOG.exists():
        return
    actual = {path.name: sha256_file(path) for path in MANIFEST_ORDER}
    claims = explicit_audit_hash_claims(AUDIT_LOG.read_text(encoding="utf-8"))
    if not claims:
        return
    for name, claimed in claims:
        assert name in actual, f"audit log claims hash for unknown retro manifest: {name}"
        assert claimed == actual[name], (
            f"audit log hash claim for {name} diverges from committed manifest bytes"
        )


def main() -> int:
    check(
        "retro manifests validate and keep files sorted",
        test_all_committed_retro_manifests_validate_and_sort_files,
    )
    check(
        "retro chain prev hashes match committed bytes",
        test_retro_manifest_chain_uses_committed_file_bytes,
    )
    check(
        "audit explicit hash tables match committed bytes",
        test_audit_log_explicit_hash_tables_match_committed_bytes,
    )
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())