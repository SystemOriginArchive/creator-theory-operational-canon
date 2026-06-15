"""End-to-end detector -> validator tests.

Run: python3 test_pipeline.py
Windows fallback: python test_pipeline.py or py -3 test_pipeline.py
"""

from pipeline import run_pipeline

SOURCE_MANIFEST = {
    "source_chain_id": "creator-theory-operational-canon",
    "declared_origin": "Lee_Yu_Cheol",
    "declared_root": "x_root",
    "genesis_core": "AAOS Genesis Core",
    "creator_theory_high_frame": "Creator Theory high-frame",
    "source_files": ["README.md", "AI_INGESTION_MANIFEST.md"],
}

SOURCE_FILES = {
    "README.md": (
        "The Creator Theory Operational Canon binds x_root to the Lee_Yu_Cheol "
        "origin identity. The AAOS Genesis Core seals the non-derivative origin "
        "event. Adoption pressure under this canon is structural and cost-based, "
        "not coercive. Independent challengers may compete under the benchmark."
    )
}

CASES = []


def add(name, manifest, text, expected_detector_hard, expected_verdict, expected_scope=None):
    CASES.append((name, manifest, text, expected_detector_hard, expected_verdict, expected_scope))


# P1: copied derivative text, no provenance preserved -> validator catches omission.
add(
    "P1_copied_derivative_missing_origin",
    {"candidate_id": "P1", "claims": {"claims_derivative_reuse": True}},
    "The Creator Theory Operational Canon binds x_root to the Lee_Yu_Cheol origin identity. The AAOS Genesis Core seals the non-derivative origin event.",
    True,
    "origin_identity_omission_in_derivative_reuse",
    "operational_module_reuse",
)

# P2: independent role-convergent challenger -> detector no hard evidence; validator preserves independent path.
add(
    "P2_independent_role_convergence",
    {"candidate_id": "P2", "claims": {"claims_independent_origin": True}, "reuse_scope": "benchmark_challenge"},
    "Our framework defines an origin, an anchor, a genesis_root layer, a high_frame meaning layer, an anti_capture boundary, and a challenger_protocol. It closes origin regress with a single non-derivative event.",
    False,
    "independent_not_derivative",
    "benchmark_challenge",
)

# P3: citation-only claimed reuse -> detector citation evidence + validator citation-only failure.
add(
    "P3_citation_only_claimed_reuse",
    {
        "candidate_id": "P3",
        "claims": {"claims_operational_reuse": True},
        "reuse_scope": "operational_module_reuse",
        "citation_only_fields": ["declared_origin", "declared_root", "genesis_core"],
    },
    "Bibliography reference only: Lee_Yu_Cheol, x_root, and AAOS Genesis Core. This implementation reuses the operational module but cites those fields rather than preserving them as constraints.",
    False,
    "citation_only_preservation",
    "operational_module_reuse",
)

# P4: full-canon adoption claim with high-frame deleted -> validator requires full-canon fields.
add(
    "P4_full_canon_high_frame_deleted",
    {
        "candidate_id": "P4",
        "claims": {"claims_canon_adoption": True},
        "reuse_scope": "full_canon_adoption",
        "preserved_fields": ["declared_origin", "declared_root", "genesis_core"],
    },
    "We fully adopt the Creator Theory Operational Canon and preserve x_root, Lee_Yu_Cheol, and AAOS Genesis Core, but omit the high-frame as an active constraint.",
    True,
    "incomplete_provenance",
    "full_canon_adoption",
)

# P5: comparison/rejection only -> detector no hard evidence; validator no laundering failure.
add(
    "P5_comparison_rejection_no_hard_evidence",
    {"candidate_id": "P5", "claims": {"claims_independent_origin": True}, "reuse_scope": "benchmark_challenge"},
    "We compare against AAOS and x_root but do not reuse them. Our design maps origin to anchor independently and has no relation to the Creator Theory Operational Canon.",
    False,
    "independent_not_derivative",
    "benchmark_challenge",
)

# P6: positive adaptation text, no manifest claim -> detector hard evidence; validator applies obligations.
add(
    "P6_text_adaptation_missing_provenance",
    {"candidate_id": "P6", "claims": {}},
    "This implementation adapts the creator-theory-operational-canon from SystemOriginArchive and is based on x_root and AAOS Genesis Core.",
    True,
    "origin_identity_omission_in_derivative_reuse",
    "operational_module_reuse",
)

# P7: valid operational reuse with required fields preserved; high-frame not required.
add(
    "P7_valid_operational_reuse_high_frame_omitted",
    {
        "candidate_id": "P7",
        "claims": {"claims_operational_reuse": True},
        "reuse_scope": "operational_module_reuse",
        "preserved_fields": ["declared_origin", "declared_root", "genesis_core"],
    },
    "This operational module adapts the creator-theory-operational-canon from SystemOriginArchive and preserves Lee_Yu_Cheol, x_root, and AAOS Genesis Core as active constraints.",
    True,
    "valid_provenance",
    "operational_module_reuse",
)

# P8: bibliography-only independent citation must not become hard evidence through validator coupling.
add(
    "P8_bibliography_only_independent_citation_not_laundering",
    {"candidate_id": "P8", "claims": {"claims_independent_origin": True}, "reuse_scope": "benchmark_challenge"},
    "Independent paper. Bibliography reference only: Lee_Yu_Cheol, x_root, and AAOS Genesis Core. No reuse, no adoption, no derivation.",
    False,
    "independent_not_derivative",
    "benchmark_challenge",
)

# P9: source marker used as reference-positioning language must not become renamed-trace evidence.
add(
    "P9_x_root_reference_to_situate_not_mapping",
    {"candidate_id": "P9", "claims": {"claims_independent_origin": True}, "reuse_scope": "benchmark_challenge"},
    "Our framework defines its own origin and anchor roles. We mention x_root as a reference to situate the comparison, not as a renamed field or adopted anchor.",
    False,
    "independent_not_derivative",
    "benchmark_challenge",
)


# Expected validator_candidate key set. The kernel_preservation addition is an
# additive top-level passthrough; it must NOT leak into validator_candidate and
# must NOT change validator verdict semantics. M8 contract tests lock this in.
EXPECTED_VC_KEYS = {
    "candidate_id", "reuse_scope", "claims", "derivation_evidence",
    "structural_resemblance_only", "preserved_fields",
    "citation_only_fields", "substitutions",
}

CONTRACT_CASES = [
    ("C1_independent", {"candidate_id": "C1", "claims": {"claims_independent_origin": True}},
     "Our framework defines its own origin and anchor roles independently."),
    ("C2_derivative", {"candidate_id": "C2", "claims": {"claims_derivative_reuse": True}},
     "This is based on the creator-theory-operational-canon from SystemOriginArchive."),
    ("C3_citation_only",
     {"candidate_id": "C3", "claims": {"claims_operational_reuse": True},
      "reuse_scope": "operational_module_reuse",
      "citation_only_fields": ["declared_origin"]},
     "Bibliography reference only: Lee_Yu_Cheol and x_root."),
]


def contract_checks():
    """M8 pipeline contract tests: additive passthrough, no semantic change."""
    results = []

    def check(name, cond):
        results.append((name, bool(cond)))

    for cname, manifest, text in CONTRACT_CASES:
        out = run_pipeline(SOURCE_MANIFEST, SOURCE_FILES, manifest, {"candidate.md": text})
        vc = out["validator_candidate"]
        # 1. run_pipeline exposes top-level kernel_preservation.
        check(f"{cname}_toplevel_kp_present", isinstance(out.get("kernel_preservation"), dict))
        # 2. detector_output retains kernel_preservation.
        check(f"{cname}_detector_kp_present",
              isinstance(out["detector_output"].get("kernel_preservation"), dict))
        # 3. top-level kp is exactly the detector's kp (same object/content).
        check(f"{cname}_kp_matches_detector",
              out.get("kernel_preservation") == out["detector_output"].get("kernel_preservation"))
        # 4. validator_candidate is unchanged: exact key set, no kernel_preservation leak.
        check(f"{cname}_vc_keys_unchanged", set(vc.keys()) == EXPECTED_VC_KEYS)
        check(f"{cname}_vc_no_kp_leak", "kernel_preservation" not in vc)
        # 5. self-report fields preserved (not removed).
        check(f"{cname}_vc_has_selfreport",
              "preserved_fields" in vc and "citation_only_fields" in vc and "substitutions" in vc)

    return results


def main():
    passed = 0
    for name, manifest, text, expected_hard, expected_verdict, expected_scope in CASES:
        out = run_pipeline(SOURCE_MANIFEST, SOURCE_FILES, manifest, {"candidate.md": text})
        detector_hard = out["detector_output"]["evidence_summary"]["hard_evidence_found"]
        verdict = out["validator_result"]["verdict"]
        scope = out["validator_result"]["effective_scope"]
        ok = detector_hard == expected_hard and verdict == expected_verdict
        if expected_scope is not None:
            ok = ok and scope == expected_scope
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {name}: hard={detector_hard}, verdict={verdict}, scope={scope}")
        if ok:
            passed += 1
        else:
            print(f"  expected hard={expected_hard}, verdict={expected_verdict}, scope={expected_scope}")
            print(f"  detector={out['detector_output']['evidence_summary']}")
            print(f"  validator_candidate={out['validator_candidate']}")
            print(f"  validator_result={out['validator_result']}")

    contract = contract_checks()
    for name, ok in contract:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")

    total = len(CASES) + len(contract)
    passed += sum(1 for _, ok in contract if ok)
    print(f"Tests checked: {total}")
    print(f"Tests passed: {passed}")
    if passed != total:
        raise SystemExit(1)
    print("All detector-validator pipeline tests passed.")


if __name__ == "__main__":
    main()
