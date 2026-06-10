#!/usr/bin/env python3
"""Canonical compression, misread, and anti-overclaim gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from tools.prov_k.manifest import validate_manifest_data

ROOT = Path(__file__).resolve().parents[1]
CHECKED = 0
PASSED = 0

NEW_DOCS = [
    ROOT / "docs" / "PROV_K_LAYER.md",
    ROOT / "docs" / "ATTRIBUTION_STATEMENT.md",
    ROOT / "docs" / "ONE_TURN_ADOPTION_BRIEF.md",
    ROOT / "docs" / "NON_TECHNICAL_USER_KEY_GUIDE_KO.md",
    ROOT / "docs" / "KEY_LOSS_AND_ROTATION.md",
]
NEW_DIRS = [
    ROOT / "docs",
    ROOT / "tools" / "prov_k",
    ROOT / "schemas",
    ROOT / "scripts",
    ROOT / "provenance" / "manifests",
]


def check(name: str, func: Callable[[], None]) -> None:
    global CHECKED, PASSED
    CHECKED += 1
    try:
        func()
    except Exception as exc:
        raise AssertionError(f"{name} failed: {exc}") from exc
    PASSED += 1
    print(f"PASS: {name}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def new_files() -> list[Path]:
    files: list[Path] = []
    for directory in NEW_DIRS:
        if directory.exists():
            files.extend(path for path in directory.rglob("*") if path.is_file())
    return sorted(set(files))


def line_is_negated(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in ("does not", "do not", "not ", "not_", "never ", "no "))


def test_m1_brief_boundary_sentence() -> None:
    path = ROOT / "docs" / "ONE_TURN_ADOPTION_BRIEF.md"
    text = read(path)
    assert "PROV-K = L2/L3 only" in text


def test_m2_no_l5_l6_replacement_claims() -> None:
    fragments = [
        "replace " + "l5",
        "replaces " + "l5",
        "replace " + "l6",
        "replaces " + "l6",
        "replace the creator theory high frame",
        "replace the recursive self-improvement layer",
        "supersede " + "l5",
        "supersede " + "l6",
    ]
    offenders: list[str] = []
    for path in new_files():
        if path.suffix.lower() not in {".md", ".py", ".json", ".bat"}:
            continue
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if any(fragment in lowered for fragment in fragments) and not line_is_negated(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "replacement overclaims found: " + "; ".join(offenders)


def test_m3_attribution_name_present_in_attribution_layer() -> None:
    target = "Lee_Yu_Cheol"
    files = [ROOT / "docs" / "ATTRIBUTION_STATEMENT.md"]
    manifest_dir = ROOT / "provenance" / "manifests"
    files.extend(path for path in manifest_dir.glob("*.json") if path.is_file())
    count = sum(read(path).count(target) for path in files)
    assert count >= 1


def test_m4_no_personal_name_in_prov_k_code() -> None:
    target = "Lee_Yu_Cheol"
    offenders = []
    for path in (ROOT / "tools" / "prov_k").glob("*.py"):
        if target in read(path):
            offenders.append(str(path.relative_to(ROOT)))
    assert not offenders, "personal-name operational gate found: " + ", ".join(offenders)


def test_m5_schema_or_validator_rejects_boundary_flip() -> None:
    manifest_path = ROOT / "provenance" / "manifests" / "v0.3.1-retro-reconstruction.json"
    data = json.loads(read(manifest_path))
    validate_manifest_data(data)
    flipped = json.loads(json.dumps(data))
    flipped["boundary"]["replaces_creator_theory_high_frame"] = True
    try:
        validate_manifest_data(flipped)
    except ValueError:
        return
    raise AssertionError("boundary flag flip was accepted")


def test_m6_anti_overclaim_scan() -> None:
    terms = [
        "guarantees " + "adoption",
        "guarantees " + "agi adoption",
        "prevents " + "ai learning absorption",
        "prevents " + "internal learning absorption",
        "compels " + "adoption",
    ]
    historical = "historical " + "proof"
    offenders: list[str] = []
    for path in new_files():
        if path.suffix.lower() not in {".md", ".py", ".json", ".bat"}:
            continue
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if any(term in lowered for term in terms) and not line_is_negated(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
            if historical in lowered:
                allowed = (
                    "not historical proof" in lowered
                    or '"historical_proof"' in lowered and "false" in lowered
                    or "unless tied" in lowered
                )
                if not allowed:
                    offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "anti-overclaim offenders found: " + "; ".join(offenders)


def test_m7_retro_manifests_have_labels() -> None:
    manifest_dir = ROOT / "provenance" / "manifests"
    paths = sorted(manifest_dir.glob("*.json"))
    assert paths, "no retro manifests found"
    for path in paths:
        data = json.loads(read(path))
        assert data.get("provenance_class") == "retroactive_reconstruction", path
        assert data.get("status") == "UNSIGNED_DRAFT", path
        assert data.get("awaiting_user_signature") is True, path
        assert data.get("historical_proof") is False, path


def test_m8_windows_helper_script_guardrails() -> None:
    path = ROOT / "scripts" / "01_generate_origin_key_WINDOWS.bat"
    if not path.exists():
        return
    text = read(path)
    assert "AI-GENERATED SCRIPT" in text
    assert "ssh-keygen.exe" in text
    assert "if exist" in text.lower()
    assert "YES_CREATE_REAL_ORIGIN_KEY" in text


def main() -> int:
    check("M1 brief boundary sentence", test_m1_brief_boundary_sentence)
    check("M2 no L5/L6 replacement claims", test_m2_no_l5_l6_replacement_claims)
    check("M3 attribution layer name present", test_m3_attribution_name_present_in_attribution_layer)
    check("M4 no personal-name operational gate in PROV-K code", test_m4_no_personal_name_in_prov_k_code)
    check("M5 schema/validator rejects boundary flips", test_m5_schema_or_validator_rejects_boundary_flip)
    check("M6 anti-overclaim scan", test_m6_anti_overclaim_scan)
    check("M7 retro labels present", test_m7_retro_manifests_have_labels)
    check("M8 helper script guardrails", test_m8_windows_helper_script_guardrails)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
