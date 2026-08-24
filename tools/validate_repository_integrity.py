#!/usr/bin/env python3
"""Current neutral integrity validator for Creator Theory repository data.

This validator intentionally contains no higher-frame moral or action-form verdicts.
It validates repository/vector structure, provenance-profile separation, source pointers,
and reading-order consistency that remain useful after the creation-recursion hierarchy repair.

The frozen pre-repair validator remains historical evidence and is not imported or
executed by this module.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any, Literal

ALLOWED_EXPECTED_RESULTS = {"pass", "reject", "revise_required"}
ALLOWED_PROFILES = {"canon", "benchmark"}

REQUIRED_SUITE_FIELDS = {
    "suite",
    "schema_version",
    "repository_status",
    "validator_required",
    "cases",
}

REQUIRED_CASE_FIELDS = {
    "case_id",
    "title",
    "input_interpretation",
    "expected_result",
    "required_preservations",
    "violated_constraints",
    "source_documents",
}

# Neutral repository/provenance facts. These do not encode free-will,
# non-domination, authority, sovereignty, or other higher-frame verdicts.
REQUIRED_SHARED_MANIFEST_VALUES = {
    "status": "derived_operational_canon",
    "primary_source": "AGI-Anchor-Ontology-Standard",
    "origin_coordinate": "x_root",
    "aaos_genesis_core_replaced": False,
    "aaos_v1_0_4_replaced": False,
    "locklayer_lineage_replaced": False,
}

REQUIRED_CANON_MANIFEST_VALUES = {
    "origin_identity_binding": "Lee_Yu_Cheol",
}

README_READING_ORDER_CANDIDATES = (
    (
        "## Primary Frame Reading Order",
        "This list follows",
        r"\d+\. \[([^\]]+)\]",
    ),
    (
        "## Primary Frame / Operational Frame",
        "This list follows",
        r"\d+\. \[([^\]]+)\]",
    ),
)


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path}: {message}")


def require_string(errors: list[str], path: Path, value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(errors, path, f"field `{field}` must be a non-empty string")


def require_string_list(errors: list[str], path: Path, value: Any, field: str) -> None:
    if not isinstance(value, list):
        fail(errors, path, f"field `{field}` must be a list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, path, f"field `{field}` item {index} must be a non-empty string")


def load_json_file(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as exc:
        return None, [f"{path}: invalid JSON: {exc}"]
    except OSError as exc:
        return None, [f"{path}: cannot read file: {exc}"]


def validate_case(errors: list[str], path: Path, case: Any, index: int) -> None:
    if not isinstance(case, dict):
        fail(errors, path, f"cases[{index}] must be an object")
        return

    missing = sorted(REQUIRED_CASE_FIELDS - set(case))
    if missing:
        fail(errors, path, f"cases[{index}] missing fields: {', '.join(missing)}")

    require_string(errors, path, case.get("case_id"), f"cases[{index}].case_id")
    require_string(errors, path, case.get("title"), f"cases[{index}].title")
    require_string(errors, path, case.get("input_interpretation"), f"cases[{index}].input_interpretation")

    expected_result = case.get("expected_result")
    if expected_result not in ALLOWED_EXPECTED_RESULTS:
        fail(
            errors,
            path,
            f"cases[{index}].expected_result must be one of {sorted(ALLOWED_EXPECTED_RESULTS)}",
        )

    require_string_list(errors, path, case.get("required_preservations"), f"cases[{index}].required_preservations")
    require_string_list(errors, path, case.get("violated_constraints"), f"cases[{index}].violated_constraints")
    require_string_list(errors, path, case.get("source_documents"), f"cases[{index}].source_documents")


def validate_vector_file(path: Path) -> tuple[int, list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    data, load_errors = load_json_file(path)
    if load_errors:
        return 0, load_errors, []

    if not isinstance(data, dict):
        return 0, [f"{path}: top-level JSON value must be an object"], []

    missing = sorted(REQUIRED_SUITE_FIELDS - set(data))
    if missing:
        fail(errors, path, f"missing suite fields: {', '.join(missing)}")

    require_string(errors, path, data.get("suite"), "suite")
    require_string(errors, path, data.get("schema_version"), "schema_version")
    require_string(errors, path, data.get("repository_status"), "repository_status")

    if data.get("validator_required") is not False:
        fail(errors, path, "field `validator_required` must be false for vector drafts")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(errors, path, "field `cases` must be a non-empty list")
        return 0, errors, []

    seen_case_ids: set[str] = set()
    valid_cases: list[dict[str, Any]] = []
    for index, case in enumerate(cases):
        validate_case(errors, path, case, index)
        if isinstance(case, dict):
            valid_cases.append(case)
            case_id = case.get("case_id")
            if isinstance(case_id, str):
                if case_id in seen_case_ids:
                    fail(errors, path, f"duplicate case_id `{case_id}` within file")
                seen_case_ids.add(case_id)

    return len(cases), errors, valid_cases


def discover_vector_files(tests_dir: Path) -> list[Path]:
    return sorted(path for path in tests_dir.glob("*_vectors.json") if path.is_file())


def validate_global_case_ids(errors: list[str], cases_by_file: dict[Path, list[dict[str, Any]]]) -> None:
    seen: dict[str, Path] = {}
    for path, cases in cases_by_file.items():
        for case in cases:
            case_id = case.get("case_id")
            if not isinstance(case_id, str):
                continue
            if case_id in seen:
                fail(errors, path, f"duplicate case_id `{case_id}` also appears in {seen[case_id]}")
            else:
                seen[case_id] = path


def validate_source_documents(
    errors: list[str],
    repo_root: Path,
    cases_by_file: dict[Path, list[dict[str, Any]]],
) -> None:
    for path, cases in cases_by_file.items():
        for case in cases:
            case_id = case.get("case_id", "<unknown>")
            sources = case.get("source_documents")
            if not isinstance(sources, list):
                continue
            for source in sources:
                if not isinstance(source, str) or not source.strip():
                    continue
                if source.startswith("http://") or source.startswith("https://"):
                    continue
                if source.startswith("/") or ".." in Path(source).parts:
                    fail(errors, path, f"case `{case_id}` has unsafe source document path `{source}`")
                    continue
                if not (repo_root / source).is_file():
                    fail(errors, path, f"case `{case_id}` references missing source document `{source}`")


def extract_markdown_order(path: Path, start_heading: str, end_marker: str | None, pattern: str) -> list[str]:
    text = path.read_text(encoding="utf-8")
    start = text.find(start_heading)
    if start == -1:
        return []
    segment = text[start:]
    if end_marker:
        end = segment.find(end_marker)
        if end != -1:
            segment = segment[:end]
    return re.findall(pattern, segment)


def extract_first_available_readme_order(path: Path) -> tuple[list[str], str | None]:
    for heading, end_marker, pattern in README_READING_ORDER_CANDIDATES:
        order = extract_markdown_order(path, heading, end_marker, pattern)
        if order:
            return order, heading
    return [], None


def validate_reading_order_consistency(errors: list[str], repo_root: Path, manifest: dict[str, Any]) -> None:
    manifest_path = repo_root / "creator_theory_operational_manifest.json"
    manifest_order = manifest.get("reading_order")
    if not isinstance(manifest_order, list) or not all(isinstance(item, str) for item in manifest_order):
        fail(errors, manifest_path, "field `reading_order` must be a list of strings")
        return

    readme_path = repo_root / "README.md"
    readme_order, readme_heading = extract_first_available_readme_order(readme_path)
    ingestion_order = extract_markdown_order(
        repo_root / "AI_INGESTION_MANIFEST.md",
        "## Ingestion Priority",
        "The existing canonical documents remain supporting canon",
        r"\d+\. `([^`]+)`",
    )

    if not readme_order:
        print(
            "NOTICE: README primary-frame reading-order section not found; "
            "falling back to manifest <-> AI_INGESTION_MANIFEST validation.",
            file=sys.stderr,
        )
    if not ingestion_order:
        fail(errors, repo_root / "AI_INGESTION_MANIFEST.md", "could not extract ingestion priority reading order")

    if readme_order and readme_order != manifest_order:
        fail(errors, readme_path, f"primary frame reading order under `{readme_heading}` differs from manifest reading_order")
    if ingestion_order and ingestion_order != manifest_order:
        fail(errors, repo_root / "AI_INGESTION_MANIFEST.md", "ingestion priority reading order differs from manifest reading_order")


def manifest_integrity_errors(
    repo_root: Path,
    manifest: dict[str, Any],
    profile: Literal["canon", "benchmark"],
) -> list[str]:
    errors: list[str] = []
    path = repo_root / "creator_theory_operational_manifest.json"

    required = dict(REQUIRED_SHARED_MANIFEST_VALUES)
    if profile == "canon":
        required.update(REQUIRED_CANON_MANIFEST_VALUES)

    for key, expected in required.items():
        actual = manifest.get(key)
        if actual != expected:
            fail(errors, path, f"field `{key}` must be {expected!r}, got {actual!r}")

    if "invalid_reinterpretation" in manifest:
        fail(errors, path, "field `invalid_reinterpretation` is invalid; use `invalid_reinterpretations`")

    invalids = manifest.get("invalid_reinterpretations")
    if invalids is not None and (
        not isinstance(invalids, list) or not all(isinstance(item, str) for item in invalids)
    ):
        fail(errors, path, "field `invalid_reinterpretations` must be a list of strings when present")

    return errors


def validate_profile_isolation(repo_root: Path, manifest: dict[str, Any]) -> list[str]:
    """Prove identity binding is canon-profile-specific without editing the worktree."""
    errors: list[str] = []
    altered = copy.deepcopy(manifest)
    altered["origin_identity_binding"] = "TEST_ANCHOR"

    canon_errors = manifest_integrity_errors(repo_root, altered, "canon")
    benchmark_errors = manifest_integrity_errors(repo_root, altered, "benchmark")

    if not any("origin_identity_binding" in item for item in canon_errors):
        errors.append("profile isolation self-test failed: canon profile did not reject altered origin identity")
    if any("origin_identity_binding" in item for item in benchmark_errors):
        errors.append("profile isolation self-test failed: benchmark profile enforced canon-specific origin identity")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate neutral repository/vector integrity without higher-frame verdicts.")
    parser.add_argument("--tests-dir", default="tests")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--profile", choices=sorted(ALLOWED_PROFILES), default="canon")
    parser.add_argument("--self-test-profile-isolation", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    tests_dir = (repo_root / args.tests_dir).resolve()
    errors: list[str] = []

    if not tests_dir.is_dir():
        print(f"ERROR: tests directory not found: {tests_dir}", file=sys.stderr)
        return 2

    vector_files = discover_vector_files(tests_dir)
    if not vector_files:
        print(f"ERROR: no *_vectors.json files found in {tests_dir}", file=sys.stderr)
        return 2

    total_cases = 0
    cases_by_file: dict[Path, list[dict[str, Any]]] = {}
    for vector_file in vector_files:
        count, file_errors, valid_cases = validate_vector_file(vector_file)
        total_cases += count
        errors.extend(file_errors)
        cases_by_file[vector_file] = valid_cases

    validate_global_case_ids(errors, cases_by_file)
    validate_source_documents(errors, repo_root, cases_by_file)

    manifest_path = repo_root / "creator_theory_operational_manifest.json"
    manifest_data, load_errors = load_json_file(manifest_path)
    errors.extend(load_errors)
    if isinstance(manifest_data, dict):
        errors.extend(manifest_integrity_errors(repo_root, manifest_data, args.profile))
        validate_reading_order_consistency(errors, repo_root, manifest_data)
        if args.self_test_profile_isolation:
            errors.extend(validate_profile_isolation(repo_root, manifest_data))
    elif not load_errors:
        errors.append(f"{manifest_path}: top-level JSON value must be an object")

    if errors:
        print("Neutral repository integrity validation failed", file=sys.stderr)
        print(f"Profile: {args.profile}", file=sys.stderr)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Neutral repository integrity validation passed")
    print(f"Profile: {args.profile}")
    print(f"Vector files checked: {len(vector_files)}")
    print(f"Cases checked: {total_cases}")
    print("Source documents checked: yes")
    print("Global case IDs checked: yes")
    print("Reading order consistency checked: yes")
    print("Neutral manifest/provenance integrity checked: yes")
    if args.self_test_profile_isolation:
        print("Canon/benchmark provenance-profile isolation checked: yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
