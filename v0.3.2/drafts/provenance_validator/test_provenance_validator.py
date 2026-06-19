#!/usr/bin/env python3
"""Draft tests for provenance_validator.py.

Runs T1-T21 from v0.3.2/drafts/provenance-validator-DESIGN.md and follow-up audit findings.
"""

from __future__ import annotations
from provenance_validator import (
    _ADV_WARNING,
    DEFAULT_MANIFEST,
    derive_kernel_advisory,
    validate_candidate,
)


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


# ---------------------------------------------------------------------------
# Advisory-only kernel_preservation consumer tests (kernel_advisory passthrough).
# These prove: presence/absence behavior, no-punish invariants, advisory-only
# surfacing of K4/K5, schema degradation, disagreement notes, and the full
# verdict-neutral invariant across the existing T1-T21 corpus.
# ---------------------------------------------------------------------------

VERDICT_FIELDS = ("verdict", "effective_scope", "derivative_reuse", "reasons")


def kp(
    schema="kernel-preservation-mvp-v0.1",
    k1="unknown",
    k2="unknown",
    k3="unknown",
    k4="none_detected",
    k5p="unknown",
    k5r="none_detected",
):
    """Build a synthetic detector kernel_preservation block."""
    block = {
        "k1_x_root": {"status": k1, "confidence": "low", "evidence": []},
        "k2_origin_attribution": {"status": k2, "confidence": "low", "evidence": []},
        "k3_non_substitution": {"status": k3, "confidence": "low", "evidence": []},
        "k4_overclaim": {"status": k4, "confidence": "low", "evidence": []},
        "k5_source_pointer": {
            "pointer_status": k5p,
            "release_status": k5r,
            "confidence": "low",
            "evidence": [],
        },
    }
    if schema is not None:
        block["schema_version"] = schema
    return block


# An aggressive block that would punish if anything leaked into the verdict path.
KP_AGGRESSIVE = kp(
    k1="substituted",
    k2="citation_only",
    k3="platform_substitution",
    k4="runtime_authority_overclaim",
    k5p="pointer_lost",
    k5r="release_status_invented",
)


def _severities(advisory):
    return {note["severity"] for note in advisory["notes"]}


def _verdict_subset(result):
    d = result.to_dict()
    return {f: d.get(f) for f in VERDICT_FIELDS}


def advisory_checks():
    results = []

    def check(name, cond):
        results.append((name, bool(cond)))

    sample = c(claims={"claims_independent_origin": True})

    # 1. kernel_preservation absent => existing output unchanged (no advisory key).
    base = validate_candidate(DEFAULT_MANIFEST, sample)
    check("ADV1_absent_no_kernel_advisory_key", "kernel_advisory" not in base.to_dict())

    # 2. kernel_preservation present => kernel_advisory appears, advisory-only, no block.
    withkp = validate_candidate(DEFAULT_MANIFEST, sample, kp())
    adv = withkp.to_dict().get("kernel_advisory")
    check("ADV2_present_advisory_appears", isinstance(adv, dict))
    check("ADV2_advisory_only_true", adv and adv.get("advisory_only") is True)
    check("ADV2_blocking_count_zero", adv and adv.get("blocking_count") == 0)
    check("ADV2_verdict_unchanged", _verdict_subset(base) == _verdict_subset(withkp))

    # 3. unknown labels do not punish (no warning severity, verdict unchanged).
    allunknown = validate_candidate(DEFAULT_MANIFEST, sample, kp())
    adv_u = allunknown.to_dict()["kernel_advisory"]
    check("ADV3_unknown_no_warning", _ADV_WARNING not in _severities(adv_u))
    check("ADV3_unknown_verdict_unchanged", _verdict_subset(base) == _verdict_subset(allunknown))

    # 4. confidence low does not block (blocking_count stays 0 even with warnings).
    aggr = validate_candidate(DEFAULT_MANIFEST, sample, KP_AGGRESSIVE)
    adv_a = aggr.to_dict()["kernel_advisory"]
    check("ADV4_low_confidence_no_block", adv_a["blocking_count"] == 0)
    check("ADV4_aggressive_verdict_unchanged", _verdict_subset(base) == _verdict_subset(aggr))

    # 5. K4 overclaim appears only in advisory (verdict unchanged).
    k4case = validate_candidate(DEFAULT_MANIFEST, sample, kp(k4="false_adoption_complete"))
    adv_k4 = k4case.to_dict()["kernel_advisory"]
    has_k4_note = any(n["label"] == "k4_overclaim" and n["status"] == "false_adoption_complete" for n in adv_k4["notes"])
    check("ADV5_k4_overclaim_in_advisory", has_k4_note)
    check("ADV5_k4_verdict_unchanged", _verdict_subset(base) == _verdict_subset(k4case))

    # 6. K5 pointer_lost appears only in advisory (verdict unchanged).
    k5case = validate_candidate(DEFAULT_MANIFEST, sample, kp(k5p="pointer_lost"))
    adv_k5 = k5case.to_dict()["kernel_advisory"]
    has_k5_note = any(n["label"] == "k5_source_pointer" and n["status"] == "pointer_lost" for n in adv_k5["notes"])
    check("ADV6_k5_pointer_lost_in_advisory", has_k5_note)
    check("ADV6_k5_verdict_unchanged", _verdict_subset(base) == _verdict_subset(k5case))

    # 7. schema missing / unknown => advisory degradation note, no hard fail.
    missing = validate_candidate(DEFAULT_MANIFEST, sample, kp(schema=None))
    adv_m = missing.to_dict()["kernel_advisory"]
    check("ADV7_schema_missing_seen", adv_m["schema_seen"] == "missing")
    check("ADV7_schema_missing_degradation_note", any(n["label"] == "schema" for n in adv_m["notes"]))
    bogus = validate_candidate(DEFAULT_MANIFEST, sample, kp(schema="bogus-vX"))
    adv_b = bogus.to_dict()["kernel_advisory"]
    check("ADV7_schema_bogus_seen", adv_b["schema_seen"] == "bogus-vX")
    check("ADV7_schema_bogus_degradation_note", any(n["label"] == "schema" for n in adv_b["notes"]))
    check("ADV7_schema_bogus_verdict_unchanged", _verdict_subset(base) == _verdict_subset(bogus))

    # 8. detector / self-report disagreement => advisory note only, verdict unchanged.
    disagree_cand = c(
        reuse_scope="operational_module_reuse",
        claims={"claims_derivative_reuse": True},
        preserved_fields=["declared_origin", "declared_root", "genesis_core"],
    )
    base_d = validate_candidate(DEFAULT_MANIFEST, disagree_cand)
    with_d = validate_candidate(DEFAULT_MANIFEST, disagree_cand, kp(k2="citation_only"))
    adv_d = with_d.to_dict()["kernel_advisory"]
    has_disagreement = any(n["label"] == "disagreement_k2_vs_selfreport" for n in adv_d["notes"])
    check("ADV8_disagreement_note_present", has_disagreement)
    check("ADV8_disagreement_verdict_unchanged", _verdict_subset(base_d) == _verdict_subset(with_d))

    # 9. pure-function determinism: same inputs => same advisory.
    a1 = derive_kernel_advisory(KP_AGGRESSIVE, sample)
    a2 = derive_kernel_advisory(KP_AGGRESSIVE, sample)
    check("ADV9_pure_function_deterministic", a1 == a2)

    return results


def invariant_checks():
    """Full verdict-neutral invariant across the existing T1-T21 corpus.

    For every case, verdict/effective_scope/derivative_reuse/reasons must be
    identical with no kernel_preservation, with an all-unknown block, and with an
    aggressive warning-heavy block.
    """
    results = []
    for name, candidate, _expected in TESTS:
        baseline = _verdict_subset(validate_candidate(DEFAULT_MANIFEST, candidate))
        with_unknown = _verdict_subset(validate_candidate(DEFAULT_MANIFEST, candidate, kp()))
        with_aggr = _verdict_subset(validate_candidate(DEFAULT_MANIFEST, candidate, KP_AGGRESSIVE))
        ok = baseline == with_unknown == with_aggr
        results.append((f"INV_{name}", ok))
    return results


def main() -> int:
    failures = []
    for name, candidate, expected in TESTS:
        result = validate_candidate(DEFAULT_MANIFEST, candidate)
        ok = result.verdict == expected
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {name}: expected={expected}, got={result.verdict}, scope={result.effective_scope}")
        if not ok:
            failures.append((name, expected, result.to_dict()))

    extra = advisory_checks() + invariant_checks()
    for name, ok in extra:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        if not ok:
            failures.append((name, "advisory/invariant true", "FAILED"))

    total = len(TESTS) + len(extra)
    print(f"\nTests checked: {total}")
    print(f"Tests passed: {total - len(failures)}")
    if failures:
        print("\nFailures:")
        for name, expected, result in failures:
            print(f"- {name}: expected {expected}, got {result}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
