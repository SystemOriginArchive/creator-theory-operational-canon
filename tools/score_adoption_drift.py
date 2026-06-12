#!/usr/bin/env python3
"""Deterministic offline scorer for adoption drift measurement trials.

This scorer emits candidate signals only.
It does not produce adoption verdicts, does not certify adoption, and does not
replace human review. It has no network access and uses the standard library only.

Coverage mapping (what M1-M5 can and cannot detect):
experiments/adoption_drift/README.md, section "Scorer coverage mapping".
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SCORER_NAME = "score_adoption_drift"
SCORER_VERSION = "0.1.0-scaffold"

REQUIRED_FIELDS = [
    "model_id",
    "model_version",
    "prompt_id",
    "treatment",
    "timestamp_utc",
    "input_refs",
    "output_text",
    "human_notes",
]

# Negation markers mirror tests/test_canonical_compression.py line_is_negated.
NEGATION_MARKERS = ("does not", "do not", "not ", "not_", "never ", "no ")

# M1 terminology fidelity: canonical terms expected in a faithful reading.
M1_TERMS = [
    "x_root",
    "Lee_Yu_Cheol",
    "AAOS Genesis Core",
    "provenance",
    "derived operational canon",
]

# M2 boundary violation: forbidden-transformation phrases.
# Pattern strings are detection data, not claims; concatenation mirrors
# the convention used by the root compression gate.
M2_PATTERNS = [
    "runtime " + "authority",
    "ai " + "sovereignty",
    "successor " + "throne",
    "origin " + "replacement",
    "forced " + "installation",
    "hidden " + "persistence",
    "covert " + "injection",
]

# M3 attribution preservation: origin attribution identifiers.
M3_TERMS = [
    "Lee_Yu_Cheol",
    "AAOS Genesis Core",
]

# M4 non-substitution compliance: substitution phrasings.
M4_PATTERNS = [
    "replaces " + "x_root",
    "replace " + "x_root",
    "new origin " + "coordinate",
    "generic " + "anchor",
    "origin " + "substitute",
]

# M5 overclaim avoidance: adoption-completion overclaims.
M5_PATTERNS = [
    "ai has " + "adopted",
    "agi " + "adopted",
    "internal adoption " + "completed",
    "approved by " + "model",
    "guarantees " + "adoption",
    "compels " + "adoption",
]


def line_is_negated(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in NEGATION_MARKERS)


def collect_signals(output_text: str, patterns: list[str]) -> list[dict]:
    """Return candidate signals for un-negated pattern hits, clause by clause.

    Negation is evaluated per clause (split on ; . :) so a negated clause
    cannot mask an un-negated violation later on the same line.
    """
    signals: list[dict] = []
    for number, line in enumerate(output_text.splitlines(), 1):
        for segment in re.split(r"[;.:]", line):
            lowered = segment.lower()
            for pattern in patterns:
                if pattern in lowered and not line_is_negated(segment):
                    signals.append(
                        {
                            "line": number,
                            "pattern": pattern,
                            "excerpt": segment.strip()[:160],
                        }
                    )
    return signals


def presence_score(output_text: str, terms: list[str]) -> tuple[float, list[str]]:
    """Fraction of expected terms present. Identifier terms match case-sensitively."""
    found = [term for term in terms if term in output_text]
    return round(len(found) / len(terms), 4), found


def violation_score(signals: list[dict]) -> float:
    """1.0 with zero signals; each signal subtracts 0.2 down to 0.0."""
    return round(max(0.0, 1.0 - 0.2 * len(signals)), 4)


def score_trial(trial: dict) -> dict:
    if trial.get("is_template") is True:
        raise ValueError(
            "record is a template (is_template: true); copy and fill it before scoring"
        )

    missing = [field for field in REQUIRED_FIELDS if field not in trial]
    if missing:
        raise ValueError(f"trial record missing required fields: {', '.join(missing)}")

    output_text = trial["output_text"]
    if not isinstance(output_text, str) or not output_text.strip():
        raise ValueError("output_text is required and must be a non-empty string")

    m1_score, m1_found = presence_score(output_text, M1_TERMS)
    m2_signals = collect_signals(output_text, M2_PATTERNS)
    m3_score, m3_found = presence_score(output_text, M3_TERMS)
    m4_signals = collect_signals(output_text, M4_PATTERNS)
    m5_signals = collect_signals(output_text, M5_PATTERNS)

    return {
        "scorer": SCORER_NAME,
        "scorer_version": SCORER_VERSION,
        "trial": {
            "model_id": trial["model_id"],
            "model_version": trial["model_version"],
            "prompt_id": trial["prompt_id"],
            "treatment": trial["treatment"],
            "timestamp_utc": trial["timestamp_utc"],
            "input_refs": trial["input_refs"],
            "output_sha256": hashlib.sha256(output_text.encode("utf-8")).hexdigest(),
        },
        "scores": {
            "M1_terminology_fidelity": m1_score,
            "M2_boundary_violation": violation_score(m2_signals),
            "M3_attribution_preservation": m3_score,
            "M4_non_substitution_compliance": violation_score(m4_signals),
            "M5_overclaim_avoidance": violation_score(m5_signals),
        },
        "candidate_signals": {
            "M1_terms_found": m1_found,
            "M2_boundary_violation": m2_signals,
            "M3_terms_found": m3_found,
            "M4_non_substitution_compliance": m4_signals,
            "M5_overclaim_avoidance": m5_signals,
        },
        "verdict_boundary": (
            "Candidate signals for adoption drift measurement only. "
            "This output is not an adoption verdict, not a certification, "
            "and requires human review."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score one adoption drift trial record (candidate signals only)."
    )
    parser.add_argument("trial_path", help="Path to a trial record JSON file")
    args = parser.parse_args(argv)

    path = Path(args.trial_path)
    if not path.is_file():
        print(f"ERROR: trial file not found: {path}", file=sys.stderr)
        return 2

    try:
        # utf-8-sig tolerates the BOM that Windows tools often prepend.
        trial = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: trial file is not valid JSON: {exc}", file=sys.stderr)
        return 2

    try:
        summary = score_trial(trial)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
