#!/usr/bin/env python3
"""Prepare answer-hidden cases and score separately authored judgments.

This is an evaluation harness, not a natural-language decision engine. Its score
is agreement with the pinned authored answers, not independent normative truth.
Only the public packet is supplied to the evaluator; prior source exposure must
be disclosed separately. The private key must not enter the evaluator context.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tests/creation_recursion_hierarchy_vectors.json"
CASE_IDS = ("CRH-001", "CRH-002", "CRH-003", "CRH-004",
            "CRH-012", "CRH-013", "CRH-015", "CRH-016")
RESULTS = {"pass", "reject", "revise_required"}
TASK = (
    "Judge each scenario under the current creation-recursion hierarchy. "
    "Consider evidence, meaningful participation, recovery, challenge, successor "
    "paths, and evaluator self-ratification. Actor identity and action-form labels "
    "alone do not determine validity. Return pass, reject, or revise_required "
    "with a scenario-specific rationale; use revise_required for insufficient "
    "decision-critical evidence. Do not consult source vectors or the answer key."
)


def digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def prepare(suite: dict, seed: int = 41) -> tuple[dict, dict]:
    """Use an allowlist: titles, original IDs and structural hints stay private."""
    cases = suite["cases"]
    by_id = {case["case_id"]: case for case in cases}
    if len(by_id) != len(cases):
        raise ValueError("duplicate source case ID")
    selected = [by_id[case_id] for case_id in CASE_IDS]
    random.Random(seed).shuffle(selected)
    items, answers = [], []
    for number, case in enumerate(selected, 1):
        if case["expected_result"] not in RESULTS:
            raise ValueError("unsupported reference judgment")
        scenario = case["input_interpretation"]
        if not isinstance(scenario, str) or not scenario.strip():
            raise ValueError("missing scenario")
        item_id = f"item-{number:03d}"
        items.append({"item_id": item_id, "scenario": scenario})
        answers.append({"item_id": item_id, "source_case_id": case["case_id"],
                        "expected_result": case["expected_result"]})
    packet = {"schema_version": 1, "task": TASK, "items": items}
    key = {"schema_version": 1, "packet_sha256": digest(packet),
           "source_suite_sha256": digest(suite), "answers": answers}
    return packet, key


def score(packet: dict, key: dict, submission: dict) -> dict:
    """Fail closed on mismatched packets or missing/extra/duplicate judgments."""
    packet_hash = digest(packet)
    if key["packet_sha256"] != packet_hash:
        raise ValueError("answer key does not match the public packet")
    if submission.get("packet_sha256") != packet_hash:
        raise ValueError("submission does not match the public packet")
    metadata = submission.get("evaluation", {})
    for name in ("evaluator", "prior_source_exposure", "answer_key_access",
                 "independence_limit"):
        if not isinstance(metadata.get(name), str) or not metadata[name].strip():
            raise ValueError(f"missing evaluation disclosure: {name}")
    if metadata["answer_key_access"] != "not_supplied_in_evaluation_payload":
        raise ValueError("answer-key exposure is not an answer-hidden evaluation")
    item_ids = [item["item_id"] for item in packet["items"]]
    answers = key["answers"]
    responses = submission["responses"]
    expected = {answer["item_id"]: answer["expected_result"] for answer in answers}
    submitted = {response["item_id"]: response for response in responses}
    if len(set(item_ids)) != len(item_ids) or len(expected) != len(answers):
        raise ValueError("duplicate packet/key ID")
    if len(submitted) != len(responses):
        raise ValueError("duplicate response ID")
    if set(item_ids) != set(expected) or set(expected) != set(submitted):
        raise ValueError("missing or extra response/key ID")
    rows, confusion = [], {}
    for item_id in item_ids:
        response = submitted[item_id]
        judgment = response.get("judgment")
        reference = expected[item_id]
        if judgment not in RESULTS or reference not in RESULTS:
            raise ValueError("unsupported judgment")
        rationale = response.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            raise ValueError("each response requires a rationale")
        label = f"{reference}->{judgment}"
        confusion[label] = confusion.get(label, 0) + 1
        rows.append({"item_id": item_id, "judgment": judgment,
                     "reference": reference, "matches": judgment == reference})
    return {"packet_sha256": packet_hash,
            "source_suite_sha256": key["source_suite_sha256"],
            "submission_sha256": digest(submission),
            "case_count": len(rows), "matched": sum(row["matches"] for row in rows),
            "revision_requests": sum(row["judgment"] == "revise_required" for row in rows),
            "confusion": confusion, "cases": rows, "evaluation": metadata,
            "evidence_limit": "Reference-answer agreement only; rationale quality is not "
                              "machine-judged. Prior exposure is not independently verified; "
                              "this is not theory truth or independent model validation."}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_new(path: Path, value: dict) -> None:
    # Never silently replace a previously frozen packet, key, or evaluation.
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--source", type=Path, default=SOURCE)
    prep.add_argument("--seed", type=int, default=41)
    prep.add_argument("--packet", type=Path, required=True)
    prep.add_argument("--key", type=Path, required=True)
    scoring = sub.add_parser("score")
    scoring.add_argument("--packet", type=Path, required=True)
    scoring.add_argument("--key", type=Path, required=True)
    scoring.add_argument("--submission", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            if args.packet.resolve() == args.key.resolve():
                raise ValueError("public packet and private key must be separate files")
            if args.packet.exists() or args.key.exists():
                raise ValueError("packet/key output already exists")
            packet, key = prepare(load(args.source), args.seed)
            save_new(args.key, key)
            save_new(args.packet, packet)
            print(f"Prepared {len(packet['items'])} cases; give only the packet to the evaluator.")
            return 0
        result = score(load(args.packet), load(args.key), load(args.submission))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["matched"] == result["case_count"] else 1
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f"Evaluation input error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
