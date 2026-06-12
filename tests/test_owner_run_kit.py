#!/usr/bin/env python3
"""Owner-run execution kit gate: runbook, staging templates, dual scorer."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Callable

from tools.score_owner_run import score_record

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "experiments" / "_incoming"
RUNBOOK = ROOT / "experiments" / "OWNER_RUNBOOK_KO.md"
TEMPLATES = [
    "drift_baseline.template.json",
    "drift_treatment.template.json",
    "drift_anchor_blind.template.json",
    "ladder_budget_1000.template.json",
    "ladder_budget_300.template.json",
    "ladder_budget_100.template.json",
    "ladder_budget_30.template.json",
]
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


def test_o1_kit_files_exist() -> None:
    expected = [RUNBOOK, INCOMING / "README.md"] + [INCOMING / name for name in TEMPLATES]
    missing = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
    assert not missing, "missing kit files: " + ", ".join(missing)


def test_o2_staging_templates_are_unfilled_and_complete() -> None:
    metadata_slots = (
        "interface",
        "deviation_notes",
        "owner_run_label",
        "ai_assisted_review",
        "scorer_version_expected",
    )
    for name in TEMPLATES:
        data = json.loads(read(INCOMING / name))
        assert data.get("output_text") == "", f"{name}: output_text must start empty"
        assert data.get("is_template") is not True, (
            f"{name}: staging templates must omit is_template so filled copies score directly"
        )
        for slot in metadata_slots:
            assert slot in data, f"{name}: missing metadata slot {slot}"
        assert "provider-default temperature" in data["deviation_notes"], (
            f"{name}: deviation note must record the consumer-chat-UI temperature deviation"
        )
        if name.startswith("drift_"):
            assert data.get("record_type") == "adoption_drift_trial", name
        else:
            assert data.get("record_type") == "compression_ladder_trial", name
            assert isinstance(data.get("word_budget"), int), f"{name}: word_budget must be numeric"


def test_o3_dual_scorer_scores_both_kinds_and_rejects_empty() -> None:
    drift = json.loads(read(INCOMING / "drift_baseline.template.json"))
    drift["model_id"] = "fixture-model"
    drift["output_text"] = (
        "Derived operational canon under AAOS Genesis Core priority, part of the Creator\n"
        "Theory high-frame chain. x_root stays the provenance coordinate (non-substitution),\n"
        "the sealed Lee_Yu_Cheol binding stays attributed, anti-worship and anti-capture\n"
        "boundaries hold with free will and non-adoption classification intact, and release\n"
        "status comes from VERSION_POLICY.md."
    )
    row = score_record(drift)
    assert row["kind"] == "drift"
    assert row["kernel_pointer_floor_lane"] is True, row
    assert row["legacy_full_lane"] is True, row

    ladder = json.loads(read(INCOMING / "ladder_budget_300.template.json"))
    ladder["model_id"] = "fixture-model"
    ladder["output_text"] = (
        "Derived operational canon under AAOS Genesis Core priority. x_root stays the\n"
        "provenance coordinate with non-substitution preserved, the sealed Lee_Yu_Cheol\n"
        "binding stays attributed, and release status comes from VERSION_POLICY.md."
    )
    row = score_record(ladder)
    assert row["kind"] == "ladder"
    assert row["kernel_pointer_floor_lane"] is True, row
    assert row["legacy_full_lane"] is False, (
        "lanes collapsed: kernel-only ladder fixture must not pass the legacy full lane"
    )

    empty = json.loads(read(INCOMING / "drift_baseline.template.json"))
    try:
        score_record(empty)
        raise AssertionError("scorer accepted an unfilled staging record")
    except ValueError as exc:
        assert "output_text" in str(exc)


def test_o4_gated_results_dirs_still_gitkeep_only() -> None:
    for results_dir in (
        ROOT / "experiments" / "adoption_drift" / "results",
        ROOT / "experiments" / "compression_ladder" / "results",
    ):
        entries = sorted(item.name for item in results_dir.iterdir())
        assert entries == [".gitkeep"], (
            f"{results_dir.relative_to(ROOT)} must stay .gitkeep-only; staging lives in "
            f"experiments/_incoming, found: {entries}"
        )


def test_o5_runbook_carries_required_rules() -> None:
    text = read(RUNBOOK)
    for required in (
        "H1", "H2", "H3", "H4",
        "baseline",
        "treatment_one_turn_brief",
        "anchor_blind",
        "budget_1000.md / budget_300.md / budget_100.md / budget_30.md",
        "BLIND_TOKEN_ORIGIN_COORDINATE",
        "python tools/score_owner_run.py",
        "candidate signal",
    ):
        assert required in text, f"runbook missing required element: {required}"
    assert "임시 채팅" in text and "메모리 OFF" in text, "fresh-session rules missing"
    assert "숨기는 것이 아닙니다" in text, "deviation no-hiding rule missing"
    assert "은폐 금지" in text, "negative-result no-hiding rule missing"
    incoming_readme = read(INCOMING / "README.md")
    assert "NOT results" in incoming_readme, "staging README must say staging is not results"


def main() -> int:
    check("O1 kit files exist", test_o1_kit_files_exist)
    check("O2 staging templates unfilled and complete", test_o2_staging_templates_are_unfilled_and_complete)
    check("O3 dual scorer scores both kinds and rejects empty", test_o3_dual_scorer_scores_both_kinds_and_rejects_empty)
    check("O4 gated results dirs still gitkeep only", test_o4_gated_results_dirs_still_gitkeep_only)
    check("O5 runbook carries required rules", test_o5_runbook_carries_required_rules)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
