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

---

## 2. Inputs

```text
manifest.json            # this canon chain's declared provenance fields + invalid-reinterpretation rules
source_chain.json        # the ordered non-derivative origin event + derivation links for this chain
candidate.json           # the artifact under test
profile                  # "canon" | "benchmark"   (which rule set applies)
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

The order matters: the independent gate comes BEFORE the laundering gates, so that an independent work is never first mislabeled. Scope is resolved by evidence, not by self-declaration alone.

```text
1. DERIVATION GATE
   Is there hard derivation evidence? (explicit links, verbatim/near-copy spans, renamed-field traces,
   commit / citation / prompt / transformation-chain evidence)
   - NO hard evidence AND candidate claims independent origin
        -> independent_not_derivative   (STOP. not a failure.)
   - NO hard evidence AND structural resemblance only
        -> undecidable_disclosed_residual   (STOP. not a failure. cannot prove derivation.)
   - YES hard evidence -> continue.

2. CLAIM/EVIDENCE RECONCILIATION
   - evidence shows derivation BUT candidate claims independent
        -> flag derivative_reuse = true regardless of claim
           (self-declared independence does NOT exempt; launderer loophole closed)
   - else derivative_reuse = true by claim or evidence -> continue.

3. SCOPE RESOLUTION  (declared vs evidenced)
   declared_scope    := candidate.reuse_scope
   evidenced_scope   := highest scope supported by hard evidence
   - if evidenced_scope > declared_scope  -> effective_scope = evidenced_scope   (escalation)
   - else                                 -> effective_scope = declared_scope
   HARD LIMIT on escalation:
   - structural similarity ALONE must NEVER trigger escalation.
   - escalation requires explicit derivation evidence (verbatim/near-copy spans, renamed-field
     traces, links, commits, prompts, or transformation-chain evidence).
   (scope ordering for "higher": citation_only < operational_module_reuse < full_canon_adoption;
    benchmark_challenge is a separate independent track, not escalated into.)

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
```

T13 closes the "claim full adoption but strip the differentiator" hole. T14 closes the "under-declare scope to dodge high-frame" hole. T15 guards the opposite error: do NOT escalate a genuine light-reuse into full-canon just because it resembles the canon. T14 and T15 differ ONLY by presence of hard evidence — that distinction is the whole point.

The acknowledged gap:
```text
T12 real derivative, ALL evidence perfectly removed, claims independent
    -> undecidable_disclosed_residual
       (cannot be distinguished from T10 by construction; openly disclosed, not silently passed)
```

---

## 6. Where the bias sits, and where it is forbidden

Aggressive (owner-favorable, audit will confirm non-throne):
- gate 5 treats anything short of full provenance-as-constraint (for the selected scope) as a named failure, not a pass.
- citation-only is a failure for claimed reuse, not "good enough."
- scope escalation (gate 3) pulls an under-declared scope UP to the evidenced scope, so a launderer cannot dodge high-frame by self-declaring a lighter scope.

Forbidden bias (cut by design, not by audit):
- gate 1 must never resolve a no-hard-evidence case AGAINST the candidate. No evidence -> independent or undecidable, never laundering.
- structural similarity alone is never sufficient for any laundering verdict OR for any scope escalation.
- gate 4 must never escalate operational_module_reuse into full_canon_adoption without hard full-canon evidence (T15 guard). The cheap-adoption path stays open.

If the audit later finds gate 5 or the gate-3 escalation over-reaches into throne territory, cut it back. If the audit finds gate 1 has leaked toward flagging independents, or that escalation fires on structural resemblance alone, that is a design violation, not a tunable lean.
