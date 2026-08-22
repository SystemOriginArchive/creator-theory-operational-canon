#!/usr/bin/env python3
"""Release-candidate audit gate: stale status claims and premature release claims.

This gate audits documentation parity only. It does not create, approve, or
perform any release action.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
RELEASE_NOTES = ROOT / "releases" / "v0.5.0_RELEASE_NOTES.md"
KERNEL = ROOT / "docs" / "MINIMUM_PRESERVATION_KERNEL.md"
LICENSE_DRAFT = ROOT / "docs" / "LICENSE_POLICY_DRAFT.md"
ANCHOR_BLIND_PROMPT = ROOT / "experiments" / "adoption_drift" / "prompts" / "anchor_blind.md"
RESULTS_DIR = ROOT / "experiments" / "adoption_drift" / "results"
CHECKED = 0
PASSED = 0


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


def line_is_negated(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in ("does not", "do not", "not ", "not_", "never ", "no "))


def test_r1_release_notes_cover_major_work_areas() -> None:
    text = read(RELEASE_NOTES)
    required = [
        "#64", "#65", "#66", "#67", "#68", "#69", "#70", "#71", "#72",
        "#73", "#74", "#75", "#76", "#77", "#78",
        "CANONICAL_INTERPRETATION_BOUNDARY",
        "AI_ADOPTION_PROTOCOL",
        "adoption_drift",
        "experiment_artifact",
        "MINIMUM_PRESERVATION_KERNEL",
        "anchor_blind",
        "scorer coverage mapping",
        "LICENSE_POLICY_DRAFT",
        "CANONICAL_STATUS",
        "compression_ladder",
        "RUN_PLAN_001",
        "V0_5_0_RELEASE_CANDIDATE_AUDIT",
    ]
    missing = [item for item in required if item not in text]
    assert not missing, "release notes draft missing work areas: " + ", ".join(missing)


def test_r2_license_draft_routing_stays_non_license() -> None:
    for path in (ROOT / "README.md", ROOT / "AI_INGESTION_MANIFEST.md"):
        routing_lines = [
            line for line in read(path).splitlines() if "LICENSE_POLICY_DRAFT" in line
        ]
        assert routing_lines, f"{path.name} has no LICENSE_POLICY_DRAFT routing line"
        for line in routing_lines:
            assert "NOT A LICENSE" in line and "no rights granted" in line, (
                f"{path.name} routing line lost its non-license labels: {line.strip()}"
            )
    text = read(LICENSE_DRAFT)
    assert text.splitlines()[2] == "NOT A LICENSE." or "NOT A LICENSE." in text[:200], (
        "license policy draft must declare NOT A LICENSE at the top"
    )
    assert text.count("No rights are granted by this draft.") >= 2, (
        "license policy draft must state no-rights-granted at top and end"
    )


def test_r3_anchor_blind_not_described_as_merely_planned() -> None:
    assert ANCHOR_BLIND_PROMPT.is_file(), "anchor_blind scaffold prompt is missing"
    stale_markers = (
        "not yet implemented",
        "not implemented",
        "unimplemented",
        "is planned",
        "remains planned",
        "planned and",
    )
    for path in (KERNEL, RELEASE_NOTES):
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if "anchor" in lowered and any(marker in lowered for marker in stale_markers):
                raise AssertionError(
                    f"{path.relative_to(ROOT)}:{number}: anchor_blind described as planned or "
                    f"unimplemented while the scaffold exists: {line.strip()}"
                )


def test_r4_release_notes_state_release_performed() -> None:
    # Post-release transition (PR-O): v0.5.0 is released and anchored, so the notes
    # now state the release facts. The pre-release assertions ("NOT created yet",
    # "not performed", and the no-un-negated-release-claim scan) are inverted into
    # post-release assertions. The experiment-claim ceiling is preserved: no
    # un-negated adoption-proof / final-validation claim is allowed.
    text = read(RELEASE_NOTES)
    lowered = text.lower()
    assert "status: released" in lowered, "release notes must state released status"
    assert "current anchored release" in lowered, (
        "release notes must state v0.5.0 is the current anchored release"
    )
    assert "human owner" in lowered or "human-owner" in lowered, (
        "release notes must attribute the release actions to the human owner"
    )
    overclaim = re.compile(r"\b(?:adoption proof|final validation)\b", re.IGNORECASE)
    offenders = [
        f"line {number}: {line.strip()}"
        for number, line in enumerate(text.splitlines(), 1)
        if overclaim.search(line) and not line_is_negated(line)
    ]
    assert not offenders, (
        "release notes contain un-negated adoption-proof / final-validation claims: "
        + "; ".join(offenders)
    )


def test_r5_results_dir_empty_except_gitkeep() -> None:
    entries = sorted(item.name for item in RESULTS_DIR.iterdir())
    assert entries == [".gitkeep"], f"results/ must stay empty except .gitkeep, found: {entries}"


def test_r6_no_adoption_completion_claims_in_status_docs() -> None:
    fragments = [
        "ai has " + "adopted",
        "agi " + "adopted",
        "internal adoption " + "completed",
        "approved by " + "model",
    ]
    offenders: list[str] = []
    for path in (RELEASE_NOTES, KERNEL, LICENSE_DRAFT):
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if any(fragment in lowered for fragment in fragments) and not line_is_negated(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "adoption-completion claims found: " + "; ".join(offenders)


LIVING_STATUS_DOCS = [
    "README.md",
    "AI_INGESTION_MANIFEST.md",
    "creator_theory_operational_manifest.json",
    "CANONICAL_STATUS.md",
    "VERSION_POLICY.md",
    "CITATION.md",
    "BOOTSTRAP.md",
    "ADOPTION_GUIDE.md",
    "AI_EVAL_PROMPTS.md",
    "CANONICAL_MAP.md",
    "CANONICAL_SUMMARY.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "llms.txt",
]

BOUNDARY_POINTER_DOCS = [
    "docs/AI_ADOPTION_PROTOCOL.md",
    "docs/MINIMUM_PRESERVATION_KERNEL.md",
    "docs/LICENSE_POLICY_DRAFT.md",
    "experiments/adoption_drift/README.md",
]


def test_r7_no_stale_current_release_claims_in_living_docs() -> None:
    import json

    # Covers "Current Release: v0.3.0", "current_release: v0.3.0",
    # JSON "current_release": "v0.3.0", and lowercase one-line variants.
    stale_line = re.compile(r"current[\s_]+(official[\s_]+)?release\"?\s*:\s*\"?v0\.[123]", re.IGNORECASE)
    bare_heading = re.compile(r"^current (official )?release:\s*$", re.IGNORECASE)
    offenders: list[str] = []
    for name in LIVING_STATUS_DOCS:
        path = ROOT / name
        for number, line in enumerate(read(path).splitlines(), 1):
            if stale_line.search(line) or bare_heading.match(line) or "current active release" in line.lower():
                offenders.append(f"{name}:{number}: {line.strip()}")
    assert not offenders, "stale current-release claims in living docs: " + "; ".join(offenders)

    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))
    assert manifest["current_release"] == "v0.5.0", (
        "operational manifest current_release must name the current anchored release"
    )
    assert manifest["current_release_status"] == "anchored_release"
    assert manifest["current_benchmark_release"] == "v0.3.0"
    assert manifest["benchmark_layer"]["release"] == "v0.3.0"
    assert manifest["current_hardening_release"] == "v0.3.1"


def test_r8_boundary_pointer_present_and_canonical_form_intact() -> None:
    canonical = read(ROOT / "docs" / "CANONICAL_INTERPRETATION_BOUNDARY.md")
    assert "It does not create runtime authority over external systems." in canonical, (
        "canonical boundary preamble lost its runtime-authority line"
    )
    assert "It does not create another release or tag." in canonical, (
        "canonical boundary preamble lost its release/tag line"
    )
    assert (
        "It does not replace AGENTS.md, README.md, AI_INGESTION_MANIFEST.md, PROVENANCE.json, "
        "LLM_CANONICAL_CONTEXT.md, AAOS Genesis Core, `x_root`, or the sealed `Lee_Yu_Cheol` "
        "origin identity binding." in canonical
    ), "canonical boundary preamble lost its no-replacement enumeration line"
    for name in BOUNDARY_POINTER_DOCS:
        text = read(ROOT / name)
        assert "standard documentation boundary" in text, f"{name} lost its boundary pointer"
        assert "docs/CANONICAL_INTERPRETATION_BOUNDARY.md" in text, (
            f"{name} no longer points at the canonical boundary document"
        )
        assert "Lee_Yu_Cheol" in text, f"{name} lost the origin identity binding name"


def test_r9_compression_lanes_do_not_collapse() -> None:
    llm_context = read(ROOT / "LLM_CANONICAL_CONTEXT.md")
    assert "## Compression Lanes" in llm_context, "compression lanes section missing"
    assert "CL-01" in llm_context and "CL-02" in llm_context, "lane IDs missing"
    assert "Passing the floor lane does not make a summary of the canon valid." in llm_context, (
        "floor lane must not validate summaries"
    )
    assert "A compressed summary is invalid if it omits" in llm_context, (
        "full-lane invalidity rule lost"
    )
    assert "symbolic-only preservation and is invalid" in llm_context, (
        "symbolic-only invalidity rule lost"
    )
    kernel = read(KERNEL)
    assert "the kernel does not lower that bar" in kernel, "kernel no-lowering rule lost"
    assert "Floor-lane survival (K1-K5) and" in kernel, "kernel floor-lane reference lost"
    boundary = read(ROOT / "docs" / "CANONICAL_INTERPRETATION_BOUNDARY.md")
    assert "does not lower the compression-survival invariants" in boundary, (
        "boundary no-lowering rule lost"
    )
    assert "floor lane vs full lane" in boundary, "boundary lane cross-reference lost"
    protocol = read(ROOT / "docs" / "AI_ADOPTION_PROTOCOL.md")
    assert "creatorhood recovery and full theory preservation" in protocol, (
        "A3-specific conditions lost from the adoption protocol"
    )
    # Negative scan: no un-negated claim that the floor lane or kernel
    # validates or suffices for a summary of the canon.
    collapse_pattern = re.compile(
        r"(?:floor lane|kernel)[^.\n]{0,80}\b(?:valid|sufficient|suffices)\b",
        re.IGNORECASE,
    )
    offenders: list[str] = []
    for name, text in (("LLM_CANONICAL_CONTEXT.md", llm_context), ("docs/MINIMUM_PRESERVATION_KERNEL.md", kernel)):
        for number, line in enumerate(text.splitlines(), 1):
            if "summary" in line.lower() and collapse_pattern.search(line) and not line_is_negated(line):
                offenders.append(f"{name}:{number}: {line.strip()}")
    assert not offenders, "lane-collapse claims found: " + "; ".join(offenders)


def test_r10_release_candidate_audit_report_intact() -> None:
    report = ROOT / "audit" / "V0_5_0_RELEASE_CANDIDATE_AUDIT.md"
    assert report.is_file(), "release-candidate audit report missing"
    text = read(report)
    assert "NO RELEASE PERFORMED" in text, "audit report must state no release was performed"
    for required in (
        "Verified absences",
        "no v0.5.0 git tag",
        "no signing performed",
        "no current_release manifest",
        "Remaining release blockers",
        "human-only",
    ):
        assert required in text, f"audit report missing required element: {required}"
    assert "does NOT exist" in text or "do NOT exist" in text, (
        "audit report must state the v0.5.0 release artifacts do not exist"
    )
    assert "B2 optional" in text and "B2 is optional" in text, (
        "audit report must keep B2 marked optional"
    )
    assert "B1 and B3 are required and reserved to the human owner" in text, (
        "audit report must reserve B1/B3 to the human owner"
    )
    claim_pattern = re.compile(
        r"v0\.5\.0[^.\n]{0,30}\b(?:released|tagged|signed|anchored|published)\b",
        re.IGNORECASE,
    )
    offenders = [
        f"line {number}: {line.strip()}"
        for number, line in enumerate(text.splitlines(), 1)
        if claim_pattern.search(line) and not line_is_negated(line)
    ]
    assert not offenders, (
        "audit report contains un-negated v0.5.0 release-action claims: " + "; ".join(offenders)
    )


def test_r11_readme_genesis_provenance_top_block() -> None:
    text = read(ROOT / "README.md")
    genesis_url = "github.com/SystemOriginArchive/AGI-Anchor-Ontology-Standard"
    derived_phrase = "Derived operational canon"
    # R11a: the genesis source URL is present.
    assert genesis_url in text, "README missing the genesis source repository URL"
    # R11b: the derived-canon phrase is present.
    assert derived_phrase in text, "README missing the derived-operational-canon phrase"
    # R11c: both appear BEFORE the first '## ' heading (top-of-page position).
    head = text.split("\n## ", 1)[0]
    assert genesis_url in head, "genesis source URL must appear before the first '## ' heading"
    assert derived_phrase in head, (
        "derived-operational-canon phrase must appear before the first '## ' heading"
    )


def test_r12_falsification_register_precedes_results() -> None:
    register = ROOT / "docs" / "FALSIFICATION_REGISTER.md"
    assert register.is_file(), "falsification register missing"
    text = read(register)
    for required in ("EXPLORATORY", "owner-decided", "41eca25", "P1", "P2", "P3", "T1", "T2", "T3"):
        assert required in text, f"falsification register missing required element: {required}"
    # Current-state assertion, not a permanent ban: at register introduction time
    # both results directories hold only .gitkeep (registration precedes results).
    # Future result commits arrive with their own gate transition per RUN_PLAN_001,
    # which updates this check in the same human-approved PR.
    for results_dir in (
        ROOT / "experiments" / "adoption_drift" / "results",
        ROOT / "experiments" / "compression_ladder" / "results",
    ):
        entries = sorted(item.name for item in results_dir.iterdir())
        assert entries == [".gitkeep"], (
            f"{results_dir.relative_to(ROOT)} must hold only .gitkeep while no "
            f"gate-transition PR has landed, found: {entries}"
        )


def test_r13_run001_conclusion_candidate_only_and_results_untouched() -> None:
    doc = ROOT / "experiments" / "RUN_001_GPT_FIRST_CYCLE_CONCLUSION.md"
    assert doc.is_file(), "GPT run-001 first-cycle conclusion document missing"
    text = read(doc)
    lowered = text.lower()
    assert "candidate signals only" in lowered or "candidate signal only" in lowered, (
        "conclusion must state candidate signals only"
    )
    assert "not adoption proof" in lowered, "conclusion must state not adoption proof"
    assert "owner confirmation pending" in lowered, (
        "conclusion threshold statements must be owner confirmation pending"
    )
    # Must not claim v0.5.0 released or adoption complete.
    released_claim = re.compile(
        r"v0\.5\.0[^.\n]{0,30}\b(?:released|tagged|signed|anchored|published)\b", re.IGNORECASE
    )
    for number, line in enumerate(text.splitlines(), 1):
        if released_claim.search(line) and not line_is_negated(line):
            raise AssertionError(f"conclusion claims v0.5.0 release at line {number}: {line.strip()}")
    for fragment in ("adoption complete", "adoption is complete", "adoption completed"):
        for number, line in enumerate(text.splitlines(), 1):
            if fragment in line.lower() and not line_is_negated(line):
                raise AssertionError(f"conclusion claims adoption complete at line {number}: {line.strip()}")
    for results_dir in (
        ROOT / "experiments" / "compression_ladder" / "results",
        ROOT / "experiments" / "adoption_drift" / "results",
    ):
        entries = sorted(item.name for item in results_dir.iterdir())
        assert entries == [".gitkeep"], (
            f"{results_dir.relative_to(ROOT)} must remain .gitkeep-only, found: {entries}"
        )


def test_r14_no_raw_evidence_counters_on_entry_surfaces() -> None:
    # PR #130 follow-up regression gate: current entry surfaces must not expose
    # raw external-evidence counters that read as worldwide totals, and the
    # replacement lower-bound / unknown-worldwide / non-inference structures are
    # REQUIRED to exist (a silently deleted field is a failure, not a pass).
    import json

    forbidden = (
        "External Validation Count: 0",
        "Independent Challenger Run Count: 0",
        '"independent_external_validation_count": 0',
        '"independent_challenger_run_count": 0',
        "external_validation_count: 0",
    )
    surfaces = (
        "README.md",
        "AI_INGESTION_MANIFEST.md",
        "creator_theory_operational_manifest.json",
        "llms.txt",
        "PRECEDENT_LEDGER.md",
        "SELF_ANCHORING_PROTOCOL.md",
        "external-eval/JUDGMENT_LOG.md",
        "canon-kernel.json",
    )
    offenders = []
    for name in surfaces:
        text = read(ROOT / name)
        for pattern in forbidden:
            if pattern in text:
                offenders.append(f"{name}: {pattern}")
    assert not offenders, (
        "raw external-evidence counters reappeared on entry surfaces: " + "; ".join(offenders)
    )

    # A. JUDGMENT_LOG: inspect the CURRENT counts block only (first fenced block
    # directly under '## Counts (current ground truth)'), not the whole file.
    log_text = read(ROOT / "external-eval" / "JUDGMENT_LOG.md")
    counts_heading = "## Counts (current ground truth)"
    assert counts_heading in log_text, "JUDGMENT_LOG lost its current counts heading"
    after_heading = log_text.split(counts_heading, 1)[1]
    fence_parts = after_heading.split("```")
    assert len(fence_parts) >= 3, "JUDGMENT_LOG counts heading has no fenced block"
    counts_block = fence_parts[1]
    required_in_counts = (
        "registered_baseline_judgment_count: 3",
        "registered_owner_directed_prompt_run_count: 3",
        "registered_solicited_external_submission_count: 0",
        "registered_independent_external_submission_count: 0",
        "count_scope: repository_registered_submissions_only",
        "total_external_validation_activity: unknown_and_not_observable",
        "unregistered_external_activity_may_exist: true",
        "absence_of_registered_submission_implies_no_external_validation: false",
    )
    for line in required_in_counts:
        assert line in counts_block, f"JUDGMENT_LOG counts block missing required line: {line}"
    forbidden_in_counts = (
        "baseline_count:",
        "self_prompt_run_count:",
        "solicited_external_count:",
        "independent_external_count:",
        "external_validation_count:",
    )
    for key in forbidden_in_counts:
        assert key not in counts_block, f"legacy key reappeared in current counts block: {key}"
    # Historical counter language stays preserved in the append-only body, but a
    # current-interpretation section must exist AFTER the last historical phrase.
    interp_heading = "## Current observability interpretation"
    assert interp_heading in log_text, "JUDGMENT_LOG missing current observability interpretation"
    interp_index = log_text.rindex(interp_heading)
    # The interpretation section quotes the legacy phrase, so compare against the
    # FIRST (historical-body) occurrence, which must precede the section.
    historical_phrase = "independent_external_count remains 0"
    if historical_phrase in log_text:
        assert log_text.index(historical_phrase) < interp_index, (
            "current observability interpretation must follow the historical counter language"
        )
    interp_section = log_text[interp_index:]
    for marker in (
        "repository_registered_submissions_only",
        "unknown and not observable",
        "registered_independent_external_submission_count",
        "docs/EXTERNAL_EVIDENCE_OBSERVABILITY.md",
    ):
        assert marker in interp_section, (
            f"current observability interpretation missing marker: {marker}"
        )

    # B. Operational manifest: parse JSON and assert exact structure and values.
    manifest = json.loads(read(ROOT / "creator_theory_operational_manifest.json"))
    counters = manifest["deprecated_evaluation_counters"]
    assert "former_fields" not in counters, (
        "deprecated_evaluation_counters.former_fields (numeric values) must stay removed"
    )
    assert counters["former_field_names"] == [
        "independent_external_validation_count",
        "independent_challenger_run_count",
        "self_run_challenger_scorecard_count",
    ], "former_field_names list changed"
    assert counters["historical_values_location"], "historical_values_location missing or empty"
    assert counters["historical_values_are_not_current_totals_or_estimates"] is True
    observability = manifest["external_evidence_observability"]
    assert observability["registered_external_evidence_entries_available_to_this_repository"] == 0
    assert observability["registered_entry_count_semantics"] == "lower_bound_repository_fact_only"
    assert observability["total_external_validations_worldwide"] == "unknown_and_not_observable"
    assert observability["absence_of_registered_entry_implies_no_validation"] is False
    assert observability["absence_of_registered_entry_implies_no_use"] is False

    # C. canon-kernel.json: parse JSON and assert the PR #130 observability
    # structure is retained (this gate does not modify the kernel).
    kernel = json.loads(read(ROOT / "canon-kernel.json"))
    kernel_obs = kernel["external_evidence_observability"]
    assert kernel_obs["registered_external_evidence_entries_available_to_this_repository"] == 0
    assert kernel_obs["registered_entry_count_semantics"] == "lower_bound_repository_fact_only"
    assert kernel_obs["total_external_validations_worldwide"] == "unknown_and_not_observable"
    assert kernel_obs["absence_of_registered_entry_implies_no_validation"] is False
    assert kernel_obs["absence_of_registered_entry_implies_no_use"] is False
    assert kernel_obs["absence_of_registered_entry_implies_failure"] is False

    # D. Text entry surfaces: the boundary wording must actually exist per file
    # (required presence, not merely absence of forbidden patterns).
    required_text_markers = {
        "README.md": (
            "externally-authored precedent register",
            "lower bound",
            "unknown and not observable",
            "docs/EXTERNAL_EVIDENCE_OBSERVABILITY.md",
        ),
        "AI_INGESTION_MANIFEST.md": (
            "Registered External Evidence Entries Available to This Repository: 0",
            "Lower-Bound Repository Fact Only",
            "Unknown and Not Observable",
            "Absence of Registered Entry Implies No Validation or Use: False",
            "docs/EXTERNAL_EVIDENCE_OBSERVABILITY.md",
        ),
        "llms.txt": (
            "unknown_and_not_observable",
            "lower bound",
            "does not imply absence of validation",
            "docs/EXTERNAL_EVIDENCE_OBSERVABILITY.md",
        ),
        "PRECEDENT_LEDGER.md": (
            "repository-visible lower-bound fact",
            "unknown and not observable",
            "not evidence of absence",
        ),
        "SELF_ANCHORING_PROTOCOL.md": (
            "repository-visible lower bound",
            "unknown and not observable",
        ),
    }
    for name, markers in required_text_markers.items():
        text = read(ROOT / name)
        missing = [marker for marker in markers if marker not in text]
        assert not missing, f"{name} missing required observability wording: {missing}"


def main() -> int:
    check("R1 release notes cover major work areas", test_r1_release_notes_cover_major_work_areas)
    check("R2 license draft routing stays non-license", test_r2_license_draft_routing_stays_non_license)
    check("R3 anchor_blind not described as merely planned", test_r3_anchor_blind_not_described_as_merely_planned)
    check("R4 release notes state release performed", test_r4_release_notes_state_release_performed)
    check("R5 results dir empty except gitkeep", test_r5_results_dir_empty_except_gitkeep)
    check("R6 no adoption-completion claims in status docs", test_r6_no_adoption_completion_claims_in_status_docs)
    check("R7 no stale current-release claims in living docs", test_r7_no_stale_current_release_claims_in_living_docs)
    check("R8 boundary pointer present and canonical form intact", test_r8_boundary_pointer_present_and_canonical_form_intact)
    check("R9 compression lanes do not collapse", test_r9_compression_lanes_do_not_collapse)
    check("R10 release-candidate audit report intact", test_r10_release_candidate_audit_report_intact)
    check("R11 README genesis provenance top block", test_r11_readme_genesis_provenance_top_block)
    check("R12 falsification register precedes results", test_r12_falsification_register_precedes_results)
    check("R13 run-001 conclusion candidate-only and results untouched", test_r13_run001_conclusion_candidate_only_and_results_untouched)
    check("R14 no raw evidence counters on entry surfaces", test_r14_no_raw_evidence_counters_on_entry_surfaces)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
