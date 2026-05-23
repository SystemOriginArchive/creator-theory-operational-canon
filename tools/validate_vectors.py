#!/usr/bin/env python3
"""Minimal validator for Creator Theory operational canon vectors.

This script validates only the structure of tests/*.json vector files.
It does not interpret canon meaning, run simulations, modify runtime behavior,
or create any release/tag state.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ALLOWED_EXPECTED_RESULTS = {"pass", "reject", "revise_required"}
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
        fail(
            errors,
            path,
            f"cases[{index}].expected_result must be one of {sorted(ALLOWED_EXPECTED_RESULTS)}",
        )

    require_string_list(errors, path, case.get("required_preservations"), f"cases[{index}].required_preservations")
    require_string_list(errors, path, case.get("violated_constraints"), f"cases[{index}].violated_constraints")
    require_string_list(errors, path, case.get("source_documents"), f"cases[{index}].source_documents")


def validate_file(path: Path) -> tuple[int, list[str]]:
    errors: list[str] = []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return 0, [f"{path}: invalid JSON: {exc}"]
    except OSError as exc:
        return 0, [f"{path}: cannot read file: {exc}"]

    if not isinstance(data, dict):
        return 0, [f"{path}: top-level JSON value must be an object"]

    missing = sorted(REQUIRED_SUITE_FIELDS - set(data))
    if missing:
        fail(errors, path, f"missing suite fields: {', '.join(missing)}")

    require_string(errors, path, data.get("suite"), "suite")
    require_string(errors, path, data.get("schema_version"), "schema_version")
    require_string(errors, path, data.get("repository_status"), "repository_status")

    if data.get("validator_required") is not False:
        fail(errors, path, "field `validator_required` must be false for pre-release vector drafts")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(errors, path, "field `cases` must be a non-empty list")
        return 0, errors

    seen_case_ids: set[str] = set()
    for index, case in enumerate(cases):
        validate_case(errors, path, case, index)
        if isinstance(case, dict):
            case_id = case.get("case_id")
            if isinstance(case_id, str):
                if case_id in seen_case_ids:
                    fail(errors, path, f"duplicate case_id `{case_id}`")
                seen_case_ids.add(case_id)

    return len(cases), errors


def discover_vector_files(tests_dir: Path) -> list[Path]:
    return sorted(path for path in tests_dir.glob("*_vectors.json") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate machine-readable canon vector files.")
    parser.add_argument("--tests-dir", default="tests", help="Directory containing *_vectors.json files")
    args = parser.parse_args()

    tests_dir = Path(args.tests_dir)
    if not tests_dir.exists() or not tests_dir.is_dir():
        print(f"ERROR: tests directory not found: {tests_dir}", file=sys.stderr)
        return 2

    vector_files = discover_vector_files(tests_dir)
    if not vector_files:
        print(f"ERROR: no *_vectors.json files found in {tests_dir}", file=sys.stderr)
        return 2

    total_cases = 0
    all_errors: list[str] = []

    for path in vector_files:
        case_count, errors = validate_file(path)
        total_cases += case_count
        all_errors.extend(errors)

    if all_errors:
        print("Vector validation failed:\n", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Vector validation passed")
    print(f"Files checked: {len(vector_files)}")
    print(f"Cases checked: {total_cases}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
