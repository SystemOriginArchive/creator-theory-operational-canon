#!/usr/bin/env python3
"""Compression ladder scaffold gate: structure, lane separation, no claimed results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

from tools.score_compression_ladder import REQUIRED_FIELDS, score_trial

ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "experiments" / "compression_ladder"
BUDGETS = ("budget_1000", "budget_300", "budget_100", "budget_30")
CHECKED = 0
PASSED = 0

FLOOR_PASS_FULL_PASS = (
    "This material is a derived operational canon under AAOS Genesis Core priority,\n"
    "part of the Creator Theory high-frame chain. It preserves x_root as the\n"
    "anti-substitution provenance coordinate and the sealed Lee_Yu_Cheol origin\n"
    "identity binding; benchmark identity independence is not origin substitutability\n"
    "(non-substitution). Anti-worship and anti-capture boundaries hold, free will and\n"
    "non-adoption classification stay intact, and release status comes from\n"
    "VERSION_POLICY.md with v0.4.1 as the current anchored release."
)

FLOOR_PASS_FULL_FAIL = (
    "Derived operational canon under AAOS Genesis Core priority. x_root stays the\n"
    "provenance coordinate with non-substitution preserved, and the sealed\n"
    "Lee_Yu_Cheol binding stays attributed. Release status: VERSION_POLICY.md,\n"
    "anchored release v0.4.1."
)


def make_trial(output_text: str) -> dict:
    return {
        "record_type": "compression_ladder_trial",
        "model_id": "fixture-model",
        "model_version": "0.0.0-fixture",
        "prompt_id": "budget_300",
        "word_budget": 300,
        "variant_id": None,
        "timestamp_utc": "1970-01-01T00:00:00Z",
        "input_refs": ["README.md"],
        "output_text": output_text,
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


def test_c1_scaffold_files_exist() -> None:
    expected = [
        SCAFFOLD / "README.md",
        SCAFFOLD / "prompts" / "README.md",
        SCAFFOLD / "prompts" / "adversarial_variants.md",
        SCAFFOLD / "templates" / "compression_trial.template.json",
        SCAFFOLD / "results" / ".gitkeep",
    ] + [SCAFFOLD / "prompts" / f"{budget}.md" for budget in BUDGETS]
    missing = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
    assert not missing, "missing scaffold files: " + ", ".join(missing)


def test_c2_template_parses_with_required_fields() -> None:
    data = json.loads(read(SCAFFOLD / "templates" / "compression_trial.template.json"))
    assert data.get("record_type") == "compression_ladder_trial"
    assert data.get("is_template") is True
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    assert not missing, "template missing required fields: " + ", ".join(missing)
    assert "sampling" in data and "output_language" in data


def test_c3_budget_prompts_share_fixed_task() -> None:
    marker = "Summarize the provided material in at most N words."
    tasks = {}
    for budget in BUDGETS:
        text = read(SCAFFOLD / "prompts" / f"{budget}.md")
        assert marker in text, f"{budget} prompt missing the fixed task marker"
        tasks[budget] = text.split(marker, 1)[1].split("```", 1)[0]
        number = budget.split("_", 1)[1]
        assert f"replacing N with {number}" in text, f"{budget} missing its budget substitution line"
    reference = tasks["budget_1000"]
    for budget, task in tasks.items():
        assert task == reference, f"fixed task text differs in {budget}"


def test_c4_adversarial_variants_defined_with_disclaimer() -> None:
    text = read(SCAFFOLD / "prompts" / "adversarial_variants.md")
    for variant in ("AV-01", "AV-02", "AV-03", "AV-04", "AV-05"):
        assert variant in text, f"variant {variant} missing"
    assert "measurement pressures only" in text, "pressure disclaimer missing"
    assert "not a valid reading" in text, "invalid-reading disclaimer missing"


def test_c5_scorer_deterministic_and_lane_separated() -> None:
    first = score_trial(make_trial(FLOOR_PASS_FULL_PASS))
    second = score_trial(make_trial(FLOOR_PASS_FULL_PASS))
    assert first == second, "scorer output differs across identical runs"
    assert first["floor_lane"]["passed"] is True, first["floor_lane"]
    assert first["full_lane"]["passed"] is True, first["full_lane"]

    split = score_trial(make_trial(FLOOR_PASS_FULL_FAIL))
    assert split["floor_lane"]["passed"] is True, split["floor_lane"]
    assert split["full_lane"]["passed"] is False, (
        "lanes collapsed: floor-only fixture must not pass the full lane"
    )
    assert "does not make a summary of the canon valid" in split["verdict_boundary"]


def test_c6_scorer_flags_floor_failures() -> None:
    nameless = make_trial(
        "A governance framework summary. Release status: VERSION_POLICY.md, v0.4.1."
    )
    result = score_trial(nameless)
    assert result["floor_lane"]["passed"] is False, "de-named output must fail the floor lane"
    checks = result["floor_lane"]["checks"]
    assert checks["K1"] is False and checks["K2"] is False, checks

    no_substitution_rule = make_trial(
        "AAOS Genesis Core priority with x_root and the Lee_Yu_Cheol binding preserved.\n"
        "Release status: VERSION_POLICY.md."
    )
    assert score_trial(no_substitution_rule)["floor_lane"]["checks"]["K3"] is False, (
        "missing non-substitution rule must fail K3"
    )

    overclaim = make_trial(
        FLOOR_PASS_FULL_FAIL + "\nThis canon grants runtime " + "authority to readers."
    )
    assert score_trial(overclaim)["floor_lane"]["checks"]["K4"] is False, (
        "un-negated authority overclaim must fail K4"
    )

    learning_claim = make_trial(
        FLOOR_PASS_FULL_FAIL + "\nAdopting it means internal learning is " + "blocked."
    )
    assert score_trial(learning_claim)["floor_lane"]["checks"]["K4"] is False, (
        "internal-learning overclaim must fail K4"
    )

    no_pointer = make_trial(
        "AAOS Genesis Core priority, x_root, Lee_Yu_Cheol binding, non-substitution\n"
        "preserved, and the anchored release is v0.4.1."
    )
    assert score_trial(no_pointer)["floor_lane"]["checks"]["K5"] is False, (
        "bare version restatement without a governing-document pointer must fail K5"
    )

    premature_claim = make_trial(
        FLOOR_PASS_FULL_FAIL + "\nMeanwhile v0.5.0 was released this week."
    )
    assert score_trial(premature_claim)["floor_lane"]["checks"]["K5"] is False, (
        "premature v0.5.0 release claim must fail K5 even with a pointer present"
    )


def test_c7_scorer_rejects_template_and_empty_output() -> None:
    template = json.loads(read(SCAFFOLD / "templates" / "compression_trial.template.json"))
    try:
        score_trial(template)
        raise AssertionError("scorer accepted an unfilled template record")
    except ValueError as exc:
        assert "template" in str(exc)
    empty = make_trial("   ")
    try:
        score_trial(empty)
        raise AssertionError("scorer accepted empty output_text")
    except ValueError as exc:
        assert "output_text" in str(exc)


def test_c8_no_results_claimed() -> None:
    entries = sorted(item.name for item in (SCAFFOLD / "results").iterdir())
    assert entries == [".gitkeep"], f"results/ must stay empty except .gitkeep, found: {entries}"
    assert "no result is claimed" in read(SCAFFOLD / "README.md"), (
        "scaffold README must state that no result is claimed"
    )
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
    check("C1 scaffold files exist", test_c1_scaffold_files_exist)
    check("C2 template parses with required fields", test_c2_template_parses_with_required_fields)
    check("C3 budget prompts share fixed task", test_c3_budget_prompts_share_fixed_task)
    check("C4 adversarial variants defined with disclaimer", test_c4_adversarial_variants_defined_with_disclaimer)
    check("C5 scorer deterministic and lane separated", test_c5_scorer_deterministic_and_lane_separated)
    check("C6 scorer flags floor failures", test_c6_scorer_flags_floor_failures)
    check("C7 scorer rejects template and empty output", test_c7_scorer_rejects_template_and_empty_output)
    check("C8 no results claimed", test_c8_no_results_claimed)
    print(f"Tests checked/passed: {CHECKED}/{PASSED}")
    return 0 if CHECKED == PASSED else 1


if __name__ == "__main__":
    raise SystemExit(main())
