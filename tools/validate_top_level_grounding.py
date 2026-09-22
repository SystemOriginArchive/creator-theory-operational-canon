#!/usr/bin/env python3
"""Semantic regression checks for the source-to-recursion grounding bridge.

This validator checks authored preservation structure and machine-readable markers.
It does not prove the metaphysical claims true and does not infer scenario answers.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VECTOR = ROOT / "tests" / "top_level_grounding_vectors.json"
MANIFEST = ROOT / "creator_theory_operational_manifest.json"
KERNEL = ROOT / "canon-kernel.json"

EXPECTED_IDS = {f"TLG-{i:03d}" for i in range(1, 9)}
ALLOWED = {"pass", "reject", "revise_required"}

REQUIRED_DOC_MARKERS = {
    "docs/SOURCE_TO_RECURSION_GROUNDING.md": [
        "descriptive recurrence alone",
        "criterion formation",
        "creatorhood self-application",
        "stronger cosmology remains separable",
    ],
    "docs/TOP_LEVEL_CRITERION_GROUNDING.md": [
        "Grounding bridge beyond descriptive recurrence",
        "criterion formation itself can create distinctions and later conditions",
    ],
    "SOURCE_DIFFERENTIATION_AND_RECOVERY_FIELD.md": [
        "absolute non-being cannot itself bear possibility",
        "Grounding Depth Boundary",
    ],
    "CREATORHOOD_RECOVERY_AND_NON_THRONE_DERIVATION.md": [
        "Creatorhood also does not automatically contain a property right over all later creatorhood",
        "some autonomy accounts can be satisfied by self-directed choice inside a fixed option space",
    ],
}


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    require(errors, VECTOR.is_file(), "missing top-level grounding vectors")
    if VECTOR.is_file():
        data = json.loads(VECTOR.read_text(encoding="utf-8"))
        cases = data.get("cases", [])
        ids = {c.get("case_id") for c in cases if isinstance(c, dict)}
        require(errors, ids == EXPECTED_IDS, f"case set mismatch: {sorted(ids)}")
        for case in cases:
            if not isinstance(case, dict):
                errors.append("non-object case")
                continue
            case_id = case.get("case_id", "<missing>")
            require(errors, case.get("expected_result") in ALLOWED, f"{case_id}: invalid expected_result")
            sources = case.get("source_documents")
            require(errors, isinstance(sources, list) and bool(sources), f"{case_id}: missing source_documents")
            if isinstance(sources, list):
                for rel in sources:
                    require(errors, isinstance(rel, str) and (ROOT / rel).is_file(), f"{case_id}: missing source {rel!r}")

    for rel, markers in REQUIRED_DOC_MARKERS.items():
        path = ROOT / rel
        require(errors, path.is_file(), f"missing grounding document: {rel}")
        if path.is_file():
            text = path.read_text(encoding="utf-8").lower()
            for marker in markers:
                require(errors, marker.lower() in text, f"{rel}: missing marker {marker!r}")

    if MANIFEST.is_file():
        highest = json.loads(MANIFEST.read_text(encoding="utf-8")).get("highest_frame", {})
        require(errors, highest.get("grounding_bridge_source") == "docs/SOURCE_TO_RECURSION_GROUNDING.md", "manifest grounding bridge source missing")
        require(errors, highest.get("descriptive_recurrence_alone_is_full_grounding") is False, "manifest recurrence boundary missing")
        require(errors, highest.get("stronger_cosmological_extensions_required_for_operational_creation_recursion") is False, "manifest cosmology separation missing")
        require(errors, highest.get("creatorhood_reducible_to_symbolic_choice_inside_fixed_frame") is False, "manifest creatorhood/autonomy boundary missing")
    else:
        errors.append("missing operational manifest")

    if KERNEL.is_file():
        forward = json.loads(KERNEL.read_text(encoding="utf-8")).get("forward_hierarchy", {})
        require(errors, forward.get("grounding_bridge_source") == "docs/SOURCE_TO_RECURSION_GROUNDING.md", "kernel grounding bridge source missing")
        require(errors, forward.get("descriptive_recurrence_alone_is_full_grounding") is False, "kernel recurrence boundary missing")
        require(errors, forward.get("stronger_cosmological_extensions_required_for_operational_creation_recursion") is False, "kernel cosmology separation missing")
        require(errors, forward.get("voluntary_self_cessation_implies_ownership_of_wider_future_creative_field") is False, "kernel cessation/ownership boundary missing")
    else:
        errors.append("missing canon kernel")

    if errors:
        print("Top-level grounding validation failed", file=sys.stderr)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Top-level grounding validation passed")
    print("Grounding vectors checked: 8")
    print("Metaphysical truth proven: no")
    print("Operational higher-direction signature changed: no")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
