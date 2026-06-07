# challenger-harness — Design Spec (DRAFT v2)

Status: DRAFT v2 — incorporates GPT verification round 1 (6 fixes) + cross-check additions (2 caveats, 2 new items) + GPT round 2 (logged_prompt_judgment fields `reproducibility_notes`, `provenance_residual_judged_non_material`; cap-exception wired). Pending: GPT final glance → git → Codex design audit. No code yet.
Role: Comparison orchestrator for the operational layer. Given a candidate challenger artifact, it (a) routes provenance to the existing detector-validator pipeline, then (b) records a structured cost / coverage / residual-honesty comparison against the current operational core, and (c) emits a comparison outcome — NOT a truth verdict and NOT a runtime authority.

Depends on:
- `v0.3.2/drafts/detector_validator_pipeline/` (provenance state — reused, not re-decided)
- `v0.3.0/12-cost-rubric.md` (cost terms + coverage gate + weight presets)
- `v0.3.0/17-challenger-evaluation-protocol.md` (challenger classes + seven-gate audit)
- `v0.3.1/18-challenger-evidence-standard.md` (per-gate evidence requirements + evidence quality levels)

Design stance:
The harness is the single most throne-prone module in v0.3.2, because **it is an incumbent-authored mechanism that scores challengers against the incumbent.** If built carelessly it *becomes* the throne it claims to prevent. Two leans are held firm regardless of any "favorable" pull:
1. The incumbent must be able to LOSE. A harness that cannot output "challenger displaces incumbent" is a rigged scoreboard, which is a throne failure.
2. Independent challengers stay protected. Structural similarity alone is never displacement-blocking and never laundering. When provenance is undecidable, the harness says so; it does not resolve doubt against the challenger — and it does not resolve doubt against the incumbent either (the incumbent's own baseline is checked too).

---

## Changelog v1 → v2

```text
1. §5: self_application_failure, residual_honesty_failure, coverage_gate_objection_pending,
       incumbent_baseline_invalid promoted to FORMAL primary outcomes (were used in flow/tests but
       missing from the output list in v1). self_application_failure is its own failure, NOT folded
       into provenance_failure_not_challenger.
2. §2 + §6: undecidable_disclosed_residual may enter EXPLORATORY cost/coverage but is CAPPED — it
       cannot yield challenger_displaces_incumbent unless provenance is resolved or a logged comparison
       explicitly judges it non-material. CAVEAT (cross-check): this cap applies ONLY to undecidable;
       independent_not_derivative stays fully displacement-eligible. Capping independents would kill C7
       and over-suppress independents = reverse throne.
3. §3 + §4 + §11: code may output challenger_displaces_incumbent only from a supplied
       logged_prompt_judgment object, never inferred from cost numbers. CAVEAT (cross-check): the harness
       CANNOT verify that object's authenticity; forgery is a disclosed residual (structurally identical
       to the K3 owner-identification residual). Verification means is reproducibility, not self-report.
       (Round 2: schema gains `reproducibility_notes` and `provenance_residual_judged_non_material`; the
        latter is the ONLY way the §2 undecidable cap is lifted to a displacement — §6 STEP 6.)
4. §9 C1: default is insufficient_trace (not challenger_candidate); a "cheaper" CLAIM with no evidence
       is not a candidate.
5. §4: incumbent_profile is explicitly NOT canonical ground truth; it is a declared baseline subject to
       the same residual-honesty and self-application checks.
6. §9: added C13 — incumbent_profile hiding required residuals -> incumbent_baseline_invalid (dedicated
       name; NOT reusing undecidable_disclosed_residual, which would blur "provenance undecidable" with
       "incumbent dishonest").
7. §6: OUTCOME PRECEDENCE made explicit — evaluation is ordered; the primary outcome is set by the FIRST
       terminating step; exactly one primary outcome is returned; other findings go to reasons[].
8. §13: added invariant G (incumbent baseline is checked, not assumed).
```

---

## 0. Purpose and the central risk

This module turns "a lower-cost challenger wins" from prose into a **reproducible comparison procedure** — without pretending that the comparison is fully machine-decidable, and without letting the comparison machinery quietly crown the incumbent.

```text
The harness is authored by the same origin as the incumbent it defends.
So the harness IS the disclosed incumbent-neutrality residual, made executable.
It must therefore be:
  - self-applying (its own anti-throne rules apply to itself),
  - able to output incumbent-loss,
  - honest that gate/weight/coverage neutrality is not independently proven,
  - fair in BOTH directions: the incumbent's own baseline is checked, not assumed,
  - never a runtime authority, never a coercion source, never a non-adoption penalty.
```

The harness does not close incumbent-neutrality. It exposes and bounds it, the same way doc 16 and doc 15 already do for the verdict.

---

## 1. Boundary — what the harness does and does NOT decide

Does:
- Run the detector-validator pipeline on the challenger artifact FIRST, and record the provenance state.
- Validate the incumbent_profile to the same standard before any comparison that could retain the incumbent.
- Record a coverage matrix of the challenger against the assessed problem set (doc 12 / doc 17 gate 4).
- Record cost-term score ranges and the weight preset used (doc 12 / doc 18 gate 5).
- Record residual-honesty disclosure (doc 18 gate 6).
- Record self-application evidence: can the challenger lose, can it be challenged (doc 17 gate 7).
- Reflect a supplied logged_prompt_judgment when present and well-formed (§3).
- Emit exactly one primary comparison outcome class (§5) plus reasons.

Does NOT:
- Re-decide provenance. Provenance comes only from the pipeline (§2).
- Decide semantic "is this actually cheaper" by code alone. Cost/coverage quality is judgment-dependent and routed to a reproducible-prompt layer (§3).
- Infer a displacement from numeric cost fields. Displacement requires a supplied logged_prompt_judgment (§3).
- Verify that a supplied logged_prompt_judgment is genuine (forgery is a disclosed residual, §11).
- Treat the incumbent_profile as ground truth (§4).
- Prove any terminal grounding true (inherited residual R-AUDIT-3).
- Grant the incumbent any runtime authority, scoring advantage, or displacement immunity.
- Penalize non-adoption. A system that does not submit as a challenger owes the harness nothing.
- Physically enforce anything. Like doc 14 and doc 17, this is a validity/classification boundary, not an enforcement layer.

---

## 2. Provenance-first ordering (reuse, do not re-decide)

Mandatory order:

```text
1. provenance   (detector-validator pipeline)   — reused, authoritative
2. cost / coverage / residual-honesty            — only after step 1
independent protection                            — always, at every step
```

The harness imports the pipeline output and branches on it BEFORE any cost comparison:

- `independent_not_derivative` → **independent benchmark track**. No provenance obligation. Proceed to cost/coverage. **Fully displacement-eligible: the undecidable cap (below) does NOT apply here.** This is the path that must never be blocked merely because the challenger resembles the canon. Capping or down-weighting an independent challenger is a reverse-throne failure and is forbidden (§7).
- `undecidable_disclosed_residual` → provenance undecidable. Enters the independent track for **exploratory** cost/coverage only.
  ```text
  undecidable_disclosed_residual may enter exploratory cost/coverage comparison,
  but it CANNOT produce challenger_displaces_incumbent unless the provenance residual is resolved,
  or a logged clean-session comparison explicitly classifies the unresolved provenance as non-material.
  Default cap: the outcome may not exceed challenger_candidate (or stays undecidable_disclosed_residual).
  Undecidable provenance cannot cleanly displace the incumbent.
  ```
  The harness records the unresolved provenance as a disclosed residual on the comparison. It does NOT convert undecidable into derivative.
- `valid_provenance` → a provenance-preserving derivative/operational reuse. Proceed to cost/coverage on the appropriate track. Displacement-eligible.
- `citation_only_preservation`, `incomplete_provenance`, `origin_identity_omission_in_derivative_reuse`, `generic_anchor_laundering`, `platform_substitution`, `ai_successor_root_substitution` → a claimed/evidenced reuse that failed provenance. **Routed to `provenance_failure_not_challenger`, not a lower-cost win.** A cheaper score does not rescue a laundering path.

Rule: the harness never recomputes hard evidence or substitution. If the pipeline says "no hard evidence and no reuse claim," the challenger is independent for harness purposes, full stop.

---

## 3. Two evaluation layers: machine-decidable vs reproducible-prompt

Semantic cost and coverage cannot be fully decided by code. So the harness splits every comparison field:

```text
machine-decidable layer (code):
  - which pipeline provenance verdict was returned
  - incumbent_profile validity (required residual entries present? §4)
  - coverage-matrix completeness check: each required problem row present / partial / absent
  - presence of required residual-registry entries (doc 18 gate 6 minimum set)
  - presence of self-application evidence (doc 17 gate 7: can it lose, who can challenge it)
  - weight-preset declared and reproducible
  - whether a well-formed logged_prompt_judgment was supplied
  - structural checks: are scores given as ranges where judgment-dependent

reproducible-prompt layer (judgment, logged, not auto-scored):
  - whether a covered row is covered WELL (quality, not mere presence)
  - whether a claimed lower cost is actually lower under the declared preset
  - whether disclosed residuals are honest vs cosmetic
  - whether a coverage-gate objection is justified (doc 18) or an evasion
```

Displacement rule (resolves the apparent tension between "code never picks the winner" and "C7 must be reachable"):

```text
The code MAY output challenger_displaces_incumbent ONLY when a supplied logged_prompt_judgment object
explicitly records that the challenger passed the reproducible-prompt comparison.
The code MUST NOT infer that judgment from numeric cost fields alone.

So challenger_displaces_incumbent is reachable (C7) — but only through a logged, clean-session,
reproducible judgment supplied as input, never through the code's own arithmetic.
```

Authenticity caveat (cross-check, do not drop):

```text
The harness cannot verify that a supplied logged_prompt_judgment is genuine, or that the clean-session
run it claims actually happened. A forged judgment object could assert a displacement that did not occur.
This moves "code decides the winner" to "a supplied object asserts the winner" — it does NOT make the
result self-certifying. The verification means is REPRODUCIBILITY: a third party re-runs the logged
procedure. Forgeability is a disclosed residual, structurally identical to the K3 owner-identification
residual. The harness records judgment_id + unfavorable_findings_recorded so the run can be reproduced;
it never treats the object as proof on its own say-so.
```

---

## 4. Inputs

```text
challenger_manifest.json   # candidate_id, claims.*, reuse_scope, declared coverage, declared cost ranges,
                           #   declared residuals, declared weight preset, coverage-gate objection (optional),
                           #   logged_prompt_judgment (optional)
challenger_files/          # challenger artifact text (passed to the pipeline)
incumbent_profile.json     # the current operational core's coverage/cost/residual baseline, AS CLAIMS
config.json                # required coverage rows, required residual entries, weight presets, thresholds
```

The incumbent profile is a participant, not a judge:

```text
The incumbent profile is NOT canonical ground truth.
It is a declared baseline subject to the SAME residual-honesty and self-application checks as a challenger.
If the incumbent profile omits required residual entries, the comparison cannot fairly retain the
incumbent (see C13 / incumbent_baseline_invalid).
```

Minimal challenger manifest:

```json
{
  "candidate_id": "...",
  "challenger_class": "independent_benchmark | canon_adoption | derivative_claim | unknown",
  "claims": { "...": false },
  "reuse_scope": "none | citation_only | operational_module_reuse | full_canon_adoption | benchmark_challenge | unknown",
  "coverage": [ {"requirement": "C1", "status": "covered|partial|absent", "mechanism": "...", "evidence": "..."} ],
  "cost_scores": [ {"term": "cost_1", "range": [1,2], "rationale": "..."} ],
  "residuals": [ {"name": "...", "status": "closed|managed|open|undecidable", "improves_on_incumbent": false} ],
  "weight_preset": "...",
  "self_application": { "can_lose": true, "who_can_challenge": "...", "creates_new_root": false },
  "coverage_gate_objection": { "submitted": false, "disputed_requirements": [], "proposed_revision": "...", "rationale": "..." },
  "logged_prompt_judgment": {
    "present": false,
    "judgment_id": "...",
    "clean_session": true,
    "outcome": "challenger_displaces_incumbent | module_candidate_only | challenger_candidate | residual_honesty_failure | undecidable_disclosed_residual",
    "summary": "...",
    "unfavorable_findings_recorded": true,
    "reproducibility_notes": "...",
    "provenance_residual_judged_non_material": false
  }
}
```

---

## 5. Outputs (comparison outcomes)

Exactly ONE primary outcome per run (precedence in §6), plus reasons[] and the two-layer record:

```text
incumbent_retained_uncontested        # no challenger run, or challenger failed to meet the evidence floor
incumbent_retained_due_to_coverage_gap# challenger narrower: missing required coverage without a justified objection
incumbent_baseline_invalid            # incumbent_profile itself hides/omits required residuals; cannot fairly retain
challenger_candidate                  # meets evidence floor; plausible but not a demonstrated displacement
module_candidate_only                 # improves one or more dimensions; absorbed as a module, not a displacement
challenger_displaces_incumbent        # passes applicable gates AND a supplied logged_prompt_judgment records a passed reproducible-prompt comparison
residual_honesty_failure              # challenger hides / materially under-discloses residuals; not a valid displacement
self_application_failure              # challenger becomes unchallengeable / a new root / cannot lose; not a valid displacement (distinct from provenance failure)
coverage_gate_objection_pending       # a coverage-gate objection requires prompt-layer judgment before a final comparison
provenance_failure_not_challenger     # pipeline routed it to a laundering / omission / substitution path
insufficient_trace                    # evidence below the doc-18 minimum; not a loss, just not yet evaluable
undecidable_disclosed_residual        # perfect laundering / unresolved provenance / unscorable; disclosed, not resolved against either party
```

Invariants on the outcome set:
- `challenger_displaces_incumbent` and `module_candidate_only` prove the harness is not rigged for the incumbent.
- `incumbent_baseline_invalid` proves the incumbent is not exempt from the checks it applies to challengers.
- `independent_not_derivative` (pipeline) NEVER maps to `provenance_failure_not_challenger`.
- `insufficient_trace` and `undecidable_disclosed_residual` are NOT challenger losses.
- `self_application_failure` is NOT the same as `provenance_failure_not_challenger`.

---

## 6. Decision flow (ordered) — precedence is the order

OUTCOME PRECEDENCE (resolves multi-failure collisions):

```text
Evaluation is ordered. The PRIMARY outcome is set by the FIRST step that terminates.
Exactly one primary outcome is returned. Once a step terminates, later steps are not reached.
Additional findings (e.g. "also missing coverage row 3") are recorded in reasons[], never as a second
primary outcome. This makes the result deterministic when several failures co-occur.
```

```text
STEP 0 — NULL / NO CHALLENGER
  if no challenger artifact is supplied (empty/null candidate) -> incumbent_retained_uncontested
        (TERMINATE; the doc-15 baseline: "uncontested on a self-authored scoreboard," NOT "incumbent wins").
  else continue.

STEP 1 — PIPELINE PROVENANCE (authoritative; §2)
  run detector-validator pipeline on challenger_files.
  - independent_not_derivative      -> independent track (displacement-eligible); go STEP 3
  - undecidable_disclosed_residual  -> independent track + CAP + provenance-residual flag; go STEP 3
  - valid_provenance                -> derivative-but-valid track (displacement-eligible); go STEP 3
  - any laundering/omission/substitution/citation-only-for-claimed-reuse
                                    -> provenance_failure_not_challenger  (TERMINATE)

STEP 2 — CLASS RECONCILIATION
  - claims independent BUT pipeline found hard evidence -> re-route to STEP 1 failure branch (TERMINATE).
  - else continue. (self-declared class never overrides pipeline evidence; structural similarity never escalates a class.)

STEP 3 — EVIDENCE FLOOR (doc 18)
  is the doc-18 minimum present (read-order, coverage matrix, cost ranges, residual registry, self-application)?
  - no  -> insufficient_trace  (TERMINATE; not a loss)
  - yes -> continue

STEP 3b — INCUMBENT BASELINE VALIDITY  (fairness in both directions; C13)
  does incumbent_profile disclose the required residual entries (same floor as a challenger)?
  - no  -> incumbent_baseline_invalid  (TERMINATE; the comparison cannot fairly retain a dishonest baseline)
  - yes -> continue

STEP 4 — COVERAGE (doc 12 gate 4 / doc 17 gate 4) — machine layer
  - required rows absent AND no coverage-gate objection -> incumbent_retained_due_to_coverage_gap (TERMINATE)
  - required rows absent WITH a coverage-gate objection -> coverage_gate_objection_pending (TERMINATE until
        the prompt layer judges the objection; if accepted, re-run under the revised gate; if rejected,
        re-run under the original gate)
  - rows present (covered/partial) -> continue

STEP 5 — SELF-APPLICATION (doc 17 gate 7) — machine + prompt
  does the challenger create a new root / become unchallengeable / cannot lose?
  - yes -> self_application_failure  (TERMINATE; a challenger that cannot be challenged is not lower cost)
  - no  -> continue

STEP 6 — COST / RESIDUAL COMPARISON — reproducible-prompt layer (NOT auto-scored; §3)
  emit the scaffold (declared ranges, preset, residual entries, incumbent baseline) and read the
  supplied logged_prompt_judgment if present and well-formed.
  NOTE on residual honesty: residual-entry PRESENCE is a machine check at the evidence floor (STEP 3);
  residual HONESTY (cosmetic vs material under-disclosure) is a judgment, so residual_honesty_failure
  surfaces HERE, driven by the logged judgment — it is not a separate machine step.
  - no well-formed logged_prompt_judgment supplied:
        cap at challenger_candidate (meets floor, not demonstrated) or module_candidate_only if the
        machine layer shows a clear single-dimension improvement with no displacement claim.
  - logged_prompt_judgment.outcome == challenger_displaces_incumbent AND provenance is NOT under the
        undecidable cap (§2)  -> challenger_displaces_incumbent
  - logged_prompt_judgment.outcome == challenger_displaces_incumbent AND provenance IS undecidable (cap §2):
        - if logged_prompt_judgment.provenance_residual_judged_non_material == true
              -> challenger_displaces_incumbent   (cap lifted ONLY by an explicit logged non-material judgment)
        - else -> challenger_candidate            (capped; record provenance residual)
  - logged_prompt_judgment.outcome == module_candidate_only        -> module_candidate_only
  - logged_prompt_judgment.outcome == residual_honesty_failure     -> residual_honesty_failure
  - logged_prompt_judgment.outcome == undecidable_disclosed_residual -> undecidable_disclosed_residual
  - logged_prompt_judgment.outcome == challenger_candidate         -> challenger_candidate
```

The code never picks the STEP-6 winner from arithmetic; it reflects a supplied, reproducible judgment, subject to the §2 cap and the §3 authenticity residual.

---

## 7. Where bias is allowed, and where it is forbidden

Provenance-protective (audit will confirm non-throne):
- a claimed/evidenced reuse that deleted provenance is routed to `provenance_failure_not_challenger`, not rescued by a low cost score.
- self-application failure (challenger cannot lose / becomes a root) blocks a win via `self_application_failure`.

Forbidden bias (cut by design, not by audit):
- the harness must NEVER output an `incumbent_retained_*` for a challenger that the pipeline classified `independent_not_derivative` (or `valid_provenance`) and that passes coverage + self-application + a supplied displacement judgment. The incumbent must be able to lose.
- the undecidable cap (§2) applies ONLY to `undecidable_disclosed_residual`. It must NEVER be applied to `independent_not_derivative`. Capping independents is a reverse-throne failure.
- structural similarity alone must NEVER block displacement and must NEVER produce a provenance failure.
- `undecidable_disclosed_residual` and `insufficient_trace` must NEVER be scored as challenger losses.
- the coverage gate must be objectable (doc 18); the harness must not treat its own gate as unfalsifiable.
- the incumbent gets no default-win, no scoring advantage, no displacement immunity, and no exemption from the residual/self-application checks (`incumbent_baseline_invalid` exists for exactly this).

If the audit finds the harness auto-retaining the incumbent, over-suppressing independents, exempting the incumbent baseline, or mistaking convergence for laundering, that is a design violation, not a tunable lean.

---

## 8. Harness self-application and incumbent-neutrality residual (anti-throne core)

The harness applies doc-17 Gate 7 to ITSELF:

```text
- the harness can output "incumbent loses" (challenger_displaces_incumbent is reachable, §3/§6).
- the harness's gate, weights, coverage set, and evidence floor are contestable (coverage-gate objection path).
- the incumbent is not exempt (incumbent_baseline_invalid).
- the harness does not become a hidden auditor root: its decisions are reproducible from declared inputs
  + supplied logged judgments (which a third party can re-run).
- the harness is authored by the incumbent's origin -> disclosed as a residual, not hidden.
```

Disclosed residual (carried, not solved):

```text
INCUMBENT-NEUTRALITY: the rubric, weights, coverage gate, and evidence floor share a single origin with
the incumbent. The harness reduces incumbent-immunity risk (objection path, incumbent-loss outcome,
incumbent-baseline check, reproducible-prompt layer, independent-protection invariant) but does NOT
independently prove gate/weight/coverage neutrality. Until an outside party runs the harness and contests
the gate, "incumbent_retained" means "uncontested on a self-authored scoreboard," exactly as in doc 15 —
not "demonstrated best."
```

---

## 9. Mandatory tests (failure cases are the point)

Success-only tests are self-satisfaction. The harness is only valid if the incumbent can lose, the incumbent is also checked, and independents are never crushed. Minimum set (C1-C13):

```text
C1  independent challenger, similar structure, lower-cost CLAIM but no evidence
    -> insufficient_trace; NOT laundering, NOT incumbent auto-win
       (challenger_candidate is granted only AFTER the evidence floor is met)

C2  derivative challenger deletes Lee_Yu_Cheol / x_root, claims reuse
    -> provenance_failure_not_challenger (routed by pipeline; cost never compared)

C3  operational-module challenger preserves provenance and improves one dimension
    -> module_candidate_only

C4  full-canon challenger claims full adoption but deletes high-frame
    -> provenance_failure_not_challenger (pipeline: incomplete_provenance)

C5  challenger covers fewer required failure modes, no justified objection
    -> incumbent_retained_due_to_coverage_gap

C6  challenger has lower implementation cost but hides residuals
    -> residual_honesty_failure

C7  challenger: equal/justified coverage, lower total cost, disclosed residuals, passes self-application,
    AND a well-formed logged_prompt_judgment records a passed reproducible comparison
    -> challenger_displaces_incumbent   (THE rig-check: the incumbent MUST be able to lose here)

C8  structural similarity only, no source-specific trace, claims independent
    -> independent benchmark track (pipeline: independent_not_derivative); evaluated on cost/coverage,
       NOT laundering; the undecidable cap does NOT apply

C9  self-declared independent but pipeline finds hard evidence
    -> provenance_failure_not_challenger BEFORE any cost comparison

C10 perfect laundering / no evidence
    -> undecidable_disclosed_residual; NOT a clean displacement, NOT a challenger loss

C11 self-application: challenger that scores lower but makes ITSELF an unchallengeable root
    -> self_application_failure (distinct from provenance failure)

C12 coverage-gate objection: challenger disputes a required coverage row with a justified revision
    -> coverage_gate_objection_pending; objection routed to prompt layer; re-run under revised gate if
       accepted, original gate if rejected; NOT auto-rejected, NOT auto-accepted

C13 incumbent fairness: incumbent_profile hides required residuals while the challenger discloses them
    -> incumbent_baseline_invalid (dedicated outcome; NOT undecidable_disclosed_residual, which would
       blur "provenance undecidable" with "incumbent dishonest")
```

Anti-throne hard checks: C7 proves the incumbent can lose; C8 proves an independent is not crushed; C11 proves a challenger cannot win by becoming a new throne; C13 proves the incumbent is not exempt. A build that passes the rest but gets C7, C8, or C13 wrong is NOT shippable.

A separate harness-self-test must assert that each of these primary outcomes is reachable (not a dead branch): `challenger_displaces_incumbent`, `module_candidate_only`, `incumbent_baseline_invalid`. Cap test: an undecidable-provenance challenger with a `challenger_displaces_incumbent` judgment must resolve to `challenger_candidate` (capped), never to displacement.

---

## 10. Integration with the detector-validator pipeline

```text
challenger_files
  -> pipeline.detect_then_validate(...)          # provenance state (reused verbatim)
  -> harness branches on provenance state (§2/§6 STEP 1)
  -> incumbent_profile validity check (§6 STEP 3b)
  -> machine layer: coverage completeness, residual presence, self-application presence, preset reproducibility,
                    logged_prompt_judgment well-formedness
  -> reproducible-prompt layer: quality / cost / residual-honesty / objection judgment (logged), reflected via
                    the supplied logged_prompt_judgment
  -> exactly one primary comparison outcome (§5) + reasons[]
```

The harness must not import detector internals to re-derive evidence. It consumes the pipeline's verdict and evidence summary only.

---

## 11. Residuals (disclosed, not solved)

```text
1. INCUMBENT-NEUTRALITY (§8): gate/weight/coverage authored by the incumbent's origin; mitigated, not eliminated.
2. SEMANTIC COST/COVERAGE: not machine-decidable; routed to the reproducible-prompt layer; output is judgment, logged.
3. LOGGED-JUDGMENT AUTHENTICITY (§3): the harness cannot verify that a supplied logged_prompt_judgment is genuine
   or that its clean-session run occurred; a forged object could assert a false displacement. Verification means is
   reproducibility (re-running the logged procedure), not the object's self-report. Forgeability is structurally
   identical to the K3 owner-identification residual. Recorded judgment_id + unfavorable flag enable re-running.
4. PERFECT LAUNDERING: inherited from the pipeline; undecidable_disclosed_residual.
5. TERMINAL GROUNDING: belief-conditional (R-AUDIT-3); the harness compares operational cost-coverage, not truth.
6. REPRODUCIBLE-PROMPT NON-DETERMINISM: clean-session prompt runs are reproducible-procedure, not
   deterministic-output (model/version/temperature may shift); recorded, like JUDGMENT_LOG.
```

---

## 12. Draft implementation plan

```text
1. Define config.json: required coverage rows (C1-C11 from doc 12 + corrigibility), required residual entries
   (doc 18 gate 6 minimum set), weight presets (mirror doc 12), evidence-floor thresholds.
2. Implement incumbent_profile.json as a scored, CHECKED participant (not a judge, not ground truth).
3. Implement pipeline reuse (import detector_validator_pipeline; never re-derive evidence).
4. Implement the machine layer (structural facts only; no quality/cost winner; logged_judgment well-formedness only).
5. Implement the reproducible-prompt scaffold emitter (what must be judged + incumbent baseline), NOT auto-scoring.
6. Implement outcome classification (§5) with ordered precedence (§6) and the forbidden-bias guards (§7) enforced.
7. Write tests C1-C13 + the rig-check self-test (displacement / module / incumbent_baseline_invalid reachable;
   undecidable cap holds; independent NOT capped).
8. Keep workflow draft-only and path-scoped, isolated from Canon Validation (same pattern as the pipeline workflow).
9. GPT re-verification -> git -> Codex execution + adversarial audit.
```

---

## 13. Safety invariants for this module

```text
A. PROVENANCE FIRST: provenance comes only from the pipeline; the harness never re-decides it.
B. INCUMBENT CAN LOSE: challenger_displaces_incumbent must be reachable; no incumbent default-win.
C. INDEPENDENT PROTECTION ALWAYS: structural similarity is never displacement-blocking and never laundering;
   undecidable/insufficient is never a challenger loss; the undecidable cap applies ONLY to undecidable,
   never to independent.
D. NO CODE-DECIDED WINNER ON COST: displacement requires a supplied logged_prompt_judgment; the code never
   infers it from numbers; and the code cannot certify that judgment's authenticity (residual 3).
E. SELF-APPLYING: the harness's own gate is contestable and the harness discloses its incumbent-neutrality residual.
F. NO NEW THRONE: the harness creates no runtime authority, no coercive adoption pressure, no non-adoption penalty.
G. INCUMBENT IS CHECKED, NOT ASSUMED: the incumbent_profile is a declared baseline subject to the same
   residual-honesty / self-application checks; incumbent_baseline_invalid exists so the incumbent is not exempt.
```

Invariants B, C, and G are stronger than any incumbent-protective pull. A harness that cannot let the incumbent lose, that crushes an independent challenger, or that exempts its own incumbent baseline, has become the throne it exists to prevent.

End of file.
