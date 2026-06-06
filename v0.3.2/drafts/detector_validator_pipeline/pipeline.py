"""detector-validator pipeline (draft-v0.3.2).

Thin integration harness connecting:
- anti_laundering_detector.detector.detect()
- provenance_validator.provenance_validator.validate_candidate()

This module adds no new final verdict semantics. It translates detector output
into validator input and returns both outputs for auditability.
"""

from __future__ import annotations
import json
import pathlib
import sys
from typing import Any, Dict, Optional

HERE = pathlib.Path(__file__).resolve().parent
DRAFTS = HERE.parent
DETECTOR_DIR = DRAFTS / "anti_laundering_detector"
VALIDATOR_DIR = DRAFTS / "provenance_validator"

sys.path.insert(0, str(DETECTOR_DIR))
sys.path.insert(0, str(VALIDATOR_DIR))

from detector import detect  # type: ignore  # noqa: E402
from provenance_validator import DEFAULT_MANIFEST, validate_candidate  # type: ignore  # noqa: E402


def load_detector_config(path: Optional[pathlib.Path] = None) -> Dict[str, Any]:
    config_path = path or DETECTOR_DIR / "config.json"
    return json.loads(config_path.read_text(encoding="utf-8"))


def build_validator_candidate(
    candidate_manifest: Dict[str, Any],
    detector_output: Dict[str, Any],
) -> Dict[str, Any]:
    """Map detector evidence into the existing validator candidate schema."""
    detector_evidence = dict(detector_output.get("derivation_evidence") or {})
    summary = detector_output.get("evidence_summary") or {}

    return {
        "candidate_id": candidate_manifest.get("candidate_id", "unknown"),
        "reuse_scope": candidate_manifest.get("reuse_scope", "unknown"),
        "claims": candidate_manifest.get("claims", {}),
        "derivation_evidence": detector_evidence,
        "structural_resemblance_only": bool(summary.get("structural_resemblance_only")),
        "preserved_fields": candidate_manifest.get("preserved_fields", []),
        "citation_only_fields": candidate_manifest.get("citation_only_fields", []),
        "substitutions": candidate_manifest.get("substitutions", {}),
    }


def run_pipeline(
    source_manifest: Dict[str, Any],
    source_files: Dict[str, str],
    candidate_manifest: Dict[str, Any],
    candidate_files: Dict[str, str],
    detector_config: Optional[Dict[str, Any]] = None,
    validator_manifest: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Run detector, translate evidence, run validator, and return both."""
    config = detector_config or load_detector_config()
    vmanifest = validator_manifest or DEFAULT_MANIFEST

    detector_output = detect(
        source_manifest=source_manifest,
        source_files=source_files,
        candidate_manifest=candidate_manifest,
        candidate_files=candidate_files,
        config=config,
    )
    validator_candidate = build_validator_candidate(candidate_manifest, detector_output)
    validator_result = validate_candidate(vmanifest, validator_candidate)

    return {
        "candidate_id": candidate_manifest.get("candidate_id", "unknown"),
        "detector_output": detector_output,
        "validator_candidate": validator_candidate,
        "validator_result": validator_result.to_dict(),
    }


if __name__ == "__main__":
    print("detector-validator pipeline draft-v0.3.2 — run test_pipeline.py")
