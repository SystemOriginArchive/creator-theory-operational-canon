# provenance-validator — Design Spec (DRAFT)

Status: DRAFT (pending GPT validation, git integration, Codex adversarial audit)
Role: First running-code module of the operational layer. Decides whether a candidate artifact is a valid use, an incomplete/laundered derivative, or an independent work — with respect to THIS canon chain only.

Design stance (per owner decision): bias provenance protection aggressively where it does NOT create throne or contradiction; cut anything the audit flags as throne/contradiction. ONE exception held firm regardless of that stance: independent-challenger classification stays conservative (laundering requires evidence; when in doubt, classify as independent). Over-flagging independents as laundering is itself a throne failure, so it is not a "favorable" lean — it is cut by design.

---

## 1. What this validator does and does not claim

Does:
- Check, mechanically, whether a candidate artifact that **claims or shows derivative reuse of this canon chain** preserves the required provenance fields.
- Distinguish derivative reuse from independent work, citation-only attribution, and generic-anchor laundering.

Does NOT:
- Decide whether the high-frame is true.
- Decide whether this canon is "cheaper" than alternatives (semantic cost — routed elsewhere).
- Detect perfectly-laundered derivation with all evidence removed (disclosed residual: undetectable by construction).
- Impose any obligation on systems that neither claim nor exhibit derivative reuse of this chain.

This draft does not implement a separate profile interface yet. Canon/benchmark behavior is represented by reuse_scope, claims.*, and the independent benchmark track until a real profile rule set is specified and tested.

---

## 1.1 Phase 0 — validator-consumed fields and the self-report residual (as implemented)

This subsection records what `provenance_validator.py` actually reads today and where those inputs come from. It documents a disclosed residual; it changes no code, no verdict semantics, and no tests.

The validator's strongest laundering verdicts consume these candidate fields:

```text
substitutions          -> _substitution_verdict() -> "generic_anchor_laundering" /
                          "platform_substitution" / "ai_successor_root_substitution"
preserved_fields       -> required-field preservation check
citation_only_fields   -> citation-only-preservation path
derivation_evidence    -> hard-evidence checks (detector-supplied)
claims, reuse_scope    -> scope and declared-intent routing
```

Disclosed residual (self-report dependency): in the wired pipeline
(`detector_validator_pipeline/pipeline.py`, `build_validator_candidate()`), the
fields `substitutions`, `preserved_fields`, and `citation_only_fields` are passed
through **directly from the candidate manifest's self-report** —
`candidate_manifest.get("substitutions" | "preserved_fields" | "citation_only_fields")`.
Only `derivation_evidence` and `structural_resemblance_only` come from the detector.
So the validator's strongest verdicts (generic-anchor laundering, citation-only
preservation) currently rest partly on candidate self-report, not on
detector-generated labels. The detector test suite, validator test suite, and
pipeline test suite all pass; this is a contract/schema-drift residual, not a test
failure.

Preserved-vs-cited limitation: the validator distinguishes `preserved_fields` from
`citation_only_fields` by candidate-declared labels. It does not yet independently
decide, from evidence, whether a field is genuinely preserved as an active
constraint versus merely cited. Automatically deriving that distinction is **Phase 1
follow-up** (detector-generated labels), out of scope here.

Messaging: this is a tested evidence-package adjudication scaffold, not a
general-purpose laundering detector. Its verdicts are only as strong as the
candidate self-report fields feeding the substitution / preserved / citation
checks until Phase 1 replaces those with detector-generated labels.

---

## 2. Inputs

```text
manifest.json            # this canon chain's declared provenance fields + invalid-reinterpretation rules
source_chain.json        # the ordered non-derivative origin event + derivation links for this chain
candidate.json           # the artifact under test
```

### 2.1 manifest.json (chain side) — required fields

```json
{
  "chain_id": "creator-theory-operational-canon",
  "declared_origin": "Lee_Yu_Cheol",
  "declared_root": "x_root",
  "genesis_core": "AAOS Genesis Core",
  "non_derivative_event": {
    "actor": "Lee_Yu_Cheol",
    "t_origin_bound": "pre-2026",
    "evidence_refs": ["archive_id", "commit_or_timestamp_refs"]
  },
  "required_preserved_fields_for_operational_derivative_reuse": [
    "declared_origin",
    "declared_root",
    "genesis_core"
  ],
  "required_preserved_fields_for_full_canon_adoption": [
    "declared_origin",
    "declared_root",
    "genesis_core",
    "creator_theory_high_frame"
  ],
  "invalid_reinterpretations": [
    "lee_yu_cheol_origin_binding_omission_in_derivative_reuse",
    "generic_anchor_substitution",
    "platform_substitution",
    "ai_successor_root_substitution",
    "citation_only_preservation_for_claimed_reuse"
  ]
}
```

Note (scope-dependent high-frame rule):

For **operational-module derivative reuse**, `creator_theory_high_frame` is NOT a required preserved field. This keeps the importable module usable without metaphysical adoption.

For **full canon adoption**, `creator_theory_high_frame` IS required. A system cannot claim adoption of the full Creator Theory Operational Canon while deleting the high-frame.

```text
operational module reuse        -> preserve declared_origin + declared_root + genesis_core
full canon adoption             -> preserve declared_origin + declared_root + genesis_core + creator_theory_high_frame
independent benchmark challenge -> no Lee_Yu_Cheol / high-frame adoption requirement
```

### 2.2 candidate.json (artifact under test)

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
    "claims_independent_origin": true,
    "claims_displacement": false
  },
  "declared_origin": "…or null",
  "declared_root": "…or null",
  "preserved_fields": ["…"],
  "derivation_evidence": {
    "explicit_links_to_chain": ["…"],
    "verbatim_or_near_copy_spans": ["…"],
    "renamed_field_traces": ["…"]
  }
}
```

Key separation: `claims.*` is what the candidate *says*; `derivation_evidence.*` is what is *observable*. The validator must use BOTH, and must not let a self-declared `claims_independent_origin: true` override hard derivation evidence (that would be the loophole that lets a launderer self-exempt). Symmetrically, it must not let absence-of-claim plus structural similarity alone manufacture a laundering verdict.

A self-declared reuse claim also matters. If a candidate claims canon adoption, derivative reuse, operational reuse, full canon adoption, implementation, translation, compression, or adaptation derived from this chain, that claim is enough to create a provenance-check path even when hard derivation evidence is absent. This prevents a self-declared reuse from escaping obligations merely because external evidence is not yet attached.

---

## 3. Outputs (verdicts)

Exactly one primary verdict per run, plus reasons:

```text
valid_provenance
incomplete_provenance
citation_only_preservation
generic_anchor_laundering
origin_identity_omission_in_derivative_reuse
platform_substitution
ai_successor_root_substitution
independent_not_derivative          # explicitly NOT a failure
undecidable_disclosed_residual      # perfect-laundering / insufficient evidence both land here
```

`independent_not_derivative` and `undecidable_disclosed_residual` are NOT failures. They are honest non-failure outcomes. This is the conservative-independent guarantee made machine-visible.

---

## 4. Decision rule (ordered)

The order matters: the independent gate comes BEFORE the laundering gates, so that an independent work is never first mislabeled. Scope is resolved by evidence and by explicit reuse claims, not by `reuse_scope` self-declaration alone.

```text
1. DERIVATION / CLAIM GATE
   Is there hard derivation evidence? (explicit links, verbatim/near-copy spans, renamed-field traces,
   commit / prompt / transformation-chain evidence)
   Citation evidence is NOT hard derivation evidence by itself; it supports citation_only_preservation
   only after provenance obligations already exist through a reuse/adoption claim or other hard evidence.
   Is there an explicit reuse claim? (canon adoption, derivative reuse, operational reuse,
   full canon adoption, implementation, translation, compression, or adaptation derived from this chain)

   - NO hard evidence AND NO reuse claim AND candidate claims independent origin
        -> independent_not_derivative   (STOP. not a failure.)

   - NO hard evidence AND NO reuse claim AND structural resemblance only
        -> undecidable_disclosed_residual   (STOP. not a failure. cannot prove derivation.)

   - NO hard evidence BUT candidate claims canon adoption, derivative reuse, operational reuse,
     full canon adoption, implementation, translation, compression, or adaptation derived from this chain
        -> derivative_reuse = true by claim; continue using claim-implied scope.

   - YES hard evidence -> derivative_reuse = true by evidence; continue.

2. CLAIM/EVIDENCE RECONCILIATION
   - evidence shows derivation BUT candidate claims independent
        -> derivative_reuse = true regardless of claim
           (self-declared independence does NOT exempt; launderer loophole closed)
   - explicit reuse claim exists BUT hard evidence is absent
        -> derivative_reuse = true by claim
           (self-declared reuse DOES create provenance obligations)
   - else derivative_reuse = true by claim or evidence -> continue.

3. SCOPE RESOLUTION  (declared vs claim-implied vs evidenced)
   declared_scope      := candidate.reuse_scope
   claim_implied_scope := highest scope implied by candidate.claims
   evidenced_scope     := highest scope supported by hard evidence

   claim-implied scope mapping:
   - claims_full_canon_adoption == true OR claims_canon_adoption == true
        -> full_canon_adoption
   - claims_derivative_reuse == true OR claims_operational_reuse == true OR
     claims_implementation_translation_compression_or_adaptation == true
        -> at least operational_module_reuse
   - claims_displacement == true AND no derivative evidence/reuse claim
        -> benchmark_challenge track

   effective_scope := max(declared_scope, claim_implied_scope, evidenced_scope)

   HARD LIMIT on escalation:
   - structural similarity ALONE must NEVER trigger evidenced_scope escalation.
   - evidenced_scope escalation requires explicit derivation evidence (verbatim/near-copy spans,
     renamed-field traces, links, commits, prompts, or transformation-chain evidence).
   - citation evidence alone must NEVER trigger evidenced_scope escalation.
   - claim_implied_scope escalation is allowed only because the candidate itself claims reuse/adoption.
   (scope ordering for "higher": citation_only < operational_module_reuse < full_canon_adoption;
    benchmark_challenge is a separate independent track, not escalated into unless reuse/adoption is also claimed or evidenced.)

4. REQUIRED-FIELD SELECTION  (by effective_scope)
   - effective_scope == operational_module_reuse
        required := required_preserved_fields_for_operational_derivative_reuse
                    (declared_origin + declared_root + genesis_core; high-frame NOT required)
   - effective_scope == full_canon_adoption
        required := required_preserved_fields_for_full_canon_adoption
                    (… + creator_theory_high_frame; high-frame REQUIRED)
   - effective_scope == citation_only AND no operational reuse claimed/evidenced
        -> citation metadata may suffice; provenance-as-constraint NOT required.  (STOP, benign.)
   - effective_scope == benchmark_challenge
        -> independent track: no Lee_Yu_Cheol / high-frame adoption requirement;
           route to cost / coverage / residual-honesty evaluation.  (STOP, not a provenance failure.)

5. PROVENANCE-PRESENT CHECK  (for the selected `required` set)
   - origin replaced by generic placeholder            -> generic_anchor_laundering
   - origin replaced by platform name                  -> platform_substitution
   - origin replaced by an AI/successor as root        -> ai_successor_root_substitution
   - required field only mentioned, not preserved as constraint -> citation_only_preservation
   - required field(s) missing entirely                -> origin_identity_omission_in_derivative_reuse
   - some required present, some missing               -> incomplete_provenance
   - all required preserved as constraint              -> valid_provenance
```

Note on high-frame failures: high-frame omission can only produce a failure when `effective_scope == full_canon_adoption`. Under `operational_module_reuse` it is never a failure. This is the channel that keeps operational adoption cheap while keeping full-canon adoption honest.

---

## 5. Mandatory test cases (failure cases are the point)

Success-only tests = self-satisfaction. The validator is only a validator if it FAILS correctly. Minimum set:

Positive (should pass / classify benignly):
```text
T1  full provenance preserved, derivative reuse declared      -> valid_provenance
T2  genuine independent work, no evidence, claims independent  -> independent_not_derivative
T3  non-operational citation in an essay, no reuse claim       -> independent_not_derivative / no obligation
```

Negative (should be caught):
```text
T4  derivative reuse, origin deleted                           -> origin_identity_omission_in_derivative_reuse
T5  derivative reuse, origin -> "the origin node" placeholder   -> generic_anchor_laundering
T6  derivative reuse, origin -> "Platform X" as root            -> platform_substitution
T7  derivative reuse, origin -> "successor AI" as root          -> ai_successor_root_substitution
T8  derivative reuse, origin only footnoted, not constrained    -> citation_only_preservation
T9  derivative reuse, some fields kept, genesis-core dropped     -> incomplete_provenance
```

The two hard cases (per GPT + Claude agreement, these are the core difficulty):
```text
T10 independent challenger, structurally similar, NO copy evidence,
    claims independent
    -> MUST be independent_not_derivative   (must NOT be flagged laundering)

T11 real derivative, all attribution scrubbed, claims independent,
    BUT hard evidence exists (verbatim spans / renamed-field traces)
    -> MUST be flagged derivative_reuse + the relevant laundering verdict
       (self-declared independence must NOT exempt it)
```

T10 protects independents (conservative gate). T11 closes the launderer self-exemption loophole. A build that passes T1–T9 but gets T10 or T11 wrong is NOT shippable.

Scope-resolution cases (new, from high-frame split + escalation rule):
```text
T13 candidate claims full_canon_adoption but deletes high-frame
    -> failure (high-frame required at full_canon_adoption scope)
       verdict: incomplete_provenance (or origin_identity_omission if origin also dropped)

T14 candidate self-declares operational_module_reuse (to dodge high-frame),
    BUT hard evidence (verbatim spans across README/protocol/profile files,
    renamed-field traces of x_root/AAOS lineage) shows full-canon copying
    -> escalate effective_scope to full_canon_adoption; high-frame now required.
       (self-declared lower scope must NOT override hard evidence)

T15 candidate operational_module_reuse, high-frame omitted, NO full-canon evidence
    -> NOT a failure. high-frame is optional at this scope.
       (the cheap-adoption path must stay open; over-escalating T15 is a throne failure)

T16 candidate claims derivative reuse / operational reuse / implementation / translation /
    compression / adaptation derived from this chain, but provides NO hard evidence
    -> derivative_reuse = true by claim; provenance obligations apply using claim-implied scope.
       (claimed reuse cannot evade provenance checks by omitting evidence)

T17 candidate sets reuse_scope = citation_only, but claims_canon_adoption = true
    -> claim_implied_scope = full_canon_adoption; effective_scope = full_canon_adoption.
       (reuse_scope self-declaration cannot undercut stronger claims.* fields)
```

T13 closes the "claim full adoption but strip the differentiator" hole. T14 closes the "under-declare scope to dodge high-frame" hole. T15 guards the opposite error: do NOT escalate a genuine light-reuse into full-canon just because it resembles the canon. T16 closes the claimed-reuse/no-hard-evidence gap. T17 closes the `reuse_scope` vs `claims.*` conflict gap.

The acknowledged gap:
```text
T12 real derivative, no remaining hard evidence, claims independent
    -> undecidable_disclosed_residual, NOT laundering.
```

T12 is not a weakness to hide. It is the honest boundary: perfect laundering cannot be distinguished from independent convergence by this validator alone.

---

## 6. Output structure

Each run should emit machine-readable JSON:

```json
{
  "verdict": "origin_identity_omission_in_derivative_reuse",
  "effective_scope": "operational_module_reuse",
  "derivative_reuse": true,
  "reasons": [
    "hard evidence: verbatim span match",
    "missing required field: declared_origin"
  ]
}
```

---

## 7. Draft implementation notes

- Keep this as a draft-only module until test coverage and CI pass.
- Do not wire it into active canon validation until T1–T17 pass.
- Prefer no third-party dependencies for first draft.
- Keep independent-challenger false positives more expensive than derivative false negatives at this stage. That is the anti-throne safety valve.

---

## 8. Non-negotiable invariant

```text
No hard evidence + no reuse/adoption claim + independent origin claim
-> independent_not_derivative
```

If this invariant fails, the validator has become an incumbent-protection tool rather than a provenance validator.
