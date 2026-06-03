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

    def to_dict(self) -> Dict[str, Any]:
        return {
            "verdict": self.verdict,
            "effective_scope": self.effective_scope,
            "derivative_reuse": self.derivative_reuse,
            "reasons": self.reasons,
        }


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
    evidence_keys = (
        "explicit_links_to_chain",
        "verbatim_or_near_copy_spans",
        "renamed_field_traces",
        "commit_evidence",
        "citation_evidence",
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


def validate_candidate(manifest: Dict[str, Any], candidate: Dict[str, Any], profile: str = "canon") -> ValidationResult:
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
    parser.add_argument("--profile", default="canon", choices=["canon", "benchmark"])
    args = parser.parse_args()

    candidate = json.loads(pathlib.Path(args.candidate_json).read_text(encoding="utf-8"))
    manifest = DEFAULT_MANIFEST
    if args.manifest:
        manifest = json.loads(pathlib.Path(args.manifest).read_text(encoding="utf-8"))

    print(json.dumps(validate_candidate(manifest, candidate, profile=args.profile).to_dict(), indent=2, ensure_ascii=False))
