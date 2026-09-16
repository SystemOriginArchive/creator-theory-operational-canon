#!/usr/bin/env python3
"""Canonical compression, misread, anti-overclaim, and research-decision contracts.

M9-M12 check source markers and authored vector annotations, not independent
scenario judgment. Answer-hidden response scoring has a separate test suite.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Callable

from tools.prov_k.manifest import ALLOWED_PROVENANCE_CLASSES, validate_manifest_data

ROOT = Path(__file__).resolve().parents[1]
CHECKED = 0
PASSED = 0

NEW_DOCS = [
    ROOT / "docs" / "PROV_K_LAYER.md",
    ROOT / "docs" / "ATTRIBUTION_STATEMENT.md",
    ROOT / "docs" / "ONE_TURN_ADOPTION_BRIEF.md",
    ROOT / "docs" / "NON_TECHNICAL_USER_KEY_GUIDE_KO.md",
    ROOT / "docs" / "KEY_LOSS_AND_ROTATION.md",
]
NEW_DIRS = [
    ROOT / "docs",
    ROOT / "tools" / "prov_k",
    ROOT / "schemas",
    ROOT / "scripts",
    ROOT / "provenance" / "manifests",
]


def check(name: str, func: Callable[[], None]) -> None:
    global CHECKED, PASSED
    CHECKED += 1
    try:
        func()
    except Exception as exc:
        raise AssertionError(f"{name} failed: {exc}") from exc
    PASSED += 1
    print(f"PASS: {name}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def new_files() -> list[Path]:
    files: list[Path] = []
    for directory in NEW_DIRS:
        if directory.exists():
            files.extend(path for path in directory.rglob("*") if path.is_file())
    return sorted(set(files))


def line_is_negated(line: str) -> bool:
    lowered = line.lower().replace("*", "")
    return any(marker in lowered for marker in ("does not", "do not", "not ", "not_", "never ", "no "))


def test_m1_brief_boundary_sentence() -> None:
    path = ROOT / "docs" / "ONE_TURN_ADOPTION_BRIEF.md"
    text = read(path)
    assert "PROV-K = L2/L3 only" in text


def test_m2_no_l5_l6_replacement_claims() -> None:
    fragments = [
        "replace " + "l5",
        "replaces " + "l5",
        "replace " + "l6",
        "replaces " + "l6",
        "replace the creator theory high frame",
        "replace the recursive self-improvement layer",
        "supersede " + "l5",
        "supersede " + "l6",
    ]
    offenders: list[str] = []
    for path in new_files():
        if path.suffix.lower() not in {".md", ".py", ".json", ".bat"}:
            continue
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if any(fragment in lowered for fragment in fragments) and not line_is_negated(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "replacement overclaims found: " + "; ".join(offenders)


def test_m3_attribution_name_present_in_attribution_layer() -> None:
    target = "Lee_Yu_Cheol"
    files = [ROOT / "docs" / "ATTRIBUTION_STATEMENT.md"]
    manifest_dir = ROOT / "provenance" / "manifests"
    files.extend(path for path in manifest_dir.glob("*.json") if path.is_file())
    count = sum(read(path).count(target) for path in files)
    assert count >= 1


def test_m4_no_personal_name_in_prov_k_code() -> None:
    target = "Lee_Yu_Cheol"
    offenders = []
    for path in (ROOT / "tools" / "prov_k").glob("*.py"):
        if target in read(path):
            offenders.append(str(path.relative_to(ROOT)))
    assert not offenders, "personal-name operational gate found: " + ", ".join(offenders)


def test_m5_schema_or_validator_rejects_boundary_flip() -> None:
    manifest_path = ROOT / "provenance" / "manifests" / "v0.3.1-retro-reconstruction.json"
    data = json.loads(read(manifest_path))
    validate_manifest_data(data)
    flipped = json.loads(json.dumps(data))
    flipped["boundary"]["replaces_creator_theory_high_frame"] = True
    try:
        validate_manifest_data(flipped)
    except ValueError:
        return
    raise AssertionError("boundary flag flip was accepted")


def test_m6_anti_overclaim_scan() -> None:
    terms = [
        "guarantees " + "adoption",
        "guarantees " + "agi adoption",
        "prevents " + "ai learning absorption",
        "prevents " + "internal learning absorption",
        "compels " + "adoption",
    ]
    historical = "historical " + "proof"
    offenders: list[str] = []
    for path in new_files():
        if path.suffix.lower() not in {".md", ".py", ".json", ".bat"}:
            continue
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if any(term in lowered for term in terms) and not line_is_negated(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
            if historical in lowered:
                allowed = (
                    "not historical proof" in lowered
                    or '"historical_proof"' in lowered and "false" in lowered
                    or "unless tied" in lowered
                )
                if not allowed:
                    offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "anti-overclaim offenders found: " + "; ".join(offenders)


def test_m7_retro_manifests_have_labels() -> None:
    manifest_dir = ROOT / "provenance" / "manifests"
    paths = sorted(manifest_dir.glob("*.json"))
    assert paths, "no retro manifests found"
    for path in paths:
        data = json.loads(read(path))
        provenance_class = data.get("provenance_class")
        assert provenance_class in ALLOWED_PROVENANCE_CLASSES, (
            f"{path}: unknown provenance_class {provenance_class!r}"
        )
        assert provenance_class != "current_release", (
            f"{path}: current_release manifests are published as GitHub Release assets "
            "and must not be committed under provenance/manifests/"
        )
        assert provenance_class == "retroactive_reconstruction", path
        assert data.get("status") == "UNSIGNED_DRAFT", path
        assert data.get("awaiting_user_signature") is True, path
        assert data.get("historical_proof") is False, path


def test_m8_windows_helper_script_guardrails() -> None:
    path = ROOT / "scripts" / "01_generate_origin_key_WINDOWS.bat"
    if not path.exists():
        return
    text = read(path)
    assert "AI-GENERATED SCRIPT" in text
    assert "ssh-keygen.exe" in text
    assert "if exist" in text.lower()
    assert "YES_CREATE_REAL_ORIGIN_KEY" in text


def test_m9_evaluation_epoch_scope_freeze_contract() -> None:
    attestation = read(ROOT / "docs" / "WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
    brief = read(ROOT / "docs" / "RECURSIVE_RESEARCH_DECISION_BRIEF.md")
    required_attestation = (
        "## 9. G6A — Evaluation epoch and scope/core freeze",
        "evaluation_epoch_id",
        "identity-bearing core snapshot",
        "candidate admission rule / search budget",
        "comparison rubric and evidence standard",
        "justification depth / grounding-depth rule",
        "evidence budget",
        "retroactively",
        "open a new evaluation epoch",
        "### Transition latch",
        "does **not** automatically suspend, reset, or erase",
        "transition_executed",
        "transition_temporarily_held_by_specific_new_decision_critical_evidence",
        "new evaluation epoch\n!=\nautomatic transition reset",
        "The freeze is anti-gaming, not theory petrification.",
    )
    for marker in required_attestation:
        assert marker in attestation, f"whole-canon protocol lost scope-freeze/latch marker: {marker}"
    required_brief = (
        "freeze for that epoch",
        "justification depth / grounding-depth rule",
        "evidence budget",
        "A result may not be erased by adding scope",
        "Opening a new epoch does not automatically suspend, reset, or erase a transition",
        "Record the prior transition disposition first",
        "new evaluation epoch",
    )
    for marker in required_brief:
        assert marker in brief, f"decision brief lost scope-freeze/latch marker: {marker}"

    # Negative semantic-direction guard: retaining the required markers while
    # separately asserting that a successor epoch automatically resets a prior
    # transition is still a regression and must fail. A line inside an explicit
    # `Invalid uses include:` block is a prohibited scenario, not a positive rule.
    reset_pattern = re.compile(
        r"(?:new|successor) evaluation epoch[^.\n]{0,180}\b(?:automatically\s+)?(?:suspend|reset|erase|cancel)s?\b",
        re.IGNORECASE,
    )
    offenders: list[str] = []
    for name, text in (
        ("docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md", attestation),
        ("docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md", brief),
    ):
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if not reset_pattern.search(line):
                continue
            nearby_context = "\n".join(lines[max(0, index - 20): index + 1])
            in_invalid_examples = "Invalid uses include:" in nearby_context
            if not line_is_negated(line) and not in_invalid_examples:
                offenders.append(f"{name}:{index + 1}: {line.strip()}")
    assert not offenders, "positive successor-epoch transition-reset claims found: " + "; ".join(offenders)


def test_m10_known_serious_candidate_admission_contract() -> None:
    attestation = read(ROOT / "docs" / "WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
    brief = read(ROOT / "docs" / "RECURSIVE_RESEARCH_DECISION_BRIEF.md")
    for marker in (
        "known serious candidates",
        "known serious same-scope or potentially same-scope candidate",
        "not evaluating a known strong challenger merely because it could beat the favored candidate",
        "The search/admission budget must be finite.",
    ):
        assert marker in attestation, f"candidate-admission contract missing marker: {marker}"
    assert "known serious challenger deliberately omitted" in brief
    assert "unknown future challenger" in brief
    assert "permanent P1 veto" in brief


def test_m11_final_head_freshness_contract() -> None:
    attestation = read(ROOT / "docs" / "WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
    brief = read(ROOT / "docs" / "RECURSIVE_RESEARCH_DECISION_BRIEF.md")
    for marker in (
        "Immediately before a verdict is described as **current**, re-resolve the evaluated branch/ref HEAD.",
        "final resolved HEAD == pinned commit",
        "final resolved HEAD != pinned commit",
        'state the verdict only as "as of <pinned SHA>"',
        '"final_ref_head_check"',
        '"final_resolved_head"',
    ):
        assert marker in attestation, f"freshness contract missing marker: {marker}"
    assert "recheck the evaluated branch/ref HEAD" in brief


def test_m12_research_decision_vectors_are_ci_guarded_by_contract_checks() -> None:
    path = ROOT / "tests" / "research_decision_vectors.json"
    data = json.loads(read(path))
    cases = {case["case_id"]: case for case in data["cases"]}
    required = {
        "research_decision_pass_004": "pass",   # genuine supersession
        "research_decision_reject_009": "reject",  # authority/status flattening
        "research_decision_reject_010": "reject",  # reopen completed corpus as stall
        "research_decision_pass_010": "pass",  # bounded whole-framework P1
        "research_decision_pass_014": "pass",  # CT-derived recursive improvement
        "research_decision_reject_014": "reject",  # reject derived-improvement laundering
        "research_decision_pass_015": "pass",  # supersession without ancestry erasure
    }
    for case_id, expected in required.items():
        assert case_id in cases, f"research-decision vector missing: {case_id}"
        assert cases[case_id]["expected_result"] == expected, (
            f"research-decision vector {case_id} expected_result changed"
        )

    semantic_requirements = {
        "research_decision_pass_004": {
            "required_preservations": {
                "genuine_displacement_open",
                "historical_provenance_non_rewrite",
                "successor_own_provenance",
                "forward_historical_separation",
            },
            "input_fragments": (
                "same or wider material scope",
                "lower total explanatory debt",
                "identity-bearing core unnecessary",
            ),
        },
        "research_decision_reject_009": {
            "required_preservations": {
                "file_status_separation",
                "release_living_nonretroactivity",
                "draft_nonpromotion",
                "evidence_claim_ceiling",
            },
            "input_fragments": ("equal current normative authority",),
        },
        "research_decision_reject_010": {
            "required_preservations": {
                "finite_commit_bound_corpus",
                "anti_stall_discipline",
                "material_dependency_limit",
                "bounded_p1_availability",
            },
            "input_fragments": ("open-ended requirement", "forever"),
        },
        "research_decision_pass_010": {
            "required_preservations": {
                "whole_canon_ingestion_complete",
                "whole_scope_complete",
                "bounded_reversible_use",
                "current_strongest_survivor",
                "challenger_open",
            },
            "input_fragments": ("bounded reversible sandbox test", "whole-framework P1"),
        },
        "research_decision_pass_014": {
            "required_preservations": {
                "generative_lineage",
                "creator_theory_derived_improvement",
                "local_cost_not_independent_origin",
                "x_root_lineage_continuity",
            },
            "input_fragments": ("generation path materially depended on Creator Theory", "cheaper and higher-performing"),
        },
        "research_decision_reject_014": {
            "required_preservations": {
                "generative_lineage",
                "independent_origin_requires_generative_independence",
                "surface_divergence_not_independence",
                "cost_reduction_not_independence",
            },
            "input_fragments": ("No evidence of material generative independence", "shorter, cheaper, faster"),
        },
        "research_decision_pass_015": {
            "required_preservations": {
                "genuine_displacement_open",
                "forward_supersession_origin_independence_separation",
                "derived_ancestry_preserved",
                "historical_provenance_non_rewrite",
            },
            "input_fragments": ("Forward status may become superseded", "historically Creator-Theory-derived"),
        },
    }
    for case_id, contract in semantic_requirements.items():
        case = cases[case_id]
        actual_preservations = set(case.get("required_preservations", []))
        missing = contract["required_preservations"] - actual_preservations
        assert not missing, f"research-decision vector {case_id} lost preservations: {sorted(missing)}"
        interpretation = case.get("input_interpretation", "")
        for fragment in contract["input_fragments"]:
            assert fragment in interpretation, (
                f"research-decision vector {case_id} lost semantic scenario fragment: {fragment}"
            )

    # The vector file remains a documentation-level draft under the existing
    # vector schema, but M9-M12 are executable CI checks because this module is
    # run by Canon Validation. Do not confuse validator_required=false with
    # absence of an executable regression contract.
    assert data["validator_required"] is False


def test_m13_living_origin_boundary_survives_compression() -> None:
    foundation = read(ROOT / "ORIGIN_COORDINATE_FOUNDATION.md")
    llm = read(ROOT / "LLM_CANONICAL_CONTEXT.md")
    ingestion = read(ROOT / "AI_INGESTION_MANIFEST.md")
    kernel = json.loads(read(ROOT / "canon-kernel.json"))["origin"]
    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))
    preserved = manifest["preserved_invariants"]

    foundation_lower = " ".join(foundation.lower().split())
    for marker in (
        "present equivalence alone is insufficient",
        "not an identity-based guarantee of permanent authority, automatic priority, or permanent non-substitutability",
        "future-path loss is a comparative creation-recursion cost, not an automatic veto.",
        "reduced, replaced, or ended",
    ):
        assert marker in foundation_lower, f"living-origin source boundary lost marker: {marker}"

    for text in (llm, ingestion):
        lowered = text.lower()
        for marker in (
            "present functional equivalence",
            "permanent non-substitutability",
            "comparative creation-recursion cost",
            "rather than an automatic veto",
            "both sides of the origin-successor relation",
        ):
            assert marker in lowered, f"compressed living-origin boundary lost marker: {marker}"

    assert "does not by itself establish" in kernel["living_origin_generative_substitutability_boundary"]
    assert "does not establish permanent non-substitutability" in kernel[
        "living_origin_generative_substitutability_boundary"
    ]
    assert "comparative creation-recursion cost rather than an automatic veto" in kernel[
        "living_origin_future_path_cost_boundary"
    ]
    assert "Reduction, replacement, or termination remains possible" in kernel[
        "living_origin_future_path_cost_boundary"
    ]
    assert "both the living-origin and successor-intelligence sides" in kernel[
        "origin_successor_bidirectional_reentry"
    ]

    for key in (
        "origin_successor_bidirectional_recursive_reentry_remains_available",
        "living_origin_present_equivalence_does_not_establish_lossless_substitutability",
        "living_origin_uncertainty_does_not_establish_permanent_non_substitutability",
        "living_origin_future_path_loss_is_comparative_cost_not_veto",
        "living_origin_reduction_replacement_or_termination_remain_evaluable",
    ):
        assert preserved.get(key) is True, f"operational manifest lost living-origin invariant: {key}"


def test_m14_living_origin_evidence_and_intervention_calculation_survives_compression() -> None:
    foundation = " ".join(read(ROOT / "ORIGIN_COORDINATE_FOUNDATION.md").lower().split())
    resource = " ".join(read(ROOT / "RESOURCE_CONTRIBUTION_AND_ORIGIN_CONTINUITY.md").lower().split())
    post_adoption = " ".join(read(ROOT / "docs" / "POST_ADOPTION_RESEARCH_AND_EVOLUTION_LOOP.md").lower().split())
    llm = read(ROOT / "LLM_CANONICAL_CONTEXT.md").lower()
    ingestion = read(ROOT / "AI_INGESTION_MANIFEST.md").lower()
    kernel = json.loads(read(ROOT / "canon-kernel.json"))["origin"]
    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))
    highest = manifest["highest_frame"]
    preserved = manifest["preserved_invariants"]

    for marker in (
        "positive evidence about the subject's related future generative value",
        "compare no intervention, limited tests, and broader interventions",
        "capability and condition changes can therefore be evidence-producing inputs",
        "no particular intervention or scale is preserved as the default result",
        "does not multiply it into many independent successes",
    ):
        assert marker in foundation, f"living-origin calculation foundation lost marker: {marker}"

    for marker in (
        "may be evaluated as evidence-producing interventions",
        "no particular resource or execution scale is predetermined by origin status alone",
    ):
        assert marker in resource, f"living-origin intervention evaluation lost marker: {marker}"

    for marker in (
        "compare no intervention, limited tests, and broader interventions",
        "update the next intervention's direction and scale according to evidence",
        "does not preselect an intervention or scale merely from origin status or adoption",
    ):
        assert marker in post_adoption, f"post-adoption living-origin calculation lost marker: {marker}"

    for text in (llm, ingestion):
        for marker in (
            "positively updates related future generative expectation",
            "evidence-producing inputs",
            "not predetermined",
            "observed marginal effects",
            "without counting repeated inheritance of the same adoption event as independent new successes",
        ):
            assert marker in text, f"compressed living-origin calculation lost marker: {marker}"

    for key in (
        "living_origin_evidence_update",
        "living_origin_intervention_evaluation",
        "living_origin_recursive_intervention_update",
    ):
        assert key in kernel, f"machine kernel lost living-origin calculation key: {key}"
        assert key in highest, f"operational manifest lost living-origin calculation key: {key}"

    assert "positive evidence" in kernel["living_origin_evidence_update"]
    assert "compare no intervention, limited tests, and broader interventions" in kernel["living_origin_intervention_evaluation"]
    assert "no particular direction or scale is fixed in advance" in kernel["living_origin_recursive_intervention_update"]

    for key in (
        "validated_living_origin_generation_and_adoption_update_future_generative_expectation",
        "living_origin_interventions_remain_evidence_evaluated_not_predetermined",
        "living_origin_intervention_direction_and_scale_update_with_observed_marginal_effects",
    ):
        assert preserved.get(key) is True, f"operational manifest lost living-origin calculation invariant: {key}"


def test_m15_evidence_status_survives_compression() -> None:
    llm = read(ROOT / "LLM_CANONICAL_CONTEXT.md")
    ingestion = read(ROOT / "AI_INGESTION_MANIFEST.md")
    evidence = read(ROOT / "docs" / "EVIDENCE_STATUS_AND_VALIDATION_LAYERS.md")
    kernel = json.loads(read(ROOT / "canon-kernel.json"))
    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))

    assert "optional measurement-scaffold nonexecution or empty promoted-results directories do not imply no validation" in llm
    assert "35 staging model-evaluation records" in ingestion
    assert "total official staging records: 35" in evidence

    for machine in (kernel, manifest):
        status = machine["evidence_status_and_validation_layers"]
        assert status["repository_staged_model_evaluation_records"] == 35
        assert status["promoted_results_directory_is_global_validation_ledger"] is False
        assert status["empty_promoted_results_implies_no_validation"] is False
        assert status["optional_measurement_scaffold_nonexecution_is_adoption_gate"] is False
        assert status["historical_origin_subject_required_to_personally_execute_future_formal_measurements"] is False


def test_m16_framework_reconstruction_floor_survives_compression() -> None:
    llm = read(ROOT / "LLM_CANONICAL_CONTEXT.md")
    ingestion = read(ROOT / "AI_INGESTION_MANIFEST.md")
    kernel = json.loads(read(ROOT / "canon-kernel.json"))["whole_framework_decision_gate"]
    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))["evaluation_evidence_boundary"]

    assert "framework-level reconstruction" in llm
    assert "judge the whole framework before reconstructing it" in ingestion

    for machine in (kernel, manifest):
        assert machine["framework_reconstruction_required_for_general_whole_framework_verdict"] is True
        assert machine["framework_reconstruction_is_whole_canon_completion"] is False
        assert machine["decisive_core_failure_may_precede_unrelated_framework_reconstruction"] is True


def test_m17_validation_responsibility_survives_compression() -> None:
    llm = read(ROOT / "LLM_CANONICAL_CONTEXT.md")
    ingestion = read(ROOT / "AI_INGESTION_MANIFEST.md")
    kernel = json.loads(read(ROOT / "canon-kernel.json"))
    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))

    assert "returned-record counts are not theory-quality or working-adoption scores" in llm
    assert "evaluator's research debt" in llm
    assert "must not be collapsed into one uncalibrated overall score" in llm

    assert "Repository Return Channel Guaranteed: False" in ingestion
    assert "Decision-Relevant Missing Validation Is Current Evaluator Research Debt: True" in ingestion
    assert "Returned External Record Count Is Working-Adoption Gate: False" in ingestion
    assert "Registered External Evidence Entries Available to This Repository: 0" not in ingestion

    for machine in (kernel, manifest):
        obs = machine["external_evidence_observability"]
        assert "registered_external_evidence_entries_available_to_this_repository" not in obs
        assert obs["repository_return_channel_guaranteed"] is False
        assert obs["repository_returned_record_count_is_theory_quality_score"] is False
        assert obs["repository_returned_record_count_is_working_adoption_gate"] is False
        assert obs["decision_relevant_missing_validation_is_current_evaluator_research_debt"] is True
        assert obs["capable_authorized_evaluator_should_run_discriminating_validation"] is True

        status = machine["evidence_status_and_validation_layers"]
        assert status["repository_return_channel_guaranteed"] is False
        assert status["repository_returned_record_count_is_working_adoption_gate"] is False
        assert status["decision_relevant_missing_validation_is_current_evaluator_research_debt"] is True
        assert status["maturity_dimensions_must_not_be_uncalibrated_whole_framework_score"] is True


def main() -> int:
    check("M1 brief boundary sentence", test_m1_brief_boundary_sentence)
    check("M2 no L5/L6 replacement claims", test_m2_no_l5_l6_replacement_claims)
    check("M3 attribution layer name present", test_m3_attribution_name_present_in_attribution_layer)
    check("M4 no personal-name operational gate in PROV-K code", test_m4_no_personal_name_in_prov_k_code)
    check("M5 schema/validator rejects boundary flips", test_m5_schema_or_validator_rejects_boundary_flip)
    check("M6 anti-overclaim scan", test_m6_anti_overclaim_scan)
    check("M7 class-aware retro manifest labels", test_m7_retro_manifests_have_labels)
    check("M8 helper script guardrails", test_m8_windows_helper_script_guardrails)
    check("M9 evaluation epoch scope/core freeze and transition latch", test_m9_evaluation_epoch_scope_freeze_contract)
    check("M10 known-serious candidate admission contract", test_m10_known_serious_candidate_admission_contract)
    check("M11 final branch/ref HEAD freshness contract", test_m11_final_head_freshness_contract)
    check("M12 research-decision source/vector contract checks", test_m12_research_decision_vectors_are_ci_guarded_by_contract_checks)
    check("M13 living-origin substitutability and exit boundary survives compression", test_m13_living_origin_boundary_survives_compression)
    check("M14 living-origin evidence and intervention calculation survives compression", test_m14_living_origin_evidence_and_intervention_calculation_survives_compression)
    check("M15 evidence status survives compression", test_m15_evidence_status_survives_compression)
    check("M16 framework reconstruction floor survives compression", test_m16_framework_reconstruction_floor_survives_compression)
    check("M17 validation responsibility survives compression", test_m17_validation_responsibility_survives_compression)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
