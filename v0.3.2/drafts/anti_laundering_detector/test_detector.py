"""Tests D1-D35 for the anti-laundering detector.

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
