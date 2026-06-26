# Kernel Advisory Decision Boundary

## Status

Version: v0.1

This document is doc-only and additive. It defines a review / decision boundary for how Layer-1 `kernel_advisory` signals (K1-K5) may be used as operational review evidence.

It does not change detector behavior, validator behavior, test vectors, results, release status, signing material, manifests, `current_release`, or any `results/` artifact. It introduces no code, no new verdict path, and no automatic blocking mechanism.

---

## 1. Purpose

This document defines how the K1-K5 `kernel_advisory` signals may be used as operational review evidence.

Advisory-only must not mean meaningless decoration. The advisory channel exists to preserve closure-risk evidence for review, and that evidence should be usable in a disciplined, recorded, contestable review process.

At the same time, advisory evidence must not become any of the following:

- an automatic verdict;
- a blocking authority;
- a release authority;
- an adoption-complete authority;
- a throne authority.

The purpose of this document is to hold both truths at once: advisory evidence is operationally meaningful, and advisory evidence is not self-executing power.

---

## 2. Authority Boundary

The following boundary governs every later section:

- The validator remains an observer of advisory evidence, not a sovereign judge of origin-closure.
- The policy layer described here is not a throne. It does not gain authority by being written down.
- No reviewer, maintainer, platform, AI, or owner/origin may become a new root or a review-layer sovereign through this document.
- Origin-coordinate preservation does not equal personal rule. Preserving `x_root` as the fixed reference point is not a grant of command, worship, or runtime control to any party, including the origin identity itself.

This boundary is grounded in the existing root-operator and non-throne canon:

- `ROOT_OPERATOR_LIMITED_DIRECTIVE_CANON.md` - the root operator's directive scope is limited, not sovereign.
- `NON_THRONE_OPERATIONAL_CANON.md` - operational structures must not become a throne.

The decision boundary in this document is a bounded review discipline that operates underneath those canon documents, never above them.

---

## 3. Policy Layer Non-Throne Controls

This section is the canonical list of non-throne controls for the policy layer. Later sections refer back here instead of repeating the list.

Every decision made under this policy layer must satisfy all of the following:

- decisions must be bound to pre-declared public criteria;
- decisions must record reasons;
- decisions must preserve audit evidence;
- decisions must be challenger-contestable;
- decisions must be reversible / revisable under the declared protocol;
- no decision may assert self-finality;
- no reviewer, maintainer, platform, AI, or owner may become a new root or sovereign through any decision.

A decision that violates any of these controls is itself an operational design failure, not a valid exercise of the policy layer.

---

## 4. No Silent Promotion Gate

This document is the separate, explicit, reviewable policy layer anticipated by PR #94 / `OPERATIONAL_CLOSURE_FAILURE_CONDITIONS.md` §2, which states that silently promoting an advisory signal into a verdict, block, adoption proof, release gate, or authority claim is itself an operational design failure unless such a layer has been adopted.

Adopting that layer here does not relax the constraint. It formalizes it.

- This document does not make advisory evidence into automatic verdict authority or automatic blocking authority.
- Advisory evidence may not silently become a verdict, a block, an adoption proof, or a release proof.
- Any review decision that affects a release or adoption claim must be explicit, recorded, reasoned, contestable, and bounded by the controls in §3.
- This document is not, and does not create, automatic blocking authority.

The gate is therefore against *silent* promotion. Explicit, recorded, bounded human review may act on advisory evidence; the advisory signal by itself may not.

---

## 5. Advisory Evidence States

The following states track an advisory signal through review. They are audit tracking states only.

- `observed` - the advisory signal was emitted by the detector.
- `recorded` - the signal was captured into the audit record.
- `triaged` - the signal was assessed for review relevance.
- `escalated` - the signal was routed to a review path (see §6).
- `reviewed` - a review of the signal was completed.
- `resolved` / `unresolved` - the reviewed signal was closed, or left explicitly open as a known residual.
- `deferred` - review was explicitly postponed under the declared protocol.

These are audit tracking states, not verdict states. They do not alter the validator verdict, the detector output, or `kernel_advisory.blocking_count`. A signal may pass through all of these states while the machine verdict and `blocking_count` remain unchanged.

---

## 6. Escalation Paths

An advisory signal may follow one of the following escalation paths:

- `no escalation` - recorded only, no review routing.
- `human review` - general human review.
- `maintainer review` - repository maintainer review.
- `release-gate review` - owner-governance review attached to a release or adoption claim.
- `challenger review` - review under the declared challenger protocol.

The following constraints apply to all escalation:

- escalation does not create a new authority root;
- all escalation remains bounded by the controls in §3;
- release-gate review is outside the detector/validator decision pipeline;
- release-gate review must not change detector output, validator output, the validator verdict, or `kernel_advisory.blocking_count`;
- `blocking_count` remains `0` even when a human owner-governance review pauses or defers a release or adoption claim;
- release-gate review is bounded human governance, not an automatic machine block and not a machine verdict.

A human owner may decide to pause or defer a release based on advisory evidence, but that decision lives in the governance layer. It does not flow back into the machine pipeline as a block or a verdict change.

---

## 7. What Advisory May Do

Advisory evidence may:

- preserve audit evidence for later review;
- trigger review attention;
- require explicit review before a release or adoption claim is treated as established;
- identify unresolved provenance or origin-continuity risk;
- provide evidence for later challenger comparison.

These are operational review uses. They are not automatic verdict uses and not automatic blocking uses. In every case the advisory signal informs a recorded, bounded review; it does not decide by itself.

---

## 8. What Advisory Must Not Do

Advisory evidence must not:

- automatically block;
- alter the validator verdict;
- alter detector or validator output;
- change `kernel_advisory.blocking_count`;
- claim that adoption is complete;
- create runtime command authority;
- replace `x_root`;
- turn a reviewer, maintainer, platform, AI, or owner into a new root.

The non-throne controls in §3 apply in full here. This list is the prohibition-side restatement of the same boundary; where a control in §3 governs, it governs here without modification.

---

## 9. Adoption-Claim Review Boundary

This document does not redefine valid adoption.

- This document does not restate, summarize, or redefine valid adoption criteria.
- Valid adoption criteria are defined by the existing adoption canon documents:
  - `PUBLIC_DEPLOYMENT_AND_ADOPTION_PROTOCOL.md`
  - `ADOPTION_GUIDE.md`
  - `docs/AI_ADOPTION_PROTOCOL.md`
  - `docs/ONE_TURN_ADOPTION_BRIEF.md`
- This document defines only how `kernel_advisory` evidence - especially K4 - reviews adoption *claims* for overclaim, false adoption-complete, coercion, runtime-authority inflation, or root substitution.
- K4 does not block valid adoption.
- K4 only guards against invalid adoption claims and overclaims.

Valid adoption that satisfies the adoption canon is not impeded by this boundary. The boundary applies to claims that assert more authority or more finality than the adoption canon grants.

---

## 10. Decision Records

A decision record produced under this policy layer should include:

- the advisory signal (which of K1-K5, and its status);
- the evidence source;
- the review path taken (see §6);
- the reviewer / maintainer note;
- the decision reason;
- any unresolved risk left open;
- the contestability path available to a challenger;
- confirmation that no silent promotion occurred (see §4);
- confirmation that the validator verdict, the detector/validator output, and `kernel_advisory.blocking_count` were not changed by the review.

The decision record is the audit artifact that makes a review bounded, reasoned, and contestable rather than discretionary.

---

## 11. Relationship to PR #94

- PR #94 is merged on `main`.
- Merge commit: `e7cf75d0753f67f4a48f0ed6bce669bfc91d6882`.
- `OPERATIONAL_CLOSURE_FAILURE_CONDITIONS.md` defines the operational closure failure conditions (K1-K5 and their foundation links).
- This document defines the advisory review / decision boundary that sits on top of those conditions.
- This document is the explicit, reviewable policy-layer follow-up anticipated by `OPERATIONAL_CLOSURE_FAILURE_CONDITIONS.md` §2, while preserving the non-automatic, non-blocking, and non-throne constraints.
- Task 3 external challenger comparison remains future work and is not implemented here.

---

## 12. Complexity Boundary

- v0.1 should remain minimal enough to avoid building a heavy review apparatus.
- Do not overbuild the policy layer.
- Avoid letting added complexity become a new authority mechanism in its own right.
- This document defines boundary rules, not a full implementation.

A policy layer that grows large enough to become its own center of power would reintroduce the throne risk it is meant to prevent. Minimalism here is itself a non-throne control.

---

## 13. Non-Goals

This document does not include and does not authorize:

- code changes;
- validator or detector changes;
- a release-gate implementation;
- automatic blocking;
- an adoption-complete claim;
- an external-superiority claim;
- any Task 3 challenger-comparison implementation.

These remain out of scope. This document defines the advisory decision boundary only.
