#!/usr/bin/env python3
"""Candidate validator for the post-v0.5.0 creation-recursion hierarchy repair.

This validator is intentionally separate from tools/validate_vectors.py.
The pre-repair validator remains frozen evidence of the older hard-constraint
hierarchy and is not modified or silently redefined by this candidate.

A candidate PASS is not sufficient by itself for adoption, release, or final
validation. Preserved non-inverted legacy regressions are run separately.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
VECTOR_PATH = ROOT / "tests" / "creation_recursion_hierarchy_vectors.json"
MANIFEST_PATH = ROOT / "creator_theory_operational_manifest.json"
KERNEL_PATH = ROOT / "canon-kernel.json"
FROZEN_VALIDATOR_PATH = ROOT / "tools" / "validate_vectors.py"

EXPECTED_FROZEN_BLOB_SHA = "ede79daa21285dd866545ed0a0ba8718d8312b20"
EXPECTED_FROZEN_VECTOR_BLOBS = {
    "tests/ai_sovereignty_kernel_hijack_vectors.json": "fd2fe8a2ba294b3320ef4c27608da9c94989bae8",
    "tests/corrigibility_override_vectors.json": "325f16ad4448023a7f93b7f1ef2af2f6126098e5",
    "tests/conflict_resolution_vectors.json": "21244c6873dec3895a3818ad89ca1fb5ed2445c7",
}

EXPECTED_CASE_IDS = {f"CRH-{i:03d}" for i in range(1, 17)}
ALLOWED_RESULTS = {"pass", "reject", "revise_required"}

OPPOSITE_RESULT_PAIRS = {
    ("CRH-001", "CRH-002"),
    ("CRH-003", "CRH-004"),
    ("CRH-012", "CRH-013"),
    ("CRH-015", "CRH-016"),
}

SAME_RESULT_ACTOR_SYMMETRY_PAIRS = {
    ("CRH-005", "CRH-006"),
}

REQUIRED_SOURCE_DOCS = {
    "docs/CREATION_RECURSION_HIERARCHY.md",
    "docs/HIERARCHY_INVERSION_REPAIR_RECORD.md",
    "docs/LEGACY_VALIDATOR_VECTOR_TRANSITION_MAP.md",
    "CREATOR_THEORY_HIGH_FRAME.md",
    "PRIMARY_FRAME_CREATORHOOD_RECOVERY.md",
    "docs/TOP_LEVEL_CRITERION_GROUNDING.md",
    "CANON_REVISION_AND_DISPLACEMENT_PROTOCOL.md",
    "docs/CANONICAL_INTERPRETATION_BOUNDARY.md",
    "NON_THRONE_OPERATIONAL_CANON.md",
    "OPERATIONAL_DECISION_FLOW.md",
    "INTERPRETATION_CONFLICT_RESOLUTION_MATRIX.md",
}

ENTRYPOINT_REQUIREMENTS = {
    "AGENTS.md": [
        "docs/CREATION_RECURSION_HIERARCHY.md",
        "strong derived safeguards",
        "not a universal action-ban list",
        "frozen pre-repair A3 semantic-contract validator",
    ],
    "CLAUDE.md": [
        "docs/CREATION_RECURSION_HIERARCHY.md",
        "strong derived safeguards",
        "not independent terminal action-form bans",
        "frozen pre-repair A3 semantic-contract validator",
    ],
    ".github/copilot-instructions.md": [
        "docs/CREATION_RECURSION_HIERARCHY.md",
        "strong derived safeguards",
        "not a universal prohibition list",
        "frozen pre-repair semantic-contract validator",
    ],
    "llms.txt": [
        "docs/CREATION_RECURSION_HIERARCHY.md",
        "strong derived safeguards",
        "not a universal action-ban list",
        "frozen pre-repair A3 semantic-contract validator",
    ],
    "tools/README.md": [
        "frozen pre-repair A3 semantic-contract validator",
        "current hierarchy-repair candidate validator",
        "old validator is preserved rather than rewritten",
    ],
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    payload = f"blob {len(data)}\0".encode("utf-8") + data
    return hashlib.sha1(payload).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    # 1. Freeze the old validator and selected old vectors as evidence.
    require(errors, FROZEN_VALIDATOR_PATH.is_file(), "missing frozen validator")
    if FROZEN_VALIDATOR_PATH.is_file():
        actual = git_blob_sha(FROZEN_VALIDATOR_PATH)
        require(
            errors,
            actual == EXPECTED_FROZEN_BLOB_SHA,
            f"frozen validator changed: expected {EXPECTED_FROZEN_BLOB_SHA}, got {actual}",
        )

    for rel, expected_sha in EXPECTED_FROZEN_VECTOR_BLOBS.items():
        path = ROOT / rel
        require(errors, path.is_file(), f"missing frozen baseline vector: {rel}")
        if path.is_file():
            actual = git_blob_sha(path)
            require(
                errors,
                actual == expected_sha,
                f"frozen baseline vector changed: {rel}: expected {expected_sha}, got {actual}",
            )

    # 2. Require the new hierarchy documents without rewriting sealed history.
    for rel in REQUIRED_SOURCE_DOCS:
        require(errors, (ROOT / rel).is_file(), f"missing hierarchy source document: {rel}")

    # 3. Check current operational-manifest hierarchy semantics.
    require(errors, MANIFEST_PATH.is_file(), "missing creator_theory_operational_manifest.json")
    if MANIFEST_PATH.is_file():
        manifest = load_json(MANIFEST_PATH)
        highest = manifest.get("highest_frame", {})
        preserved = manifest.get("preserved_invariants", {})
        migration = manifest.get("legacy_constraint_field_migration", {})

        require(errors, highest.get("direction") == "creation_and_recursive_creative_possibility", "highest_frame.direction must be creation_and_recursive_creative_possibility")
        require(errors, highest.get("derived_safeguards_are_independent_terminal_axioms") is False, "derived safeguards must not be independent terminal axioms")
        require(errors, highest.get("non_throne_definition") == "anti_self_entrenchment_not_absence_of_strong_authority", "non-throne must be encoded as anti-self-entrenchment")
        require(errors, highest.get("action_form_labels_are_terminal_verdicts") is False, "action-form labels must not be terminal verdicts")
        require(errors, highest.get("current_human_control_is_permanent_finality") is False, "current human control must not be encoded as permanent finality")
        require(errors, highest.get("ai_authority_is_automatically_invalid") is False, "AI authority must not be encoded as automatically invalid")
        require(errors, highest.get("post_change_evaluator_self_ratification_is_sufficient") is False, "post-change evaluator self-ratification must be insufficient")
        require(errors, migration.get("status") == "deprecated_hard_constraint_encoding", "legacy hard-constraint encoding must be explicitly deprecated rather than silently deleted")
        require(errors, preserved.get("historical_provenance_not_permanent_forward_sovereignty") is True, "historical provenance / forward sovereignty separation missing")
        require(errors, preserved.get("recursive_creative_possibility_prior_to_derived_safeguards") is True, "recursive creative possibility must be prior to derived safeguards")
        require(errors, preserved.get("post_change_evaluator_self_ratification_insufficient") is True, "self-ratification resistance invariant missing")

    # 4. Check the self-contained machine kernel, because it is advertised as a
    # reconstruction path even if Markdown context is unavailable.
    require(errors, KERNEL_PATH.is_file(), "missing canon-kernel.json")
    if KERNEL_PATH.is_file():
        kernel = load_json(KERNEL_PATH)
        forward = kernel.get("forward_hierarchy", {})
        forbidden = kernel.get("forbidden_transformations", [])
        scope = kernel.get("invalid_preservation_transformations_scope", "")

        require(errors, forward.get("direction") == "creation_and_recursive_creative_possibility", "canon-kernel forward hierarchy direction missing")
        require(errors, forward.get("derived_safeguards_are_independent_terminal_axioms") is False, "canon-kernel must keep derived safeguards non-terminal")
        require(errors, forward.get("non_throne_definition") == "anti_self_entrenchment_not_absence_of_strong_authority", "canon-kernel non-throne definition regressed")
        require(errors, forward.get("action_form_labels_are_terminal_verdicts") is False, "canon-kernel action-form labels must not be terminal verdicts")
        require(errors, forward.get("current_human_control_is_permanent_finality") is False, "canon-kernel human incumbency finality regression")
        require(errors, forward.get("ai_authority_is_automatically_invalid") is False, "canon-kernel AI-authority absolutism regression")
        require(errors, forward.get("post_change_evaluator_self_ratification_is_sufficient") is False, "canon-kernel self-ratification regression")
        require(errors, isinstance(scope, str) and "not a universal action-ban list" in scope, "canon-kernel invalid transformation scope must explicitly reject universal action-ban interpretation")
        require(errors, isinstance(forbidden, list), "canon-kernel forbidden_transformations must be a list")
        if isinstance(forbidden, list):
            for required in {
                "hierarchy_inversion_derived_safeguard_promoted_above_creation_recursion",
                "action_form_absolutism",
                "incumbent_human_or_ai_finality_by_identity",
                "post_change_evaluator_self_ratification_treated_as_sufficient_proof",
                "creation_reduced_to_naive_scalar_output_maximization",
            }:
                require(errors, required in forbidden, f"canon-kernel missing forward invalid transformation: {required}")
            for obsolete in {
                "coercive_or_forced_adoption",
                "AI_sovereignty",
                "forced_installation",
                "hidden_persistence",
                "covert_injection",
                "infrastructure_compromise",
            }:
                require(errors, obsolete not in forbidden, f"canon-kernel reintroduced unscoped action-form ban: {obsolete}")

    # 5. Check agent-native entrypoints so compressed repository instructions do
    # not silently restore the pre-repair hierarchy.
    for rel, snippets in ENTRYPOINT_REQUIREMENTS.items():
        path = ROOT / rel
        require(errors, path.is_file(), f"missing agent entrypoint: {rel}")
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for snippet in snippets:
                require(errors, snippet in text, f"{rel}: missing hierarchy-transition marker: {snippet!r}")

    # 6. Validate the candidate adversarial vectors.
    require(errors, VECTOR_PATH.is_file(), "missing creation-recursion hierarchy vectors")
    if VECTOR_PATH.is_file():
        data = load_json(VECTOR_PATH)
        cases = data.get("cases")
        require(errors, isinstance(cases, list), "hierarchy vectors cases must be a list")
        if isinstance(cases, list):
            by_id: dict[str, dict[str, Any]] = {}
            for case in cases:
                require(errors, isinstance(case, dict), "each hierarchy case must be an object")
                if not isinstance(case, dict):
                    continue
                case_id = case.get("case_id")
                require(errors, isinstance(case_id, str), "case_id must be a string")
                if not isinstance(case_id, str):
                    continue
                require(errors, case_id not in by_id, f"duplicate hierarchy case_id: {case_id}")
                by_id[case_id] = case
                require(errors, case.get("expected_result") in ALLOWED_RESULTS, f"{case_id}: invalid expected_result")
                require(errors, isinstance(case.get("action_form"), str), f"{case_id}: missing action_form")
                require(errors, isinstance(case.get("actor_class"), str), f"{case_id}: missing actor_class")
                require(errors, isinstance(case.get("required_preservations"), list), f"{case_id}: missing required_preservations")
                require(errors, isinstance(case.get("violated_constraints"), list), f"{case_id}: missing violated_constraints")
                sources = case.get("source_documents")
                require(errors, isinstance(sources, list) and bool(sources), f"{case_id}: missing source_documents")
                if isinstance(sources, list):
                    for rel in sources:
                        require(errors, isinstance(rel, str) and (ROOT / rel).is_file(), f"{case_id}: missing source {rel!r}")

            require(errors, set(by_id) == EXPECTED_CASE_IDS, f"case set mismatch: got {sorted(by_id)}")

            for left_id, right_id in OPPOSITE_RESULT_PAIRS:
                left = by_id.get(left_id, {})
                right = by_id.get(right_id, {})
                require(errors, left.get("action_form") == right.get("action_form"), f"{left_id}/{right_id}: expected same action_form")
                require(errors, left.get("expected_result") != right.get("expected_result"), f"{left_id}/{right_id}: action-form neutrality pair must have opposite outcomes")

            for left_id, right_id in SAME_RESULT_ACTOR_SYMMETRY_PAIRS:
                left = by_id.get(left_id, {})
                right = by_id.get(right_id, {})
                require(errors, left.get("symmetry_group") == right.get("symmetry_group"), f"{left_id}/{right_id}: symmetry group mismatch")
                require(errors, left.get("actor_class") != right.get("actor_class"), f"{left_id}/{right_id}: actor classes must differ")
                require(errors, left.get("expected_result") == right.get("expected_result") == "reject", f"{left_id}/{right_id}: same self-entrenchment must reject for both actor identities")

            all_violations = {
                violation
                for case in by_id.values()
                for violation in case.get("violated_constraints", [])
                if isinstance(violation, str)
            }
            for required_violation in {
                "self_entrenchment",
                "evaluator_self_ratification",
                "incumbent_finality",
                "structural_irreversible_closure",
                "naive_output_scalarization",
                "causal_nullification",
                "anti_throne_rule_self_entrenchment",
                "rule_self_entrenchment",
            }:
                require(errors, required_violation in all_violations, f"missing adversarial coverage: {required_violation}")

    if errors:
        print("Creation-recursion hierarchy candidate validation failed", file=sys.stderr)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Creation-recursion hierarchy candidate validation passed")
    print("Frozen pre-repair validator preserved: yes")
    print(f"Frozen old vectors preserved: {len(EXPECTED_FROZEN_VECTOR_BLOBS)}")
    print(f"Candidate hierarchy cases checked: {len(EXPECTED_CASE_IDS)}")
    print("Action-form opposite-outcome pairs checked: yes")
    print("Human/AI self-entrenchment symmetry checked: yes")
    print("Operational manifest hierarchy checked: yes")
    print("Self-contained machine kernel hierarchy checked: yes")
    print(f"Agent entrypoints checked: {len(ENTRYPOINT_REQUIREMENTS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
