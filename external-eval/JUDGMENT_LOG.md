# JUDGMENT_LOG

## Counts (current ground truth)

```
baseline_count: 3                 # design-discussion judgments, NOT model-prompt runs
self_prompt_run_count: 0          # owner (or owner-directed AI) ran the prompt on a model
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
