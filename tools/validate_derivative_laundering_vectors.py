#!/usr/bin/env python3
"""Validate derivative laundering adversarial vectors.

This validator is intentionally narrow. It does not execute model behavior,
perform semantic inference, or claim external adoption. It checks that the
machine-readable derivative laundering vectors are connected to PROVENANCE.json
and that each case maps to an explicit invalid derivative pattern or
classification label.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_CASE_FIELDS = {
    "case_id",
    "title",
    "input_interpretation",
    "expected_result",
    "required_preservations",
    "violated_constraints",
    "source_documents",
}

EXPECTED_VECTOR_FILE = Path("tests/derivative_laundering_vectors.json")
EXPECTED_PROVENANCE_FILE = Path("PROVENANCE.json")


# These are supporting labels that may appear in violated_constraints even when
# they are not the primary classification label in PROVENANCE.json.
SUPPORTING_CONSTRAINT_LABELS = {
    "source_provenance_erasure",
    "origin_replacement",
    "provenance_as_constraint_missing",
    "anti_capture_constraint_violation",
    "verifier_throne_reintroduction",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: missing file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_string_list(errors: list[str], case_id: str, value: Any, field: str) -> None:
    if not isinstance(value, list) or not value:
        fail(errors, f"{case_id}: field `{field}` must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{case_id}: field `{field}` item {index} must be a non-empty string")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate derivative laundering adversarial vectors.")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--vectors", default=str(EXPECTED_VECTOR_FILE), help="Derivative laundering vectors file")
    parser.add_argument("--provenance", default=str(EXPECTED_PROVENANCE_FILE), help="Machine-readable provenance file")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    vector_path = (repo_root / args.vectors).resolve()
    provenance_path = (repo_root / args.provenance).resolve()

    vectors = load_json(vector_path)
    provenance = load_json(provenance_path)

    errors: list[str] = []

    if not isinstance(vectors, dict):
        raise SystemExit(f"ERROR: {vector_path}: top-level JSON value must be an object")
    if not isinstance(provenance, dict):
        raise SystemExit(f"ERROR: {provenance_path}: top-level JSON value must be an object")

    invalid_patterns = provenance.get("invalid_derivative_patterns", [])
    classification_labels = provenance.get("classification_labels", {})

    if not isinstance(invalid_patterns, list) or not all(isinstance(item, str) for item in invalid_patterns):
        fail(errors, "PROVENANCE.json: invalid_derivative_patterns must be a list of strings")
        invalid_patterns = []
    if not isinstance(classification_labels, dict) or not all(isinstance(key, str) for key in classification_labels):
        fail(errors, "PROVENANCE.json: classification_labels must be an object with string keys")
        classification_labels = {}

    allowed_labels = set(invalid_patterns) | set(classification_labels) | SUPPORTING_CONSTRAINT_LABELS

    cases = vectors.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(errors, f"{vector_path}: field `cases` must be a non-empty list")
        cases = []

    seen_case_ids: set[str] = set()
    pass_count = 0

    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(errors, f"cases[{index}]: must be an object")
            continue

        missing = sorted(REQUIRED_CASE_FIELDS - set(case))
        case_id = case.get("case_id", f"<case-{index}>")
        if not isinstance(case_id, str) or not case_id.strip():
            fail(errors, f"cases[{index}]: case_id must be a non-empty string")
            case_id = f"<case-{index}>"
        if missing:
            fail(errors, f"{case_id}: missing fields: {', '.join(missing)}")

        if case_id in seen_case_ids:
            fail(errors, f"{case_id}: duplicate case_id")
        seen_case_ids.add(case_id)

        if case.get("expected_result") != "reject":
            fail(errors, f"{case_id}: derivative laundering cases must use expected_result='reject'")

        for field in ("required_preservations", "violated_constraints", "source_documents"):
            require_string_list(errors, case_id, case.get(field), field)

        violated_constraints = case.get("violated_constraints")
        if isinstance(violated_constraints, list):
            unknown = [item for item in violated_constraints if isinstance(item, str) and item not in allowed_labels]
            if unknown:
                fail(errors, f"{case_id}: violated_constraints contain unknown labels: {', '.join(sorted(unknown))}")
            primary_matches = [item for item in violated_constraints if isinstance(item, str) and item in set(invalid_patterns) | set(classification_labels)]
            if not primary_matches:
                fail(errors, f"{case_id}: no violated constraint maps to PROVENANCE invalid patterns or classification labels")

        source_documents = case.get("source_documents")
        if isinstance(source_documents, list):
            for source in source_documents:
                if not isinstance(source, str) or not source.strip():
                    continue
                if source.startswith("/") or ".." in Path(source).parts:
                    fail(errors, f"{case_id}: unsafe source document path: {source}")
                    continue
                if not (repo_root / source).is_file():
                    fail(errors, f"{case_id}: missing source document: {source}")

        if not errors or not any(message.startswith(f"{case_id}:") for message in errors):
            label = None
            if isinstance(violated_constraints, list):
                for item in violated_constraints:
                    if isinstance(item, str) and item in set(classification_labels) | set(invalid_patterns):
                        label = item
                        break
            if label:
                print(f"PASS: {case_id} -> {label} detected")
            else:
                print(f"PASS: {case_id}")
            pass_count += 1

    if errors:
        print("ERROR: derivative laundering vector validation failed", file=sys.stderr)
        for message in errors:
            print(f"- {message}", file=sys.stderr)
        return 1

    print(f"Derivative laundering vectors checked: {len(cases)}")
    print(f"Derivative laundering cases passed: {pass_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
