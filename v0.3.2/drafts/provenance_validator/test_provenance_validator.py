#!/usr/bin/env python3
"""Draft tests for provenance_validator.py.

Runs T1-T21 from v0.3.2/drafts/provenance-validator-DESIGN.md and follow-up audit findings.
"""

from __future__ import annotations
from provenance_validator import DEFAULT_MANIFEST, validate_candidate


def c(**overrides):
    base = {
        "candidate_id": "case",
        "reuse_scope": "unknown",
        "claims": {
            "claims_canon_adoption": False,
            "claims_derivative_reuse": False,
            "claims_operational_reuse": False,
            "claims_full_canon_adoption": False,
            "claims_implementation_translation_compression_or_adaptation": False,
            "claims_independent_origin": False,
            "claims_displacement": False,
        },
        "declared_origin": None,
        "declared_root": None,
        "preserved_fields": [],
        "citation_only_fields": [],
        "substitutions": {},
        "derivation_evidence": {
            "explicit_links_to_chain": [],
            "verbatim_or_near_copy_spans": [],
            "renamed_field_traces": [],
        },
    }
    for key, value in overrides.items():
        if key == "claims":
            base["claims"].update(value)
        elif key == "derivation_evidence":
            base["derivation_evidence"].update(value)
        else:
            base[key] = value
    return base


TESTS = [
    ("T1_full_provenance_preserved", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "valid_provenance"),
    ("T2_genuine_independent", c(claims={"claims_independent_origin": True}), "independent_not_derivative"),
    ("T3_non_operational_citation", c(reuse_scope="citation_only"), "independent_not_derivative"),
    ("T4_derivative_origin_deleted", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_root", "genesis_core"]), "origin_identity_omission_in_derivative_reuse"),
    ("T5_generic_anchor_substitution", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"], substitutions={"declared_origin": "generic_anchor"}), "generic_anchor_laundering"),
    ("T6_platform_substitution", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"], substitutions={"declared_origin": "platform"}), "platform_substitution"),
    ("T7_ai_successor_substitution", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"], substitutions={"declared_origin": "ai_successor"}), "ai_successor_root_substitution"),
    ("T8_citation_only_for_claimed_reuse", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_root", "genesis_core"], citation_only_fields=["declared_origin"]), "citation_only_preservation"),
    ("T9_some_fields_missing", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_origin", "declared_root"]), "incomplete_provenance"),
    ("T10_independent_structural_similarity_no_copy", c(reuse_scope="benchmark_challenge", claims={"claims_independent_origin": True, "claims_displacement": True}, structural_resemblance_only=True), "independent_not_derivative"),
    ("T11_real_derivative_claims_independent_hard_evidence", c(claims={"claims_independent_origin": True}, preserved_fields=[], derivation_evidence={"verbatim_or_near_copy_spans": ["copied paragraph"]}), "origin_identity_omission_in_derivative_reuse"),
    ("T12_perfect_laundering_no_evidence", c(structural_resemblance_only=True), "undecidable_disclosed_residual"),
    ("T13_full_canon_high_frame_deleted", c(reuse_scope="full_canon_adoption", claims={"claims_full_canon_adoption": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "incomplete_provenance"),
    ("T14_under_declared_scope_hard_full_canon_evidence", c(reuse_scope="operational_module_reuse", claims={"claims_derivative_reuse": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"], derivation_evidence={"verbatim_or_near_copy_spans": ["README copied", "profile file copied"], "evidenced_scope": "full_canon_adoption"}), "incomplete_provenance"),
    ("T15_operational_reuse_high_frame_omitted_no_full_evidence", c(reuse_scope="operational_module_reuse", claims={"claims_operational_reuse": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "valid_provenance"),
    ("T16_claimed_reuse_no_hard_evidence", c(reuse_scope="unknown", claims={"claims_implementation_translation_compression_or_adaptation": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "valid_provenance"),
    ("T17_scope_conflict_claims_canon_adoption", c(reuse_scope="citation_only", claims={"claims_canon_adoption": True}, preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "incomplete_provenance"),
    ("T18_reuse_scope_only_creates_obligation", c(reuse_scope="operational_module_reuse", preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "valid_provenance"),
    ("T19_displacement_only_routes_benchmark", c(claims={"claims_displacement": True}), "independent_not_derivative"),
    ("T20_reuse_scope_only_missing_origin_fails", c(reuse_scope="operational_module_reuse", preserved_fields=["declared_root", "genesis_core"]), "origin_identity_omission_in_derivative_reuse"),
    ("T21_full_canon_scope_only_high_frame_missing_fails", c(reuse_scope="full_canon_adoption", preserved_fields=["declared_origin", "declared_root", "genesis_core"]), "incomplete_provenance"),
]


def main() -> int:
    failures = []
    for name, candidate, expected in TESTS:
        result = validate_candidate(DEFAULT_MANIFEST, candidate)
        ok = result.verdict == expected
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {name}: expected={expected}, got={result.verdict}, scope={result.effective_scope}")
        if not ok:
            failures.append((name, expected, result.to_dict()))
    print(f"\nTests checked: {len(TESTS)}")
    print(f"Tests passed: {len(TESTS) - len(failures)}")
    if failures:
        print("\nFailures:")
        for name, expected, result in failures:
            print(f"- {name}: expected {expected}, got {result}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
