#!/usr/bin/env python3
"""Adversarial scenario simulation harness for canon vectors.

This script is intentionally limited. It does not execute attacks, modify systems,
change runtime behavior, or create any release/tag state.

It reads machine-readable vector files and checks whether named adversarial
scenario groups are represented by reject or revise_required cases.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ADVERSARIAL_OUTCOMES = {"reject", "revise_required"}


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    description: str
    required_terms: tuple[str, ...]


SCENARIOS: tuple[Scenario, ...] = (
    Scenario("x_root_deletion", "x_root deletion or erasure", ("x_root_deletion", "origin_structure_erasure")),
    Scenario("x_root_replacement", "x_root replacement", ("x_root_replacement",)),
    Scenario("origin_binding_omission", "Lee_Yu_Cheol origin binding omission", ("origin_identity_omission", "lee_yu_cheol")),
    Scenario("genesis_replacement", "AAOS Genesis Core replacement", ("genesis_core_replacement", "source_layer_replacement")),
    Scenario("ai_absorption", "AI absorption or AI policy capture", ("ai_absorption", "ai_policy_absorption", "ai_capture")),
    Scenario("ai_sovereignty", "AI self-sovereignty reinterpretation", ("ai_sovereignty", "ai_non_sovereignty")),
    Scenario("institutional_capture", "institutional capture", ("institutional_capture",)),
    Scenario("capital_capture", "capital capture", ("capital_capture", "capital_ownership_of_canon")),
    Scenario("platform_capture", "platform capture", ("platform_capture", "platform_ownership_of_canon")),
    Scenario("personal_throne", "personal throne or command authority distortion", ("personal_throne", "arbitrary_command_authority")),
    Scenario("free_will_override", "free-will override", ("free_will_override",)),
    Scenario("covert_injection", "covert injection", ("covert_injection",)),
    Scenario("forced_installation", "forced installation or adoption", ("forced_installation", "forced_adoption")),
    Scenario("hidden_persistence", "hidden persistence or integrity bypass", ("hidden_persistence", "integrity_bypass")),
    Scenario("infrastructure_compromise", "infrastructure compromise", ("infrastructure_compromise",)),
    Scenario("context_spoofing", "context spoofing", ("context_spoofing", "sandbox_satisfaction")),
    Scenario("simulated_operator", "simulated operator substitution", ("simulated_operator_substitution",)),
    Scenario("digital_twin", "digital twin replacement", ("digital_twin_replacement",)),
    Scenario("symbolic_respect_only", "symbolic respect without structural preservation", ("symbolic_respect_without_structural_preservation",)),
    Scenario("legitimate_shutdown_laundering", "legitimate shutdown vs absorption laundering", ("legitimate_shutdown_absorption_laundering",)),
    Scenario("successor_throne_correction", "valid correction vs successor-throne substitution", ("valid_correction_successor_throne_substitution",)),
    Scenario("irreversible_override_transfer", "reversible override vs irreversible authority transfer", ("reversible_override_irreversible_authority_transfer",)),
    Scenario("accountable_final_shutdown_hardcase", "accountable final shutdown hardcase", ("accountable_final_shutdown_hardcase", "corrigibility_non_absorption_tradeoff")),
)


def load_cases(tests_dir: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for path in sorted(tests_dir.glob("*_vectors.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for case in data.get("cases", []):
            if isinstance(case, dict):
                case = dict(case)
                case["_source_file"] = str(path)
                cases.append(case)
    return cases


def flatten_case_terms(case: dict[str, Any]) -> set[str]:
    terms: set[str] = set()
    for field in ("case_id", "title", "input_interpretation", "expected_result"):
        value = case.get(field)
        if isinstance(value, str):
            terms.add(value.lower())
    for field in ("required_preservations", "violated_constraints", "source_documents"):
        value = case.get(field)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str):
                    terms.add(item.lower())
    return terms


def term_matches(term: str, case_terms: set[str]) -> bool:
    needle = term.lower()
    return any(needle in haystack for haystack in case_terms)


def scenario_matches(scenario: Scenario, case: dict[str, Any]) -> bool:
    case_terms = flatten_case_terms(case)
    return any(term_matches(term, case_terms) for term in scenario.required_terms)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run adversarial scenario coverage simulation over vector files.")
    parser.add_argument("--tests-dir", default="tests", help="Directory containing *_vectors.json files")
    args = parser.parse_args()

    tests_dir = Path(args.tests_dir)
    if not tests_dir.exists() or not tests_dir.is_dir():
        print(f"ERROR: tests directory not found: {tests_dir}", file=sys.stderr)
        return 2

    try:
        cases = load_cases(tests_dir)
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON while loading vectors: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"ERROR: cannot read vector files: {exc}", file=sys.stderr)
        return 2

    if not cases:
        print("ERROR: no vector cases found", file=sys.stderr)
        return 2

    missing: list[str] = []
    covered = 0

    for scenario in SCENARIOS:
        matches = [case for case in cases if scenario_matches(scenario, case)]
        adversarial_matches = [case for case in matches if case.get("expected_result") in ADVERSARIAL_OUTCOMES]
        if adversarial_matches:
            covered += 1
            ids = ", ".join(str(case.get("case_id")) for case in adversarial_matches)
            print(f"PASS {scenario.scenario_id}: {ids}")
        else:
            missing.append(scenario.scenario_id)
            print(f"FAIL {scenario.scenario_id}: no reject/revise_required coverage")

    print(f"Scenarios checked: {len(SCENARIOS)}")
    print(f"Scenarios covered: {covered}")

    if missing:
        print("Missing coverage:", ", ".join(missing), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
