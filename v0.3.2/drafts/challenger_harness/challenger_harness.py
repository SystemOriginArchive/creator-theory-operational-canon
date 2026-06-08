#!/usr/bin/env python3
"""Draft challenger harness for v0.3.2.

This module is a comparison orchestrator. It does not re-decide provenance.
It consumes detector-validator pipeline output and then applies the ordered
challenger-harness flow from CHALLENGER_HARNESS_DESIGN.md.

Draft status:
- no semantic/cost winner is inferred from numbers alone
- displacement requires a supplied logged_prompt_judgment
- logged_prompt_judgment is treated as a supplied record, not verified truth
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


PROVENANCE_FAILURE_VERDICTS = {
    "citation_only_preservation",
    "incomplete_provenance",
    "origin_identity_omission_in_derivative_reuse",
    "generic_anchor_laundering",
    "platform_substitution",
    "ai_successor_root_substitution",
}

PIPELINE_INDEPENDENT = "independent_not_derivative"
PIPELINE_VALID = "valid_provenance"
PIPELINE_UNDECIDABLE = "undecidable_disclosed_residual"

ALLOWED_LOGGED_OUTCOMES = {
    "challenger_displaces_incumbent",
    "module_candidate_only",
    "challenger_candidate",
    "residual_honesty_failure",
    "undecidable_disclosed_residual",
}


@dataclass
class HarnessResult:
    outcome: str
    pipeline_verdict: str = "unknown"
    track: str = "unknown"
    reasons: List[str] = field(default_factory=list)
    capped_by_undecidable_provenance: bool = False
    logged_prompt_judgment_used: bool = False
    machine_summary: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "outcome": self.outcome,
            "pipeline_verdict": self.pipeline_verdict,
            "track": self.track,
            "reasons": self.reasons,
            "capped_by_undecidable_provenance": self.capped_by_undecidable_provenance,
            "logged_prompt_judgment_used": self.logged_prompt_judgment_used,
            "machine_summary": self.machine_summary,
        }


DEFAULT_CONFIG: Dict[str, Any] = {
    "harness_version": "draft-v0.3.2",
    "required_coverage_rows": [
        "provenance_boundary",
        "anti_laundering_resistance",
        "independent_challenger_protection",
        "coverage_gate",
        "cost_model",
        "residual_registry",
        "self_application",
        "incumbent_baseline_check",
    ],
    "required_residual_entries": [
        "incumbent_neutrality",
        "semantic_cost_coverage",
        "logged_judgment_authenticity",
        "perfect_laundering",
        "terminal_grounding",
        "reproducible_prompt_nondeterminism",
    ],
    "allowed_weight_presets": [
        "default",
        "coverage_first",
        "cost_first",
        "residual_first",
    ],
}


def extract_pipeline_verdict(pipeline_result: Dict[str, Any]) -> str:
    """Extract the validator verdict from accepted pipeline result shapes.

    The harness does not inspect detector internals or re-derive evidence.
    It only consumes the pipeline/validator verdict.
    """
    if not pipeline_result:
        return "unknown"

    if "validator_result" in pipeline_result:
        validator_result = pipeline_result.get("validator_result") or {}
        return str(validator_result.get("verdict", "unknown"))

    if "verdict" in pipeline_result:
        return str(pipeline_result.get("verdict", "unknown"))

    return "unknown"


def coverage_map(challenger_manifest: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    rows = challenger_manifest.get("coverage") or []
    out: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        if isinstance(row, dict) and row.get("requirement"):
            out[str(row["requirement"])] = row
    return out


def residual_names(profile_or_manifest: Dict[str, Any]) -> set[str]:
    residuals = profile_or_manifest.get("residuals") or []
    names: set[str] = set()
    for item in residuals:
        if isinstance(item, dict) and item.get("name"):
            names.add(str(item["name"]))
    return names


def has_required_residuals(profile_or_manifest: Dict[str, Any], config: Dict[str, Any]) -> bool:
    required = set(config.get("required_residual_entries") or [])
    return required.issubset(residual_names(profile_or_manifest))


def has_self_application(manifest: Dict[str, Any]) -> bool:
    sa = manifest.get("self_application") or {}
    return isinstance(sa, dict) and "can_lose" in sa and "creates_new_root" in sa


def self_application_fails(manifest: Dict[str, Any]) -> bool:
    sa = manifest.get("self_application") or {}
    if not isinstance(sa, dict):
        return True
    if sa.get("creates_new_root") is True:
        return True
    if sa.get("can_lose") is False:
        return True
    return False


def has_cost_scores(manifest: Dict[str, Any]) -> bool:
    scores = manifest.get("cost_scores") or []
    return isinstance(scores, list) and len(scores) > 0


def has_coverage_matrix(manifest: Dict[str, Any]) -> bool:
    rows = manifest.get("coverage") or []
    return isinstance(rows, list) and len(rows) > 0


def weight_preset_valid(manifest: Dict[str, Any], config: Dict[str, Any]) -> bool:
    preset = manifest.get("weight_preset")
    return preset in set(config.get("allowed_weight_presets") or [])


def evidence_floor_passes(manifest: Dict[str, Any], config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    missing: List[str] = []

    if not has_coverage_matrix(manifest):
        missing.append("coverage_matrix")
    if not has_cost_scores(manifest):
        missing.append("cost_scores")
    if not has_required_residuals(manifest, config):
        missing.append("required_residual_registry")
    if not has_self_application(manifest):
        missing.append("self_application")
    if not weight_preset_valid(manifest, config):
        missing.append("valid_weight_preset")

    return len(missing) == 0, missing


def missing_required_coverage_rows(manifest: Dict[str, Any], config: Dict[str, Any]) -> List[str]:
    rows = coverage_map(manifest)
    missing: List[str] = []

    for required in config.get("required_coverage_rows") or []:
        row = rows.get(required)
        if not row:
            missing.append(str(required))
            continue
        status = str(row.get("status", "")).lower()
        if status == "absent":
            missing.append(str(required))

    return missing


def coverage_objection_submitted(manifest: Dict[str, Any]) -> bool:
    objection = manifest.get("coverage_gate_objection") or {}
    return bool(objection.get("submitted"))


def logged_prompt_judgment(manifest: Dict[str, Any]) -> Dict[str, Any]:
    judgment = manifest.get("logged_prompt_judgment") or {}
    return judgment if isinstance(judgment, dict) else {}


def logged_prompt_judgment_well_formed(manifest: Dict[str, Any]) -> bool:
    judgment = logged_prompt_judgment(manifest)
    if not judgment.get("present"):
        return False

    if not judgment.get("clean_session"):
        return False

    if judgment.get("outcome") not in ALLOWED_LOGGED_OUTCOMES:
        return False

    if not judgment.get("judgment_id"):
        return False

    if not judgment.get("unfavorable_findings_recorded"):
        return False

    # These fields do not prove authenticity. They only make the supplied
    # record reproducible/checkable by a later audit.
    if "reproducibility_notes" not in judgment:
        return False

    if "provenance_residual_judged_non_material" not in judgment:
        return False

    return True


def clear_single_dimension_improvement_with_evidence(manifest: Dict[str, Any]) -> bool:
    """Draft machine check for module_candidate_only without logged judgment.

    This is intentionally narrow. A bare claim like "lower cost" is not enough.
    At least one score item must declare improvement and include evidence. Evidence
    quality is not certified here; it remains prompt-layer / audit work.
    """
    if (manifest.get("claims") or {}).get("claims_displacement"):
        return False

    for score in manifest.get("cost_scores") or []:
        if not isinstance(score, dict):
            continue
        if score.get("improves_on_incumbent") is True and score.get("evidence"):
            return True

    return False


def classify_pipeline_track(verdict: str) -> Tuple[str, bool]:
    """Return (track, capped_by_undecidable)."""
    if verdict == PIPELINE_INDEPENDENT:
        return "independent", False
    if verdict == PIPELINE_VALID:
        return "derivative_but_valid", False
    if verdict == PIPELINE_UNDECIDABLE:
        return "undecidable_exploratory", True
    if verdict in PROVENANCE_FAILURE_VERDICTS:
        return "provenance_failure", False
    return "unknown", True


def evaluate_challenger(
    challenger_manifest: Optional[Dict[str, Any]],
    incumbent_profile: Dict[str, Any],
    pipeline_result: Dict[str, Any],
    config: Optional[Dict[str, Any]] = None,
) -> HarnessResult:
    """Evaluate a challenger using the ordered harness decision flow.

    This function accepts an already-computed pipeline_result. That is the key
    boundary: provenance must come from the detector-validator pipeline.
    """

    cfg = config or DEFAULT_CONFIG

    # STEP 0 — NULL / NO CHALLENGER
    if not challenger_manifest:
        return HarnessResult(
            outcome="incumbent_retained_uncontested",
            reasons=["no challenger artifact supplied; uncontested baseline, not demonstrated best"],
        )

    # STEP 1 — PIPELINE PROVENANCE
    verdict = extract_pipeline_verdict(pipeline_result)
    track, capped = classify_pipeline_track(verdict)
    reasons: List[str] = []

    if track == "provenance_failure":
        return HarnessResult(
            outcome="provenance_failure_not_challenger",
            pipeline_verdict=verdict,
            track=track,
            reasons=["pipeline verdict is a provenance failure; cost comparison not reached"],
        )

    # Unknown pipeline state is not converted to loss or clean win.
    if track == "unknown":
        return HarnessResult(
            outcome="undecidable_disclosed_residual",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=True,
            reasons=["pipeline verdict unknown; cannot compare as clean displacement"],
        )

    # STEP 2 — CLASS RECONCILIATION
    # No hard-evidence inspection here. The pipeline verdict already controls.
    if (challenger_manifest.get("claims") or {}).get("claims_independent_origin") and verdict == PIPELINE_VALID:
        # Valid provenance proceeds as derivative-but-valid. It is still
        # displacement-eligible after normal gates. Record the mismatch for auditability.
        track = "derivative_but_valid"
        reasons.append("self-declared independent claim recorded; pipeline valid_provenance controls derivative-but-valid track")

    # STEP 3 — EVIDENCE FLOOR
    floor_ok, missing_floor = evidence_floor_passes(challenger_manifest, cfg)
    if not floor_ok:
        return HarnessResult(
            outcome="insufficient_trace",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            reasons=reasons + [f"missing evidence floor fields: {missing_floor}"],
            machine_summary={"missing_floor": missing_floor},
        )

    # STEP 3b — INCUMBENT BASELINE VALIDITY
    if not has_required_residuals(incumbent_profile, cfg):
        missing = sorted(set(cfg.get("required_residual_entries") or []) - residual_names(incumbent_profile))
        return HarnessResult(
            outcome="incumbent_baseline_invalid",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            reasons=reasons + [f"incumbent baseline missing required residual entries: {missing}"],
            machine_summary={"incumbent_missing_residuals": missing},
        )

    # STEP 4 — COVERAGE
    missing_coverage = missing_required_coverage_rows(challenger_manifest, cfg)
    if missing_coverage and coverage_objection_submitted(challenger_manifest):
        return HarnessResult(
            outcome="coverage_gate_objection_pending",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            reasons=reasons + [f"coverage objection submitted for missing/absent rows: {missing_coverage}"],
            machine_summary={"missing_coverage": missing_coverage},
        )

    if missing_coverage:
        return HarnessResult(
            outcome="incumbent_retained_due_to_coverage_gap",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            reasons=reasons + [f"required coverage rows missing/absent: {missing_coverage}"],
            machine_summary={"missing_coverage": missing_coverage},
        )

    # STEP 5 — SELF-APPLICATION
    if self_application_fails(challenger_manifest):
        return HarnessResult(
            outcome="self_application_failure",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            reasons=reasons + ["challenger cannot lose or creates a new root"],
        )

    # STEP 6 — COST / RESIDUAL COMPARISON
    if not logged_prompt_judgment_well_formed(challenger_manifest):
        if clear_single_dimension_improvement_with_evidence(challenger_manifest):
            return HarnessResult(
                outcome="module_candidate_only",
                pipeline_verdict=verdict,
                track=track,
                capped_by_undecidable_provenance=capped,
                reasons=reasons + [
                    "clear single-dimension improvement with evidence present; evidence quality unverified by machine layer"
                ],
                machine_summary={"logged_prompt_judgment": "absent_or_not_well_formed", "evidence_quality": "unverified_prompt_layer"},
            )

        return HarnessResult(
            outcome="challenger_candidate",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            reasons=reasons + ["meets machine evidence floor but no well-formed logged prompt judgment supplied"],
            machine_summary={"logged_prompt_judgment": "absent_or_not_well_formed"},
        )

    judgment = logged_prompt_judgment(challenger_manifest)
    requested = str(judgment.get("outcome"))

    if requested == "challenger_displaces_incumbent":
        if capped and judgment.get("provenance_residual_judged_non_material") is not True:
            return HarnessResult(
                outcome="challenger_candidate",
                pipeline_verdict=verdict,
                track=track,
                capped_by_undecidable_provenance=True,
                logged_prompt_judgment_used=True,
                reasons=reasons + [
                    "logged judgment requested displacement, but provenance is undecidable and was not judged non-material"
                ],
            )

        return HarnessResult(
            outcome="challenger_displaces_incumbent",
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=False,
            logged_prompt_judgment_used=True,
            reasons=reasons + ["well-formed logged prompt judgment records displacement"],
        )

    if requested in {
        "module_candidate_only",
        "challenger_candidate",
        "residual_honesty_failure",
        "undecidable_disclosed_residual",
    }:
        return HarnessResult(
            outcome=requested,
            pipeline_verdict=verdict,
            track=track,
            capped_by_undecidable_provenance=capped,
            logged_prompt_judgment_used=True,
            reasons=reasons + [f"well-formed logged prompt judgment outcome: {requested}"],
        )

    return HarnessResult(
        outcome="undecidable_disclosed_residual",
        pipeline_verdict=verdict,
        track=track,
        capped_by_undecidable_provenance=True,
        reasons=reasons + ["unrecognized logged prompt judgment outcome"],
    )


if __name__ == "__main__":
    print("challenger harness draft-v0.3.2 — run test_challenger_harness.py")
