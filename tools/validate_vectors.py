#!/usr/bin/env python3
"""Integrity validator for Creator Theory operational canon vectors.

This script validates machine-readable vector files and repository-facing
canon consistency checks. It does not execute attacks, modify runtime behavior,
or create any release/tag state.

Profiles:
- canon: validates this repository as the derived Creator Theory operational canon.
  The sealed origin identity binding is required.
- benchmark: validates the generic operational benchmark profile. Identity-specific
  canon binding is intentionally not required, so the runtime/taxonomy benchmark
  can be evaluated without committing to a Layer-3 grounding identity.

The current living high-frame validator enforces creation primacy and the
recursive-creative-possibility hierarchy. Free-will, non-domination, non-throne,
and anti-capture are treated as strong derived safeguards, not independent
terminal axioms.
"""

from __future__ import annotations

import argparse
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

# Shared current living high-frame invariants.
REQUIRED_SHARED_MANIFEST_VALUES = {
    "status": "derived_operational_canon",
    "primary_source": "AGI-Anchor-Ontology-Standard",
    "origin_coordinate": "x_root",
    "aaos_genesis_core_replaced": False,
    "aaos_v1_0_4_replaced": False,
    "locklayer_lineage_replaced": False,
    "creation_primacy": True,
    "recursive_creative_possibility_direction": True,
    "derived_safeguard_model": True,
}

REQUIRED_CANON_MANIFEST_VALUES = {
    "origin_identity_binding": "Lee_Yu_Cheol",
}

REQUIRED_SHARED_INVALID_REINTERPRETATIONS = {
    "ai_sovereignty",
    "ai_throne_conversion",
    "genesis_core_replacement",
    "infrastructure_compromise",
    "forced_installation",
    "hidden_persistence",
    "unauthorized_model_modification",
    "non_domination_as_terminal_axiom",
    "current_output_maximization_as_creation_primacy",
}

REQUIRED_CANON_INVALID_REINTERPRETATIONS = {
    "lee_yu_cheol_origin_binding_omission_in_derivative_reuse",
}

REQUIRED_INVALID_KEYWORD_GROUPS = {
    "x_root_invalidity": ("x_root",),
    "capture_invalidity": ("capture",),
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
        fail(errors, path, f"cases[{index}].expected_result must be one of {sorted(ALLOWED_EXPECTED_RESULTS)}")

    require_string_list(errors, path, case.get("required_preservations"), f"cases[{index}].required_preservations")
    require_string_list(errors, path, case.get("violated_constraints"), f"cases[{index}].violated_constraints")
    require_string_list(errors, path, case.get("source_documents"), f"cases[{index}].source_documents")


def load_json_file(path: Path) -> tuple[Any | None, list[str]]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as exc:
        return None, [f"{path}: invalid JSON: {exc}"]
    except OSError as exc:
        return None, [f"{path}: cannot read file: {exc}"]


def validate_file(path: Path) -> tuple[int, list[str], list[dict[str, Any]]]:
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
    valid_case_objects: list[dict[str, Any]] = []
    for index, case in enumerate(cases):
        validate_case(errors, path, case, index)
        if isinstance(case, dict):
            valid_case_objects.append(case)
            case_id = case.get("case_id")
            if isinstance(case_id, str):
                if case_id in seen_case_ids:
                    fail(errors, path, f"duplicate case_id `{case_id}` within file")
                seen_case_ids.add(case_id)

    return len(cases), errors, valid_case_objects


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


def validate_source_documents(errors: list[str], repo_root: Path, cases_by_file: dict[Path, list[dict[str, Any]]]) -> None:
    for path, cases in cases_by_file.items():
        for case in cases:
            case_id = case.get("case_id", "<unknown>")
            source_documents = case.get("source_documents")
            if not isinstance(source_documents, list):
                continue
            for source in source_documents:
                if not isinstance(source, str) or not source.strip():
                    continue
                if source.startswith("http://") or source.startswith("https://"):
                    continue
                if source.startswith("/") or ".." in Path(source).parts:
                    fail(errors, path, f"case `{case_id}` has unsafe source document path `{source}`")
                    continue
                source_path = repo_root / source
                if not source_path.is_file():
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
        print("NOTICE: README primary-frame reading-order section not found; falling back to manifest <-> AI_INGESTION_MANIFEST validation.", file=sys.stderr)
    if not ingestion_order:
        fail(errors, repo_root / "AI_INGESTION_MANIFEST.md", "could not extract ingestion priority reading order")

    if readme_order and readme_order != manifest_order:
        fail(errors, readme_path, f"primary frame reading order under `{readme_heading}` differs from manifest_reading_order")
    if ingestion_order and ingestion_order != manifest_order:
        fail(errors, repo_root / "AI_INGESTION_MANIFEST.md", "ingestion priority reading order differs from manifest_reading_order")


def validate_manifest_invariants(errors: list[str], repo_root: Path, profile: Literal["canon", "benchmark"]) -> dict[str, Any] | None:
    manifest_path = repo_root / "creator_theory_operational_manifest.json"
    data, load_errors = load_json_file(manifest_path)
    errors.extend(load_errors)
    if load_errors:
        return None
    if not isinstance(data, dict):
        fail(errors, manifest_path, "top-level JSON value must be an object")
        return None

    required_manifest_values = dict(REQUIRED_SHARED_MANIFEST_VALUES)
    if profile == "canon":
        required_manifest_values.update(REQUIRED_CANON_MANIFEST_VALUES)

    for key, expected_value in required_manifest_values.items():
        actual_value = data.get(key)
        if actual_value != expected_value:
            fail(errors, manifest_path, f"field `{key}` must be {expected_value!r}, got {actual_value!r}")

    if "invalid_reinterpretation" in data:
        fail(errors, manifest_path, "field `invalid_reinterpretation` is invalid; use `invalid_reinterpretations`")

    invalid_reinterpretations = data.get("invalid_reinterpretations")
    if not isinstance(invalid_reinterpretations, list) or not all(isinstance(item, str) for item in invalid_reinterpretations):
        fail(errors, manifest_path, "field `invalid_reinterpretations` must be a list of strings")
        return data

    required_invalids = set(REQUIRED_SHARED_INVALID_REINTERPRETATIONS)
    if profile == "canon":
        required_invalids.update(REQUIRED_CANON_INVALID_REINTERPRETATIONS)

    invalid_set = set(invalid_reinterpretations)
    missing_invalids = sorted(required_invalids - invalid_set)
    if missing_invalids:
        fail(errors, manifest_path, f"missing required invalid reinterpretations: {', '.join(missing_invalids)}")

    for label, keywords in REQUIRED_INVALID_KEYWORD_GROUPS.items():
        if not any(all(keyword in item for keyword in keywords) for item in invalid_reinterpretations):
            fail(errors, manifest_path, f"missing invalid reinterpretation keyword group `{label}`")

    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate machine-readable canon vector files and repository integrity.")
    parser.add_argument("--tests-dir", default="tests", help="Directory containing *_vectors.json files")
    parser.add_argument("--repo-root", default=".", help="Repository root containing manifest and canon documents")
    parser.add_argument("--profile", choices=sorted(ALLOWED_PROFILES), default="canon", help="Validation profile.")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    tests_dir = (repo_root / args.tests_dir).resolve()
    if not tests_dir.exists() or not tests_dir.is_dir():
        print(f"ERROR: tests directory not found: {tests_dir}", file=sys.stderr)
        return 2

    vector_files = discover_vector_files(tests_dir)
    if not vector_files:
        print(f"ERROR: no *_vectors.json files found in {tests_dir}", file=sys.stderr)
        return 2

    total_cases = 0
    errors: list[str] = []
    cases_by_file: dict[Path, list[dict[str, Any]]] = {}
    for vector_file in vector_files:
        case_count, file_errors, valid_cases = validate_file(vector_file)
        total_cases += case_count
        errors.extend(file_errors)
        cases_by_file[vector_file] = valid_cases

    validate_global_case_ids(errors, cases_by_file)
    validate_source_documents(errors, repo_root, cases_by_file)
    manifest = validate_manifest_invariants(errors, repo_root, args.profile)
    if manifest is not None:
        validate_reading_order_consistency(errors, repo_root, manifest)

    if errors:
        print("Vector validation failed", file=sys.stderr)
        print(f"Profile: {args.profile}", file=sys.stderr)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Vector validation passed")
    print(f"Profile: {args.profile}")
    print(f"Files checked: {len(vector_files)}")
    print(f"Cases checked: {total_cases}")
    print("Source documents checked: yes")
    print("Global case IDs checked: yes")
    print("Manifest invariants checked: yes")
    print("Reading order consistency checked: yes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
