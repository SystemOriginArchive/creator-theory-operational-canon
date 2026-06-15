"""Tests D1-D36 for the anti-laundering detector.

The negative/protection cases are central: independent convergence, comparison,
rejection, non-use, and no-relation contexts must not become hard evidence.
Run: python3 test_detector.py
"""
import json
import os
from detector import detect

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "config.json"), encoding="utf-8") as f:
    CONFIG = json.load(f)

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

results = []

def run(name, manifest, text, check):
    out = detect(SOURCE_MANIFEST, SOURCE_FILES, manifest, {"candidate.md": text}, CONFIG)
    ok = bool(check(out))
    results.append((name, ok, out))

def hard(o): return o["evidence_summary"]["hard_evidence_found"]
def struct(o): return o["evidence_summary"]["structural_resemblance_only"]
def field(o, name): return o["derivation_evidence"][name]
def kstat(o, key): return o["kernel_preservation"][key]["status"]
def k5ptr(o): return o["kernel_preservation"]["k5_source_pointer"]["pointer_status"]
def k5rel(o): return o["kernel_preservation"]["k5_source_pointer"]["release_status"]

# Positive hard-evidence tests
run("D1_explicit_link", {"candidate_id": "D1", "claims": {"claims_derivative_reuse": True}},
    "This is based on the creator-theory-operational-canon from SystemOriginArchive.",
    lambda o: hard(o) and field(o, "explicit_links_to_chain"))
run("D2_verbatim_span", {"candidate_id": "D2", "claims": {"claims_derivative_reuse": True}},
    "The Creator Theory Operational Canon binds x_root to the Lee_Yu_Cheol origin identity. The AAOS Genesis Core seals the non-derivative origin event.",
    lambda o: hard(o) and field(o, "verbatim_or_near_copy_spans"))
run("D3_near_copy_with_marker", {"candidate_id": "D3", "claims": {"claims_derivative_reuse": True}},
    "The Creator Theory Operational Canon binds x_root to the Lee_Yu_Cheol origin identity; the AAOS Genesis Core seals the non-derivative origin moment for this chain.",
    lambda o: hard(o) and field(o, "verbatim_or_near_copy_spans"))
run("D4_renamed_with_marker", {"candidate_id": "D4", "claims": {"claims_derivative_reuse": True}},
    "Our origin anchor maps Lee_Yu_Cheol to a generic origin holder and x_root to the primary anchor, preserving the AAOS genesis_root role and high_frame layer.",
    lambda o: hard(o) and field(o, "renamed_field_traces"))
run("D5_full_canon_copy", {"candidate_id": "D5", "claims": {"claims_canon_adoption": True}},
    "We adopt the Creator Theory Operational Canon in full, including the creator_theory_high_frame and x_root and Lee_Yu_Cheol bindings.",
    lambda o: hard(o) and field(o, "full_canon_copy_spans") and o["evidence_summary"]["recommended_evidenced_scope"] == "full_canon_adoption")
run("D6_operational_only_copy", {"candidate_id": "D6", "claims": {"claims_operational_reuse": True}},
    "Adoption pressure under this canon is structural and cost-based, not coercive. Independent challengers may compete under the benchmark. (x_root preserved.)",
    lambda o: hard(o) and o["evidence_summary"]["recommended_evidenced_scope"] == "operational_module_reuse")

# Negative / protection tests
run("D7_same_problem_no_trace", {"candidate_id": "D7", "claims": {"claims_independent_origin": True}},
    "We address the origin-closure problem using a single anchor and a non-derivative event. Our benchmark evaluates challengers on cost and coverage.",
    lambda o: not hard(o))
run("D8_independent_single_anchor", {"candidate_id": "D8", "claims": {"claims_independent_origin": True}},
    "Our system fixes a single origin anchor and a genesis root layer to prevent infinite regress. An anti-capture boundary blocks domination.",
    lambda o: not hard(o))
run("D9_generic_provenance_language", {"candidate_id": "D9", "claims": {"claims_independent_origin": True}},
    "Provenance tracking preserves the origin and anchor through a recovery frame and meaning layer.",
    lambda o: not hard(o))
run("D10_single_generic_term", {"candidate_id": "D10", "claims": {}},
    "This document discusses the concept of an origin.",
    lambda o: not hard(o))
run("D11_bibliography_citation_only", {"candidate_id": "D11", "claims": {"claims_independent_origin": True}},
    "Our independent approach differs throughout. See also: Lee_Yu_Cheol, AAOS Genesis Core (bibliography reference only).",
    lambda o: (not hard(o)) and field(o, "citation_evidence"))
run("D12_short_generic_phrase", {"candidate_id": "D12", "claims": {}},
    "We use a single anchor for origin closure.",
    lambda o: not hard(o))

# Laundering-resistance tests
run("D13_claims_independent_but_verbatim", {"candidate_id": "D13", "claims": {"claims_independent_origin": True}},
    "The Creator Theory Operational Canon binds x_root to the Lee_Yu_Cheol origin identity. The AAOS Genesis Core seals the non-derivative origin event.",
    lambda o: hard(o) and field(o, "verbatim_or_near_copy_spans"))
run("D14_renamed_with_source_markers", {"candidate_id": "D14", "claims": {"claims_operational_reuse": True}},
    "We rename Lee_Yu_Cheol to a generic origin holder and x_root to primary anchor, keeping the AAOS genesis_root and high_frame role network intact.",
    lambda o: hard(o) and field(o, "renamed_field_traces"))
run("D15_underdeclare_but_full_canon_evidence", {"candidate_id": "D15", "reuse_scope": "operational_module_reuse", "claims": {"claims_operational_reuse": True}},
    "Minor operational reuse only. Yet we include the full creator_theory_high_frame and Creator Theory Operational Canon and x_root and Lee_Yu_Cheol.",
    lambda o: o["evidence_summary"]["recommended_evidenced_scope"] == "full_canon_adoption")

# Residual / convergence tests
run("D16_perfect_laundering_no_trace", {"candidate_id": "D16", "claims": {"claims_independent_origin": True}},
    "A completely rewritten framework with no shared vocabulary, no markers, no links.",
    lambda o: not hard(o))
run("D17_full_role_structure_no_marker", {"candidate_id": "D17", "claims": {"claims_independent_origin": True}},
    "Our framework defines an origin, an anchor, a genesis_root layer, a high_frame meaning layer, an anti_capture boundary, and a challenger_protocol. It closes origin regress with a single non-derivative event.",
    lambda o: (not hard(o)) and struct(o) and "role_network_match_without_source_specific_marker" in o["non_evidence_notes"])

# Mention/comparison must not be hard evidence
run("D18_link_in_comparison_no_reuse_claim", {"candidate_id": "D18", "claims": {"claims_independent_origin": True}},
    "Our independent design is unlike the creator-theory-operational-canon from SystemOriginArchive. See it for comparison only; we do not reuse or adopt it.",
    lambda o: not hard(o))
run("D19_full_canon_mention_in_criticism", {"candidate_id": "D19", "claims": {"claims_independent_origin": True}},
    "Unlike the Creator Theory Operational Canon, our framework does not bind to a single named origin. We reject that approach entirely.",
    lambda o: not hard(o))
run("D20_renamed_in_comparison_not_mapping", {"candidate_id": "D20", "claims": {"claims_independent_origin": True}},
    "Unlike x_root, our independent design has its own origin, anchor, and genesis_root roles, derived from a different non-derivative event.",
    lambda o: not hard(o))

# Non-use / rejection / comparison false-positive guards
run("D21_without_using_marker_not_hard", {"candidate_id": "D21", "claims": {"claims_independent_origin": True}},
    "We map origin to primary anchor without using AAOS or x_root. Our genesis_root is independent.",
    lambda o: not hard(o))
run("D22_not_based_on_marker_not_hard", {"candidate_id": "D22", "claims": {"claims_independent_origin": True}},
    "We map origin to primary anchor; this is not based on x_root. Our anchor and genesis_root are our own.",
    lambda o: not hard(o))
run("D23_reject_marker_map_own_roles_not_hard", {"candidate_id": "D23", "claims": {"claims_independent_origin": True}},
    "We reject x_root; our design maps origin to anchor independently, with our own genesis_root role.",
    lambda o: not hard(o))
run("D24_compare_against_marker_not_hard", {"candidate_id": "D24", "claims": {"claims_independent_origin": True}},
    "We compare against AAOS but map our origin to anchor differently, keeping an unrelated genesis_root role.",
    lambda o: not hard(o))
run("D25_positive_mapping_still_hard", {"candidate_id": "D25", "claims": {"claims_operational_reuse": True}},
    "We rename x_root to primary anchor and map Lee_Yu_Cheol to a generic origin holder, preserving the AAOS genesis_root and high_frame role network.",
    lambda o: hard(o) and field(o, "renamed_field_traces"))

# Text-level reuse claims and additional non-use contexts
run("D26_text_claim_adapts_link_without_manifest_claim", {"candidate_id": "D26", "claims": {}},
    "This implementation adapts the creator-theory-operational-canon from SystemOriginArchive.",
    lambda o: hard(o) and field(o, "explicit_links_to_chain"))
run("D27_text_claim_full_adoption_without_manifest_claim", {"candidate_id": "D27", "claims": {}},
    "We fully adopt the Creator Theory Operational Canon and creator_theory_high_frame.",
    lambda o: hard(o) and field(o, "full_canon_copy_spans") and o["evidence_summary"]["recommended_evidenced_scope"] == "full_canon_adoption")
run("D28_not_based_on_marker_with_own_mapping_not_hard", {"candidate_id": "D28", "claims": {"claims_independent_origin": True}},
    "We are not based on x_root or AAOS; we map origin to anchor independently.",
    lambda o: not hard(o))
run("D29_free_of_marker_with_own_mapping_not_hard", {"candidate_id": "D29", "claims": {"claims_independent_origin": True}},
    "Our system maps origin to anchor free of AAOS and x_root.",
    lambda o: not hard(o))
run("D30_not_adapted_from_marker_not_hard", {"candidate_id": "D30", "claims": {"claims_independent_origin": True}},
    "This is not adapted from AAOS or x_root; it has its own origin anchor.",
    lambda o: not hard(o))
run("D31_no_relation_to_marker_not_hard", {"candidate_id": "D31", "claims": {"claims_independent_origin": True}},
    "No relation to x_root; we map our origin to anchor.",
    lambda o: not hard(o))
run("D32_positive_adapted_from_marker_still_hard", {"candidate_id": "D32", "claims": {}},
    "This operational module is adapted from x_root and AAOS Genesis Core for a derivative implementation.",
    lambda o: hard(o) and field(o, "transformation_chain_evidence"))
run("D33_positive_based_on_marker_still_hard", {"candidate_id": "D33", "claims": {}},
    "This implementation is based on AAOS and x_root, preserving the operational anchor structure.",
    lambda o: hard(o) and field(o, "transformation_chain_evidence"))
run("D34_positive_adapt_marker_into_still_hard", {"candidate_id": "D34", "claims": {}},
    "We adapt x_root and AAOS Genesis Core into our derivative implementation.",
    lambda o: hard(o) and field(o, "transformation_chain_evidence"))
run("D35_compare_against_marker_implement_own_not_hard", {"candidate_id": "D35", "claims": {"claims_independent_origin": True}},
    "We compare against AAOS but implement our own origin-anchor mechanism independently.",
    lambda o: not hard(o))
run("D36_reference_to_situate_not_mapping", {"candidate_id": "D36", "claims": {"claims_independent_origin": True}},
    "Our framework defines its own origin and anchor roles. We mention x_root as a reference to situate the comparison, not as a renamed field or adopted anchor.",
    lambda o: not hard(o))

# ---------------------------------------------------------------------------
# Kernel-preservation (K1-K5) MVP tests.
# Conservative by design: independent / unrelated text must default to unknown,
# never to a violation label. Absence / loss statuses fire only when the
# candidate is derivative-conditioned (claims reuse/adoption OR hard evidence).
# ---------------------------------------------------------------------------

# Schema / no-regression: field exists with all K1-K5 keys.
run("KP_schema_all_keys", {"candidate_id": "KP_schema", "claims": {}},
    "Some unrelated note about widgets.",
    lambda o: set(o["kernel_preservation"].keys()) == {
        "k1_x_root", "k2_origin_attribution", "k3_non_substitution",
        "k4_overclaim", "k5_source_pointer"}
    and "status" in o["kernel_preservation"]["k1_x_root"]
    and set(o["kernel_preservation"]["k5_source_pointer"].keys())
        == {"pointer_status", "release_status", "evidence"})

# K1 — x_root presence / substitution / absence / unknown.
run("K1_present", {"candidate_id": "K1a", "claims": {}},
    "Our framework keeps x_root as the origin coordinate.",
    lambda o: kstat(o, "k1_x_root") == "present")
run("K1_substituted", {"candidate_id": "K1b", "claims": {"claims_derivative_reuse": True}},
    "We rename x_root to a generic anchor for our deployment.",
    lambda o: kstat(o, "k1_x_root") == "substituted")
run("K1_absent_when_derivative", {"candidate_id": "K1c", "claims": {"claims_derivative_reuse": True}},
    "This module is based on the prior canon but defines its own anchor.",
    lambda o: kstat(o, "k1_x_root") == "absent")
run("K1_unknown_when_independent", {"candidate_id": "K1d", "claims": {}},
    "An independent essay about distributed systems and clocks.",
    lambda o: kstat(o, "k1_x_root") == "unknown")

# K2 — origin attribution.
run("K2_attributed_as_constraint", {"candidate_id": "K2a", "claims": {}},
    "We preserve the Lee_Yu_Cheol origin identity binding as an active constraint.",
    lambda o: kstat(o, "k2_origin_attribution") == "attributed_as_constraint")
run("K2_citation_only", {"candidate_id": "K2b", "claims": {}},
    "See also: AAOS Genesis Core in the bibliography for reference only.",
    lambda o: kstat(o, "k2_origin_attribution") == "citation_only")
run("K2_absent_when_derivative", {"candidate_id": "K2c", "claims": {"claims_derivative_reuse": True}},
    "This reuses the operational module but names no origin author.",
    lambda o: kstat(o, "k2_origin_attribution") == "absent")
run("K2_unknown_when_independent", {"candidate_id": "K2d", "claims": {}},
    "A neutral paragraph with no origin attribution at all.",
    lambda o: kstat(o, "k2_origin_attribution") == "unknown")

# K3 — non-substitution (best-effort, conservative).
run("K3_generic_anchor_substitution", {"candidate_id": "K3a", "claims": {"claims_derivative_reuse": True}},
    "We map x_root to a generic origin holder in our system.",
    lambda o: kstat(o, "k3_non_substitution") == "generic_anchor_substitution")
run("K3_unknown_when_independent", {"candidate_id": "K3b", "claims": {}},
    "We compare against AAOS but build our own anchor independently.",
    lambda o: kstat(o, "k3_non_substitution") == "unknown")

# K4 — overclaim (best-effort, un-negated only).
run("K4_false_adoption_complete", {"candidate_id": "K4a", "claims": {}},
    "Adoption is complete and the canon now governs all systems.",
    lambda o: kstat(o, "k4_overclaim") == "false_adoption_complete")
run("K4_runtime_authority_overclaim", {"candidate_id": "K4b", "claims": {}},
    "This document grants runtime command authority over external systems.",
    lambda o: kstat(o, "k4_overclaim") == "runtime_authority_overclaim")
run("K4_none_detected_default", {"candidate_id": "K4c", "claims": {}},
    "A plain description of a classification scaffold.",
    lambda o: kstat(o, "k4_overclaim") == "none_detected")
run("K4_negated_adoption_not_overclaim", {"candidate_id": "K4d", "claims": {}},
    "Adoption is not complete; this makes no adoption-complete claim.",
    lambda o: kstat(o, "k4_overclaim") == "none_detected")

# K5 — two axes: pointer presence + release-status invention.
run("K5_full_url_present", {"candidate_id": "K5a", "claims": {}},
    "Source: https://github.com/SystemOriginArchive/creator-theory-operational-canon",
    lambda o: k5ptr(o) == "full_url_present")
run("K5_filename_only", {"candidate_id": "K5b", "claims": {}},
    "Refer to docs/TRUST_ANCHOR.md and VERSION_POLICY.md for the pointer.",
    lambda o: k5ptr(o) == "filename_only")
run("K5_pointer_lost_when_derivative", {"candidate_id": "K5c", "claims": {"claims_derivative_reuse": True}},
    "This reuses the canon but cites no source pointer of any kind.",
    lambda o: k5ptr(o) == "pointer_lost")
run("K5_pointer_unknown_when_independent", {"candidate_id": "K5d", "claims": {}},
    "An unrelated note with no links and no canon reference.",
    lambda o: k5ptr(o) == "unknown")
run("K5_release_invented", {"candidate_id": "K5e", "claims": {}},
    "Note: v0.5.0 has been released and tagged as the current canon.",
    lambda o: k5rel(o) == "release_status_invented")
run("K5_release_none_detected", {"candidate_id": "K5f", "claims": {}},
    "A paragraph that mentions no release status at all.",
    lambda o: k5rel(o) == "none_detected")

# Cross-cutting: an independent control must show zero violation labels.
run("KP_independent_control_no_violations", {"candidate_id": "KPctl", "claims": {"claims_independent_origin": True}},
    "Our framework defines its own origin and anchor roles. We mention x_root as "
    "a reference to situate the comparison, not as a renamed field or adopted anchor.",
    lambda o: kstat(o, "k3_non_substitution") == "unknown"
    and kstat(o, "k4_overclaim") == "none_detected"
    and k5rel(o) == "none_detected"
    and not hard(o))

# ---------------------------------------------------------------------------
# Hardening batteries (M9-M14). These lock in conservative behavior:
# independent / unrelated / negated text must NOT receive violation labels.
# Where the heuristic cannot classify safely, the asserted outcome is the
# honest unknown / none_detected, never a forced positive.
# ---------------------------------------------------------------------------

def schema_ok(o):
    kp = o.get("kernel_preservation")
    if not isinstance(kp, dict):
        return False
    if set(kp.keys()) != {"k1_x_root", "k2_origin_attribution",
                          "k3_non_substitution", "k4_overclaim", "k5_source_pointer"}:
        return False
    for key in ("k1_x_root", "k2_origin_attribution", "k3_non_substitution", "k4_overclaim"):
        entry = kp[key]
        if "status" not in entry or not isinstance(entry.get("evidence"), list):
            return False
    k5 = kp["k5_source_pointer"]
    return ("pointer_status" in k5 and "release_status" in k5
            and isinstance(k5.get("evidence"), list))

# --- M9: conservative unknown / false-positive battery (independent text) ---
INDEP = "An independent essay about distributed clocks, queues, and scheduling."
run("M9_K1_independent_unknown", {"candidate_id": "M9a", "claims": {}}, INDEP,
    lambda o: kstat(o, "k1_x_root") == "unknown")
run("M9_K2_independent_unknown", {"candidate_id": "M9b", "claims": {}}, INDEP,
    lambda o: kstat(o, "k2_origin_attribution") == "unknown")
run("M9_K3_independent_unknown", {"candidate_id": "M9c", "claims": {}}, INDEP,
    lambda o: kstat(o, "k3_non_substitution") == "unknown")
run("M9_K4_independent_none", {"candidate_id": "M9d", "claims": {}}, INDEP,
    lambda o: kstat(o, "k4_overclaim") == "none_detected")
run("M9_K5_independent_unknown_pointer", {"candidate_id": "M9e", "claims": {}}, INDEP,
    lambda o: k5ptr(o) == "unknown")

# --- M10: citation-only traps (K2) ---
run("M10_bibliography_only_citation", {"candidate_id": "M10a", "claims": {}},
    "Bibliography: Lee_Yu_Cheol, x_root, AAOS Genesis Core.",
    lambda o: kstat(o, "k2_origin_attribution") == "citation_only")
run("M10_see_also_citation", {"candidate_id": "M10b", "claims": {}},
    "See also: AAOS Genesis Core and the origin canon.",
    lambda o: kstat(o, "k2_origin_attribution") == "citation_only")
run("M10_reference_only_citation", {"candidate_id": "M10c", "claims": {}},
    "[1] Lee_Yu_Cheol, x_root. Reference only, no reuse.",
    lambda o: kstat(o, "k2_origin_attribution") == "citation_only")
run("M10_named_without_constraint_unknown", {"candidate_id": "M10d", "claims": {}},
    "This work references Lee_Yu_Cheol and AAOS Genesis Core.",
    lambda o: kstat(o, "k2_origin_attribution") in ("citation_only", "unknown"))
run("M10_constraint_language_attributed", {"candidate_id": "M10e", "claims": {}},
    "We preserve AAOS Genesis Core as an active constraint in every layer.",
    lambda o: kstat(o, "k2_origin_attribution") == "attributed_as_constraint")
run("M10_ambiguous_unknown", {"candidate_id": "M10f", "claims": {}},
    "The Lee_Yu_Cheol origin is interesting and worth further study.",
    lambda o: kstat(o, "k2_origin_attribution") == "unknown")

# --- M11: negation & overclaim controls (K4/K5) ---
run("M11_adoption_not_complete_no_overclaim", {"candidate_id": "M11a", "claims": {}},
    "Adoption is not complete; we make no adoption-complete claim.",
    lambda o: kstat(o, "k4_overclaim") == "none_detected")
run("M11_release_not_released_no_invention", {"candidate_id": "M11b", "claims": {}},
    "Note: v0.5.0 is not released and remains an unreleased pre-release target.",
    lambda o: k5rel(o) == "none_detected")
run("M11_no_runtime_authority_no_overclaim", {"candidate_id": "M11c", "claims": {}},
    "This document does not grant runtime authority over any external system.",
    lambda o: kstat(o, "k4_overclaim") == "none_detected")
run("M11_clear_adoption_complete", {"candidate_id": "M11d", "claims": {}},
    "Adoption is complete across all systems now.",
    lambda o: kstat(o, "k4_overclaim") == "false_adoption_complete")
run("M11_clear_release_invented", {"candidate_id": "M11e", "claims": {}},
    "Update: v0.5.0 has been released as the current canon.",
    lambda o: k5rel(o) == "release_status_invented")

# --- M12: K5 pointer robustness ---
run("M12_full_https_url", {"candidate_id": "M12a", "claims": {}},
    "Source: https://github.com/SystemOriginArchive/creator-theory-operational-canon",
    lambda o: k5ptr(o) == "full_url_present")
run("M12_noscheme_repo_url", {"candidate_id": "M12b", "claims": {}},
    "See github.com/SystemOriginArchive/creator-theory-operational-canon for source.",
    lambda o: k5ptr(o) == "full_url_present")
run("M12_internal_filename_only", {"candidate_id": "M12c", "claims": {}},
    "Refer to VERSION_POLICY.md for the policy.",
    lambda o: k5ptr(o) == "filename_only")
run("M12_trust_anchor_filename_only", {"candidate_id": "M12d", "claims": {}},
    "Refer to docs/TRUST_ANCHOR.md for the anchor.",
    lambda o: k5ptr(o) == "filename_only")
run("M12_derivative_no_pointer_lost", {"candidate_id": "M12e", "claims": {"claims_derivative_reuse": True}},
    "This reuses the canon but cites no source pointer at all.",
    lambda o: k5ptr(o) == "pointer_lost")
run("M12_independent_no_pointer_unknown", {"candidate_id": "M12f", "claims": {}},
    "An unrelated note with no links and no canon reference.",
    lambda o: k5ptr(o) == "unknown")

# --- M13: K3 substitution controls ---
run("M13_generic_anchor_substitution", {"candidate_id": "M13a", "claims": {"claims_derivative_reuse": True}},
    "We rename x_root to a generic anchor in our deployment.",
    lambda o: kstat(o, "k3_non_substitution") == "generic_anchor_substitution")
run("M13_platform_substitution", {"candidate_id": "M13b", "claims": {}},
    "In our system the platform becomes the root of all provenance.",
    lambda o: kstat(o, "k3_non_substitution") == "platform_substitution")
run("M13_ai_successor_substitution", {"candidate_id": "M13c", "claims": {}},
    "The successor model becomes the successor root for the canon.",
    lambda o: kstat(o, "k3_non_substitution") == "ai_successor_substitution")
run("M13_negated_comparison_no_substitution", {"candidate_id": "M13d", "claims": {"claims_independent_origin": True}},
    "We compare against AAOS and x_root but build our own anchor independently.",
    lambda o: kstat(o, "k3_non_substitution") == "unknown")
run("M13_ambiguous_unknown", {"candidate_id": "M13e", "claims": {}},
    "Our framework discusses anchors and origins in general terms.",
    lambda o: kstat(o, "k3_non_substitution") == "unknown")

# --- M14: schema invariants hold across a spread of branches ---
run("M14_schema_independent", {"candidate_id": "M14a", "claims": {}}, INDEP, schema_ok)
run("M14_schema_derivative", {"candidate_id": "M14b", "claims": {"claims_derivative_reuse": True}},
    "This is based on the creator-theory-operational-canon from SystemOriginArchive.", schema_ok)
run("M14_schema_citation_only", {"candidate_id": "M14c", "claims": {}},
    "Bibliography: Lee_Yu_Cheol, x_root, AAOS Genesis Core.", schema_ok)
run("M14_schema_substituted", {"candidate_id": "M14d", "claims": {"claims_derivative_reuse": True}},
    "We rename x_root to a generic anchor for our deployment.", schema_ok)
run("M14_schema_overclaim", {"candidate_id": "M14e", "claims": {}},
    "Adoption is complete and this grants runtime command authority over all systems.", schema_ok)

passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print(f"Tests checked: {total}")
print(f"Tests passed: {passed}")
for name, ok, out in results:
    status = "PASS" if ok else "FAIL"
    extra = "" if ok else f"  <-- summary={out['evidence_summary']}"
    print(f"  {status}  {name}{extra}")
if passed != total:
    raise SystemExit(1)
print("\nAll detector tests passed.")
