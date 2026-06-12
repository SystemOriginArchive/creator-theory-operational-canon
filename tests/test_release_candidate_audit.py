#!/usr/bin/env python3
"""Release-candidate audit gate: stale status claims and premature release claims.

This gate audits documentation parity only. It does not create, approve, or
perform any release action.
"""

from __future__ import annotations

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
        "CANONICAL_INTERPRETATION_BOUNDARY",
        "AI_ADOPTION_PROTOCOL",
        "adoption_drift",
        "experiment_artifact",
        "MINIMUM_PRESERVATION_KERNEL",
        "anchor_blind",
        "scorer coverage mapping",
        "LICENSE_POLICY_DRAFT",
        "CANONICAL_STATUS",
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
    claim_terms = ("released", "tagged", "signed", "anchored", "published")
    offenders: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        lowered = line.lower()
        if "v0.5.0" in lowered and any(term in lowered for term in claim_terms):
            if not line_is_negated(line):
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


def main() -> int:
    check("R1 release notes cover major work areas", test_r1_release_notes_cover_major_work_areas)
    check("R2 license draft routing stays non-license", test_r2_license_draft_routing_stays_non_license)
    check("R3 anchor_blind not described as merely planned", test_r3_anchor_blind_not_described_as_merely_planned)
    check("R4 release notes claim no release actions", test_r4_release_notes_claim_no_release_actions)
    check("R5 results dir empty except gitkeep", test_r5_results_dir_empty_except_gitkeep)
    check("R6 no adoption-completion claims in status docs", test_r6_no_adoption_completion_claims_in_status_docs)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
