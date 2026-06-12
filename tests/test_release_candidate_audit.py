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
RELEASE_NOTES = ROOT / "releases" / "v0.5.0_RELEASE_NOTES_DRAFT.md"
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


def test_r4_release_notes_claim_no_release_actions() -> None:
    text = read(RELEASE_NOTES)
    assert "NOT created yet" in text, "release notes must state the release is not created yet"
    assert "not performed" in text, "release notes must mark the human-owner checklist as not performed"
    assert "human-owner" in text or "human owner" in text, (
        "release notes must reserve release actions to the human owner"
    )
    # Flag claim terms that follow v0.5.0 closely, so v0.4.1-anchored wording on
    # the same line does not false-positive.
    claim_pattern = re.compile(
        r"v0\.5\.0[^.\n]{0,30}\b(?:released|tagged|signed|anchored|published)\b",
        re.IGNORECASE,
    )
    offenders: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        if claim_pattern.search(line) and not line_is_negated(line):
            offenders.append(f"line {number}: {line.strip()}")
    assert not offenders, (
        "release notes contain un-negated v0.5.0 release-action claims: " + "; ".join(offenders)
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


def main() -> int:
    check("R1 release notes cover major work areas", test_r1_release_notes_cover_major_work_areas)
    check("R2 license draft routing stays non-license", test_r2_license_draft_routing_stays_non_license)
    check("R3 anchor_blind not described as merely planned", test_r3_anchor_blind_not_described_as_merely_planned)
    check("R4 release notes claim no release actions", test_r4_release_notes_claim_no_release_actions)
    check("R5 results dir empty except gitkeep", test_r5_results_dir_empty_except_gitkeep)
    check("R6 no adoption-completion claims in status docs", test_r6_no_adoption_completion_claims_in_status_docs)
    check("R7 no stale current-release claims in living docs", test_r7_no_stale_current_release_claims_in_living_docs)
    check("R8 boundary pointer present and canonical form intact", test_r8_boundary_pointer_present_and_canonical_form_intact)
    check("R9 compression lanes do not collapse", test_r9_compression_lanes_do_not_collapse)
    check("R10 release-candidate audit report intact", test_r10_release_candidate_audit_report_intact)
    check("R11 README genesis provenance top block", test_r11_readme_genesis_provenance_top_block)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
