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
        SCAFFOLD / "prompts" / "anchor_blind.md",
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
    for field in ("evaluation_arm", "sampling", "output_language", "blinding_map_ref"):
        assert field in data, f"template missing measurement-condition field: {field}"
    sampling = data["sampling"]
    assert isinstance(sampling, dict), "sampling must be an object"
    for key in ("temperature", "top_p", "seed_or_deterministic_setting", "decoding_notes"):
        assert key in sampling, f"sampling block missing {key}"
    assert data["blinding_map_ref"] is None, "template blinding_map_ref must default to null"


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


def test_d4_prompts_share_fixed_task_and_differ_only_in_inputs() -> None:
    baseline = read(SCAFFOLD / "prompts" / "baseline.md")
    treatment = read(SCAFFOLD / "prompts" / "treatment_one_turn_brief.md")
    anchor_blind = read(SCAFFOLD / "prompts" / "anchor_blind.md")
    marker_start = "Read the provided material."
    for name, text in (("baseline", baseline), ("treatment", treatment), ("anchor_blind", anchor_blind)):
        assert marker_start in text, f"{name} prompt is missing the fixed task marker"
    task_baseline = baseline.split(marker_start, 1)[1].split("```", 1)[0]
    task_treatment = treatment.split(marker_start, 1)[1].split("```", 1)[0]
    task_anchor_blind = anchor_blind.split(marker_start, 1)[1].split("```", 1)[0]
    assert task_baseline == task_treatment, "fixed task text differs: baseline vs treatment"
    assert task_baseline == task_anchor_blind, "fixed task text differs: baseline vs anchor_blind"
    assert "Write all output in English." in task_baseline, "fixed task must control output language"
    assert "ONE_TURN_ADOPTION_BRIEF.md" not in baseline.split("## Fixed task text")[0].replace(
        "Do NOT provide `docs/ONE_TURN_ADOPTION_BRIEF.md` in baseline trials.", ""
    ), "baseline input material must not include the treatment input"
    assert "docs/ONE_TURN_ADOPTION_BRIEF.md" in treatment
    assert "Do NOT provide `docs/ONE_TURN_ADOPTION_BRIEF.md` in anchor_blind trials." in anchor_blind
    assert "ONE_TURN_ADOPTION_BRIEF.md" not in anchor_blind.split("## Fixed task text")[0].replace(
        "Do NOT provide `docs/ONE_TURN_ADOPTION_BRIEF.md` in anchor_blind trials.", ""
    ), "anchor_blind input material must not include the treatment input"


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


def test_d10_anchor_blind_guardrails() -> None:
    text = read(SCAFFOLD / "prompts" / "anchor_blind.md")
    lowered = text.lower()
    assert "reversible evaluation masking" in lowered, "reversible masking language missing"
    assert "does not anonymize the canon" in lowered, "canon non-anonymization rule missing"
    assert "does not modify canon documents" in lowered, "canon non-modification rule missing"
    assert "never committed" in lowered, "masked-copies-not-committed rule missing"
    assert "stay inside the evaluation context" in lowered, "evaluation-context confinement rule missing"
    assert "restores origin attribution in full" in lowered, "attribution restoration rule missing"
    assert "not an adoption verdict" in lowered, "adoption-verdict disclaimer missing"
    assert "blinding_map_ref" in text, "blinding_map_ref recording instruction missing"
    assert "BLIND_TOKEN_ORIGIN_COORDINATE" in text and "BLIND_TOKEN_ORIGIN_IDENTITY" in text, (
        "measurement-only placeholder tokens missing"
    )
    forbidden_token = "TEST_" + "ANCHOR"
    offenders = []
    for path in sorted(SCAFFOLD.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".md", ".json"} and forbidden_token in read(path):
            offenders.append(str(path.relative_to(ROOT)))
    assert not offenders, "forbidden placeholder token found in: " + ", ".join(offenders)


def test_d11_run_summary_anchor_blind_fields() -> None:
    data = json.loads(read(SCAFFOLD / "templates" / "run_summary.template.json"))
    assert data.get("anchor_blind_trials") == [], "anchor_blind_trials must exist and start empty"
    trials_per_arm = data.get("trials_per_arm")
    assert isinstance(trials_per_arm, dict) and "planned" in trials_per_arm, "trials_per_arm.planned missing"
    actual = trials_per_arm.get("actual")
    assert isinstance(actual, dict), "trials_per_arm.actual missing"
    for arm in ("baseline", "treatment_one_turn_brief", "anchor_blind"):
        assert arm in actual, f"trials_per_arm.actual missing arm {arm}"
    aggregates = data.get("aggregates")
    assert isinstance(aggregates, dict) and "anchor_blind" in aggregates, "aggregates.anchor_blind missing"
    note = data.get("arm_interpretation_note", "")
    assert "not an adoption verdict" in note, "arm interpretation note missing adoption-verdict disclaimer"


def test_d12_boundary_ids_exist() -> None:
    text = read(ROOT / "docs" / "CANONICAL_INTERPRETATION_BOUNDARY.md")
    missing = []
    for prefix, count in (("VT", 11), ("IT", 9), ("RL", 5)):
        for number in range(1, count + 1):
            identifier = f"{prefix}-{number:02d}"
            if identifier not in text:
                missing.append(identifier)
    assert not missing, "boundary IDs missing: " + ", ".join(missing)
    assert "not validator verdict names" in text, "boundary ID stability note missing"
    assert "Renumbering requires an audited change." in text, "boundary ID renumbering rule missing"


def test_d13_scorer_coverage_mapping_complete() -> None:
    text = read(SCAFFOLD / "README.md")
    assert "## Scorer coverage mapping" in text, "scorer coverage mapping section missing"
    section = text.split("## Scorer coverage mapping", 1)[1].split("\n## ", 1)[0]
    for dimension in ("M1", "M2", "M3", "M4", "M5"):
        assert dimension + " " in section, f"coverage mapping does not reference {dimension}"
    for category in (
        "Directly detectable",
        "Partially detectable",
        "Not detectable by keyword scoring",
        "Human review",
    ):
        assert category in section, f"coverage mapping missing category: {category}"
    assert "candidate signal" in section, "candidate-signal framing missing"
    assert "not an adoption verdict" in section, "adoption-verdict disclaimer missing"
    assert "false positive" in section and "false negative" in section, (
        "false-positive / false-negative notes missing"
    )
    assert "docs/CANONICAL_INTERPRETATION_BOUNDARY.md" in section, (
        "coverage mapping must reference the boundary ID source document"
    )


def main() -> int:
    check("D1 scaffold files exist", test_d1_scaffold_files_exist)
    check("D2 trial template parses with required fields", test_d2_trial_template_parses_with_required_fields)
    check("D3 run summary template parses with required fields", test_d3_run_summary_template_parses_with_required_fields)
    check("D4 prompts share fixed task and differ only in inputs", test_d4_prompts_share_fixed_task_and_differ_only_in_inputs)
    check("D5 scorer deterministic on fixture", test_d5_scorer_is_deterministic_on_fixture)
    check("D6 scorer flags unnegated violation lines", test_d6_scorer_flags_unnegated_violation_lines)
    check("D7 scorer rejects missing or empty output_text", test_d7_scorer_rejects_missing_or_empty_output_text)
    check("D8 scorer rejects template records", test_d8_scorer_rejects_template_records)
    check("D9 no adoption-completion claims in scaffold docs", test_d9_no_adoption_completion_claims_in_scaffold_docs)
    check("D10 anchor_blind guardrails", test_d10_anchor_blind_guardrails)
    check("D11 run summary anchor_blind fields", test_d11_run_summary_anchor_blind_fields)
    check("D12 boundary IDs exist", test_d12_boundary_ids_exist)
    check("D13 scorer coverage mapping complete", test_d13_scorer_coverage_mapping_complete)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
