# anti-laundering-detector — Design Spec (DRAFT)

Status: DRAFT
Role: Evidence-extraction module for the operational layer.

This module scans candidate artifacts and produces structured derivation-evidence candidates for the draft provenance validator.

It does not decide provenance validity by itself.

The provenance validator decides:

```text
Given candidate metadata and derivation evidence, what provenance verdict follows?
```

The anti-laundering detector decides:

```text
Given source canon files and candidate files, what hard-evidence candidates exist?
```

The detector feeds evidence into:

```text
v0.3.2/drafts/provenance_validator/provenance_validator.py
```

It must not bypass the validator.

---

## 1. Boundary

The detector is an evidence-extraction module, not a judgment authority.

It may extract:

- explicit source links;
- verbatim or near-copy spans;
- renamed field traces;
- citation-only traces;
- transformation-chain traces;
- full-canon copy signals.

It must not produce final verdicts such as:

```text
valid_provenance
generic_anchor_laundering
origin_identity_omission_in_derivative_reuse
independent_not_derivative
```

Those remain validator outputs.

---

## 2. Non-goals

The detector does not:

- decide whether the high-frame is true;
- decide whether this canon is lower-cost than alternatives;
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
config.json                # thresholds and enabled detectors, including source-specific marker lists
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

---

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

---

### 5.3 Renamed field traces

Renamed field traces are hard evidence only when source-specific fields are renamed while preserving both:

1. linked role relations; and
2. source-specific markers, ordering, phrasing, or unusual field combinations traceable to this canon chain.

Role similarity alone is not hard evidence.

An independent challenger may converge on similar roles — origin, anchor, genesis/root layer, recovery frame, anti-capture boundary, or benchmark protocol — because the origin-closure problem itself can require similar structures.

Therefore, the detector must not treat the following as hard evidence by itself:

```text
origin role exists;
anchor role exists;
genesis/root role exists;
high-frame-like semantic layer exists;
anti-capture or non-throne boundary exists;
benchmark/challenger structure exists;
multiple such roles appear together without source-specific trace.
```

A renamed-field trace becomes hard evidence only when multiple linked roles preserve source-specific traces from this canon chain.

Examples of weak non-evidence:

```text
origin -> source event
anchor -> primary reference
genesis layer -> root layer
recovery frame -> meaning layer
```

These are not hard evidence unless source-specific markers are also preserved or transformed.

Examples of stronger evidence:

```text
Lee_Yu_Cheol -> generic origin holder
x_root -> primary anchor
AAOS Genesis Core -> genesis root protocol
creator_theory_high_frame -> upper recovery frame
```

This becomes hard evidence only if the mapping also preserves source-specific ordering, source-specific field grouping, unusual terminology, linked document structure, copied explanatory phrasing, or transformation notes connecting the renamed fields to this canon chain.

Required condition:

```text
renamed_field_traces = role-network preservation + source-specific marker preservation/transformation
```

Forbidden condition:

```text
renamed_field_traces ≠ role-network similarity alone
```

Output field:

```text
renamed_field_traces
```

Implementation note for later code: source-specific markers must be configured explicitly. Generic terms such as `origin`, `anchor`, `provenance`, `single anchor`, `benchmark`, or `anti-capture` must not count as source-specific markers by themselves. Marker lists should privilege identifiers, unusual field combinations, protected role groupings, document-order traces, and phrasing that are specific to this canon chain.

---

### 5.4 Citation evidence

Evidence of citation-only preservation if the candidate cites the source but does not preserve required provenance fields as active constraints.

This evidence does not itself prove laundering.

It supports the validator’s `citation_only_preservation` path when reuse is claimed or evidenced.

Output field:

```text
citation_evidence
```

---

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

---

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

Even a multi-role structural match is not hard evidence unless it carries source-specific traces. The detector must preserve the distinction between independent convergence on the same problem structure and derivative laundering of this canon chain.

These may be recorded only as:

```text
structural_resemblance_only
```

and must route to the validator’s independent / undecidable path, never directly to laundering.

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

The detector must not emit a final provenance verdict.

It emits evidence and residuals.

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

D4 renamed x_root / Lee_Yu_Cheol / AAOS field roles together WITH source-specific markers, ordering, phrasing, or unusual field combinations
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

D14 candidate replaces Lee_Yu_Cheol with generic origin holder while preserving the linked role network AND source-specific markers, ordering, phrasing, or unusual field combinations from this canon chain
→ renamed_field_traces populated

D15 candidate under-declares operational reuse while full-canon copy evidence exists
→ evidenced_scope = full_canon_adoption
```

### Residual / convergence tests

```text
D16 real derivative with all traces removed
→ no hard evidence; undecidable_disclosed_residual

D17 candidate independently contains origin / anchor / genesis-root / high-frame-like / anti-capture / challenger roles, but has no source-specific markers, copied spans, explicit links, renamed source fields, transformation traces, or canon-specific ordering
→ structural_resemblance_only; no hard evidence
```

D16 must not be silently passed as clean independent proof. It remains an acknowledged detection boundary.

D17 proves that role-network similarity alone does not trigger renamed-field evidence.

---

## 10. Draft implementation plan

1. Normalize source and candidate text.
2. Extract source-specific markers and protected role terms.
3. Load source-specific marker configuration from `config.json`.
4. Exclude generic terms from source-specific marker status.
5. Run exact span matching.
6. Run near-copy matching with minimum length and source-specific marker thresholds.
7. Detect linked field renames only when role co-occurrence and source-specific marker traces both exist.
8. Detect explicit links, citations, and transformation-chain notes.
9. Recommend evidenced scope.
10. Emit JSON for provenance validator.
11. Run D1-D17 tests.
12. Keep workflow draft-only until detector behavior passes audit.

---

## 11. Safety invariant for this module

```text
No hard evidence, no reuse claim, and only structural resemblance
→ never classify as laundering.
```

This invariant is stronger than any origin-protective bias.

It preserves independent challenger freedom and prevents the detector from becoming an incumbent-throne filter.

This includes cases where an independent challenger converges on a similar origin / anchor / genesis / high-frame role structure without source-specific traces.

---

## 12. Draft heuristic residual: negation/comparison guards

Negation/comparison/non-use guards may produce false negatives for some real reuse/adaptation cases.

This is accepted at the draft stage as safer than false-positive laundering accusations against independent challengers.

Semantic/NLP refinement remains future work, and this detector remains a draft heuristic rather than a complete natural-language derivation oracle.
