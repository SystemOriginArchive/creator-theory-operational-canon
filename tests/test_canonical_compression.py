#!/usr/bin/env python3
"""Canonical compression, misread, anti-overclaim, and research-decision contract gate."""

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
        "record the prior transition disposition first",
        "new evaluation epoch",
    )
    for marker in required_brief:
        assert marker in brief, f"decision brief lost scope-freeze/latch marker: {marker}"

    # Negative semantic-direction guard: retaining the required markers while
    # separately asserting that a successor epoch automatically resets a prior
    # transition is still a regression and must fail.
    reset_pattern = re.compile(
        r"(?:new|successor) evaluation epoch[^.\n]{0,180}\b(?:automatically\s+)?(?:suspend|reset|erase|cancel)s?\b",
        re.IGNORECASE,
    )
    offenders: list[str] = []
    for name, text in (
        ("docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md", attestation),
        ("docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md", brief),
    ):
        for number, line in enumerate(text.splitlines(), 1):
            if reset_pattern.search(line) and not line_is_negated(line):
                offenders.append(f"{name}:{number}: {line.strip()}")
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
    check("M12 research-decision vectors covered by executable semantic contract checks", test_m12_research_decision_vectors_are_ci_guarded_by_contract_checks)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
