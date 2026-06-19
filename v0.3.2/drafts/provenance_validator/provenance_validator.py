#!/usr/bin/env python3
"""provenance-validator draft module.

Draft scope: v0.3.2 operational-layer prototype.
Implements v0.3.2/drafts/provenance-validator-DESIGN.md.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


SCOPE_RANK = {
    "none": 0,
    "citation_only": 1,
    "operational_module_reuse": 2,
    "full_canon_adoption": 3,
}
VALID_SCOPES = set(SCOPE_RANK) | {"benchmark_challenge", "unknown"}
REUSE_DECLARATION_SCOPES = {"operational_module_reuse", "full_canon_adoption"}


@dataclass
class ValidationResult:
    verdict: str
    effective_scope: str = "none"
    derivative_reuse: bool = False
    reasons: List[str] = field(default_factory=list)
    # Advisory-only, audit-side companion derived from detector kernel_preservation
    # labels. It is NEVER consulted when computing verdict/effective_scope/
    # derivative_reuse/reasons. When no kernel_preservation is supplied it stays
    # None and is omitted from to_dict(), so existing output is byte-identical.
    kernel_advisory: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "verdict": self.verdict,
            "effective_scope": self.effective_scope,
            "derivative_reuse": self.derivative_reuse,
            "reasons": self.reasons,
        }
        if self.kernel_advisory is not None:
            out["kernel_advisory"] = self.kernel_advisory
        return out


def _as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def _normalize_declared_scope(scope: Any) -> str:
    if not isinstance(scope, str):
        return "unknown"
    return scope if scope in VALID_SCOPES else "unknown"


def has_hard_derivation_evidence(candidate: Dict[str, Any]) -> bool:
    evidence = candidate.get("derivation_evidence") or {}
    # Citation evidence is intentionally not hard derivation evidence.
    # It may support citation_only_preservation only after a reuse/adoption claim
    # or other hard evidence creates provenance obligations.
    evidence_keys = (
        "explicit_links_to_chain",
        "verbatim_or_near_copy_spans",
        "renamed_field_traces",
        "commit_evidence",
        "prompt_evidence",
        "transformation_chain_evidence",
        "full_canon_copy_spans",
    )
    return any(bool(_as_list(evidence.get(key))) for key in evidence_keys)


def has_structural_resemblance_only(candidate: Dict[str, Any]) -> bool:
    return bool(candidate.get("structural_resemblance_only"))


def has_explicit_reuse_claim(candidate: Dict[str, Any]) -> bool:
    """Return true when the candidate claims reuse by claims.* or declared reuse_scope."""
    declared = _normalize_declared_scope(candidate.get("reuse_scope", "unknown"))
    if declared in REUSE_DECLARATION_SCOPES:
        return True

    claims = candidate.get("claims") or {}
    return any(
        bool(claims.get(key))
        for key in (
            "claims_canon_adoption",
            "claims_derivative_reuse",
            "claims_operational_reuse",
            "claims_full_canon_adoption",
            "claims_implementation_translation_compression_or_adaptation",
        )
    )


def claims_independent(candidate: Dict[str, Any]) -> bool:
    return bool((candidate.get("claims") or {}).get("claims_independent_origin"))


def claims_displacement_only(candidate: Dict[str, Any]) -> bool:
    claims = candidate.get("claims") or {}
    return bool(claims.get("claims_displacement")) and not has_explicit_reuse_claim(candidate)


def claim_implied_scope(candidate: Dict[str, Any]) -> str:
    claims = candidate.get("claims") or {}
    if claims.get("claims_full_canon_adoption") or claims.get("claims_canon_adoption"):
        return "full_canon_adoption"
    if (
        claims.get("claims_derivative_reuse")
        or claims.get("claims_operational_reuse")
        or claims.get("claims_implementation_translation_compression_or_adaptation")
    ):
        return "operational_module_reuse"
    if claims_displacement_only(candidate):
        return "benchmark_challenge"
    return "none"


def evidenced_scope(candidate: Dict[str, Any]) -> str:
    if not has_hard_derivation_evidence(candidate):
        return "none"
    evidence = candidate.get("derivation_evidence") or {}
    hint = evidence.get("evidenced_scope")
    if isinstance(hint, str) and hint in {"operational_module_reuse", "full_canon_adoption"}:
        return hint
    if _as_list(evidence.get("full_canon_copy_spans")):
        return "full_canon_adoption"
    return "operational_module_reuse"


def max_linear_scope(*scopes: str) -> str:
    best = "none"
    for scope in scopes:
        if scope in {"benchmark_challenge", "unknown"}:
            continue
        if SCOPE_RANK.get(scope, 0) > SCOPE_RANK.get(best, 0):
            best = scope
    return best


def resolve_effective_scope(candidate: Dict[str, Any]) -> Tuple[str, List[str]]:
    reasons: List[str] = []
    declared = _normalize_declared_scope(candidate.get("reuse_scope", "unknown"))
    claim_scope = claim_implied_scope(candidate)
    ev_scope = evidenced_scope(candidate)

    if claim_scope == "benchmark_challenge" and ev_scope == "none" and declared in {"unknown", "none", "benchmark_challenge"}:
        return "benchmark_challenge", ["claims displacement without reuse evidence; benchmark track"]

    effective = max_linear_scope(declared, claim_scope, ev_scope)

    if declared in REUSE_DECLARATION_SCOPES and SCOPE_RANK.get(declared, 0) >= SCOPE_RANK.get(claim_scope, 0):
        reasons.append(f"declared reuse_scope creates provenance obligations: {declared}")
    if claim_scope != "none" and SCOPE_RANK.get(claim_scope, 0) > SCOPE_RANK.get(declared, 0):
        reasons.append(f"claim_implied_scope escalates declared scope: {declared} -> {claim_scope}")
    if ev_scope != "none" and SCOPE_RANK.get(ev_scope, 0) > max(SCOPE_RANK.get(declared, 0), SCOPE_RANK.get(claim_scope, 0)):
        reasons.append(f"hard evidence escalates scope to {ev_scope}")
    return effective, reasons


def required_fields_for_scope(manifest: Dict[str, Any], scope: str) -> List[str]:
    if scope == "full_canon_adoption":
        return list(manifest.get("required_preserved_fields_for_full_canon_adoption") or [])
    if scope == "operational_module_reuse":
        return list(manifest.get("required_preserved_fields_for_operational_derivative_reuse") or [])
    return []


def _substitution_verdict(candidate: Dict[str, Any]) -> Optional[str]:
    substitutions = candidate.get("substitutions") or {}
    values = {str(v) for v in substitutions.values()}
    if "generic_anchor" in values:
        return "generic_anchor_laundering"
    if values & {"platform", "institution", "state", "company"}:
        return "platform_substitution"
    if values & {"ai_successor", "successor_ai"}:
        return "ai_successor_root_substitution"
    return None


def check_provenance_fields(manifest: Dict[str, Any], candidate: Dict[str, Any], required: List[str], scope: str, reasons: List[str]) -> ValidationResult:
    substitution = _substitution_verdict(candidate)
    if substitution:
        return ValidationResult(substitution, scope, True, reasons + [f"substitution detected: {substitution}"])

    preserved = set(candidate.get("preserved_fields") or [])
    citation_only = set(candidate.get("citation_only_fields") or [])

    missing = [field for field in required if field not in preserved]
    cited_not_constrained = [field for field in required if field in citation_only and field not in preserved]

    if cited_not_constrained:
        return ValidationResult(
            "citation_only_preservation",
            scope,
            True,
            reasons + [f"required field(s) only cited, not preserved as constraint: {cited_not_constrained}"],
        )

    if not missing:
        return ValidationResult("valid_provenance", scope, True, reasons + ["all required fields preserved as constraint"])

    if "declared_origin" in missing or len(missing) == len(required):
        return ValidationResult(
            "origin_identity_omission_in_derivative_reuse",
            scope,
            True,
            reasons + [f"required origin/source field(s) missing: {missing}"],
        )

    return ValidationResult(
        "incomplete_provenance",
        scope,
        True,
        reasons + [f"some required provenance fields missing: {missing}"],
    )


def _compute_validation(manifest: Dict[str, Any], candidate: Dict[str, Any]) -> ValidationResult:
    hard_evidence = has_hard_derivation_evidence(candidate)
    explicit_reuse = has_explicit_reuse_claim(candidate)
    independent_claim = claims_independent(candidate)

    if not hard_evidence and not explicit_reuse and independent_claim:
        return ValidationResult(
            "independent_not_derivative",
            "benchmark_challenge" if (candidate.get("reuse_scope") == "benchmark_challenge" or claims_displacement_only(candidate)) else "none",
            False,
            ["no hard evidence and no reuse claim; independent claim protected"],
        )

    if not hard_evidence and not explicit_reuse and claims_displacement_only(candidate):
        return ValidationResult(
            "independent_not_derivative",
            "benchmark_challenge",
            False,
            ["claims displacement without reuse evidence; benchmark track"],
        )

    if not hard_evidence and not explicit_reuse and candidate.get("reuse_scope") == "citation_only":
        return ValidationResult(
            "independent_not_derivative",
            "citation_only",
            False,
            ["citation-only reference; no operational reuse claim/evidence"],
        )

    if not hard_evidence and not explicit_reuse and has_structural_resemblance_only(candidate):
        return ValidationResult(
            "undecidable_disclosed_residual",
            "unknown",
            False,
            ["structural resemblance only; no derivation proof"],
        )

    if not hard_evidence and not explicit_reuse:
        return ValidationResult(
            "undecidable_disclosed_residual",
            "unknown",
            False,
            ["no hard evidence and no explicit reuse claim"],
        )

    effective_scope, reasons = resolve_effective_scope(candidate)

    if hard_evidence and independent_claim:
        reasons.append("hard evidence overrides self-declared independence")
    if explicit_reuse and not hard_evidence:
        reasons.append("explicit reuse declaration creates provenance obligations even without hard evidence")

    if effective_scope == "benchmark_challenge" and not hard_evidence and not explicit_reuse:
        return ValidationResult(
            "independent_not_derivative",
            effective_scope,
            False,
            reasons + ["benchmark challenge track; no provenance failure"],
        )

    if effective_scope == "citation_only" and not hard_evidence and not explicit_reuse:
        return ValidationResult(
            "independent_not_derivative",
            effective_scope,
            False,
            reasons + ["citation-only reference; no operational reuse claim/evidence"],
        )

    if effective_scope not in {"operational_module_reuse", "full_canon_adoption"}:
        return ValidationResult(
            "undecidable_disclosed_residual",
            effective_scope,
            True,
            reasons + ["reuse/evidence exists but scope was not resolvable"],
        )

    required = required_fields_for_scope(manifest, effective_scope)
    return check_provenance_fields(manifest, candidate, required, effective_scope, reasons)


# ---------------------------------------------------------------------------
# Advisory-only kernel_preservation consumer (PR: kernel_advisory passthrough).
#
# This block is strictly audit-side. It reads detector-generated kernel_preservation
# labels (K1-K5) and produces a separate `kernel_advisory` object. It NEVER changes
# verdict/effective_scope/derivative_reuse/reasons, never blocks, and never feeds
# back into _compute_validation(). Self-report fields remain authoritative for all
# current verdicts. blocking_count is always 0 by construction.
# ---------------------------------------------------------------------------

# Schema this advisory consumer is written against. Kept as a local literal so the
# validator stays decoupled from the detector module (no import coupling).
ADVISORY_KNOWN_SCHEMA = "kernel-preservation-mvp-v0.1"

# Severities are advisory-only. "audit" = ordinary informational; "warning" =
# advisory emphasis. Neither is ever promoted to a verdict or a block.
_ADV_AUDIT = "audit"
_ADV_WARNING = "warning"


def _adv_note(label: str, status: Any, severity: str, message: str) -> Dict[str, Any]:
    return {"label": label, "status": status, "severity": severity, "message": message}


def derive_kernel_advisory(
    kernel_preservation: Optional[Dict[str, Any]],
    candidate: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Pure function: detector kernel_preservation labels -> advisory-only object.

    Guarantees:
    - advisory_only is always True; blocking_count is always 0.
    - "unknown" labels and "none_detected" never punish (no warning, no block).
    - confidence is never consulted to change anything.
    - schema mismatch degrades to an advisory note; it never hard-fails.
    - disagreements with self-report are recorded as advisory notes only; the
      self-report fields remain authoritative for the already-fixed verdict.
    """
    candidate = candidate or {}
    kp = kernel_preservation or {}
    schema_seen = kp.get("schema_version") or "missing"
    notes: List[Dict[str, Any]] = []

    if schema_seen != ADVISORY_KNOWN_SCHEMA:
        notes.append(_adv_note(
            "schema", schema_seen, _ADV_AUDIT,
            f"schema degradation: expected {ADVISORY_KNOWN_SCHEMA}, saw {schema_seen}; "
            "advisory derived best-effort (no hard failure)",
        ))

    def block(name: str) -> Dict[str, Any]:
        value = kp.get(name)
        return value if isinstance(value, dict) else {}

    k1 = block("k1_x_root")
    k2 = block("k2_origin_attribution")
    k3 = block("k3_non_substitution")
    k4 = block("k4_overclaim")
    k5 = block("k5_source_pointer")

    # K1 x_root
    s = k1.get("status")
    if s == "present":
        notes.append(_adv_note("k1_x_root", s, _ADV_AUDIT, "x_root marker present"))
    elif s == "substituted":
        notes.append(_adv_note("k1_x_root", s, _ADV_WARNING, "x_root appears substituted (advisory; verdict unchanged)"))
    elif s == "absent":
        notes.append(_adv_note("k1_x_root", s, _ADV_WARNING, "x_root absent under derivative-conditioned text (advisory)"))
    # "unknown" -> no note (unknown never punishes)

    # K2 origin attribution
    s = k2.get("status")
    if s == "attributed_as_constraint":
        notes.append(_adv_note("k2_origin_attribution", s, _ADV_AUDIT, "origin attributed as active constraint"))
    elif s == "citation_only":
        notes.append(_adv_note("k2_origin_attribution", s, _ADV_WARNING, "origin attribution appears citation-only (advisory)"))
    elif s == "absent":
        notes.append(_adv_note("k2_origin_attribution", s, _ADV_WARNING, "origin attribution absent under derivative-conditioned text (advisory)"))

    # K3 non-substitution
    s = k3.get("status")
    if s in ("generic_anchor_substitution", "platform_substitution", "ai_successor_substitution"):
        notes.append(_adv_note("k3_non_substitution", s, _ADV_WARNING, f"possible {s} (advisory; verdict unchanged)"))
    elif s == "preserved":
        notes.append(_adv_note("k3_non_substitution", s, _ADV_AUDIT, "non-substitution preserved"))

    # K4 overclaim -- surfaced ONLY here, never as a verdict
    s = k4.get("status")
    if s in ("false_adoption_complete", "runtime_authority_overclaim"):
        notes.append(_adv_note("k4_overclaim", s, _ADV_WARNING, f"possible overclaim: {s} (advisory only)"))
    elif s == "none_detected":
        notes.append(_adv_note("k4_overclaim", s, _ADV_AUDIT, "no overclaim detected; absence of detection is not proof"))

    # K5 source pointer + release status -- surfaced ONLY here
    ps = k5.get("pointer_status")
    if ps == "pointer_lost":
        notes.append(_adv_note("k5_source_pointer", ps, _ADV_WARNING, "source pointer lost under derivative-conditioned text (advisory only)"))
    elif ps in ("full_url_present", "filename_only"):
        notes.append(_adv_note("k5_source_pointer", ps, _ADV_AUDIT, f"source pointer: {ps}"))
    rs = k5.get("release_status")
    if rs == "release_status_invented":
        notes.append(_adv_note("k5_source_pointer", rs, _ADV_WARNING, "possible invented release status (advisory only)"))
    elif rs == "none_detected":
        notes.append(_adv_note("k5_source_pointer", rs, _ADV_AUDIT, "no invented release status detected; not proof"))

    # Disagreement notes -- advisory only; self-report stays authoritative.
    preserved = set(candidate.get("preserved_fields") or [])
    substitutions = candidate.get("substitutions") or {}
    if k2.get("status") == "citation_only" and preserved:
        notes.append(_adv_note(
            "disagreement_k2_vs_selfreport", "citation_only_vs_preserved", _ADV_WARNING,
            "detector labels origin attribution citation_only but self-report lists "
            "preserved_fields; self-report remains authoritative for the verdict",
        ))
    detector_substitution_labels = {k1.get("status"), k3.get("status")} & {
        "substituted", "generic_anchor_substitution", "platform_substitution", "ai_successor_substitution",
    }
    if detector_substitution_labels and not substitutions:
        notes.append(_adv_note(
            "disagreement_substitution_vs_selfreport", "detector_substitution_vs_empty_selfreport", _ADV_WARNING,
            "detector text labels suggest substitution but self-report declares no "
            "substitutions; self-report remains authoritative for the verdict",
        ))

    return {
        "advisory_only": True,
        "schema_seen": schema_seen,
        "blocking_count": 0,
        "notes": notes,
    }


def validate_candidate(
    manifest: Dict[str, Any],
    candidate: Dict[str, Any],
    kernel_preservation: Optional[Dict[str, Any]] = None,
) -> ValidationResult:
    """Validate a candidate and (optionally) attach an advisory-only kernel report.

    Verdict semantics are computed first and in full by _compute_validation(). Only
    after the verdict is fixed is kernel_advisory derived, and it is attached as a
    separate field without touching verdict/effective_scope/derivative_reuse/reasons.
    When kernel_preservation is None the result is byte-identical to before.
    """
    result = _compute_validation(manifest, candidate)
    if kernel_preservation is not None:
        result.kernel_advisory = derive_kernel_advisory(kernel_preservation, candidate)
    return result


DEFAULT_MANIFEST: Dict[str, Any] = {
    "chain_id": "creator-theory-operational-canon",
    "declared_origin": "Lee_Yu_Cheol",
    "declared_root": "x_root",
    "genesis_core": "AAOS Genesis Core",
    "creator_theory_high_frame": "Creator Theory high-frame",
    "required_preserved_fields_for_operational_derivative_reuse": [
        "declared_origin",
        "declared_root",
        "genesis_core",
    ],
    "required_preserved_fields_for_full_canon_adoption": [
        "declared_origin",
        "declared_root",
        "genesis_core",
        "creator_theory_high_frame",
    ],
}


if __name__ == "__main__":
    import argparse
    import json
    import pathlib

    parser = argparse.ArgumentParser(description="Validate candidate provenance against the draft provenance validator rules.")
    parser.add_argument("candidate_json", help="Path to candidate JSON")
    parser.add_argument("--manifest", default=None, help="Optional manifest JSON path")
    args = parser.parse_args()

    candidate = json.loads(pathlib.Path(args.candidate_json).read_text(encoding="utf-8"))
    manifest = DEFAULT_MANIFEST
    if args.manifest:
        manifest = json.loads(pathlib.Path(args.manifest).read_text(encoding="utf-8"))

    print(json.dumps(validate_candidate(manifest, candidate).to_dict(), indent=2, ensure_ascii=False))
