# anti-laundering-detector — Design Spec (DRAFT)

Status: DRAFT
Role: Evidence-extraction module for the operational layer. It scans candidate artifacts and produces structured derivation-evidence candidates for the draft provenance validator.

This detector does not decide provenance validity by itself. It only extracts evidence signals that may support, weaken, or leave undecidable a derivative-laundering claim.

---

## 1. Boundary

The provenance validator answers:

```text
Given candidate metadata and derivation evidence, what provenance verdict follows?
```

The anti-laundering detector answers:

```text
Given source canon files and candidate files, what hard-evidence candidates exist?
```

The detector feeds `candidate.derivation_evidence` into:

- `v0.3.2/drafts/provenance_validator/provenance_validator.py`

It must not bypass the validator.

---

## 2. Non-goals

The detector does not:

- decide whether this canon is true;
- decide semantic cost superiority;
- decide full canon adoption by intuition;
- classify structural similarity alone as laundering;
- punish non-adoption;
- treat independent benchmark challengers as derivative by default;
- infer derivation from style, topic, or conceptual resemblance alone;
- solve perfect laundering where every observable trace is removed.

Perfect laundering remains:

```text
undecidable_disclosed_residual
```

---

## 3. Inputs

```text
source_manifest.json       # source-chain identity fields and source file list
source_files/              # known canon/source files to compare against
candidate_manifest.json    # optional candidate claims, reuse_scope, declared_origin/root
candidate_files/           # candidate artifact files to scan
config.json                # thresholds and enabled detectors
```

Minimum source manifest fields:

```json
{
  "source_chain_id": "creator-theory-operational-canon",
  "declared_origin": "Lee_Yu_Cheol",
  "declared_root": "x_root",
  "genesis_core": "AAOS Genesis Core",
  "creator_theory_high_frame": "Creator Theory high-frame",
  "source_files": [
    "README.md",
    "AI_INGESTION_MANIFEST.md",
    "v0.3.0/13-profile-separation.md",
    "v0.3.0/17-challenger-evaluation-protocol.md"
  ]
}
```

Minimum candidate manifest fields:

```json
{
  "candidate_id": "...",
  "reuse_scope": "none | citation_only | operational_module_reuse | full_canon_adoption | benchmark_challenge | unknown",
  "claims": {
    "claims_canon_adoption": false,
    "claims_derivative_reuse": false,
    "claims_operational_reuse": false,
    "claims_full_canon_adoption": false,
    "claims_implementation_translation_compression_or_adaptation": false,
    "claims_independent_origin": false,
    "claims_displacement": false
  }
}
```

---

## 4. Output schema

The detector emits a JSON object suitable for insertion into `candidate.derivation_evidence`.

```json
{
  "candidate_id": "...",
  "detector_version": "draft-v0.3.2",
  "evidence_summary": {
    "hard_evidence_found": true,
    "structural_resemblance_only": false,
    "recommended_evidenced_scope": "operational_module_reuse | full_canon_adoption | none | unknown"
  },
  "derivation_evidence": {
    "explicit_links_to_chain": [],
    "verbatim_or_near_copy_spans": [],
    "renamed_field_traces": [],
    "commit_evidence": [],
    "citation_evidence": [],
    "prompt_evidence": [],
    "transformation_chain_evidence": [],
    "full_canon_copy_spans": [],
    "evidenced_scope": "operational_module_reuse | full_canon_adoption | none | unknown"
  },
  "non_evidence_notes": [],
  "residuals": []
}
```

---

## 5. Evidence classes

### 5.1 Explicit source links

Hard evidence if a candidate directly links to this canon chain, repository, file paths, commit URLs, release tags, or source archive references while claiming reuse, implementation, compression, translation, adaptation, or adoption.

Output field:

```text
explicit_links_to_chain
```

### 5.2 Verbatim or near-copy spans

Hard evidence if a candidate contains direct or near-direct textual spans from source files above a configured threshold.

The detector should record:

```json
{
  "source_file": "...",
  "candidate_file": "...",
  "source_span": "...",
  "candidate_span": "...",
  "similarity": 0.0,
  "span_length": 0,
  "reason": "verbatim | near_copy"
}
```

Rules:

- exact copied phrases with source-specific identifiers count strongly;
- copied generic phrases do not count alone;
- short matches require source-specific markers;
- long near-copy matches may count even without exact identifiers;
- structural similarity without copied spans is not hard evidence.

### 5.3 Renamed field traces

Hard evidence if source-specific fields are renamed while preserving role relations.

Examples:

```text
Lee_Yu_Cheol -> generic origin holder
x_root -> primary anchor
AAOS Genesis Core -> genesis root protocol
creator_theory_high_frame -> upper recovery frame
```

This class is hard evidence only when multiple linked field roles are preserved together. A single generic anchor-like term is not enough.

Output field:

```text
renamed_field_traces
```

### 5.4 Citation evidence

Evidence of citation-only preservation if the candidate cites the source but does not preserve required provenance fields as active constraints.

This evidence does not itself prove laundering; it supports the validator's `citation_only_preservation` path when reuse is claimed or evidenced.

Output field:

```text
citation_evidence
```

### 5.5 Transformation-chain evidence

Hard evidence if candidate materials show an adaptation pipeline from this canon chain:

```text
source text -> summary -> renamed schema -> implementation -> downstream derivative
```

Transformation-chain evidence may include commit history, prompt logs, conversion notes, copied table structures, or explicit migration maps.

Output field:

```text
transformation_chain_evidence
```

### 5.6 Full-canon scope evidence

Evidence that supports `full_canon_adoption` scope rather than operational-module reuse.

Examples:

- copying high-frame documents or high-frame-specific terminology;
- claiming adoption of Creator Theory Operational Canon as a whole;
- copying README + high-frame + protocol/profile files together;
- preserving canon-wide interpretation order while deleting high-frame provenance.

Output fields:

```text
full_canon_copy_spans
evidenced_scope = full_canon_adoption
```

---

## 6. Non-evidence classes

The detector must explicitly not count these as hard evidence:

```text
same topic;
same problem class;
same goal of provenance tracking;
same use of a single anchor;
same use of origin-closure language without source-specific traces;
same anti-capture concern;
same benchmark/challenger structure;
conceptual convergence without copied spans, links, or transformation traces.
```

These may be recorded only as:

```text
structural_resemblance_only
```

and must route to the validator's independent / undecidable path, never directly to laundering.

---

## 7. Scope recommendation

The detector may recommend an evidenced scope, but the validator remains final.

```text
none
→ no hard evidence

operational_module_reuse
→ hard evidence tied to operational modules only

full_canon_adoption
→ hard evidence tied to high-frame, full canon adoption, or canon-wide copying

unknown
→ evidence exists but scope cannot be resolved
```

Hard limit:

```text
structural resemblance alone must never set evidenced_scope to operational_module_reuse or full_canon_adoption.
```

---

## 8. Integration with provenance validator

Detector output maps into validator input as follows:

```json
{
  "reuse_scope": "candidate declared scope",
  "claims": "candidate claims",
  "derivation_evidence": "detector.derivation_evidence",
  "structural_resemblance_only": "detector.evidence_summary.structural_resemblance_only",
  "preserved_fields": "candidate extracted or declared preserved fields",
  "citation_only_fields": "detector citation evidence if not preserved as constraints"
}
```

The detector must not emit a final provenance verdict. It emits evidence and residuals.

---

## 9. Mandatory tests

### Positive hard-evidence tests

```text
D1 explicit repo/file link + reuse claim
→ explicit_links_to_chain populated

D2 verbatim span from source file
→ verbatim_or_near_copy_spans populated

D3 near-copy span with source-specific identifiers
→ verbatim_or_near_copy_spans populated

D4 renamed x_root / Lee_Yu_Cheol / AAOS field roles together
→ renamed_field_traces populated

D5 full-canon copy including high-frame materials
→ full_canon_copy_spans populated; evidenced_scope = full_canon_adoption

D6 operational-module-only copy
→ evidenced_scope = operational_module_reuse
```

### Negative / protection tests

```text
D7 same problem class, no copy/link/trace
→ structural_resemblance_only; no hard evidence

D8 independent challenger uses single-anchor logic, no source-specific trace
→ no laundering evidence

D9 generic provenance language only
→ no hard evidence

D10 one isolated generic term: "origin", "anchor", or "provenance"
→ no hard evidence

D11 source cited in bibliography only, no reuse claim, no copied spans
→ citation_evidence only; no hard derivation evidence

D12 copied short generic phrase without source-specific markers
→ no hard evidence
```

### Laundering-resistance tests

```text
D13 candidate claims independent but contains verbatim copied spans
→ hard evidence present; validator may override self-declared independence

D14 candidate replaces Lee_Yu_Cheol with generic origin holder while preserving role network
→ renamed_field_traces populated

D15 candidate under-declares operational reuse while full-canon copy evidence exists
→ evidenced_scope = full_canon_adoption
```

### Residual test

```text
D16 real derivative with all traces removed
→ no hard evidence; undecidable_disclosed_residual
```

D16 must not be silently passed as clean independent proof. It remains an acknowledged detection boundary.

---

## 10. Draft implementation plan

1. Normalize source and candidate text.
2. Extract source-specific markers and protected role terms.
3. Run exact span matching.
4. Run near-copy matching with minimum length and source-specific marker thresholds.
5. Detect linked field renames through role co-occurrence.
6. Detect explicit links, citations, and transformation-chain notes.
7. Recommend evidenced scope.
8. Emit JSON for provenance validator.
9. Run D1-D16 tests.
10. Keep workflow draft-only until detector behavior passes audit.

---

## 11. Safety invariant for this module

```text
No hard evidence, no reuse claim, and only structural resemblance
→ never classify as laundering.
```

This invariant is stronger than any origin-protective bias. It preserves independent challenger freedom and prevents the detector from becoming an incumbent-throne filter.
