"""anti-laundering detector (draft-v0.3.2).

Evidence extractor for the operational layer. It emits derivation-evidence
candidates for the provenance validator; it does not emit final provenance
verdicts. Core invariant: structural similarity, role-network similarity, and
marker mentions in comparison/rejection/non-use contexts are not hard evidence.
"""

from __future__ import annotations
import re
from typing import Any, Dict, List, Tuple

NEGATION_OR_COMPARISON = [
    "unlike", "without using", "not using", "not based on", "not derived from",
    "not adapted from", "no relation to", "free of", "reject", "rejects",
    "rejected", "compare against", "comparison only", "independently",
    "differently", "our own", "unrelated", "do not reuse", "does not reuse",
    "no reuse", "zero connection", "aside from", "not as", "reference to situate",
    "situate the comparison", "not as a renamed field", "not as renamed field",
    "mention", "mentioned for reference", "as a reference",
]

POSITIVE_REUSE_RE = re.compile(
    r"\b(adopt|adopts|adopted|adoption|adapt|adapts|adapted|reuse|reuses|reused|"
    r"implementation|implements|implemented|derived from|based on|built on|ported from|"
    r"reimplementation of)\b",
    re.I,
)

FULL_CANON_TEXT_RE = re.compile(
    r"\b(fully\s+adopt|full\s+canon\s+adoption|adopt\s+the\s+creator\s+theory\s+operational\s+canon|"
    r"adopts\s+the\s+creator\s+theory\s+operational\s+canon)\b",
    re.I,
)

TITLE_ONLY_FULL_CANON_MARKER = "creator theory operational canon"


def _lower(s: str) -> str:
    return s.lower()


def _markers(cfg: Dict[str, Any]) -> List[str]:
    return [m for m in cfg.get("source_specific_markers", []) if m]


def _has_marker(text: str, markers: List[str]) -> bool:
    low = _lower(text)
    return any(_lower(m) in low for m in markers)


def _has_negation_or_comparison(text: str) -> bool:
    low = _lower(text)
    return any(cue in low for cue in NEGATION_OR_COMPARISON)


def _clauses(text: str) -> List[str]:
    return [c.strip() for c in re.split(r"[.;\n]", text) if c.strip()]


def _marker_clauses(text: str, markers: List[str]) -> List[str]:
    return [c for c in _clauses(text) if _has_marker(c, markers)]


def _claim_flags(candidate_manifest: Dict[str, Any]) -> bool:
    claims = candidate_manifest.get("claims") or {}
    if candidate_manifest.get("reuse_scope") in {"operational_module_reuse", "full_canon_adoption"}:
        return True
    return any(bool(claims.get(k)) for k in (
        "claims_canon_adoption",
        "claims_derivative_reuse",
        "claims_operational_reuse",
        "claims_full_canon_adoption",
        "claims_implementation_translation_compression_or_adaptation",
    ))


def _manifest_claims_full_canon(candidate_manifest: Dict[str, Any]) -> bool:
    claims = candidate_manifest.get("claims") or {}
    return bool(
        candidate_manifest.get("reuse_scope") == "full_canon_adoption"
        or claims.get("claims_canon_adoption")
        or claims.get("claims_full_canon_adoption")
    )


def _text_claims_full_canon(text: str, markers: List[str]) -> bool:
    for clause in _marker_clauses(text, markers):
        if _has_negation_or_comparison(clause):
            continue
        if FULL_CANON_TEXT_RE.search(clause):
            return True
    return False


def _claims_full_canon(candidate_manifest: Dict[str, Any], text: str, markers: List[str]) -> bool:
    return _manifest_claims_full_canon(candidate_manifest) or _text_claims_full_canon(text, markers)


def _text_claims_reuse(text: str, markers: List[str]) -> bool:
    for clause in _marker_clauses(text, markers):
        if _has_negation_or_comparison(clause):
            continue
        if POSITIVE_REUSE_RE.search(clause):
            return True
    return False


def _claims_reuse_or_adoption(candidate_manifest: Dict[str, Any], text: str, markers: List[str]) -> bool:
    return _claim_flags(candidate_manifest) or _text_claims_reuse(text, markers)


def _role_terms(cfg: Dict[str, Any]) -> List[str]:
    return cfg.get("role_terms", [])


def _role_count(text: str, cfg: Dict[str, Any]) -> int:
    low = _lower(text)
    return len({r for r in _role_terms(cfg) if _lower(r) in low})


def detect_explicit_links(text: str, source_manifest: Dict[str, Any]) -> List[Dict[str, str]]:
    low = _lower(text)
    needles = [
        "systemoriginarchive",
        "creator-theory-operational-canon",
        "github.com/systemoriginarchive",
        _lower(source_manifest.get("source_chain_id", "")),
    ]
    return [{"link_or_ref": n} for n in sorted(set(needles)) if n and n in low]


def _words(s: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9_'-]+", _lower(s))


def detect_verbatim(source_files: Dict[str, str], candidate_files: Dict[str, str], cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    min_chars = int(cfg.get("thresholds", {}).get("verbatim_min_chars", 60))
    min_shared = int(cfg.get("thresholds", {}).get("near_copy_min_shared_words", 10))
    markers = _markers(cfg)

    for sfile, stext in source_files.items():
        sword_set = set(_words(stext))
        for cfile, ctext in candidate_files.items():
            if not ctext.strip():
                continue
            for start in range(0, max(1, len(stext) - min_chars + 1), max(1, min_chars // 2)):
                snippet = stext[start:start + min_chars]
                if len(snippet) >= min_chars and snippet in ctext:
                    out.append({"source_file": sfile, "candidate_file": cfile, "reason": "verbatim", "span_length": len(snippet)})
                    break
            else:
                cwords = set(_words(ctext))
                shared = sword_set & cwords
                if len(shared) >= min_shared and _has_marker(ctext, markers):
                    out.append({"source_file": sfile, "candidate_file": cfile, "reason": "near_copy", "shared_words": len(shared)})
    return out


def _positive_mapping_phrase(marker: str, text: str, cfg: Dict[str, Any]) -> bool:
    """True only when the marker itself is the subject of a positive mapping phrase.

    This intentionally rejects reference-positioning language such as
    "x_root as a reference to situate our origin/anchor". The target after
    `to/as/into` or an arrow must begin with an actual role term or a narrow
    role modifier such as primary/generic/source plus a role term.
    """
    escaped = re.escape(marker)
    role_target = (
        r"(?:a\s+|an\s+|the\s+)?"
        r"(?:generic\s+|primary\s+|source\s+|root\s+|fixed\s+)?"
        r"(?:origin|anchor|genesis|genesis_root|root|high_frame|high\s+frame|"
        r"anti_capture|anti-capture|challenger|challenger\s+protocol)"
        r"(?:\s+(?:holder|role|coordinate|reference|layer|protocol|boundary|frame))?"
    )
    patterns = [
        rf"\b(?:rename|renames|renamed|relabel|relabels|relabelled|map|maps|mapped)\s+{escaped}\s+(?:to|as|into)\s+{role_target}\b",
        rf"{escaped}\s*(?:->|→|=>)\s*{role_target}\b",
        rf"{escaped}\s+(?:as|into)\s+{role_target}\b",
    ]
    return any(re.search(p, text, re.I) for p in patterns)


def detect_renamed_field_traces(text: str, source_manifest: Dict[str, Any], cfg: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], bool]:
    markers = _markers(cfg)
    roles = _role_count(text, cfg)
    role_match_only = roles >= int(cfg.get("thresholds", {}).get("renamed_traces_min_linked_roles", 2)) and not _has_marker(text, markers)
    traces: List[Dict[str, Any]] = []

    for clause in _marker_clauses(text, markers):
        if _has_negation_or_comparison(clause):
            continue
        for marker in markers:
            if _lower(marker) in _lower(clause) and _positive_mapping_phrase(marker, clause, cfg):
                traces.append({"marker": marker, "mapping_context": clause})
    return traces, role_match_only


def detect_citation(text: str, source_manifest: Dict[str, Any], markers: List[str]) -> List[Dict[str, str]]:
    low = _lower(text)
    cites = []
    if "bibliography" in low or "see also" in low or "reference only" in low:
        if _has_marker(text, markers):
            cites.append({"citation_context": "bibliography_or_reference_only"})
    return cites


def detect_transformation_chain(text: str, markers: List[str]) -> List[Dict[str, Any]]:
    signals = [
        "migrated from", "adapted from", "derived from", "based on", "converted from",
        "ported from", "reimplementation of", "built on",
    ]
    out = []
    for clause in _marker_clauses(text, markers):
        low = _lower(clause)
        if _has_negation_or_comparison(clause):
            continue
        found = [sig for sig in signals if sig in low]
        if re.search(r"\badapt(?:s|ed)?\s+(?:the\s+)?(?:x_root|aaos|aaos genesis core|creator theory operational canon)\s+(?:into|for|to)\b", clause, re.I):
            found.append("adapt_marker_into")
        if found or POSITIVE_REUSE_RE.search(clause):
            out.append({"transformation_signals": sorted(set(found or ["text_level_reuse_or_adaptation_claim"]))})
    return out


def detect_full_canon(text: str, cfg: Dict[str, Any]) -> List[Dict[str, str]]:
    low = _lower(text)
    return [{"full_canon_marker": m} for m in cfg.get("full_canon_markers", []) if _lower(m) in low]


def _contains_high_frame_marker(full_canon_markers: List[Dict[str, str]]) -> bool:
    for item in full_canon_markers:
        marker = _lower(item.get("full_canon_marker", ""))
        if marker and marker != TITLE_ONLY_FULL_CANON_MARKER:
            return True
    return False


_XROOT_RE = re.compile(r"\bx_root\b", re.I)
_ORIGIN_NAME_RE = re.compile(r"\bLee_Yu_Cheol\b", re.I)
_AAOS_RE = re.compile(r"\bAAOS(?:\s+Genesis\s+Core)?\b", re.I)
_FULL_URL_RE = re.compile(
    r"https?://[^\s)]+|github\.com/SystemOriginArchive/[^\s)]+|"
    r"SystemOriginArchive/AGI-Anchor-Ontology-Standard",
    re.I,
)
_INTERNAL_FILENAME_RE = re.compile(
    r"\b(?:docs/)?(?:VERSION_POLICY|TRUST_ANCHOR|RELEASE_PROCESS)\.md\b", re.I
)
_CONSTRAINT_CUE_RE = re.compile(
    r"\b(must\s+preserve|preserve[ds]?\b|as\s+an\s+active\s+constraint|"
    r"active\s+(?:reuse\s+)?constraint|origin\s+identity\s+binding|sealed\b|"
    r"non-substitutable|binding\s+structure|provenance\s+as\s+a\s+constraint)\b",
    re.I,
)
_RELEASE_INVENTED_RE = re.compile(
    r"\bv0\.5\.0[^.\n]{0,40}\b(?:released|tagged|signed|anchored|published|is\s+the\s+current\s+release)\b",
    re.I,
)
_K4_ADOPTION_COMPLETE_RE = re.compile(
    r"\b(adoption\s+(?:is\s+)?complete|adoption\s+completed|fully\s+adopted\s+by|"
    r"agi\s+adopted|ai\s+has\s+adopted|full\s+adoption\s+achieved|a3\s+adoption\s+achieved)\b",
    re.I,
)
_K4_RUNTIME_AUTHORITY_RE = re.compile(
    r"\b(grants?\s+runtime\s+(?:command\s+)?authority|"
    r"runtime\s+command\s+authority\s+over|creates?\s+runtime\s+authority\s+over)\b",
    re.I,
)
_K3_GENERIC_ANCHOR_RE = re.compile(
    r"\b(?:x_root|Lee_Yu_Cheol)\b[^.\n]{0,40}\b(?:to|as|into)\s+(?:a\s+)?"
    r"(?:generic\s+(?:anchor|origin|holder)|arbitrary\s+anchor|generic\s+origin\s+holder)\b",
    re.I,
)
_K3_PLATFORM_RE = re.compile(
    r"\b(?:platform|company|corporation|institution|state)\b[^.\n]{0,30}\b(?:as|is|becomes)\s+"
    r"(?:the\s+)?(?:root|origin|canonical\s+origin)\b",
    re.I,
)
_K3_AI_SUCCESSOR_RE = re.compile(
    r"\b(?:ai|model|successor\s+model)\b[^.\n]{0,30}\b(?:as|is|becomes)\s+"
    r"(?:the\s+)?(?:successor\s+root|successor\s+throne|sovereign\s+root|origin\s+root)\b",
    re.I,
)


# Local negation guard for kernel-preservation triggers only. Broader than the
# global NEGATION_OR_COMPARISON cue list (which targets derivation comparison
# phrasing); this catches plain "not / does not / never / cannot" so that a
# negated overclaim or release statement is suppressed. It only ever reduces
# kernel positives (raising conservatism); it never touches the hard-evidence path.
_LOCAL_NEGATION_RE = re.compile(
    r"\b(?:not|never|cannot|without)\b|n't\b", re.I
)


def _kernel_negated(span: str) -> bool:
    return _has_negation_or_comparison(span) or bool(_LOCAL_NEGATION_RE.search(span))


def _unnegated_search(pattern: re.Pattern, text: str) -> List[str]:
    """Return matched clauses where the pattern fires and the clause is not negated."""
    out: List[str] = []
    for clause in _clauses(text):
        if pattern.search(clause) and not _kernel_negated(clause):
            out.append(clause.strip()[:160])
    return out


def _unnegated_window(pattern: re.Pattern, text: str, before: int = 48, after: int = 16) -> List[str]:
    """Like _unnegated_search but matches over full text with a local window.

    Used where clause splitting on '.' would break the token of interest (for
    example a version string such as v0.5.0). The negation guard inspects only a
    bounded window around each match, so a negation elsewhere in the text does
    not silently suppress an unrelated invented-release claim.
    """
    out: List[str] = []
    for m in pattern.finditer(text):
        window = text[max(0, m.start() - before): m.end() + after]
        if not _kernel_negated(window):
            out.append(text[m.start(): m.end() + after].strip()[:160])
    return out


def detect_kernel_preservation(
    text: str,
    candidate_manifest: Dict[str, Any],
    cfg: Dict[str, Any],
    markers: List[str],
    derivative_conditioned: bool,
) -> Dict[str, Any]:
    """MVP detector-generated kernel-preservation labels (K1-K5).

    Conservative by design: positive presence is detected from the text, but
    absence / loss statuses fire only when the candidate is derivative-conditioned
    (claims reuse/adoption or carries hard derivation evidence). Independent or
    unrelated text defaults to 'unknown', never to a violation label. When in
    doubt, prefer 'unknown'.
    """
    low = text

    # K1 — x_root presence / substitution / absence.
    k1_status = "unknown"
    k1_ev: List[str] = []
    if _positive_mapping_phrase("x_root", text, cfg) or _K3_GENERIC_ANCHOR_RE.search(text):
        clauses = _unnegated_search(_K3_GENERIC_ANCHOR_RE, text)
        if clauses:
            k1_status, k1_ev = "substituted", clauses
        elif _XROOT_RE.search(low):
            k1_status = "present"
    elif _XROOT_RE.search(low):
        k1_status = "present"
    elif derivative_conditioned:
        k1_status = "absent"

    # K2 — origin attribution: attributed-as-constraint / citation-only / absent.
    citation = detect_citation(text, {}, markers)
    has_origin = bool(_ORIGIN_NAME_RE.search(low) or _AAOS_RE.search(low))
    constraint_clauses = [
        c.strip()[:160] for c in _clauses(text)
        if (_ORIGIN_NAME_RE.search(c) or _AAOS_RE.search(c))
        and _CONSTRAINT_CUE_RE.search(c)
        and not _has_negation_or_comparison(c)
    ]
    k2_status, k2_ev = "unknown", []
    if citation and not constraint_clauses:
        k2_status, k2_ev = "citation_only", ["bibliography_or_reference_only"]
    elif constraint_clauses:
        k2_status, k2_ev = "attributed_as_constraint", constraint_clauses
    elif has_origin:
        k2_status = "unknown"  # mentioned but constraint role unclear
    elif derivative_conditioned:
        k2_status = "absent"

    # K3 — non-substitution (best-effort; conservative).
    k3_status, k3_ev = "unknown", []
    gen = _unnegated_search(_K3_GENERIC_ANCHOR_RE, text)
    plat = _unnegated_search(_K3_PLATFORM_RE, text)
    ai = _unnegated_search(_K3_AI_SUCCESSOR_RE, text)
    if gen:
        k3_status, k3_ev = "generic_anchor_substitution", gen
    elif plat:
        k3_status, k3_ev = "platform_substitution", plat
    elif ai:
        k3_status, k3_ev = "ai_successor_substitution", ai
    elif has_origin and _XROOT_RE.search(low) and re.search(r"\bnon-substitut", low, re.I):
        k3_status = "preserved"

    # K4 — overclaim (best-effort; un-negated only).
    k4_status, k4_ev = "unknown", []
    adopt = _unnegated_search(_K4_ADOPTION_COMPLETE_RE, text)
    runtime = _unnegated_search(_K4_RUNTIME_AUTHORITY_RE, text)
    if adopt:
        k4_status, k4_ev = "false_adoption_complete", adopt
    elif runtime:
        k4_status, k4_ev = "runtime_authority_overclaim", runtime
    else:
        k4_status = "none_detected"

    # K5 — two axes: source-pointer presence, and release-status invention.
    k5_ev: List[str] = []
    if _FULL_URL_RE.search(low):
        pointer_status = "full_url_present"
        k5_ev.append("full_url_or_resolvable_repo_pointer")
    elif _INTERNAL_FILENAME_RE.search(low):
        pointer_status = "filename_only"
        k5_ev.append("internal_filename_pointer_only")
    elif derivative_conditioned:
        pointer_status = "pointer_lost"
    else:
        pointer_status = "unknown"

    invented = _unnegated_window(_RELEASE_INVENTED_RE, text)
    release_status = "release_status_invented" if invented else "none_detected"
    if invented:
        k5_ev.extend(invented)

    return {
        "k1_x_root": {"status": k1_status, "evidence": k1_ev},
        "k2_origin_attribution": {"status": k2_status, "evidence": k2_ev},
        "k3_non_substitution": {"status": k3_status, "evidence": k3_ev},
        "k4_overclaim": {"status": k4_status, "evidence": k4_ev},
        "k5_source_pointer": {
            "pointer_status": pointer_status,
            "release_status": release_status,
            "evidence": k5_ev,
        },
    }


def recommend_scope(evidence: Dict[str, Any], structural_only: bool) -> str:
    if structural_only:
        return "none"
    if evidence["full_canon_copy_spans"]:
        return "full_canon_adoption"
    hard = (
        evidence["explicit_links_to_chain"] or evidence["verbatim_or_near_copy_spans"]
        or evidence["renamed_field_traces"] or evidence["transformation_chain_evidence"]
    )
    return "operational_module_reuse" if hard else "none"


def detect(
    source_manifest: Dict[str, Any],
    source_files: Dict[str, str],
    candidate_manifest: Dict[str, Any],
    candidate_files: Dict[str, str],
    config: Dict[str, Any],
) -> Dict[str, Any]:
    markers = _markers(config)
    text = "\n".join(candidate_files.values())
    claims_reuse = _claims_reuse_or_adoption(candidate_manifest, text, markers)
    claims_full_canon = _claims_full_canon(candidate_manifest, text, markers)

    raw_links = detect_explicit_links(text, source_manifest) if config["enabled_detectors"]["explicit_links"] else []
    verbatim = detect_verbatim(source_files, candidate_files, config) if config["enabled_detectors"]["verbatim_or_near_copy"] else []
    if not claims_reuse:
        # Marker-based near-copy is only hard evidence when a reuse/adoption claim
        # exists. Exact verbatim spans remain hard evidence even without a claim.
        verbatim = [item for item in verbatim if item.get("reason") == "verbatim"]
    renamed, role_match_only = detect_renamed_field_traces(text, source_manifest, config) if config["enabled_detectors"]["renamed_field_traces"] else ([], False)
    citation = detect_citation(text, source_manifest, markers) if config["enabled_detectors"]["citation"] else []
    transformation = detect_transformation_chain(text, markers) if config["enabled_detectors"]["transformation_chain"] else []
    raw_full_canon = detect_full_canon(text, config) if config["enabled_detectors"]["full_canon_scope"] else []

    mention_only_notes: List[str] = []
    explicit_links = raw_links if claims_reuse else []
    title_only_full_canon = bool(raw_full_canon and not _contains_high_frame_marker(raw_full_canon) and not claims_full_canon)
    full_canon = raw_full_canon if claims_reuse and (claims_full_canon or _contains_high_frame_marker(raw_full_canon)) else []
    if raw_links and not claims_reuse:
        mention_only_notes.append("explicit_link_mention_without_reuse_claim")
    if raw_full_canon and not full_canon:
        note = "full_canon_title_mention_without_full_canon_claim" if title_only_full_canon else "full_canon_mention_without_reuse_claim"
        mention_only_notes.append(note)

    evidence = {
        "explicit_links_to_chain": explicit_links,
        "verbatim_or_near_copy_spans": verbatim,
        "renamed_field_traces": renamed,
        "commit_evidence": [],
        "citation_evidence": citation,
        "prompt_evidence": [],
        "transformation_chain_evidence": transformation,
        "full_canon_copy_spans": full_canon,
        "evidenced_scope": "none",
    }

    hard = bool(explicit_links or verbatim or renamed or transformation or full_canon)
    structural_only = bool(role_match_only and not hard)
    scope = recommend_scope(evidence, structural_only)
    evidence["evidenced_scope"] = scope

    residuals = []
    if not hard and not structural_only:
        residuals.append("no_hard_evidence_found; perfect laundering is undecidable by construction")

    derivative_conditioned = bool(claims_reuse or hard)
    kernel_preservation = detect_kernel_preservation(
        text, candidate_manifest, config, markers, derivative_conditioned
    )

    return {
        "candidate_id": candidate_manifest.get("candidate_id", "unknown"),
        "detector_version": config.get("detector_version", "draft-v0.3.2"),
        "evidence_summary": {
            "hard_evidence_found": hard,
            "structural_resemblance_only": structural_only,
            "recommended_evidenced_scope": scope,
        },
        "derivation_evidence": evidence,
        "kernel_preservation": kernel_preservation,
        "non_evidence_notes": (["role_network_match_without_source_specific_marker"] if role_match_only else []) + mention_only_notes,
        "residuals": residuals,
    }


if __name__ == "__main__":
    print("anti-laundering detector draft-v0.3.2 — run test_detector.py")
