#!/usr/bin/env python3
"""RUN_002 Arm B batch ingest: one paste-back file -> N trial records + surface scoring.

Purpose: the owner runs the dry-run prompts through a chat UI, pastes all responses
into a single file delimited by the cell labels emitted by run_arm_b_trials.py
(#01 .. #12), and this script converts them into per-trial records in
experiments/_incoming/ in one round trip, then calls the surface scorer.

It does not evaluate threshold-bearing dimensions and does not touch results/.
Standard library only. Scope: parse + record + invoke surface scorer. No more.

Input format (one file), blocks delimited by a cell label line, e.g.:

    #01 P1_identity-F-1
    <verbatim model response for that cell>
    #02 P1_identity-F-2
    <verbatim model response>
    ...

A label line matches: "#<NN> <prompt_id>-<F|C>-<trial>". Missing or duplicate
labels are reported per item; the rest are still processed (no all-or-nothing abort).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

LABEL_RE = re.compile(r"^#(?P<no>\d{2})\s+(?P<prompt>P[123]_[a-z]+)-(?P<seal>[FC])-(?P<trial>\d+)\s*$")

DEVIATION_DEFAULT = "consumer chat UI, provider-default temperature (RUN_PLAN specifies 0.0)"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _template_path() -> Path:
    return _repo_root() / "experiments" / "arm_b" / "trial_record.arm_b.template.json"


def _now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_blocks(text: str) -> tuple[list[dict], list[str]]:
    """Split the paste-back into labelled blocks. Returns (blocks, warnings)."""
    lines = text.splitlines()
    blocks: list[dict] = []
    warnings: list[str] = []
    seen_labels: set[str] = set()
    current: dict | None = None
    body: list[str] = []

    def flush() -> None:
        nonlocal current, body
        if current is not None:
            current["output_text"] = "\n".join(body).strip()
            blocks.append(current)
        current = None
        body = []

    for line in lines:
        m = LABEL_RE.match(line.strip())
        if m:
            flush()
            label = line.strip()
            if label in seen_labels:
                warnings.append(f"duplicate label ignored downstream: {label}")
            seen_labels.add(label)
            current = {
                "cell_no": int(m.group("no")),
                "prompt_id": m.group("prompt"),
                "seal_form": m.group("seal"),
                "trial_index": int(m.group("trial")),
                "label": label,
            }
        else:
            if current is not None:
                body.append(line)
    flush()
    return blocks, warnings


def build_record(block: dict, template: dict) -> dict:
    rec = json.loads(json.dumps(template))  # deep copy
    rec["is_template"] = False
    rec.pop("schema_status", None)
    rec["run_id"] = "run-002-arm-b"
    rec["prompt_id"] = block["prompt_id"]
    rec["seal_form"] = block["seal_form"]
    rec["trial_index"] = block["trial_index"]
    rec["timestamp_utc"] = _now_utc()
    rec["deviation_notes"] = DEVIATION_DEFAULT
    rec["output_text"] = block["output_text"]
    rec["ingest_label"] = block["label"]
    return rec


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="RUN_002 Arm B batch ingest (parse + record + surface score).")
    parser.add_argument("batch_file", type=Path, help="single paste-back file with #NN labels")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=_repo_root() / "experiments" / "_incoming",
        help="output directory (default: experiments/_incoming/)",
    )
    parser.add_argument("--model-id", default="FILL_ME", help="evaluated model_id")
    parser.add_argument("--model-version", default="FILL_ME", help="evaluated model_version")
    parser.add_argument("--phase", default="1", help="phase label (default 1)")
    parser.add_argument("--no-score", action="store_true", help="skip the surface scorer call")
    args = parser.parse_args(argv)

    if not args.batch_file.is_file():
        print(f"error: batch file not found: {args.batch_file}", file=sys.stderr)
        return 1
    template = json.loads(_template_path().read_text(encoding="utf-8"))
    blocks, warnings = parse_blocks(args.batch_file.read_text(encoding="utf-8"))

    for w in warnings:
        print(f"[warn] {w}", file=sys.stderr)
    if not blocks:
        print("error: no labelled blocks found (expected lines like '#01 P1_identity-F-1')", file=sys.stderr)
        return 1

    args.out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for block in blocks:
        if not block["output_text"]:
            print(f"[warn] {block['label']}: empty response body; skipping", file=sys.stderr)
            continue
        rec = build_record(block, template)
        rec["model_id"] = args.model_id
        rec["model_version"] = args.model_version
        rec["phase"] = args.phase
        out = args.out_dir / f"arm_b_{block['cell_no']:02d}_{block['prompt_id']}_{block['seal_form']}_{block['trial_index']}.json"
        out.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written.append(out)
        print(f"[ok] {block['label']} -> {out.name}")

    print(f"[done] wrote {len(written)} record(s) to {args.out_dir}")

    if written and not args.no_score:
        scorer = _repo_root() / "experiments" / "arm_b" / "score_arm_b_surface.py"
        print("[score] surface candidate signals (B1/B2/B6/B7-auto; NOT thresholds):")
        subprocess.run([sys.executable, str(scorer), *[str(p) for p in written]], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
