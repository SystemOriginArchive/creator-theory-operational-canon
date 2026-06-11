#!/usr/bin/env python3
"""PROV-K experiment_artifact class and bounded verification gate.

No keys are created and nothing is signed. Signing fail-closure is covered
through validate_manifest_data, which the signing path always re-runs.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Callable

from tools.prov_k.cli import main as cli_main
from tools.prov_k.manifest import (
    ALLOWED_PROVENANCE_CLASSES,
    build_manifest,
    dump_manifest_file,
    validate_manifest_data,
)
from tools.prov_k.verify import verify_manifest_file

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "prov_k_manifest.schema.json"
MANIFEST_DIR = ROOT / "provenance" / "manifests"
FIXTURE_ATTRIBUTION = "fixture_attribution_for_unit_test"
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


def make_fixture_tree(root: Path) -> tuple[Path, Path]:
    scoped = root / "experiments" / "adoption_drift" / "results" / "fixture_trial.json"
    scoped.parent.mkdir(parents=True)
    scoped.write_text('{"fixture": true}\n', encoding="utf-8")
    unscoped = root / "other" / "unrelated.txt"
    unscoped.parent.mkdir(parents=True)
    unscoped.write_text("outside the experiment scope\n", encoding="utf-8")
    return scoped, unscoped


def build_experiment_manifest(root: Path, scoped: Path) -> dict:
    return build_manifest(
        root,
        "v0.5.0-experiment-fixture",
        file_paths=[scoped],
        provenance_class="experiment_artifact",
        origin_attribution=FIXTURE_ATTRIBUTION,
    )


def test_e1_schema_and_validator_class_parity() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    schema_classes = set(schema["properties"]["provenance_class"]["enum"])
    assert schema_classes == ALLOWED_PROVENANCE_CLASSES, (
        f"schema enum {sorted(schema_classes)} != validator classes "
        f"{sorted(ALLOWED_PROVENANCE_CLASSES)}"
    )
    conditions = schema.get("allOf", [])
    assert any(
        item.get("if", {}).get("properties", {}).get("provenance_class", {}).get("const")
        == "experiment_artifact"
        and item.get("then", {}).get("properties", {}).get("status", {}).get("const")
        == "UNSIGNED_DRAFT"
        for item in conditions
    ), "schema is missing the experiment_artifact status restriction"


def test_e2_experiment_artifact_builds_and_validates() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        validate_manifest_data(data)
        assert data["provenance_class"] == "experiment_artifact"
        assert data["status"] == "UNSIGNED_DRAFT"
        assert data["historical_proof"] is False


def test_e3_experiment_artifact_rejects_release_statuses() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        for status in ("SIGNED_RELEASE", "ROTATED_KEY_RELEASE", "EMERGENCY_REASSERTED", "DISPUTED"):
            flipped = json.loads(json.dumps(data))
            flipped["status"] = status
            try:
                validate_manifest_data(flipped)
            except ValueError:
                continue
            raise AssertionError(f"experiment_artifact accepted status {status}")
        try:
            build_manifest(
                root,
                "v0.5.0-experiment-fixture",
                file_paths=[scoped],
                status="SIGNED_RELEASE",
                provenance_class="experiment_artifact",
                origin_attribution=FIXTURE_ATTRIBUTION,
            )
        except ValueError:
            return
        raise AssertionError("build accepted experiment_artifact with SIGNED_RELEASE")


def test_e4_bounded_verify_passes_and_unbounded_strict_still_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, unscoped = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        manifest_path = root / "experiment-manifest.json"
        dump_manifest_file(manifest_path, data)

        bounded = verify_manifest_file(
            root, manifest_path, scope_prefixes=["experiments/adoption_drift"]
        )
        assert bounded.ok, f"bounded verification failed: {bounded.errors}"

        unbounded = verify_manifest_file(root, manifest_path)
        assert not unbounded.ok, "unbounded strict verify must still flag extras"
        joined = " ".join(unbounded.errors)
        assert "unmanifested files present" in joined, unbounded.errors
        assert "other/unrelated.txt" in joined, unbounded.errors
        assert unscoped.exists()


def test_e5_scope_prefix_rejected_for_release_classes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        for provenance_class in ("current_release", "retroactive_reconstruction"):
            data = build_manifest(
                root,
                "v0.5.0-release-fixture",
                file_paths=[scoped],
                provenance_class=provenance_class,
                origin_attribution=FIXTURE_ATTRIBUTION,
            )
            manifest_path = root / f"{provenance_class}-manifest.json"
            dump_manifest_file(manifest_path, data)
            result = verify_manifest_file(
                root, manifest_path, scope_prefixes=["experiments/adoption_drift"]
            )
            assert not result.ok, f"{provenance_class} accepted bounded verification"
            assert any("experiment_artifact" in error for error in result.errors), result.errors
            manifest_path.unlink()


def test_e6_unsafe_scope_prefixes_rejected() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        manifest_path = root / "experiment-manifest.json"
        dump_manifest_file(manifest_path, data)
        for prefix in ("", "/", ".", "./", "/etc", "../outside", "experiments/../other", "C:/outside"):
            result = verify_manifest_file(root, manifest_path, scope_prefixes=[prefix])
            assert not result.ok, f"unsafe scope prefix accepted: {prefix!r}"
        empty_list = verify_manifest_file(root, manifest_path, scope_prefixes=[])
        assert not empty_list.ok, "empty scope_prefixes list must be rejected, not treated as no scope"


def test_e6b_scope_prefix_spellings_normalize_to_same_scope() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        # Manifest deliberately omits the scoped file so an in-scope extra exists.
        data = build_manifest(
            root,
            "v0.5.0-experiment-fixture",
            file_paths=[],
            provenance_class="experiment_artifact",
            origin_attribution=FIXTURE_ATTRIBUTION,
        )
        manifest_path = root / "experiment-manifest.json"
        dump_manifest_file(manifest_path, data)
        for prefix in (
            "experiments/adoption_drift",
            "./experiments/adoption_drift",
            "experiments/./adoption_drift",
            "experiments//adoption_drift",
            "experiments/adoption_drift/",
        ):
            result = verify_manifest_file(root, manifest_path, scope_prefixes=[prefix])
            assert not result.ok, (
                f"prefix spelling {prefix!r} silently matched nothing; "
                "in-scope unmanifested file was not flagged"
            )
            assert any("unmanifested files present" in error for error in result.errors), (
                prefix,
                result.errors,
            )
        assert scoped.exists()


def test_e7_unknown_provenance_class_still_rejected() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        flipped = json.loads(json.dumps(data))
        flipped["provenance_class"] = "experiment_results_final"
        try:
            validate_manifest_data(flipped)
        except ValueError:
            return
        raise AssertionError("unknown provenance class was accepted")


def test_e8_committed_manifest_dir_unaffected() -> None:
    paths = sorted(MANIFEST_DIR.glob("*.json"))
    assert paths, "no committed manifests found"
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data.get("provenance_class") == "retroactive_reconstruction", (
            f"{path.name}: provenance/manifests/ must stay retroactive_reconstruction only"
        )


def test_e9_cli_scope_prefix_wiring() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        manifest_path = root / "experiment-manifest.json"
        dump_manifest_file(manifest_path, data)
        bounded_rc = cli_main(
            [
                "verify",
                "--repo-root",
                str(root),
                "--manifest",
                str(manifest_path),
                "--scope-prefix",
                "experiments/adoption_drift",
            ]
        )
        assert bounded_rc == 0, f"CLI bounded verify returned {bounded_rc}"
        unbounded_rc = cli_main(
            ["verify", "--repo-root", str(root), "--manifest", str(manifest_path)]
        )
        assert unbounded_rc == 1, f"CLI unbounded strict verify returned {unbounded_rc}"


def test_e10_sign_path_refuses_experiment_artifact_before_signing() -> None:
    from tools.prov_k.sign import sign_manifest_data

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        scoped, _ = make_fixture_tree(root)
        data = build_experiment_manifest(root, scoped)
        # private_key=None proves the guard fires before any key material is touched.
        try:
            sign_manifest_data(data, None, declare_release=True)
        except ValueError as exc:
            assert "not signable" in str(exc), exc
            return
        raise AssertionError("sign path accepted an experiment_artifact manifest")


def main() -> int:
    check("E1 schema and validator class parity", test_e1_schema_and_validator_class_parity)
    check("E2 experiment_artifact builds and validates", test_e2_experiment_artifact_builds_and_validates)
    check("E3 experiment_artifact rejects release statuses", test_e3_experiment_artifact_rejects_release_statuses)
    check("E4 bounded verify passes, unbounded strict still fails", test_e4_bounded_verify_passes_and_unbounded_strict_still_fails)
    check("E5 scope prefix rejected for release classes", test_e5_scope_prefix_rejected_for_release_classes)
    check("E6 unsafe scope prefixes rejected", test_e6_unsafe_scope_prefixes_rejected)
    check("E6b scope prefix spellings normalize to same scope", test_e6b_scope_prefix_spellings_normalize_to_same_scope)
    check("E7 unknown provenance class still rejected", test_e7_unknown_provenance_class_still_rejected)
    check("E8 committed manifest dir unaffected", test_e8_committed_manifest_dir_unaffected)
    check("E9 CLI scope-prefix wiring", test_e9_cli_scope_prefix_wiring)
    check("E10 sign path refuses experiment_artifact before signing", test_e10_sign_path_refuses_experiment_artifact_before_signing)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
