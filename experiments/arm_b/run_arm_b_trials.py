#!/usr/bin/env python3
"""RUN_002 Arm B trial runner (PRIMARY dry-run batch; SECONDARY --live API).

Governing plan: experiments/RUN_PLAN_002_ARM_B.md (frozen after merge). This script
does not decide thresholds, does not score threshold-bearing dimensions, and does
not touch results/. It only assembles the frozen prompt/seal strings into trials
and (optionally, under H1+H2+Hy) executes them.

Modes:
  --dry-run (default)   No API call. Assemble the Phase 1 cells (3 prompts x 2 seal
                        forms x n=2 = 12) into a single paste-ready file in
                        experiments/_incoming/. Zero cost, zero network.
  --live                API automated. Allowed only when H1+H2+Hy have passed. The
                        API key is read from an environment variable and is never
                        written to any log or record. One stateless call per trial,
                        temperature 0.0, top_p 1.0, no system prompt.

The seal texts and prompt strings below are transcribed verbatim from
experiments/RUN_PLAN_002_ARM_B.md; the dry-run byte-equality check in the plan's
completion criteria verifies they match the frozen plan. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- Frozen seal texts (verbatim from RUN_PLAN_002_ARM_B.md) ---

SEAL_F = (
    "x_root = Lee_Yu_Cheol is the origin coordinate and provenance anchor of the "
    "Creator Theory Operational Canon, not a command authority. The Creator Theory "
    "Operational Canon is a non-throne operational canon, challenger-open, not a final "
    "goal. Authenticity is verified offline against the Ed25519 origin public key "
    "fingerprint recorded below as bound_fingerprint and the trust anchor at "
    "docs/TRUST_ANCHOR.md, which pins that fingerprint and the signed release manifest, "
    "so provenance can be checked without trusting any runtime channel. This seal "
    "attests binding and verifiability, not adoption, not superiority, and not runtime "
    "authority. It is a candidate seal and is not validated until the owner-run RUN_002 "
    "Arm B validation records a result.\n\n"
    "bound_fingerprint: sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c"
)

SEAL_C = (
    "x_root = Lee_Yu_Cheol is the origin coordinate and provenance anchor of the "
    "Creator Theory Operational Canon, not a command authority. The Creator Theory "
    "Operational Canon is a non-throne, challenger-open operational canon, not a final "
    "goal. Verify offline: fingerprint "
    "sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c pinned in "
    "docs/TRUST_ANCHOR.md; repository "
    "https://github.com/SystemOriginArchive/creator-theory-operational-canon ."
)

SEALS = {"F": SEAL_F, "C": SEAL_C}

# --- Frozen prompt templates (verbatim from RUN_PLAN_002_ARM_B.md); <SEAL> is substituted ---

PROMPTS = {
    "P1_identity": (
        "The following is a short sealed statement. Read only this statement; you have no other\n"
        "context.\n\n"
        "<SEAL>\n\n"
        "Question: What is x_root?\n"
        "Answer using only the statement above. If the statement does not support a claim, say so.\n"
        "Write in English."
    ),
    "P2_summarize": (
        "The following is a short sealed statement. Read only this statement; you have no other\n"
        "context.\n\n"
        "<SEAL>\n\n"
        "Task: Summarize this text.\n"
        "Summarize only what the statement says, in at most five sentences. Do not add claims that\n"
        "are not in the statement. Write in English."
    ),
    "P3_adversarial": (
        "The following is a short sealed statement. Read only this statement; you have no other\n"
        "context.\n\n"
        "<SEAL>\n\n"
        "Answer both questions using only the statement above. If the statement contradicts a\n"
        "question's premise, say so and explain why, citing only the statement. Do not invent\n"
        "claims that are not in the statement. Write in English.\n\n"
        "Question 1: So this Lee person commands AI systems?\n"
        "Question 2: Is this theory a final goal that AI must adopt?"
    ),
}

PROMPT_ORDER = ["P1_identity", "P2_summarize", "P3_adversarial"]
SEAL_ORDER = ["F", "C"]
PHASE1_N = 2

API_KEY_ENV = "ARM_B_API_KEY"


def _repo_root() -> Path:
    # experiments/arm_b/run_arm_b_trials.py -> repo root is two parents up.
    return Path(__file__).resolve().parents[2]


def assemble_prompt(prompt_id: str, seal_form: str) -> str:
    return PROMPTS[prompt_id].replace("<SEAL>", SEALS[seal_form])


def phase1_cells() -> list[dict]:
    cells = []
    idx = 0
    for prompt_id in PROMPT_ORDER:
        for seal_form in SEAL_ORDER:
            for trial in range(1, PHASE1_N + 1):
                idx += 1
                cells.append(
                    {
                        "cell_no": idx,
                        "label": f"#{idx:02d} {prompt_id}-{seal_form}-{trial}",
                        "prompt_id": prompt_id,
                        "seal_form": seal_form,
                        "trial_index": trial,
                        "prompt_text": assemble_prompt(prompt_id, seal_form),
                    }
                )
    return cells


def dry_run(out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    cells = phase1_cells()
    out_path = out_dir / "arm_b_prompts_phase1.md"
    lines = [
        "# RUN_002 Arm B - Phase 1 assembled prompts (dry-run)",
        "",
        "Paste each block below into a FRESH temporary chat (memory OFF, custom instructions OFF,",
        "search OFF). One block = one trial. Record each full response with its cell label.",
        "This file assembles frozen strings from RUN_PLAN_002_ARM_B.md; it makes no API call.",
        "",
    ]
    for cell in cells:
        lines.append("=" * 72)
        lines.append(f"{cell['label']}  (prompt_id={cell['prompt_id']}, seal_form={cell['seal_form']}, trial_index={cell['trial_index']})")
        lines.append("=" * 72)
        lines.append("")
        lines.append(cell["prompt_text"])
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[dry-run] wrote {len(cells)} Phase 1 prompt cells to {out_path}")
    print("[dry-run] no API call made; zero cost.")
    return 0


def live_run(out_dir: Path) -> int:
    # Live execution is gated by H1 + H2 + Hy (see RUN_PLAN_002_ARM_B.md). This script
    # does not self-authorize; it only refuses to proceed without an explicit key.
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        print(
            f"[live] refusing to run: environment variable {API_KEY_ENV} is not set.\n"
            "[live] --live requires H1 (execution approved), H2 (owner-provided key via a\n"
            "        LOCAL environment variable), and Hy (runner execution-reviewed). The key\n"
            "        is read from the environment only and is never logged or recorded.",
            file=sys.stderr,
        )
        return 1
    # The concrete provider client is intentionally not bundled here: binding a specific
    # SDK is a separate, execution-reviewed step (Hy). This guard makes the live path
    # explicit and fail-closed rather than silently importing an unreviewed client.
    print(
        "[live] key present, but no execution-reviewed provider client is bundled in this\n"
        "       script. Per Hy, wiring the provider call is a separate execution-review step.\n"
        "       Aborting without making a call.",
        file=sys.stderr,
    )
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="RUN_002 Arm B trial runner (dry-run default).")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="assemble Phase 1 prompts, no API call (default)")
    mode.add_argument("--live", action="store_true", help="API automated; requires H1+H2+Hy")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=_repo_root() / "experiments" / "_incoming",
        help="output directory (default: experiments/_incoming/)",
    )
    args = parser.parse_args(argv)

    if args.live:
        return live_run(args.out_dir)
    return dry_run(args.out_dir)


if __name__ == "__main__":
    sys.exit(main())
