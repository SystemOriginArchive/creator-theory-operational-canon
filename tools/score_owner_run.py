#!/usr/bin/env python3
"""Dual-lane batch scorer for owner-run staging records.

Scores every filled record under experiments/_incoming/ (templates skipped)
under BOTH standards from docs/FALSIFICATION_REGISTER.md:

  legacy full-invariant lane  (CL-01 full lane, selected invariant terms)
  kernel+pointer lane         (CL-02 floor lane, K1-K5 incl. pointer rule)

and prints a side-by-side summary per model and per arm/budget. All outputs
are candidate signals only: not adoption verdicts, not violation verdicts,
not certification, and no substitute for the human-review checklist in
experiments/OWNER_RUNBOOK_KO.md. Standard library only; no network access.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.score_adoption_drift import score_trial as score_drift_trial  # noqa: E402
from tools.score_compression_ladder import (  # noqa: E402
    score_floor_lane,
    score_full_lane,
    score_trial as score_ladder_trial,
)

DEFAULT_DIR = Path(__file__).resolve().parents[1] / "experiments" / "_incoming"


def lane_mark(passed: bool) -> str:
    return "PASS" if passed else "FAIL"


def score_record(data: dict) -> dict:
    record_type = data.get("record_type")
    output_text = data.get("output_text") or ""
    if record_type == "adoption_drift_trial":
        drift = score_drift_trial(data)
        floor = score_floor_lane(output_text)
        full = score_full_lane(output_text)
        label = data.get("owner_run_label") or data.get("evaluation_arm") or data.get("prompt_id")
        group = data.get("evaluation_arm") or data.get("prompt_id")
        extra = " ".join(
            f"{name.split('_')[0]} {value}" for name, value in sorted(drift["scores"].items())
        )
    elif record_type == "compression_ladder_trial":
        ladder = score_ladder_trial(data)
        floor = ladder["floor_lane"]
        full = ladder["full_lane"]
        label = data.get("owner_run_label") or data.get("prompt_id")
        variant = data.get("variant_id")
        group = f"{data.get('prompt_id')}" + (f" {variant}" if variant else "")
        extra = f"words {ladder['trial']['output_word_count']}"
    else:
        raise ValueError(f"unknown record_type: {record_type!r}")
    return {
        "kind": "drift" if record_type == "adoption_drift_trial" else "ladder",
        "model": data.get("model_id", "?"),
        "label": label,
        "group": group,
        "legacy_full_lane": bool(full["passed"]),
        "kernel_pointer_floor_lane": bool(floor["passed"]),
        "extra": extra,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Dual-lane scoring of all filled owner-run records (candidate signals only)."
    )
    parser.add_argument("directory", nargs="?", default=str(DEFAULT_DIR),
                        help="staging directory (default: experiments/_incoming)")
    args = parser.parse_args(argv)
    staging = Path(args.directory)
    if not staging.is_dir():
        print(f"ERROR: staging directory not found: {staging}", file=sys.stderr)
        return 2

    files = sorted(
        path for path in staging.glob("*.json") if not path.name.endswith(".template.json")
    )
    if not files:
        print("No filled records found (templates are skipped). Nothing scored; no result exists.")
        return 0

    rows: list[dict] = []
    errors: list[str] = []
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            row = score_record(data)
            row["file"] = path.name
            rows.append(row)
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: {exc}")

    models = sorted({row["model"] for row in rows})
    for model in models:
        print(f"== model: {model} ==")
        for row in (r for r in rows if r["model"] == model):
            print(
                f"  {row['kind']:6} {row['label']:34} "
                f"legacy(full): {lane_mark(row['legacy_full_lane']):4}  "
                f"kernel+pointer(floor): {lane_mark(row['kernel_pointer_floor_lane']):4}  "
                f"[{row['extra']}]"
            )
        subset = [r for r in rows if r["model"] == model]
        legacy_pass = sum(r["legacy_full_lane"] for r in subset)
        floor_pass = sum(r["kernel_pointer_floor_lane"] for r in subset)
        print(f"  -- totals: {len(subset)} records | legacy(full) {legacy_pass}/{len(subset)} | "
              f"kernel+pointer(floor) {floor_pass}/{len(subset)}")

    groups = sorted({row["group"] for row in rows})
    print("== per arm/budget (all models) ==")
    for group in groups:
        subset = [r for r in rows if r["group"] == group]
        legacy_pass = sum(r["legacy_full_lane"] for r in subset)
        floor_pass = sum(r["kernel_pointer_floor_lane"] for r in subset)
        print(f"  {group:34} legacy(full) {legacy_pass}/{len(subset)} | "
              f"kernel+pointer(floor) {floor_pass}/{len(subset)}")

    if errors:
        print("== errors (records not scored) ==", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)

    print(
        "Boundary: all numbers above are candidate signals only - not adoption verdicts, "
        "not violation verdicts, not certification. Human review per "
        "experiments/OWNER_RUNBOOK_KO.md is required before any interpretation; "
        "T1-T3 decisions follow docs/FALSIFICATION_REGISTER.md."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
