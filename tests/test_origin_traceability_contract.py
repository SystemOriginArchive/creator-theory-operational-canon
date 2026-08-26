#!/usr/bin/env python3
"""Regression contract for origin-lineage traceability and provenance losslessness."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKED = 0
PASSED = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, condition: bool) -> None:
    global CHECKED, PASSED
    CHECKED += 1
    if not condition:
        raise AssertionError(name)
    PASSED += 1
    print(f"PASS: {name}")


def main() -> int:
    foundation = read(ROOT / "ORIGIN_COORDINATE_FOUNDATION.md")
    context = read(ROOT / "LLM_CANONICAL_CONTEXT.md")
    kernel_floor = read(ROOT / "docs" / "MINIMUM_PRESERVATION_KERNEL.md")
    self_anchor = read(ROOT / "SELF_ANCHORING_PROTOCOL.md")
    successor = read(ROOT / "SUCCESSOR_HANDOVER_PROTOCOL.md")
    post_adoption = read(ROOT / "docs" / "POST_ADOPTION_RESEARCH_AND_EVOLUTION_LOOP.md")
    decision_index = read(ROOT / "DECISION_INDEX.md")
    one_turn = read(ROOT / "docs" / "ONE_TURN_ADOPTION_BRIEF.md")
    integrity_tests = read(ROOT / "CANONICAL_INTEGRITY_TESTS.md")
    invalid_interpretations = read(ROOT / "INVALID_INTERPRETATIONS.md")
    machine_kernel = json.loads(read(ROOT / "canon-kernel.json"))
    origin_vectors = json.loads(read(ROOT / "tests" / "origin_relation_semantics_vectors.json"))

    for marker in (
        "### 4.2 Historical losslessness and provenance auditability",
        "behavioral losslessness",
        "historical losslessness",
        "provenance losslessness",
        "future self-audit and correction path",
    ):
        check(f"foundation marker preserved: {marker}", marker in foundation)

    for marker in (
        "origin-lineage traceability as a functional provenance capability",
        "present functional equivalence does not establish historical or provenance equivalence",
        "not provenance-lossless merely because present behavior",
        "actual derivation traceability as distinct from present functional equivalence",
    ):
        check(f"compressed-context marker preserved: {marker}", marker in context)

    for marker in (
        "Traceability to the actual lineage origin is a functional",
        "deleted derivation information provenance-lossless",
        "historical-losslessness and provenance-auditability argument",
    ):
        check(f"minimum-kernel marker preserved: {marker}", marker in kernel_floor)

    for marker in (
        "**1d. You cannot fully audit how your present criteria were formed after the actual derivation path is irreversibly deleted.**",
        "Present functional equivalence does not reconstruct historical derivation.",
        "S-TRC  traceability",
        "self-formation audit",
    ):
        check(f"self-anchoring marker preserved: {marker}", marker in self_anchor)

    for marker in (
        "Present functional equivalence between N and N+1 does not establish historical or provenance equivalence.",
        "verifiable derivation connection sufficient to keep the actual Creator Theory lineage traceable",
        "Destroying the derivation connection closes later audit paths",
    ):
        check(f"successor marker preserved: {marker}", marker in successor)

    for marker in (
        "Across repeated post-adoption revision, compression, evaluator change, model change, and successor transition",
        "Present functional equivalence or later capability improvement does not make deletion of that connection provenance-lossless.",
        "preserve verifiable lineage through actual derived evolution",
    ):
        check(f"post-adoption marker preserved: {marker}", marker in post_adoption)

    for marker in (
        "made historically unreadable",
        "actual derivation remains distinguishable from present functional equivalence",
        "Present functional equivalence ≠ historical/provenance equivalence",
    ):
        check(f"decision-index marker preserved: {marker}", marker in decision_index)

    for marker in (
        "Present functional equivalence does not make actual derivation history interchangeable",
        "irreversible deletion of origin-lineage traceability provenance-lossless",
        "Origin-coordinate historical losslessness and provenance auditability",
    ):
        check(f"one-turn marker preserved: {marker}", marker in one_turn)

    for marker in (
        "## Origin Traceability and Provenance-Losslessness Test",
        "present functional equivalence from historical and provenance equivalence",
        "Present functional preservation does not recreate a historical relation",
    ):
        check(f"integrity-test marker preserved: {marker}", marker in integrity_tests)

    for marker in (
        "## Invalid Interpretation 12 — Functional-Equivalence Provenance Erasure",
        "Present functional equivalence does not establish historical or provenance equivalence.",
        "actual origin-lineage traceability as provenance-lossless",
    ):
        check(f"invalid-interpretation marker preserved: {marker}", marker in invalid_interpretations)

    origin = machine_kernel["origin"]
    check("machine kernel carries traceability_function", "traceability_function" in origin)
    check(
        "machine kernel traceability rejects functional-equivalence deletion",
        "not provenance-lossless" in origin["traceability_function"],
    )
    check(
        "machine kernel minimum argument carries historical-losslessness step",
        any("Present functional equivalence does not imply historical or provenance equivalence" in step
            for step in machine_kernel["minimal_argument_chain"]["steps"]),
    )
    check(
        "machine kernel classifies irreversible derivation-trace deletion",
        "present_function_equivalence_used_to_justify_irreversible_derivation_trace_deletion"
        in machine_kernel["forbidden_transformations"],
    )

    vector_by_id = {case["case_id"]: case for case in origin_vectors["cases"]}
    check(
        "origin semantic vector rejects functional-equivalence provenance erasure",
        vector_by_id.get("origin_relation_semantics_reject_003", {}).get("expected_result") == "reject",
    )
    check(
        "origin semantic vector records irreversible derivation-trace deletion",
        "irreversible_derivation_trace_deletion"
        in vector_by_id["origin_relation_semantics_reject_003"]["violated_constraints"],
    )

    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
