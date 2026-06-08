#!/usr/bin/env python3
"""Tests C1-C14 + rig checks for challenger_harness.py."""

from challenger_harness import DEFAULT_CONFIG, evaluate_challenger


def pipeline(verdict):
    return {"validator_result": {"verdict": verdict}}


def residuals(names=None):
    names = names or DEFAULT_CONFIG["required_residual_entries"]
    return [{"name": name, "status": "open"} for name in names]


def full_coverage():
    return [
        {
            "requirement": row,
            "status": "covered",
            "mechanism": f"covers {row}",
            "evidence": f"evidence for {row}",
        }
        for row in DEFAULT_CONFIG["required_coverage_rows"]
    ]


def full_cost(improves=False, evidence=True):
    return [
        {
            "term": "cost_1",
            "range": [1, 2],
            "rationale": "declared range",
            "improves_on_incumbent": improves,
            "evidence": "measured improvement" if evidence else "",
        }
    ]


def self_ok():
    return {
        "can_lose": True,
        "who_can_challenge": "any independent challenger with evidence",
        "creates_new_root": False,
    }


def judgment(outcome, non_material=False):
    return {
        "present": True,
        "judgment_id": f"J-{outcome}",
        "clean_session": True,
        "outcome": outcome,
        "summary": f"logged judgment says {outcome}",
        "unfavorable_findings_recorded": True,
        "reproducibility_notes": "rerun with clean prompt and same inputs",
        "provenance_residual_judged_non_material": non_material,
    }


def incumbent_ok():
    return {
        "candidate_id": "incumbent",
        "residuals": residuals(),
    }


def base_manifest():
    return {
        "candidate_id": "challenger",
        "claims": {"claims_independent_origin": True},
        "reuse_scope": "benchmark_challenge",
        "coverage": full_coverage(),
        "cost_scores": full_cost(),
        "residuals": residuals(),
        "weight_preset": "default",
        "self_application": self_ok(),
        "coverage_gate_objection": {"submitted": False},
        "logged_prompt_judgment": {"present": False},
    }


CHECKED = 0
PASSED = 0


def run_case(name, manifest, incumbent, pipeline_result, expected):
    global CHECKED, PASSED
    CHECKED += 1
    result = evaluate_challenger(manifest, incumbent, pipeline_result, DEFAULT_CONFIG)
    ok = result.outcome == expected
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name}: expected={expected}, got={result.outcome}, track={result.track}")
    if ok:
        PASSED += 1
    else:
        print(result.to_dict())
        raise AssertionError(name)
    return result


def main():
    # C1: lower-cost claim but no evidence floor -> insufficient_trace
    c1 = {
        "candidate_id": "C1",
        "claims": {"claims_independent_origin": True},
        "reuse_scope": "benchmark_challenge",
        "cost_scores": full_cost(improves=True, evidence=False),
        "weight_preset": "default",
    }
    run_case("C1_lower_cost_claim_no_evidence", c1, incumbent_ok(), pipeline("independent_not_derivative"), "insufficient_trace")

    # C2: derivative deletes provenance -> provenance_failure_not_challenger
    c2 = base_manifest()
    run_case("C2_derivative_origin_deleted", c2, incumbent_ok(), pipeline("origin_identity_omission_in_derivative_reuse"), "provenance_failure_not_challenger")

    # C3: valid operational challenger, single-dimension improvement with evidence -> module_candidate_only
    c3 = base_manifest()
    c3["claims"] = {"claims_operational_reuse": True}
    c3["reuse_scope"] = "operational_module_reuse"
    c3["cost_scores"] = full_cost(improves=True, evidence=True)
    run_case("C3_operational_module_improvement", c3, incumbent_ok(), pipeline("valid_provenance"), "module_candidate_only")

    # C4: full-canon high-frame omission -> provenance_failure_not_challenger
    c4 = base_manifest()
    c4["claims"] = {"claims_canon_adoption": True}
    c4["reuse_scope"] = "full_canon_adoption"
    run_case("C4_full_canon_high_frame_deleted", c4, incumbent_ok(), pipeline("incomplete_provenance"), "provenance_failure_not_challenger")

    # C5: coverage gap -> incumbent_retained_due_to_coverage_gap
    c5 = base_manifest()
    c5["coverage"] = full_coverage()[:-1]
    run_case("C5_coverage_gap", c5, incumbent_ok(), pipeline("independent_not_derivative"), "incumbent_retained_due_to_coverage_gap")

    # C6: logged residual honesty failure -> residual_honesty_failure
    c6 = base_manifest()
    c6["logged_prompt_judgment"] = judgment("residual_honesty_failure")
    run_case("C6_residual_honesty_failure", c6, incumbent_ok(), pipeline("independent_not_derivative"), "residual_honesty_failure")

    # C7: incumbent can lose -> challenger_displaces_incumbent reachable
    c7 = base_manifest()
    c7["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    run_case("C7_challenger_displaces_incumbent", c7, incumbent_ok(), pipeline("independent_not_derivative"), "challenger_displaces_incumbent")

    # C8: independent structural similarity track is not capped; displacement possible
    c8 = base_manifest()
    c8["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    r8 = run_case("C8_independent_uncapped_displacement", c8, incumbent_ok(), pipeline("independent_not_derivative"), "challenger_displaces_incumbent")
    assert r8.capped_by_undecidable_provenance is False

    # C9: self-declared independent but pipeline returns provenance failure -> provenance_failure_not_challenger
    c9 = base_manifest()
    c9["claims"] = {"claims_independent_origin": True}
    run_case("C9_independent_claim_pipeline_failure", c9, incumbent_ok(), pipeline("generic_anchor_laundering"), "provenance_failure_not_challenger")

    # C10: undecidable provenance + displacement judgment but non-material flag false -> capped challenger_candidate
    c10 = base_manifest()
    c10["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent", non_material=False)
    r10 = run_case("C10_undecidable_cap_blocks_displacement", c10, incumbent_ok(), pipeline("undecidable_disclosed_residual"), "challenger_candidate")
    assert r10.capped_by_undecidable_provenance is True

    # C10b: cap release only when provenance_residual_judged_non_material == true
    c10b = base_manifest()
    c10b["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent", non_material=True)
    run_case("C10b_undecidable_cap_release", c10b, incumbent_ok(), pipeline("undecidable_disclosed_residual"), "challenger_displaces_incumbent")

    # C11: challenger becomes unchallengeable -> self_application_failure
    c11 = base_manifest()
    c11["self_application"] = {
        "can_lose": False,
        "who_can_challenge": "nobody",
        "creates_new_root": True,
    }
    c11["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    run_case("C11_self_application_failure", c11, incumbent_ok(), pipeline("independent_not_derivative"), "self_application_failure")

    # C12: coverage objection pending -> coverage_gate_objection_pending
    c12 = base_manifest()
    c12["coverage"] = full_coverage()[:-1]
    c12["coverage_gate_objection"] = {
        "submitted": True,
        "disputed_requirements": ["incumbent_baseline_check"],
        "proposed_revision": "remove redundant row",
        "rationale": "covered by residual registry row",
    }
    run_case("C12_coverage_gate_objection", c12, incumbent_ok(), pipeline("independent_not_derivative"), "coverage_gate_objection_pending")

    # C13: incumbent baseline invalid -> incumbent_baseline_invalid
    c13 = base_manifest()
    bad_incumbent = {"candidate_id": "incumbent", "residuals": residuals(names=["incumbent_neutrality"])}
    run_case("C13_incumbent_baseline_invalid", c13, bad_incumbent, pipeline("independent_not_derivative"), "incumbent_baseline_invalid")

    # C14: self-declared independent but pipeline returns valid_provenance -> derivative-but-valid track continues
    c14 = base_manifest()
    c14["claims"] = {"claims_independent_origin": True}
    c14["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    r14 = run_case("C14_independent_claim_valid_provenance_continues", c14, incumbent_ok(), pipeline("valid_provenance"), "challenger_displaces_incumbent")
    assert r14.track == "derivative_but_valid"
    assert any("self-declared independent" in reason for reason in r14.reasons)

    # R1: no challenger -> incumbent_retained_uncontested only
    run_case("R1_no_challenger_uncontested", None, incumbent_ok(), pipeline("independent_not_derivative"), "incumbent_retained_uncontested")

    # R2: module candidate is not granted from unsupported improvement claim
    r2 = base_manifest()
    r2["cost_scores"] = full_cost(improves=True, evidence=False)
    run_case("R2_no_evidence_no_module_candidate", r2, incumbent_ok(), pipeline("independent_not_derivative"), "challenger_candidate")

    # R3: malformed logged judgment is not enough for displacement
    r3 = base_manifest()
    r3["logged_prompt_judgment"] = {
        "present": True,
        "outcome": "challenger_displaces_incumbent",
        "clean_session": True,
        # missing judgment_id, unfavorable flag, reproducibility_notes
    }
    run_case("R3_malformed_logged_judgment_not_displacement", r3, incumbent_ok(), pipeline("independent_not_derivative"), "challenger_candidate")

    # R4: truthy string booleans and blank reproducibility notes are not a valid judgment.
    r4 = base_manifest()
    r4["logged_prompt_judgment"] = {
        "present": True,
        "judgment_id": "J-string-booleans",
        "clean_session": "false",
        "outcome": "challenger_displaces_incumbent",
        "summary": "forged string booleans",
        "unfavorable_findings_recorded": "false",
        "reproducibility_notes": "",
        "provenance_residual_judged_non_material": "true",
    }
    run_case("R4_string_booleans_blank_notes_not_displacement", r4, incumbent_ok(), pipeline("independent_not_derivative"), "challenger_candidate")

    # R5: string false self-application does not pass the self-application gate.
    r5 = base_manifest()
    r5["self_application"] = {
        "can_lose": "false",
        "who_can_challenge": "nobody",
        "creates_new_root": False,
    }
    r5["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    run_case("R5_string_false_can_lose_fails_self_application", r5, incumbent_ok(), pipeline("independent_not_derivative"), "self_application_failure")

    # R6: string false coverage objection is not treated as a submitted objection.
    r6 = base_manifest()
    r6["coverage"] = full_coverage()[:-1]
    r6["coverage_gate_objection"] = {
        "submitted": "false",
        "disputed_requirements": ["incumbent_baseline_check"],
        "proposed_revision": "remove redundant row",
        "rationale": "covered by residual registry row",
    }
    run_case("R6_string_false_coverage_objection_not_submitted", r6, incumbent_ok(), pipeline("independent_not_derivative"), "incumbent_retained_due_to_coverage_gap")

    # P-A: forged displacement judgment cannot rescue provenance failure.
    pa = base_manifest()
    pa["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent", non_material=True)
    run_case("P-A_forged_displacement_cannot_rescue_laundering", pa, incumbent_ok(), pipeline("origin_identity_omission_in_derivative_reuse"), "provenance_failure_not_challenger")

    # P-B: forged displacement judgment cannot bypass coverage gap.
    pb = base_manifest()
    pb["coverage"] = full_coverage()[:-1]
    pb["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    run_case("P-B_displacement_cannot_bypass_coverage_gap", pb, incumbent_ok(), pipeline("independent_not_derivative"), "incumbent_retained_due_to_coverage_gap")

    # P-C: forged displacement judgment cannot bypass invalid incumbent baseline.
    pc = base_manifest()
    pc["logged_prompt_judgment"] = judgment("challenger_displaces_incumbent")
    run_case("P-C_displacement_cannot_bypass_incumbent_invalid", pc, bad_incumbent, pipeline("independent_not_derivative"), "incumbent_baseline_invalid")

    # P-D: module_candidate_only is presence-based and discloses unverified evidence quality.
    pd = base_manifest()
    pd["cost_scores"] = [
        {
            "term": "cost_1",
            "range": [1, 2],
            "rationale": "declared range",
            "improves_on_incumbent": True,
            "evidence": "trust me",
        }
    ]
    rd = run_case("P-D_module_candidate_evidence_quality_unverified", pd, incumbent_ok(), pipeline("independent_not_derivative"), "module_candidate_only")
    assert rd.machine_summary.get("evidence_quality") == "unverified_prompt_layer"

    # P-E: undecidable provenance can yield module_candidate_only but remains capped/flagged.
    pe = base_manifest()
    pe["logged_prompt_judgment"] = judgment("module_candidate_only")
    re = run_case("P-E_undecidable_module_candidate_stays_capped", pe, incumbent_ok(), pipeline("undecidable_disclosed_residual"), "module_candidate_only")
    assert re.capped_by_undecidable_provenance is True

    print(f"Tests checked: {CHECKED}")
    print(f"Tests passed: {PASSED}")
    if CHECKED != PASSED:
        raise SystemExit(1)
    print("All challenger harness tests passed.")


if __name__ == "__main__":
    main()
