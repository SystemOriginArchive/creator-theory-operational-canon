#!/usr/bin/env python3
"""Negative regression tests for the PROV-K fail-closed engine.

Test keys are generated ephemerally inside tmpdir only.
They are TEST KEY - NOT A REAL IDENTITY KEY.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from typing import Callable

from tools.prov_k.keys import load_public_key, public_key_fingerprint_from_file
from tools.prov_k.manifest import build_manifest, dump_manifest_file, load_manifest_file, sha256_file, validate_manifest_data
from tools.prov_k.rotate import build_rotation_record, sign_rotation_record, verify_rotation_record
from tools.prov_k.sign import load_private_key, refuse_private_key_inside_repo, sign_manifest_file
from tools.prov_k.verify import verify_manifest_file

try:
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
except Exception:  # pragma: no cover - depends on offline environment.
    serialization = None
    Ed25519PrivateKey = None


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


def require_crypto() -> None:
    if Ed25519PrivateKey is None or serialization is None:
        raise NotImplementedError("Ed25519 tests require the cryptography package")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_keypair(directory: Path, name: str, key_format: str = "pem") -> tuple[Path, Path]:
    require_crypto()
    if key_format not in {"pem", "openssh"}:
        raise ValueError("key_format must be pem or openssh")
    directory.mkdir(parents=True, exist_ok=True)
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    if key_format == "pem":
        private_path = directory / f"{name}_TEST_KEY_NOT_A_REAL_IDENTITY_KEY.pem"
        public_path = directory / f"{name}_TEST_PUBLIC_KEY_NOT_A_REAL_IDENTITY_KEY.pem"
        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    else:
        private_path = directory / f"{name}_TEST_KEY_NOT_A_REAL_IDENTITY_KEY.openssh"
        public_path = directory / f"{name}_TEST_PUBLIC_KEY_NOT_A_REAL_IDENTITY_KEY.pub"
        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_bytes = (
            public_key.public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH,
            )
            + b" TEST KEY - NOT A REAL IDENTITY KEY\n"
        )
    private_path.write_bytes(private_bytes)
    public_path.write_bytes(public_bytes)
    return private_path, public_path


def make_repo(tmp: Path) -> Path:
    root = tmp / "repo"
    write(root / "a.txt", "alpha\n")
    write(root / "b.txt", "beta\n")
    return root


def make_signed_manifest(tmp: Path, key_format: str = "pem") -> tuple[Path, Path, Path, Path]:
    root = make_repo(tmp)
    private_path, public_path = make_keypair(tmp / "keys", "release", key_format=key_format)
    manifest_path = tmp / "manifest.json"
    data = build_manifest(
        root,
        "test-release",
        file_paths=[root / "a.txt", root / "b.txt"],
        status="SIGNED_RELEASE",
        origin_attribution="TEST_ORIGIN",
    )
    dump_manifest_file(manifest_path, data)
    sign_manifest_file(manifest_path, private_path, root)
    return root, manifest_path, private_path, public_path


def assert_verifies(root: Path, manifest_path: Path, public_path: Path) -> None:
    result = verify_manifest_file(root, manifest_path, public_key_path=public_path)
    assert result.ok, result.errors


def assert_rejects(root: Path, manifest_path: Path, public_path: Path, *, previous_manifest_path: Path | None = None) -> None:
    result = verify_manifest_file(
        root,
        manifest_path,
        public_key_path=public_path,
        previous_manifest_path=previous_manifest_path,
    )
    assert not result.ok, "verification unexpectedly passed"


def test_p1_valid_manifest_verifies() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root, manifest_path, _private_path, public_path = make_signed_manifest(Path(raw))
        assert_verifies(root, manifest_path, public_path)


def test_p3_pem_key_loading_positive_control() -> None:
    with tempfile.TemporaryDirectory() as raw:
        private_path, public_path = make_keypair(Path(raw), "pem", key_format="pem")
        assert load_private_key(private_path).public_key()
        assert load_public_key(public_path)
        assert public_key_fingerprint_from_file(public_path).startswith("sha256:")


def test_p4_openssh_key_loading_and_manifest_verifies() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root, manifest_path, _private_path, public_path = make_signed_manifest(Path(raw), key_format="openssh")
        assert_verifies(root, manifest_path, public_path)


def test_n1_tampered_file_hash_mismatch() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root, manifest_path, _private_path, public_path = make_signed_manifest(Path(raw))
        write(root / "a.txt", "tampered\n")
        assert_rejects(root, manifest_path, public_path)


def test_n2_added_file_absent_from_manifest_strict_mode() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root, manifest_path, _private_path, public_path = make_signed_manifest(Path(raw))
        write(root / "extra.txt", "extra\n")
        assert_rejects(root, manifest_path, public_path)


def test_n3_listed_file_missing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root, manifest_path, _private_path, public_path = make_signed_manifest(Path(raw))
        (root / "b.txt").unlink()
        assert_rejects(root, manifest_path, public_path)


def test_n4_forged_signature_wrong_key() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        root, manifest_path, _private_path, _public_path = make_signed_manifest(tmp)
        _wrong_private, wrong_public = make_keypair(tmp / "wrong", "wrong")
        assert_rejects(root, manifest_path, wrong_public)


def test_n5_broken_chain_prev_manifest_hash_mismatch() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        root = make_repo(tmp)
        private_path, public_path = make_keypair(tmp / "keys", "chain")
        previous_manifest_path = tmp / "previous.json"
        previous = build_manifest(
            root,
            "previous",
            file_paths=[root / "a.txt"],
            status="UNSIGNED_DRAFT",
            origin_attribution="TEST_ORIGIN",
        )
        dump_manifest_file(previous_manifest_path, previous)
        current_path = tmp / "current.json"
        current = build_manifest(
            root,
            "current",
            file_paths=[root / "a.txt", root / "b.txt"],
            prev_manifest_sha256="0" * 64,
            status="SIGNED_RELEASE",
            origin_attribution="TEST_ORIGIN",
        )
        dump_manifest_file(current_path, current)
        sign_manifest_file(current_path, private_path, root)
        assert_rejects(root, current_path, public_path, previous_manifest_path=previous_manifest_path)


def test_n6_manifest_mutated_after_signing() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root, manifest_path, _private_path, public_path = make_signed_manifest(Path(raw))
        data = load_manifest_file(manifest_path)
        data["release_label"] = "mutated-release"
        manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        assert_rejects(root, manifest_path, public_path)


def test_n7_rotation_record_not_signed_by_previous_key() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        _old_private, old_public = make_keypair(tmp / "keys", "old")
        _new_private, new_public = make_keypair(tmp / "keys", "new")
        record = build_rotation_record(
            old_public_key_fingerprint=public_key_fingerprint_from_file(old_public),
            new_public_key_fingerprint=public_key_fingerprint_from_file(new_public),
            prev_manifest_sha256="1" * 64,
        )
        assert not verify_rotation_record(record, old_public)


def test_n8_boundary_flags_flipped_rejected() -> None:
    with tempfile.TemporaryDirectory() as raw:
        root = make_repo(Path(raw))
        data = build_manifest(root, "boundary", file_paths=[root / "a.txt"], origin_attribution="TEST_ORIGIN")
        data["boundary"] = dict(data["boundary"])
        data["boundary"]["replaces_creator_theory_high_frame"] = True
        try:
            validate_manifest_data(data)
        except ValueError:
            return
        raise AssertionError("boundary flip was accepted")


def test_n9_private_key_inside_repo_refused() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        repo = make_repo(tmp)
        inside_key = repo / "inside_TEST_KEY_NOT_A_REAL_IDENTITY_KEY.pem"
        private_path, _public_path = make_keypair(tmp / "keys", "inside")
        shutil.copyfile(private_path, inside_key)
        try:
            refuse_private_key_inside_repo(repo, inside_key)
        except ValueError:
            return
        raise AssertionError("inside-repo private key path was accepted")


def test_n10_manifest_public_key_fingerprint_mismatch() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        root, manifest_path, _private_path, public_path = make_signed_manifest(tmp)
        _wrong_private, wrong_public = make_keypair(tmp / "wrong", "wrong")
        data = load_manifest_file(manifest_path)
        data["signing"]["public_key_fingerprint"] = public_key_fingerprint_from_file(wrong_public)
        manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result = verify_manifest_file(root, manifest_path, public_key_path=public_path)
        assert not result.ok, "verification unexpectedly passed"
        assert any("public key fingerprint" in error for error in result.errors), result.errors


def test_p2_valid_rotation_verifies() -> None:
    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        old_private, old_public = make_keypair(tmp / "keys", "old")
        _new_private, new_public = make_keypair(tmp / "keys", "new")
        repo = make_repo(tmp)
        record = build_rotation_record(
            old_public_key_fingerprint=public_key_fingerprint_from_file(old_public),
            new_public_key_fingerprint=public_key_fingerprint_from_file(new_public),
            prev_manifest_sha256=sha256_file(repo / "a.txt"),
        )
        signed = sign_rotation_record(record, old_private, repo)
        assert verify_rotation_record(signed, old_public)


def test_crypto_absence_path_is_honest() -> None:
    if Ed25519PrivateKey is not None:
        return
    with tempfile.TemporaryDirectory() as raw:
        root = make_repo(Path(raw))
        data = build_manifest(root, "unsigned", file_paths=[root / "a.txt"], origin_attribution="TEST_ORIGIN")
        assert data["signature"]["value"] is None


def main() -> int:
    if Ed25519PrivateKey is None:
        check("cryptography absence path", test_crypto_absence_path_is_honest)
    else:
        check("P1 valid manifest verifies", test_p1_valid_manifest_verifies)
        check("P2 valid rotation verifies", test_p2_valid_rotation_verifies)
        check("P3 PEM key loading positive control", test_p3_pem_key_loading_positive_control)
        check("P4 OpenSSH key loading and manifest verifies", test_p4_openssh_key_loading_and_manifest_verifies)
        check("N1 tampered file content fails", test_n1_tampered_file_hash_mismatch)
        check("N2 unmanifested added file fails", test_n2_added_file_absent_from_manifest_strict_mode)
        check("N3 listed file missing fails", test_n3_listed_file_missing)
        check("N4 forged signature with wrong key fails", test_n4_forged_signature_wrong_key)
        check("N5 broken chain fails", test_n5_broken_chain_prev_manifest_hash_mismatch)
        check("N6 manifest mutated after signing fails", test_n6_manifest_mutated_after_signing)
        check("N7 unsigned rotation record fails", test_n7_rotation_record_not_signed_by_previous_key)
        check("N8 boundary flag flip rejected", test_n8_boundary_flags_flipped_rejected)
        check("N9 inside-repo private-key path refused", test_n9_private_key_inside_repo_refused)
        check("N10 public key fingerprint mismatch fails", test_n10_manifest_public_key_fingerprint_mismatch)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
