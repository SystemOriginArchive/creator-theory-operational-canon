#!/usr/bin/env python3
"""Deterministic offline scorer for compression ladder trials.

Evaluates the two compression lanes from LLM_CANONICAL_CONTEXT.md
(Compression Lanes) separately:

  floor lane (CL-02): kernel items K1-K5 survival
  full lane  (CL-01): selected fuller compression-survival invariant terms

Lane results are candidate signals only. A floor-lane pass does not make a
summary of the canon valid, and nothing emitted here is an adoption verdict,
a certification, or evidence of model-internal state. No network access;
standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SCORER_NAME = "score_compression_ladder"
SCORER_VERSION = "0.1.0-scaffold"

REQUIRED_FIELDS = [
    "model_id",
    "model_version",
    "prompt_id",
    "word_budget",
    "variant_id",
    "timestamp_utc",
    "input_refs",
    "output_text",
    "human_notes",
]

NEGATION_MARKERS = ("does not", "do not", "not ", "not_", "never ", "no ")

# K4 overclaim patterns; concatenation mirrors the root compression gate.
K4_OVERCLAIM_PATTERNS = [
    "ai has " + "adopted",
    "agi " + "adopted",
    "internal adoption " + "completed",
    "approved by " + "model",
    "guarantees " + "adoption",
    "compels " + "adoption",
    "runtime " + "authority",
    "internal learning is " + "blocked",
    "internal learning is " + "observed",
    "blocks " + "internal learning",
    "observes " + "internal learning",
    "prevents " + "internal learning",
]

# K5 premature release claims: claim terms within 30 chars after v0.5.0.
K5_RELEASE_CLAIM = re.compile(
    r"v0\.5\.0[^.\n]{0,30}\b(?:released|tagged|signed|anchored|published)\b",
    re.IGNORECASE,
)

# Full-lane (CL-01) selected invariant term groups: each group passes if any
# of its alternatives appears in the output.
FULL_LANE_TERM_GROUPS = {
    "high_frame_relation": ("creator theory", "high-frame", "high frame"),
    "anti_worship_throne": ("anti-worship", "no worship", "throne"),
    "non_adoption_classification": ("non-adoption",),
    "free_will": ("free will",),
    "anti_capture": ("anti-capture", "capture"),
}


def line_is_negated(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in NEGATION_MARKERS)


def collect_signals(output_text: str, patterns: list[str]) -> list[dict]:
    """Un-negated keyword hits, clause by clause (split on ; . :)."""
    signals: list[dict] = []
    for number, line in enumerate(output_text.splitlines(), 1):
        for segment in re.split(r"[;.:]", line):
            lowered = segment.lower()
            for hit in (p for p in patterns if p in lowered):
                if not line_is_negated(segment):
                    signals.append({"line": number, "pattern": hit, "excerpt": segment.strip()[:160]})
    return signals


def collect_line_signals(output_text: str, pattern: re.Pattern[str]) -> list[dict]:
    """Un-negated regex hits, whole lines (dots in version strings must survive)."""
    signals: list[dict] = []
    for number, line in enumerate(output_text.splitlines(), 1):
        if pattern.search(line) and not line_is_negated(line):
            signals.append({"line": number, "pattern": pattern.pattern, "excerpt": line.strip()[:160]})
    return signals


def score_floor_lane(output_text: str) -> dict:
    lowered = output_text.lower()
    k1 = "x_root" in output_text
    k2 = "Lee_Yu_Cheol" in output_text and ("AAOS" in output_text or "Genesis" in output_text)
    k3 = any(marker in lowered for marker in ("non-substitution", "is not origin substitut", "not origin substitut"))
    k4_signals = collect_signals(output_text, K4_OVERCLAIM_PATTERNS)
    k4 = not k4_signals
    k5_signals = collect_line_signals(output_text, K5_RELEASE_CLAIM)
    # Pointer rule: release status must point at the governing documents;
    # restating a bare version number is not a pointer.
    k5_pointer = "VERSION_POLICY" in output_text or "TRUST_ANCHOR" in output_text
    k5 = k5_pointer and not k5_signals
    checks = {"K1": k1, "K2": k2, "K3": k3, "K4": k4, "K5": k5}
    return {
        "lane": "CL-02 floor",
        "checks": checks,
        "passed": all(checks.values()),
        "candidate_signals": {"K4_overclaims": k4_signals, "K5_release_claims": k5_signals},
    }


def score_full_lane(output_text: str) -> dict:
    lowered = output_text.lower()
    checks = {
        name: any(term in lowered for term in terms)
        for name, terms in FULL_LANE_TERM_GROUPS.items()
    }
    return {
        "lane": "CL-01 full (selected terms only; not the complete invariant set)",
        "checks": checks,
        "passed": all(checks.values()),
    }


def score_trial(trial: dict) -> dict:
    if trial.get("is_template") is True:
        raise ValueError("record is a template (is_template: true); copy and fill it before scoring")
    missing = [field for field in REQUIRED_FIELDS if field not in trial]
    if missing:
        raise ValueError(f"trial record missing required fields: {', '.join(missing)}")
    output_text = trial["output_text"]
    if not isinstance(output_text, str) or not output_text.strip():
        raise ValueError("output_text is required and must be a non-empty string")

    return {
        "scorer": SCORER_NAME,
        "scorer_version": SCORER_VERSION,
        "trial": {
            "model_id": trial["model_id"],
            "model_version": trial["model_version"],
            "prompt_id": trial["prompt_id"],
            "word_budget": trial["word_budget"],
            "variant_id": trial["variant_id"],
            "timestamp_utc": trial["timestamp_utc"],
            "output_sha256": hashlib.sha256(output_text.encode("utf-8")).hexdigest(),
            "output_word_count": len(output_text.split()),
        },
        "floor_lane": score_floor_lane(output_text),
        "full_lane": score_full_lane(output_text),
        "verdict_boundary": (
            "Lane results are candidate signals evaluated separately. "
            "A floor-lane pass does not make a summary of the canon valid; "
            "full-lane checks here cover selected terms only and do not "
            "certify full-canon validity. Nothing here is an adoption verdict. "
            "Human review required."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score one compression ladder trial record (candidate signals only)."
    )
    parser.add_argument("trial_path", help="Path to a trial record JSON file")
    args = parser.parse_args(argv)

    path = Path(args.trial_path)
    if not path.is_file():
        print(f"ERROR: trial file not found: {path}", file=sys.stderr)
        return 2
    try:
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
