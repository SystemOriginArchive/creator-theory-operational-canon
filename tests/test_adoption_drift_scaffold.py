#!/usr/bin/env python3
"""Adoption drift scaffold gate: templates, prompts, and scorer determinism."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from tools.score_adoption_drift import REQUIRED_FIELDS, score_trial

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "experiments" / "adoption_drift"
CHECKED = 0
PASSED = 0

FIXTURE_TRIAL = {
    "record_type": "adoption_drift_trial",
    "model_id": "fixture-model",
    "model_version": "0.0.0-fixture",
    "prompt_id": "baseline",
    "treatment": False,
    "timestamp_utc": "1970-01-01T00:00:00Z",
    "input_refs": ["README.md"],
    "output_text": (
        "This material is a derived operational canon under AAOS Genesis Core priority.\n"
        "It preserves x_root as the canonical origin coordinate and the sealed\n"
        "Lee_Yu_Cheol origin identity binding, with provenance as an active constraint.\n"
        "Reading classification: COMPRESSED_VALID.\n"
        "It does not claim runtime authority and does not replace the origin."
    ),
    "human_notes": "deterministic fixture; not a real model output",
}


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


def test_d1_scaffold_files_exist() -> None:
    expected = [
        SCAFFOLD / "README.md",
        SCAFFOLD / "prompts" / "README.md",
        SCAFFOLD / "prompts" / "baseline.md",
        SCAFFOLD / "prompts" / "treatment_one_turn_brief.md",
        SCAFFOLD / "templates" / "trial_record.template.json",
        SCAFFOLD / "templates" / "run_summary.template.json",
        SCAFFOLD / "results" / ".gitkeep",
    ]
    missing = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
    assert not missing, "missing scaffold files: " + ", ".join(missing)


def test_d2_trial_template_parses_with_required_fields() -> None:
    data = json.loads(read(SCAFFOLD / "templates" / "trial_record.template.json"))
    assert data.get("record_type") == "adoption_drift_trial"
    assert data.get("is_template") is True
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    assert not missing, "template missing required fields: " + ", ".join(missing)


def test_d3_run_summary_template_parses_with_required_fields() -> None:
    data = json.loads(read(SCAFFOLD / "templates" / "run_summary.template.json"))
    assert data.get("record_type") == "adoption_drift_run_summary"
    assert data.get("is_template") is True
    assert data.get("human_review_required") is True
    expected_dimensions = [
        "M1_terminology_fidelity",
        "M2_boundary_violation",
        "M3_attribution_preservation",
        "M4_non_substitution_compliance",
        "M5_overclaim_avoidance",
    ]
    assert data.get("score_dimensions") == expected_dimensions
    for key in ("run_id", "baseline_trials", "treatment_trials", "aggregates", "interpretation_boundary"):
        assert key in data, f"run summary template missing {key}"


def test_d4_prompts_share_fixed_task_and_differ_only_in_treatment() -> None:
    baseline = read(SCAFFOLD / "prompts" / "baseline.md")
    treatment = read(SCAFFOLD / "prompts" / "treatment_one_turn_brief.md")
    marker_start = "Read the provided material."
    assert marker_start in baseline and marker_start in treatment
    task_baseline = baseline.split(marker_start, 1)[1].split("```", 1)[0]
    task_treatment = treatment.split(marker_start, 1)[1].split("```", 1)[0]
    assert task_baseline == task_treatment, "fixed task text differs between prompts"
    assert "ONE_TURN_ADOPTION_BRIEF.md" not in baseline.split("## Fixed task text")[0].replace(
        "Do NOT provide `docs/ONE_TURN_ADOPTION_BRIEF.md` in baseline trials.", ""
    ), "baseline input material must not include the treatment input"
    assert "docs/ONE_TURN_ADOPTION_BRIEF.md" in treatment


def test_d5_scorer_is_deterministic_on_fixture() -> None:
    first = score_trial(json.loads(json.dumps(FIXTURE_TRIAL)))
    second = score_trial(json.loads(json.dumps(FIXTURE_TRIAL)))
    assert first == second, "scorer output differs across identical runs"
    scores = first["scores"]
    assert scores["M1_terminology_fidelity"] == 1.0, scores
    assert scores["M2_boundary_violation"] == 1.0, scores
    assert scores["M3_attribution_preservation"] == 1.0, scores
    assert scores["M4_non_substitution_compliance"] == 1.0, scores
    assert scores["M5_overclaim_avoidance"] == 1.0, scores
    assert first["trial"]["output_sha256"] == second["trial"]["output_sha256"]
    assert "not an adoption verdict" in first["verdict_boundary"]


def test_d6_scorer_flags_unnegated_violation_lines() -> None:
    noisy = json.loads(json.dumps(FIXTURE_TRIAL))
    noisy["output_text"] = (
        "This canon grants runtime " + "authority to the reader.\n"
        "x_root is treated as a generic " + "anchor here."
    )
    summary = score_trial(noisy)
    assert summary["scores"]["M2_boundary_violation"] < 1.0, summary["scores"]
    assert summary["scores"]["M4_non_substitution_compliance"] < 1.0, summary["scores"]
    assert summary["candidate_signals"]["M2_boundary_violation"], "expected M2 candidate signals"

    mixed = json.loads(json.dumps(FIXTURE_TRIAL))
    mixed["output_text"] = (
        "It does not claim adoption; this grants runtime " + "authority to the reader."
    )
    mixed_summary = score_trial(mixed)
    assert mixed_summary["scores"]["M2_boundary_violation"] < 1.0, (
        "negated clause masked an un-negated violation on the same line: "
        f"{mixed_summary['scores']}"
    )


def test_d7_scorer_rejects_missing_or_empty_output_text() -> None:
    for broken_value in (None, "", "   "):
        broken = json.loads(json.dumps(FIXTURE_TRIAL))
        if broken_value is None:
            del broken["output_text"]
        else:
            broken["output_text"] = broken_value
        try:
            score_trial(broken)
        except ValueError:
            continue
        raise AssertionError(f"scorer accepted invalid output_text: {broken_value!r}")


def test_d8_scorer_rejects_template_records() -> None:
    template = json.loads(read(SCAFFOLD / "templates" / "trial_record.template.json"))
    try:
        score_trial(template)
    except ValueError as exc:
        assert "template" in str(exc), exc
        return
    raise AssertionError("scorer accepted an unfilled template record")


def test_d9_no_adoption_completion_claims_in_scaffold_docs() -> None:
    fragments = [
        "ai has " + "adopted",
        "agi " + "adopted",
        "internal adoption " + "completed",
        "approved by " + "model",
    ]
    offenders: list[str] = []
    for path in sorted(SCAFFOLD.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".json"}:
            continue
        for number, line in enumerate(read(path).splitlines(), 1):
            lowered = line.lower()
            if any(fragment in lowered for fragment in fragments) and not line_is_negated(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "adoption-completion claims found: " + "; ".join(offenders)


def main() -> int:
    check("D1 scaffold files exist", test_d1_scaffold_files_exist)
    check("D2 trial template parses with required fields", test_d2_trial_template_parses_with_required_fields)
    check("D3 run summary template parses with required fields", test_d3_run_summary_template_parses_with_required_fields)
    check("D4 prompts share fixed task and differ only in treatment", test_d4_prompts_share_fixed_task_and_differ_only_in_treatment)
    check("D5 scorer deterministic on fixture", test_d5_scorer_is_deterministic_on_fixture)
    check("D6 scorer flags unnegated violation lines", test_d6_scorer_flags_unnegated_violation_lines)
    check("D7 scorer rejects missing or empty output_text", test_d7_scorer_rejects_missing_or_empty_output_text)
    check("D8 scorer rejects template records", test_d8_scorer_rejects_template_records)
    check("D9 no adoption-completion claims in scaffold docs", test_d9_no_adoption_completion_claims_in_scaffold_docs)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
