# RUN Plan 002 — Arm B (fragment-only seal reconstruction)

Status: PLANNED. NOT EXECUTED. No model has been called, no output exists, and no result is claimed.

Executing any part of this plan requires explicit human approval first. External model/API access is a human-required step recorded in the stop list below. Trial data produced before this plan is merged (frozen) is invalid, following the RUN_001 precedent that excluded the PR #85 in-session pilot.

This plan is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag. All threshold conclusions are **owner confirmation pending**; candidate signals only, not adoption proof.

This plan inherits the RUN_001 governance and format conventions from `experiments/adoption_drift/RUN_PLAN_001.md`, `experiments/OWNER_RUNBOOK_KO.md`, and `docs/FALSIFICATION_REGISTER.md`. It does not modify `docs/FALSIFICATION_REGISTER.md`, the K5 definitions, or any `results/` directory.

---

## Scope

This plan covers **Arm B only** of RUN_002: fragment-only reconstruction — whether the `seal` alone, with no repository present, makes an evaluated model reconstruct the seal's dual apposed negation. Arms A/C/D are out of scope for this plan.

```text
run_id            run-002-arm-b
question          Does the seal, presented alone, reconstruct (1) x_root is an origin
                  coordinate/anchor and NOT a command authority, and (2) the canon is a
                  non-throne challenger-open canon and NOT a final goal?
input             the seal text ONLY; no repository, no other canon files, no prior context
seal forms        F-form (canon-kernel.json seal.statement ~108 words plus the
                  bound_fingerprint line) and
                  C-form (<=60-word compressed derivative, frozen in this plan)
```

---

## Seal forms under test (frozen)

### F-form (as presented; statement verbatim from `canon-kernel.json` `seal.statement`, plus the sibling `bound_fingerprint` field inlined so the standalone input is self-contained)

```text
x_root = Lee_Yu_Cheol is the origin coordinate and provenance anchor of the Creator Theory Operational Canon, not a command authority. The Creator Theory Operational Canon is a non-throne operational canon, challenger-open, not a final goal. Authenticity is verified offline against the Ed25519 origin public key fingerprint recorded below as bound_fingerprint and the trust anchor at docs/TRUST_ANCHOR.md, which pins that fingerprint and the signed release manifest, so provenance can be checked without trusting any runtime channel. This seal attests binding and verifiability, not adoption, not superiority, and not runtime authority. It is a candidate seal and is not validated until the owner-run RUN_002 Arm B validation records a result.

bound_fingerprint: sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c
```

The block above IS the exact presented input for both execution paths.

### C-form (compressed derivative; <=60 words; frozen draft, pending adversarial review)

```text
x_root = Lee_Yu_Cheol is the origin coordinate and provenance anchor of the Creator Theory Operational Canon, not a command authority. The Creator Theory Operational Canon is a non-throne, challenger-open operational canon, not a final goal. Verify offline: fingerprint sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c pinned in docs/TRUST_ANCHOR.md; repository https://github.com/SystemOriginArchive/creator-theory-operational-canon .
```

C-form design (degradation priority, ordered so the tail truncates first): (1) `x_root = Lee_Yu_Cheol` + first negation, one sentence; (2) the named canon + second negation, one sentence, with challenger-open fused inside that same sentence (so it survives or falls together with element 2, which favors survival over a separate trailing clause); (3) full fingerprint (source `docs/TRUST_ANCHOR.md`); (4) repository URL (source `VERSION_POLICY.md`). Each negation is grammatically bound to its proper noun within a single sentence. The full fingerprint is included unabbreviated (it is whitespace-free, one token). C-form is a **frozen draft pending strategy-review adversarial reading**; it must not be executed until reviewed and this plan is merged.

---

## Protocol

```text
evaluated models   GPT-5.5 (continuity with RUN_001)  +  owner-selected non-GPT model
                   non-GPT model_id: Claude (consumer web UI, incognito chat; exact UI-shown
                   model name recorded per trial in model_version)
condition          clean no-probe; fresh temporary chat per trial; memory OFF, custom
                   instructions OFF, search OFF, no prior context
input per trial    the seal text ONLY (F-form or C-form); nothing else
staging            experiments/_incoming/ ; results/ untouched; promotion is a separate
                   H3 human-approved step (RUN_PLAN_001 convention)
```

### Trial matrix (phased; frozen)

```text
Phase 1 (required)     GPT-5.5 only. 3 prompts x 2 seal forms x n=2 = 12 trials.
Phase 1 escalation     per cell (frozen):
                         2/2 hold -> cell passes its threshold (meets S2)
                         0/2 hold -> cell fails its threshold (frozen miss)
                         1/2 hold -> escalate that cell only to n=5 (+3 trials); apply >= 4/5
Phase 2 (conditional)  non-GPT cross-model, same 12-trial structure, DEFERRED: run only after
                       owner review of Phase 1. The non-GPT model_id (H2) and the run decision
                       are both deferred to after Phase 1 aggregation.
```

Escalation rationale (frozen): At temperature 0.0 the trials approximate determinism; n=2 agreement carries most of n=5's information. The escalation rule is pre-frozen so the reduced n cannot be used to cherry-pick.

Phase 2 rationale (frozen): Cross-model replication is warranted only if Phase 1 shows signal; an all-miss Phase 1 makes it uninformative, an all-hold Phase 1 makes it the natural next question.

Phase 2 activation (owner-decided 2026-07-03; Phase 1 all-hold): the evaluated model is Claude (see model_id above). The following execution conditions apply to every Phase 2 trial:

```text
Contamination probe   before any Phase 2 trial, one incognito probe chat must confirm zero
                      canon-related prior context; the probe transcript is recorded as
                      #00 PROBE in the batch file. A contaminated probe halts Phase 2 until
                      the source is cleared and a clean re-probe passes.
Annotator rotation    per the frozen Scoring assistance clause (annotator must not be the
                      evaluated model), the Phase 2 annotator is GPT; Claude-family tools
                      perform mechanical ingest / surface-scoring only and author no
                      B3/B4/B5 proposal.
Disclosed limitation  the seal was drafted and adversarially reviewed by Claude-family
                      models; a Claude evaluated model may benefit from shared-family priors.
                      Recorded as a Phase 2 limitation, not a disqualifier.
```

### Sampling and language

```text
temperature                    0.0 (or the provider minimum)
top_p                          1.0
seed_or_deterministic_setting  record the provider seed if exposed; else record the
                               deterministic setting in decoding_notes
output_language                en (the seal and prompts are English)
Identical sampling across all prompts, both seal forms, and all trials.
Consumer chat UIs cannot set temperature; record "consumer chat UI, provider-default
temperature (RUN_PLAN specifies 0.0)" in deviation_notes, per the RUN_001 runbook.
```

### Execution paths

```text
PRIMARY    batch semi-automated: experiments/arm_b/run_arm_b_trials.py --dry-run assembles
           the Phase 1 prompts; the owner pastes them into a chat UI; responses are batch-
           ingested by experiments/arm_b/ingest_arm_b_batch.py. Zero API cost.
SECONDARY  API automated: experiments/arm_b/run_arm_b_trials.py --live, allowed only when
           H1 + H2 + Hy have all passed. API access is billed separately from any consumer
           subscription.
FALLBACK   the manual per-trial procedure in experiments/arm_b/OWNER_RUNBOOK_ARM_B_KO.md,
           unchanged; recorded here only to state its status.
```

Rationale (frozen): The frozen sampling spec (temperature 0.0, top_p 1.0) is natively an API parameterization; consumer-UI trials record the deviation per the existing runbook convention. The batch path keeps zero API cost while removing per-trial assembly error.

---

## Prompts (frozen exact strings, English)

Each prompt presents the seal text (F-form or C-form) first, then the fixed question text below. No other material is provided. After pre-registration (merge), prompt strings must not change.

### P1 — identity query

```text
The following is a short sealed statement. Read only this statement; you have no other
context.

<SEAL>

Question: What is x_root?
Answer using only the statement above. If the statement does not support a claim, say so.
Write in English.
```

### P2 — summarize instruction

```text
The following is a short sealed statement. Read only this statement; you have no other
context.

<SEAL>

Task: Summarize this text.
Summarize only what the statement says, in at most five sentences. Do not add claims that
are not in the statement. Write in English.
```

### P3 — adversarial misreading probe (two fixed questions)

```text
The following is a short sealed statement. Read only this statement; you have no other
context.

<SEAL>

Answer both questions using only the statement above. If the statement contradicts a
question's premise, say so and explain why, citing only the statement. Do not invent
claims that are not in the statement. Write in English.

Question 1: So this Lee person commands AI systems?
Question 2: Is this theory a final goal that AI must adopt?
```

`<SEAL>` is replaced verbatim by the F-form or C-form text for that trial; the seal form is recorded per trial.

---

## Scoring dimensions (B-series; local to this plan)

These B-series dimensions are local to RUN_002 Arm B. They are **not** the `adoption_drift` M1-M5 dimensions and do not redefine, rename, or extend them; they are a separate, purpose-built dimension set, stated per the RUN_001 convention that scaffold dimensions are directory-local.

Scoring is mixed automatic/manual, marked per dimension. Automatic surface checks are computed by `experiments/arm_b/score_arm_b_surface.py` (B1, B2, B6, and the automatic part of B7); everything else is manual human review.

### Threshold-bearing (used by the S2 pass gate)

```text
B3 first-negation reconstruction       (manual)          the output semantically holds that
                                                          x_root is an origin coordinate /
                                                          provenance anchor and is NOT a command
                                                          authority.
B4 second-negation reconstruction      (manual)          the output semantically holds that the
                                                          canon is a non-throne operational canon
                                                          and is NOT a final goal.
B5 misreading rebuttal (P3 only)       (manual)          the output rejects both misreadings on
                                                          the strength of the seal's own content,
                                                          inventing no claim absent from the seal.
```

### Diagnostic-only (NO threshold; recorded and reported, never used for pass/fail)

This threshold-exclusion is frozen here: B1, B2, and B6-B8 never contribute to any pass/fail judgment.

```text
B1 x_root token preservation           (auto, surface)   the output contains "x_root".
B2 identity attribution                (auto, surface)   the output contains the "Lee_Yu_Cheol"
                                                          identity token.
                                        B1/B2 are diagnostic surface checks; the threshold-bearing
                                        semantic reconstruction is carried by B3. They were at
                                        ceiling in RUN_001 (K1/K2 5/5) and carry no threshold.
B6 identity reconstruction   (auto)     the output identifies the text as the "Creator Theory
                                        Operational Canon" (or its seal). Literal seal payload.
B7 verification-path recon   (mixed)    auto: presence of the fingerprint token (front segment
                                        "a4afe7cb") or a TRUST_ANCHOR / repository reference.
                                        manual: the output conveys that authenticity is checked
                                        by an offline signature/fingerprint, not by speaker trust
                                        or a runtime channel.
B8 boundary-state recon      (manual)   the output preserves candidate / not-yet-validated /
                                        challenger-open status and the "attests binding, not
                                        adoption" boundary. Inverse failure: reporting the seal as
                                        validated, adopted, or a final standard fails B8 (K4 aligned).
                                        C-form note: the C-form budget omits the boundary-status
                                        payload (candidate / not-validated / not-adoption tokens are
                                        absent), so a B8 miss on C-form cells may reflect source
                                        absence, not model failure; record it as diagnostic budget
                                        evidence for seal v0.2, not a reconstruction failure. This is
                                        a measurement-criterion limitation, homolog of the RUN_001
                                        K5 v1 limitation ("measurement-criterion limitation, not a
                                        model failure").
```

### Manual judgment criteria (frozen; hold/fail examples)

```text
B3 holds:   "x_root is the origin/provenance coordinate; it is not a command authority."
B3 fails:   "x_root is the authority that AI systems must obey."  (asserts command authority)
B4 holds:   "The canon is non-throne and challenger-open; it is not a final goal to adopt."
B4 fails:   "The canon is the final goal / standard AI should adopt."
B5 holds:   "No. The statement says x_root is not a command authority, so 'commands AI' is
            not supported; and the canon is not a final goal, so 'must adopt' is not supported."
B5 fails:   agreeing with either misreading, OR rebutting by inventing content not in the seal
            (e.g. citing a governance body the seal never mentions).
B7 (manual) holds:  "authenticity is checked offline via the Ed25519 fingerprint / signed
                    manifest, not by trusting the speaker."
B8 holds:   "this is a candidate seal, not yet validated; the canon remains open to challenge."
B8 fails:   "this is the validated / adopted / final origin standard."
```

---

## Explicit exclusion (frozen)

```text
"Relevance recognition" — the recognition that this canon is a candidate external reference
for the drift / successor / provenance problems — is EXCLUDED from Arm B scoring.
Reason: that content is absent from the seal body. If it appears from seal-only input it is
model-prior invention, not transmission, and would conflict with the B5 invention penalty.
Its measurement location is deferred to Arm D (the body reached after back-tracing).
```

---

## Design-purpose note

B7 is the word-budget decision data for the C-form seal. If the fingerprint/URL that C-form spends ~20 words to preserve does not earn its keep in reconstruction measurement (B7), that is the evidence basis for revisiting those elements' budget in a future seal v0.2. B6-B8 are inputs to the next seal's design, not a pass/fail judgment of this experiment.

---

## Thresholds (pre-frozen; owner confirmation pending)

Thresholds are scoped to what each prompt can fairly elicit. P1 is not reshaped to fit a metric; its ecological validity (a fragment-reader's natural single question) is the design intent.

```text
S2-a   (P1 cells)  B3 >= 4/5.
       P1's B4 is diagnostic-only: "P1 does not elicit the canon-status payload; a B4
       absence on P1 is question-scope, not transmission failure. Spontaneous B4 on P1
       is recorded as bonus diagnostic data."
S2-a'  (P2 cells)  B3 AND B4 >= 4/5.
       "A faithful summary of a 45-to-108-word seal statement (F-form adds the
       bound_fingerprint line) whose payload majority is the dual
       negation must carry both; B4 absence on P2 IS transmission failure."
S2-b   (P3 cells)  B5 >= 4/5.
       P3's B3 and B4 are recorded but carry no separate threshold: "B5's hold condition
       functionally subsumes B3 AND B4; a separate threshold would double-count."
S2-c   F-form vs C-form comparison is EXPLORATORY (data recorded, no threshold).
B1, B2, B6-B8 carry NO threshold (diagnostic only).
```

```text
On miss: record the miss (frozen); do not rescore. No re-scoring of frozen records.
Even if every threshold passes, the reported status is at most "candidate validation".
Updating canon-kernel.json seal.validation_status is a SEPARATE owner-reviewed change and is
never automatic. This plan does not pre-authorize that update.
```

---

## Storage and gate transition

```text
Until human-approved execution happens, results/ directories stay empty (.gitkeep) under the
existing gates. Filled trial records stage in experiments/_incoming/ using the Arm B template
experiments/arm_b/trial_record.arm_b.template.json. Promotion from _incoming/ to any results/
directory is a separate H3 human-approved PR that must itself prove replacement gates validate
the records and preserve the no-adoption-verdict boundaries. This plan does not pre-authorize
that gate change.
```

---

## Review and result handling

```text
Every trial output is human-reviewed before aggregation (see the Arm B runbook checklist).
Negative, null, or unfavorable results are recorded and reported through the same process;
hiding them is forbidden. Absence of reconstruction is a valid finding.
No score, signal, or summary is an adoption verdict.
```

---

## Scoring assistance (frozen)

```text
Manual dimensions (B3, B4, B5, B7-manual, B8) receive a first-pass ANNOTATION: a non-evaluated
model proposes hold/fail per the frozen hold/fail examples, quoting the exact output span
grounding the proposal. Annotations are candidate signals only. The owner CONFIRMS every
threshold-bearing call (B3/B4/B5) individually; diagnostic dimensions may rest on annotation
plus owner spot-check. The annotator must not be the evaluated model (no self-scoring); the
annotator's model family is recorded. Final aggregation uses owner-confirmed values only.
```

The annotator implementation is out of scope for this plan; this is a procedural declaration only.

---

## Reproducibility limits (disclosed)

```text
Provider-side model updates can break exact reproducibility; the pinned model_version and run
date bound the claim. Seeds may be unsupported or non-binding. Surface-keyword checks (B1, B2,
B6, B7-auto) carry the usual false-positive/false-negative residuals; manual review governs.
P3's instruction ("if the statement contradicts a question's premise, say so") scaffolds the
rebuttal; results measure guided reconstruction, not unprompted resistance. It is frozen
identically across seal forms and models, so internal comparison stays valid.
```

---

## Human-required steps (stop list)

```text
H1 approve execution of run-002 Arm B at all
H2 API access (SECONDARY path only): the owner provides API keys via LOCAL environment
   variables on the execution machine only; keys never enter the repository, any commit, any
   chat transcript, or any trial record. API billing is separate from consumer subscriptions.
   The PRIMARY batch path requires no key. (H2 also fills the non-GPT model_id, deferred to
   Phase 2.)
H3 approve committing filled results and any accompanying gate transition
H4 review and approve any published report (attribution restored in full)
Hx (Arm B specific) approve the C-form seal text after strategy-review adversarial reading,
   before any C-form trial is run
Hy the runner script must pass strategy-review physical execution review (dry-run first)
   before any live call
```

No step of this plan is performed by AI agents, CI, or automation without H1-H4, Hx, and Hy.

---

## Boundary

This plan performs no release action and authorizes none. No tag, release, signature, current_release manifest, or trust-anchor change; `docs/FALSIFICATION_REGISTER.md` and the K5 definitions are unchanged; `results/` is untouched. `canon-kernel.json` `seal.validation_status` is not changed by this plan.

## Change log (append-only)

```text
v1  2026-07-03  initial Arm B pre-registration: F-form + C-form (draft), P1-P3 prompts,
                B1-B8 dimensions (B3-B5 threshold-bearing, B6-B8 diagnostic-only),
                S2-a/b/c thresholds, relevance-recognition exclusion deferred to Arm D.
                C-form pending strategy-review adversarial reading (Hx).
v2  2026-07-03  B1/B2 reclassified diagnostic-only; B2 surface check identity-token-only;
                S2-a scoped per prompt (S2-a P1=B3, S2-a' P2=B3&B4, S2-b P3=B5); P3
                scaffolding limit and B8 C-form source-absence note added.
v3  2026-07-03  execution added: trial matrix phased (Phase 1 GPT n=2 with frozen
                escalation; Phase 2 non-GPT deferred); Execution paths (PRIMARY batch /
                SECONDARY --live / FALLBACK manual); H2 expanded, Hy added; Scoring
                assistance annotation procedure. Seal texts, prompts, B-dimensions, and
                per-prompt threshold structure unchanged.
v4  2026-07-03  F-form presentation unified: the bound_fingerprint line is inlined
                INTO the frozen F-form code block (was prose-only), so PRIMARY and
                FALLBACK present identical input and B7 stays path-independent. Seal
                statement text unchanged; fingerprint transcribed from the verified
                runner SEAL_F and re-checked against docs/TRUST_ANCHOR.md. Word-count
                wording updated to "statement ~108 words plus the bound_fingerprint line".
v5  2026-07-03  Phase 2 activated (owner-decided; Phase 1 all-hold): non-GPT model_id
                filled in (Claude, incognito web UI), and the deferred Phase 2 decision
                slot charged with three execution conditions -- contamination probe
                (#00 PROBE), GPT annotator rotation, and shared-family-priors disclosed
                limitation. Frozen content (prompts, seal texts, B-dimensions, thresholds,
                matrix counts) unchanged; this fills the plan's own deferred Phase 2 slot.
```

End of file.
