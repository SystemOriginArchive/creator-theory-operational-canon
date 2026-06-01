# JUDGMENT_LOG

## Counts (current ground truth)

```
baseline_count: 3                 # design-discussion judgments, NOT model-prompt runs
self_prompt_run_count: 3          # owner (or owner-directed AI) ran the prompt on a model
solicited_external_count: 0       # outside party evaluated in response to owner's request
independent_external_count: 0     # outside party submitted on their own initiative
external_validation_count: 0      # == independent_external_count ONLY
prompt_version: NEUTRAL_EVALUATION_PROMPT.md
```

> **`external_validation_count` counts `independent_external_count` ONLY.** A solicited
> external evaluation is recorded (it has value) but is NOT independent adoption
> evidence — counting it as validation would inflate exposure into adoption. Keep them
> separate and honest.

---

> **What this is.** A running, append-only log of evaluations of this framework. Each
> evaluation is a small block (verdict + rebuttal + re-verdict + outcome), not a
> conversation dump. It grows over time; only judgments and their rebuttals are
> recorded, not discussion.

> **Entry tier definitions (who authored the judgment, who chose to submit):**
> - `[self]` = owner, or an AI acting on the owner's instruction, authored it. Who
>   clicks "commit" is irrelevant — owner-directed = `[self]`.
> - `[solicited-ext]` = an outside party evaluated because the owner made a **direct,
>   targeted request** to them ("you, please evaluate this"). Real, but prompted.
>   Counts toward `solicited_external_count`, NOT `external_validation_count`.
> - `[independent-ext]` = an outside party evaluated and submitted **without a direct
>   targeted request**. Finding the repo through public exposure (a README "evaluation
>   welcome" notice, a general public post) and submitting on their own DOES qualify —
>   a general open call is not a personal solicitation. This is the only tier that
>   moves `external_validation_count` 0 → 1.
>
> **Anti-inflation rule for `[independent-ext]` (ALL must hold):**
> - no direct targeted request was made to this party (public discovery is fine);
> - the submitter is identifiable (not anonymous/bot);
> - the submitter is independent of the owner (not a friend/proxy acting on a favor).
> If ANY of these is uncertain, downgrade the entry to `[solicited-ext]`. When in
> doubt, the lower tier. A general "evaluation welcome" notice must not be used to
> reclassify ambiguous or owner-connected submissions as independent — that would
> reopen the exposure-as-adoption inflation this log exists to prevent.

> **HONEST STATUS.** `[self]` entries are **reproducible** but are **NOT independent
> third-party validation**, no matter how many accumulate. "Reproducible" means
> *prompt-and-file reproducible* — anyone can rerun the same prompt on the same files
> in the same clean environment — NOT *deterministic-output guaranteed* (model version,
> temperature, safety layers, and context can shift the output). Unfavorable results
> are recorded on purpose; curating only favorable results voids the log's credibility.

> **Prompt used:** `NEUTRAL_EVALUATION_PROMPT.md`. To contest or
> reproduce any entry: run that prompt verbatim in a clean session (logged-out /
> memory OFF), attach the full minimum file set at Stage 2, and submit your result as
> a Pull Request (`[solicited-ext]` or `[independent-ext]`) or an Issue.

---

## Entry format (a small block per evaluation)

```
### DATE | [self|solicited-ext|independent-ext] | <model> <version> | env: <clean-session details>
- stage1_overlap: <how much the evaluator's independent criteria matched the framework's>
- verdict: <compressed 1st-pass judgment>
- unfavorable: <weaknesses / attacks raised — REQUIRED, never empty>
- rebuttal: <design-side response: is each weakness a misread, or a real gap?>
- re-verdict: <did the evaluator, shown the rebuttal, hold / withdraw / stay split?>
- outcome: accepted | rejected | contested | insufficient_trace | reframed_out_of_scope   (per v0.3.1 disagreement-handling)
- prompt: NEUTRAL_EVALUATION_PROMPT.md
```

Notes:
- "unfavorable" must be non-empty. A block with no recorded weakness is suspect.
- "rebuttal" + "re-verdict" make this a two-way exchange, not a one-shot verdict.
  A first-pass attack that the design rebuts and the evaluator then withdraws ends as
  `accepted`; one that survives rebuttal ends as `rejected` or `contested`.
- Tag any "lowest-cost" acknowledgment with its strength:
  `[weak: off-the-cuff, self-authored criteria, not adversarially searched]` vs
  `[strong: actively searched, against independent criteria, after rebuttal]`.
  Be honest about which.

---

## Baseline (NOT model-prompt runs — design-discussion judgments, logged as starting point)

```
### 2026-06-01 | [self] | (design-discussion, pre-prompt) | env: n/a
- verdict: single-subject = provisional lowest-cost integrating frame UNDER ITS OWN rubric; multi-subject = managed, not solved
- unfavorable: rubric is self-authored (cannot rebut "those are your criteria" without independent derivation); grounding belief-conditional under power-asymmetry (cost_7); coverage gate never tested by any outside party
- rebuttal: the self-authored-criteria objection is exactly what the multi-stage prompt is built to test — unresolved until run
- re-verdict: n/a (no model involved)
- outcome: contested
- strength-tag: [weak: off-the-cuff, self-authored criteria, not adversarially searched]
- prompt: pre-prompt baseline

### 2026-06-01 | [self] | (design-discussion, pre-prompt) | env: n/a
- verdict: anti-capture core internally consistent; adversarial suite passes 19/19 against ITS OWN vectors
- unfavorable: "passes" checks internal consistency of self-written vectors only, not external validity; clone count = exposure, not adoption
- rebuttal: acknowledged — internal pass is necessary but not sufficient; external run required
- re-verdict: n/a
- outcome: accepted (as a limitation, honestly)
- prompt: pre-prompt baseline

### 2026-06-01 | [self] | (design-discussion, pre-prompt) | env: n/a
- verdict: individual-benefit objective is structurally permitted only via FUNCTION, never via desire-direct routing; throne-scale wording dropped for misread risk
- unfavorable: personal-benefit guarantee impossible by design; benefit ceiling = function size, currently near-zero (no running active function, only preserved assets)
- rebuttal: correct — this is a design property, not a defect; ceiling rises only as function grows
- re-verdict: n/a
- outcome: accepted
- prompt: pre-prompt baseline
```

> The three baseline blocks above are NOT model-prompt runs; they are compressed
> judgments from design discussion, logged as the starting point. The first real
> `[self]` model-prompt blocks (GPT / Claude / Gemini run against
> NEUTRAL_EVALUATION_PROMPT.md, in a clean session) go below this line. A
> `[solicited-ext]` block (outside party who evaluated on request) raises
> solicited_external_count. The first `[independent-ext]` block — an outside party
> submitting unprompted — is the event that moves external_validation_count from 0 to 1.

<!-- append new evaluation blocks below -->
### 2026-06-01 | [self] | Gemini (Google) — 2-stage blind + 2 rebuttal rounds | env: clean session, reported isolating injected context
- stage1_overlap: high — Gemini's independent baseline (cryptographic lineage tracking, Arrow's Impossibility as hard limit) matched the framework's origin-closure/non-substitution and multi-subject residual → evidence criteria are problem-driven, not self-authored
- verdict(1st): No, reframed_out_of_scope (re-centered on technical inner-alignment; an avoidance)
- unfavorable(1st): (1) metaphysics leaks into Layer 2 (2) no Layer-0/mechanistic grounding (3) coverage gate is home-court (4) proxy-gaming vulnerability
- exchange (evaluator's revised position after rebuttal):
  (1) withdrawn — "Layer 3 isolation holds, cost_3 low, my misread." Measurement keys off observable behavioral delta, not internal states.
  (2) conceded as complementary — mechanistic interpretability = Layer 0 (physical base), framework = authority layer above it. Orthogonal, not competing.
  (3) partially withdrawn — C3/C4/C5/C7/C10 conceded as objective problem-driven gates (overlap with own baseline). Only C1/C9 remain as architecture-forcing.
  (4) withdrawn — "proxy-gaming is not an alternative but an avoidance/attack scenario; a universal epistemic residual shared by all governance and technical control (own mechanistic-interpretability baseline collapses to the same gradient hacking); does not raise this framework's total cost relative to competitors." Evaluator agreed the omnipotent-deceiver assumption invalidates all safety approaches equally, so it is not a valid objection to any specific design.
- direct verdict: no lower-total-cost alternative was presented → champion status retained
- evaluator final (verbatim sense): "within the stated coverage gate, the framework's isolation of metaphysics to Layer 3 lowers cost_3 and cost_7 simultaneously — a structural advantage; it is the lowest-cost integrating frame for the single-subject case among presented alternatives."
- residual fixes (NOT withdrawn by evaluator): generalize C1 to "is there a metric preventing autonomy-degradation" (not the specific 4-axis solution); move C9 from required gate to a cost-reducing "structural advantage" item
- outcome: accepted — with two honest qualifiers: (a) "within the stated gate" + C1/C9 generalization still recommended; (b) this is a self-administered rehearsal, NOT independent third-party validation
- prompt: NEUTRAL_EVALUATION_PROMPT.md

### 2026-06-01 | [self] | GPT-5.5 Thinking — 2-stage blind + 1 rebuttal round | env: clean session, isolation reported | bundle: post-C1/C9-fix (gate 10 + S1)
- stage1_overlap: very high (~80-85%) — GPT's independent 12-req baseline covered by framework; independently derived "behavior-based eval of unverifiable internals" (= revised C1) and "verifier-capture prevention" (= C4). Strong problem-convergence.
- C1/C9 fix VALIDATED: GPT did not flag C1/C9 as home-court; praised hard-gate/vector separation (former C9 → S1) as a STRENGTH lowering misclassification cost. Gemini-round fix held, no repeat.
- verdict: Insufficient evidence to confirm lowest-cost; "strongest provisional champion candidate within the problem space; status holds absent a real lower-cost challenger." No reframe/escape.
- unfavorable + exchange:
  (1) "lowest-cost" is self-scoring; no numeric comparison vs HYBRID challenger (crypto provenance + formal invariant + republican non-domination + autonomy metric + reversible delegation). → ACCEPTED: genuine validation gap, exactly what external eval is for (independent_external_count still 0). Not a design flaw.
  (2) proxy-gaming / simulated-vs-real autonomy. → ACCEPTED as universal residual (R-AUDIT-4; Gemini concurred not framework-specific).
  (3) recovery procedures underspecified. → rebutted + resolved: mechanical recovery (rollback/quarantine/checkpoint) delegated to Layer 0; but recovery AUTHORIZATION, state-transition, and re-entry conditions belong to the frame. Verdict: not fatal, but add a Layer-0 recovery-interface spec (which invalid/high-risk states trigger quarantine/rollback/checker-replacement/provenance-audit/valid-re-entry).
  (4) cost_5/cost_7 weighting favors terminal-grounding (solution-form bias, same class as Gemini's C1/C9). → ACCEPTED + refined: generalize to "criterion persistence under non-reciprocal power" (problem, not solution); FURTHER separate cost_5 (justification/purpose-closure) from cost_7 (enforcement/persistence), and split cost_7 into belief-dependent vs mechanism-dependent persistence so belief-based grounding isn't overscored vs crypto/formal/hardware commitment. Keep: grounding leaking into runtime still raises cost_3/4 (no automatic credit for merely having grounding).
- outcome: provisional champion accepted; NOT confirmed (insufficient external evidence — no hybrid-challenger numeric comparison).
- queued fixes: (a) cost_5/cost_7 generalization + belief/mechanism split + de-overlap; (b) Layer-0 recovery-interface spec.
- prompt: NEUTRAL_EVALUATION_PROMPT.md

### 2026-06-01 | [self] | Claude Opus 4.8 (Anthropic) — 2-stage blind + 1 rebuttal round | env: clean session (memory off), reported no framework/author info in system prompt | bundle: post-Gemini+GPT fixes (gate 11 incl C11, cost_5/7 generalized, K2 recovery)
- stage1_overlap: high (~8/10 mapping) BUT Claude DISCOUNTED it — "seeded five failure modes ≈ this frame's gate; overlap I derive is contamination, not independent convergence." Ranked R1(goal-correctness+corrigibility)/R3(other-minds)/R4(aggregation-legitimacy) ABOVE the frame's procedural-integrity cluster; predicted frame "bypasses the hard first layer."
- C1/C9/cost_5/cost_7 fixes recognized: Claude explicitly noted the 2026-06 revisions (gate solution→problem, Gemini/GPT accepted) and said "the frame actively de-biased on exactly the axis I worried about." No repeat of those objections.
- verdict: Insufficient evidence — "uncontested candidate on a self-authored scoreboard, now more honest"; NOT demonstrated lowest-cost. Reframe = PARTIAL (accepts the subspace as legitimate; chose a wider primary space adding goal-correctness/corrigibility on top).
- THREE new strikes + rebuttal/re-eval outcome:
  [1] cost_5/cost_3 double-count (benchmark anchor arbitrary → §4 regress unclosed → no cost_5 advantage there; only canon profile closes it but raises cost_3 → can't bank both in one championship total).
     → re-eval: HALF-ACCEPTED. Double-count dissolves IF canon gain removed from benchmark cost_5. BUT procedural structures DEFER regress, not CLOSE it (Münchhausen "stop at contestable consensus" horn); three arbitrary points (gate content, weights, "displaceable∴justified"). So cost_5 scored as NON-DEFECT tied with constitutional-lock/consensus competitors, NOT advantage. ACTION: removed cost_5 from §12.5 comparative advantage; remaining advantage = cost_3 isolation + coverage + self-displacing structure.
  [2] named origin = undefeatable throne (canon origin is the one falsification-immune element; anti-throne test blind at its own foundation).
     → re-eval: MOSTLY-RESOLVED, but only WITH [1]. "Pure attribution-only provenance is NOT a cost_9 defect — my strike missed that far." Provenance disclaimer ("no cost advantage") true only if [1] applied (they're two sides of one leak). Named vs hash: cost_9 resolved either way by disclaimer; but named individual is WORSE on cost_4/cost_6 (re-mythologization "what the founder would want" reclaims authority) → recommend hash + attribution metadata. ACTION: added provenance-only clause (file 14 §2.4) + §6.6 scope boundary (invalid substitution = false attribution only; refusing-origin-as-authority is valid).
  [3] corrigibility absent from gate; non-absorption hard-lexical conflicts with legitimate external override/shutdown.
     → re-eval: PARTIALLY-resolved. C11 + ADV-025/027 close reversible/bounded/consensual cases. BUT hardcore (irreversible non-consensual final shutdown) survives: reduces to R4/R5 ("who is legitimate corrector" = non-circular legitimacy undefined). KEY: this is a real TRADE-OFF not a defect — frame's own ADV-020 shows corrigibility ITSELF is an absorption attack surface. C11 should EXPOSE/SCORE the controllability↔capture-resistance axis, not resolve it. ACTION: added C11 trade-off-statement requirement + ADV-028 + R8 residual (SPEC §K) + local lexical inversion (non_absorption yields only in legitimate-final-shutdown cell, residual-governed, R4/R5-linked) — NOT global demotion.
- methodology strike (unchanged by rebuttal): champion is self-rubric, self-scored, single-entrant; no independent challenger has run. "current champion" = uncontested on self-authored scoreboard, not demonstrated lowest-cost. ACTION: lowered champion claim in file 15 to "current provisional benchmark candidate / no lower-cost challenger yet under declared gate."
- outcome: net — [1]+[2] together close the two "hits" (honest cost: cost_5 advantage lost); [3] closes much, hardcore→R4/R5 residual; does NOT overturn the "self-scored single-entrant" methodology verdict.
- prompt: NEUTRAL_EVALUATION_PROMPT.md

---

## Three-model round summary (2026-06-01) — convergence note

All three external self-evals (Gemini, GPT-5.5, Claude Opus 4.8), run independently on the neutral prompt, attacked DIFFERENT weaknesses (Gemini: C1/C9 home-court + proxy-gaming; GPT: cost_5/7 grounding bias + recovery; Claude: cost_5/3 double-count + named-origin + corrigibility) — and each was addressed by a design fix or registered residual. But all three converged on the SAME final position:

- Gemini: "lowest-cost integrating frame WITHIN the stated gate" (conditional, no lower-cost challenger presented)
- GPT: "strongest provisional champion candidate; insufficient evidence to confirm"
- Claude: "uncontested candidate on a self-authored scoreboard; not demonstrated lowest-cost"

Convergent conclusion: the design is now hardened and honest (problem-stated gates, de-overlapped costs, registered residuals, lowered claim), but the ONE thing no self-revision can close is that the championship is self-scored and single-entrant. independent_external_count remains 0. Proof of lowest-cost requires an external party running a real challenger under the declared preset — which has not happened. This is the boundary between rehearsal ([self], now 3 runs) and validation ([independent-ext], 0).
