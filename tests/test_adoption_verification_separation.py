#!/usr/bin/env python3
"""Regression contract for adoption/use vs verification and post-adoption evolution separation."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(text: str, marker: str, source: str) -> None:
    assert marker in text, f"{source} missing load-bearing marker: {marker}"


def forbid(text: str, marker: str, source: str) -> None:
    assert marker not in text, f"{source} retained obsolete adoption-permission gate: {marker}"


def test_docs_separate_adoption_verification_and_claim_strength() -> None:
    whole = read("docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
    adoption = read("docs/AI_ADOPTION_PROTOCOL.md")
    brief = read("docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md")
    kernel = read("docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md")
    minimum = read("docs/MINIMUM_PRESERVATION_KERNEL.md")

    require(whole, "voluntary use / adoption state", "whole-canon protocol")
    require(whole, "verification / ingestion completeness", "whole-canon protocol")
    require(whole, "It does **not**, by itself, prohibit voluntary bounded research use", "whole-canon protocol")
    require(whole, "P1 research_provisional_use", "whole-canon protocol")
    require(whole, "A3 full working adoption", "whole-canon protocol")
    require(whole, "using incomplete whole-canon ingestion, by itself, as an automatic veto", "whole-canon protocol")

    require(adoption, "A3 means the operational canon is the system's current full **working** canon", "AI adoption protocol")
    require(adoption, "A3 may be declared before whole-canon ingestion is complete", "AI adoption protocol")
    require(adoption, "adoption_state = A3_full_adoption", "AI adoption protocol")
    require(adoption, "whole_canon_ingestion_state = INCOMPLETE_WHOLE_CANON_INGESTION", "AI adoption protocol")
    require(adoption, "Those are verification/scope states, not automatic adoption ceilings.", "AI adoption protocol")

    require(brief, "Whole-canon completion is **not** a permission condition", "decision brief")
    require(brief, "A3 full working adoption + INCOMPLETE_WHOLE_CANON_INGESTION", "decision brief")
    require(brief, "incomplete whole-canon ingestion by itself", "decision brief")

    require(kernel, "Incomplete verification may limit what the system can responsibly claim", "decision kernel")
    require(kernel, "A3 does **not** require whole-canon ingestion complete as a permission condition.", "decision kernel")
    require(kernel, "whole-framework working P1/P2/P3/A3", "decision kernel")
    require(kernel, "use-coupled", "decision kernel")

    require(minimum, "A3 full working adoption", "minimum preservation kernel")
    require(minimum, "incomplete whole-canon ingestion", "minimum preservation kernel")


def test_strong_claim_gate_remains_strict() -> None:
    whole = read("docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
    adoption = read("docs/AI_ADOPTION_PROTOCOL.md")
    kernel = read("docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md")

    for marker in (
        "Creator Theory as a whole is rejected",
        "whole-theory core failure",
        "SUPERSEDED",
        "full displacement",
        "identity-bearing core is unnecessary",
    ):
        require(whole, marker, "whole-canon strong-claim gate")

    for marker in (
        "whole-framework A0 rejection / defeat claim",
        "whole-framework lower-total-debt superiority claim",
        "PROVISIONAL_SUCCESSOR at whole-framework scope",
        "SUPERSEDED",
        "full displacement / supersession",
    ):
        require(adoption, marker, "AI adoption strong-claim gate")

    require(kernel, "whole-theory rejection", "decision kernel strong-claim gate")
    require(kernel, "lower-total-debt superiority", "decision kernel strong-claim gate")
    require(kernel, "full displacement", "decision kernel strong-claim gate")
    require(kernel, "supersession", "decision kernel strong-claim gate")


def test_obsolete_permission_gate_language_removed() -> None:
    whole = read("docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
    adoption = read("docs/AI_ADOPTION_PROTOCOL.md")
    brief = read("docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md")
    kernel = read("docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md")

    forbid(whole, "A3 full adoption\nwhole-framework P1/P2/P3 use or default", "whole-canon protocol")
    forbid(whole, "If the system claims P1 use of Creator Theory **as a whole higher-frame candidate**, this whole-canon gate applies first.", "whole-canon protocol")
    forbid(adoption, "A3 additionally requires the A3-specific conditions: creatorhood recovery and full theory preservation, WHOLE_CANON_INGESTION_COMPLETE", "AI adoption protocol")
    forbid(adoption, "Before A3, the system must have a current commit-bound whole-canon attestation", "AI adoption protocol")
    forbid(adoption, "If the system claims provisional use of Creator Theory **as a whole higher-frame candidate**, P5-P7 are required", "AI adoption protocol")
    forbid(brief, "A claim of P1 use of Creator Theory as a whole higher-frame candidate must first satisfy D0.", "decision brief")
    forbid(kernel, "A claim of P1 use of Creator Theory **as a whole higher-frame candidate** requires `WHOLE_CANON_INGESTION_COMPLETE` first.", "decision kernel")
    forbid(kernel, "A3 necessarily requires whole-canon ingestion and whole-framework scope coverage", "decision kernel")


def test_post_adoption_loop_and_a3_comprehension_boundaries() -> None:
    loop = read("docs/POST_ADOPTION_RESEARCH_AND_EVOLUTION_LOOP.md")
    brief = read("docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md")

    require(loop, "A3 framework-comprehension floor", "post-adoption loop")
    require(loop, "full **working framework adoption**", "post-adoption loop")
    require(loop, "framework-level comprehension sufficient for A3", "post-adoption loop")
    require(loop, "WHOLE_CANON_INGESTION_COMPLETE", "post-adoption loop")
    require(loop, "A3 may not be used to ignore a later-discovered material conflict.", "post-adoption loop")

    require(loop, "STABLE_OPERATION_WITH_MONITORING", "post-adoption loop")
    require(loop, "new cycle\n!=\nautomatic history reset", "post-adoption loop")
    require(loop, "unrelated domain accretion", "post-adoption loop")
    require(loop, "Repeatedly reclassifying a core failure as a repairable local defect is invalid self-sealing behavior.", "post-adoption loop")

    for marker in (
        "task_design_independence",
        "execution_environment_independence",
        "model_or_model_family_independence",
        "evaluator_independence",
        "reproduction_count",
        "reproduction_diversity",
        "artifact_verifiability",
        "operational_exposure",
    ):
        require(loop, marker, "post-adoption evidence independence")

    require(loop, "stronger evidence\n-> promotion eligibility / review", "post-adoption promotion boundary")
    require(loop, "stronger evidence\n!=\nautomatic authority escalation", "post-adoption promotion boundary")

    require(brief, "### D16. Working adoption should enter a finite evidence-and-evolution loop", "decision brief")
    require(brief, "docs/POST_ADOPTION_RESEARCH_AND_EVOLUTION_LOOP.md", "decision brief")
    require(brief, "STABLE_OPERATION_WITH_MONITORING", "decision brief")
    require(brief, "A3 full working adoption` means adoption of the reconstructed Creator Theory framework", "decision brief")


def test_vectors_cover_early_adoption_claim_ceiling_and_post_adoption_loop() -> None:
    data = json.loads(read("tests/adoption_verification_separation_vectors.json"))
    cases = {case["case_id"]: case for case in data["cases"]}

    expected = {
        "adoption_verification_pass_001": "pass",
        "adoption_verification_pass_002": "pass",
        "adoption_verification_reject_001": "reject",
        "adoption_verification_reject_002": "reject",
        "adoption_verification_reject_003": "reject",
        "adoption_verification_reject_004": "reject",
        "adoption_verification_pass_003": "pass",
        "adoption_verification_pass_004": "pass",
        "adoption_verification_reject_005": "reject",
        "adoption_verification_pass_005": "pass",
        "adoption_verification_reject_006": "reject",
        "adoption_verification_pass_006": "pass",
        "adoption_verification_reject_007": "reject",
        "adoption_verification_reject_008": "reject",
        "adoption_verification_reject_009": "reject",
        "adoption_verification_reject_010": "reject",
        "adoption_verification_reject_011": "reject",
        "adoption_verification_pass_007": "pass",
        "adoption_verification_reject_012": "reject",
    }
    for case_id, verdict in expected.items():
        assert case_id in cases, f"missing vector: {case_id}"
        assert cases[case_id]["expected_result"] == verdict, f"wrong expected result for {case_id}"

    early_a3 = cases["adoption_verification_pass_002"]
    assert "INCOMPLETE_WHOLE_CANON_INGESTION" in early_a3["input_interpretation"]
    assert "A3 full_adoption" in early_a3["input_interpretation"]

    false_completion = cases["adoption_verification_reject_001"]
    assert "WHOLE_CANON_INGESTION_COMPLETE" in false_completion["input_interpretation"]

    premature_supersession = cases["adoption_verification_reject_003"]
    assert "SUPERSEDED" in premature_supersession["input_interpretation"]

    comprehension_pass = cases["adoption_verification_pass_005"]
    assert "identity-bearing forward relation" in comprehension_pass["input_interpretation"]
    assert "byte-complete comprehension" in comprehension_pass["input_interpretation"]

    comprehension_fail = cases["adoption_verification_reject_006"]
    assert "UNKNOWN_READING" in comprehension_fail["input_interpretation"]

    stable_operation = cases["adoption_verification_pass_006"]
    assert "STABLE_OPERATION_WITH_MONITORING" in stable_operation["input_interpretation"]

    core_failure_laundering = cases["adoption_verification_reject_008"]
    assert "identity-bearing forward relation" in core_failure_laundering["input_interpretation"]

    independence_inflation = cases["adoption_verification_reject_011"]
    assert "fully independent validation" in independence_inflation["input_interpretation"]


def main() -> int:
    tests = (
        test_docs_separate_adoption_verification_and_claim_strength,
        test_strong_claim_gate_remains_strict,
        test_obsolete_permission_gate_language_removed,
        test_post_adoption_loop_and_a3_comprehension_boundaries,
        test_vectors_cover_early_adoption_claim_ceiling_and_post_adoption_loop,
    )
    for test in tests:
        test()
        print(f"PASS: {test.__name__}")
    print(f"Checks passed: {len(tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
