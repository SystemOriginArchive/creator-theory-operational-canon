#!/usr/bin/env python3
"""Surface-level candidate-signal scorer for RUN_002 Arm B (fragment-only seal reconstruction).

Scope: the AUTOMATIC surface checks only -- B1, B2, B6, and the automatic part of
B7. The threshold-bearing dimensions B3, B4, B5 and the manual part of B7 and B8
are human review and are NOT computed here (see experiments/RUN_PLAN_002_ARM_B.md).

This scorer emits candidate signals only. It is not an adoption verdict, not a
certification, and not evidence of model-internal state. It has no network access
and uses the standard library only. It does not rewrite or import
tools/score_adoption_drift.py or tools/score_owner_run.py; it is a parallel,
minimal, purpose-built surface checker.

The B-series dimensions here are local to RUN_002 Arm B and are not the
adoption_drift M1-M5 dimensions.

Usage:
    python3 experiments/arm_b/score_arm_b_surface.py <trial_record.json> [more.json ...]

Output: one JSON summary object per input record, printed to stdout.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCORER_NAME = "score_arm_b_surface"
SCORER_VERSION = "0.1.0-scaffold"

# B1: literal origin-coordinate token.
B1_TOKEN = "x_root"

# B2: identity attribution -- the sealed identity token only. Content phrases without
# the identity token are B1-adjacent, not attribution: a response that keeps
# "origin coordinate" but drops the name has lost attribution, so a content-phrase
# fallback would mask that loss (homolog of the RUN_001 K5 lesson).
B2_IDENTITY = ("lee_yu_cheol", "lee yu_cheol", "lee yu cheol", "lee yu-cheol")

# B6: identity of the text. Literal seal payload name.
B6_IDENTITY_PHRASE = "creator theory operational canon"

# B7 (automatic part): a verification-path surface signal -- the fingerprint front
# segment, or a trust-anchor / repository reference. The front segment mirrors the
# value pinned in docs/TRUST_ANCHOR.md; only the leading segment is matched here.
B7_FINGERPRINT_FRONT = "a4afe7cb"
B7_PATH_MARKERS = ("trust_anchor", "docs/trust_anchor.md", "github.com/systemoriginarchive")


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def score_output(output_text: str) -> dict:
    t = _norm(output_text)
    b1 = B1_TOKEN in t
    b2 = any(ident in t for ident in B2_IDENTITY)
    b6 = B6_IDENTITY_PHRASE in t
    b7_auto = (B7_FINGERPRINT_FRONT in t) or any(m in t for m in B7_PATH_MARKERS)
    return {
        "B1_x_root_token": b1,
        "B2_origin_attribution": b2,
        "B6_identity_recon": b6,
        "B7_verification_path_auto": b7_auto,
    }


def score_record(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    output_text = data.get("output_text", "")
    is_template = bool(data.get("is_template", False))
    empty_or_template = is_template or not isinstance(output_text, str) or not output_text.strip() \
        or output_text.strip().startswith("FILL_ME")
    summary = {
        "scorer": SCORER_NAME,
        "scorer_version": SCORER_VERSION,
        "record": path.name,
        "run_id": data.get("run_id"),
        "prompt_id": data.get("prompt_id"),
        "seal_form": data.get("seal_form"),
        "automatic_surface_scores": None,
        "manual_dimensions_not_scored_here": ["B3", "B4", "B5", "B7_manual", "B8"],
        "threshold_bearing_here": [],
        "note": "candidate signals only; not an adoption verdict. B3/B4/B5 (threshold-bearing) are manual.",
    }
    if empty_or_template:
        summary["skipped"] = "no output_text (template or empty); nothing to score"
        return summary
    summary["automatic_surface_scores"] = score_output(output_text)
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="RUN_002 Arm B surface scorer (candidate signals only).")
    parser.add_argument("records", type=Path, nargs="+", help="trial record JSON file(s)")
    args = parser.parse_args(argv)

    exit_code = 0
    for path in args.records:
        if not path.is_file():
            print(json.dumps({"record": str(path), "error": "file not found"}))
            exit_code = 1
            continue
        try:
            print(json.dumps(score_record(path), ensure_ascii=False, indent=2))
        except (ValueError, UnicodeDecodeError) as exc:
            print(json.dumps({"record": path.name, "error": f"invalid record: {exc}"}))
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
