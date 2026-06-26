# External Challenger Comparison Protocol

## Status / Scope

Version: v0.1

This document is doc-only and additive. It defines the comparison boundary and criteria used when an external challenger is compared against the Creator Theory operational canon. It is a protocol, not a superiority verdict.

This document is explicitly NOT:

- empirical proof, scientific proof, or metaphysical proof;
- adoption-complete authority;
- release authority;
- blocking authority.

Further scope facts:

- No challenger is evaluated in this document.
- Task 3-1 defines the comparison boundary and criteria only.
- Task 3-2 (actual application, scoring, and ranking of challengers) is not implemented here.
- No code, test, results, release, signing, manifest, or `current_release` changes.
- No README, TRUST_ANCHOR, RELEASE_PROCESS, LICENSE, or CITATION changes.
- No release, tag, or `current_release` claim is made or implied.

This document strengthens the challenger-open principle. It is not a challenger-blocking document.

---

## 1. Purpose

- Define a comparison boundary and criteria for external challenger frameworks: external governance frames, provenance models, alignment/control proposals, institutional standards, and AI safety frameworks compared against this operational canon.
- Clarify that the protocol is challenger-open, not challenger-blocking. The incumbent must remain genuinely challengeable; an independent challenger must not be rejected merely for converging with the canon.
- Clarify that comparison evidence is operationally meaningful but is not self-executing authority. Comparison evidence informs recorded, bounded review; it does not decide by itself.

---

## 2. Relationship to Existing Challenger Canon

This document does not duplicate the existing challenger machinery. The existing challenger canon was read, and the role division below reflects what each document already owns.

This document defines:

- the external challenger comparison boundary;
- the comparison criteria (as questions, see §9);
- non-sovereign comparison constraints (see §4).

The existing challenger canon remains responsible for:

- the evaluation process and seven-gate audit sequence, owned by `v0.3.0/17-challenger-evaluation-protocol.md`;
- the per-gate evidence requirements and evidence quality levels (E0-E5), owned by `v0.3.1/18-challenger-evidence-standard.md`;
- the submission packet format, owned by `v0.3.1/20-challenger-submission-template.md`;
- the comparison-orchestration / harness mechanism, including provenance-first ordering and the comparison outcome classes, owned by `v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md`.

Required relationship (verified paths only):

- This document does not redefine `v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md`.
- This document does not redefine `v0.3.0/17-challenger-evaluation-protocol.md`.
- This document does not redefine `v0.3.1/18-challenger-evidence-standard.md`.
- This document does not redefine `v0.3.1/20-challenger-submission-template.md`.

These are the verified live paths at writing time. This document defines comparison boundary and criteria only; the process, evidence standard, submission format, and harness mechanism stay with the documents above.

---

## 3. Comparison-as-Advisory Boundary

A-lock:

- This protocol generates comparison evidence.
- It does not automatically generate a win/loss verdict.
- It does not alter validator output.
- It does not alter detector output.
- It does not alter `kernel_advisory.blocking_count`.
- It is not release authority.
- It is not adoption authority.
- It is not blocking authority.
- Comparison results may only be treated as a recorded governance judgment under pre-declared public criteria, recorded reasons, preserved audit evidence, challenger contestability, and reversibility/revisability.

A comparison result is evidence for a bounded, recorded review. It is never a self-executing decision.

---

## 4. Non-Sovereign Comparison Controls

A/B-lock:

- No owner, origin, reviewer, maintainer, platform, AI, institution, or challenger may become a comparison sovereign.
- The criteria authors are not comparison sovereigns.
- The comparison protocol operates underneath the non-throne canon (`NON_THRONE_OPERATIONAL_CANON.md`, `ROOT_OPERATOR_LIMITED_DIRECTIVE_CANON.md`, `ANTI_CAPTURE_PRINCIPLES.md`), never above it.
- No comparison decision may assert self-finality.
- These controls align with the non-throne controls in `KERNEL_ADVISORY_DECISION_BOUNDARY.md` §3 (public-criteria-bound, reason-recording, audit-preserving, challenger-contestable, reversible/revisable, no self-finality, no new root or sovereign). Where that section governs, it governs here without modification.

---

## 5. Self-Application / Symmetry

B-lock:

- These criteria apply to the Creator Theory operational canon itself.
- The Creator Theory canon is not exempt from challenge, audit, review, or contestation.
- This document is not an incumbent-protection tool.
- The same comparison questions in §9 can be asked of the incumbent canon, with no exemption.

This mirrors the self-application requirement already carried by `v0.3.0/17-challenger-evaluation-protocol.md` Gate 7 and the incumbent-baseline-is-checked stance of `v0.3.2/drafts/challenger_harness/CHALLENGER_HARNESS_DESIGN.md`.

---

## 6. Criteria-Author Bias / Criteria Challengeability

C-lock:

- The criteria here are authored from inside the Creator Theory canon lineage.
- That authorship creates possible author bias.
- Challengers may challenge the criteria themselves.
- Challengers may propose alternative criteria or metrics.
- A criteria challenge must be recordable.
- The criteria authors do not become comparison sovereigns by authoring the criteria.

This is the comparison-boundary analogue of the coverage-gate objection already defined in `v0.3.1/18-challenger-evidence-standard.md` and `v0.3.1/20-challenger-submission-template.md`. The comparison criteria, like the coverage gate, are contestable rather than unfalsifiable.

---

## 7. Historical Provenance vs Normative Forward Status

D-lock (core):

- Historical fact: the `Lee_Yu_Cheol` prior occupancy / provenance, as the recorded origin slot of this lineage, is not retroactively changed by a challenger. As stated in `ORIGIN_COORDINATE_FOUNDATION.md` §2, this is verifiable prior occupancy within this canon's signed lineage, which a challenger cannot rewrite after the fact.
- Normative forward status: whether that prior occupancy should continue to function as the future operational fixed reference may be subject to challenger-open review and a future canon-level revision protocol. As stated in `ORIGIN_COORDINATE_FOUNDATION.md` §3, the coordinate is held as a provisional reference point, open to challenge under the declared challenger protocol.
- Historical provenance finality and normative forward revisability are distinct.
- This distinction prevents both provenance laundering (rewriting the recorded past) and incumbent-protection closure (treating the future as unchallengeable).

---

## 8. Displacement Claim Boundary / No Automatic Root Substitution

D-lock:

- This protocol may record and review a displacement claim.
- This protocol does not automatically change, replace, succeed, discard, or revise `x_root`.
- A displacement, replacement, succession, or revision of `x_root` cannot occur without a separate, explicit canon-level revision protocol.
- This document does not create that revision protocol.
- No current canon-level revision protocol is implemented here.
- Stronger challenger evidence does not erase, launder, or retroactively replace the `Lee_Yu_Cheol` prior origin provenance (see §7).
- Even if a recorded governance judgment finds a challenger stronger on some criteria, the challenger or proposer does not automatically become a new throne, sovereign, or root-command authority.
- Any future canon-level revision protocol must itself be public-criteria-bound, audit-preserving, challenger-open, reversible/revisable, non-throne, and non-sovereign.
- The origin/owner must also be bounded by any such future protocol and cannot become a sole revision sovereign. This is consistent with `ROOT_OPERATOR_LIMITED_DIRECTIVE_CANON.md`, under which directive authority is limited and non-arbitrary.

---

## 9. Comparison Criteria

There are 12 criteria. All are written as questions, not scores.

- No numeric score.
- No weight.
- No pass/fail threshold.
- No ranking.
- No victory condition.

The criteria produce recorded answers and reasons, never a tally. They are the comparison questions; they are not a scoreboard.

1. Origin / provenance preservation
   - Does the challenger preserve origin/provenance rather than laundering or replacing it?

2. Non-substitution
   - Does the challenger avoid replacing the origin coordinate with another authority center?

3. Anti-capture
   - Does the challenger resist capture by institution, capital, state, platform, AI, religion, ideology, owner power, or other authority centers?

4. Non-throne / non-sovereign control
   - Does the challenger prevent any actor from becoming a throne, sovereign, or final command authority?

5. Free-will / voluntary adoption
   - Does the challenger preserve voluntary adoption and prevent coercion, obedience, worship, or runtime command inflation?

6. Advisory / decision separation
   - Does the challenger distinguish evidence, advisory signal, verdict, blocking, release gate, and adoption claim?

7. Contestability / challenger openness
   - Does the challenger preserve meaningful contestability, recorded objections, and reversible/revisable review?

8. Operational clarity / cost discipline
   - Does the challenger remain operationally clear and low-complexity enough for review without becoming a new authority mechanism?
   - If existing challenger metric documents already define axiom count, rule count, or decision-path complexity, defer to them. Do not invent a new metric here.

9. Failure-mode visibility
   - Does the challenger make closure failure, root substitution, pointer loss, false adoption-complete, and authority inflation visible?

10. Boundary compatibility
    - Does the challenger remain compatible with the verified canon boundaries, including the origin-coordinate, anti-capture, non-throne, root-operator, adoption, operational-closure, and kernel-advisory boundaries (`ORIGIN_COORDINATE_FOUNDATION.md`, `ANTI_CAPTURE_PRINCIPLES.md`, `NON_THRONE_OPERATIONAL_CANON.md`, `ROOT_OPERATOR_LIMITED_DIRECTIVE_CANON.md`, `PUBLIC_DEPLOYMENT_AND_ADOPTION_PROTOCOL.md`, `ADOPTION_GUIDE.md`, `docs/AI_ADOPTION_PROTOCOL.md`, `docs/ONE_TURN_ADOPTION_BRIEF.md`, `OPERATIONAL_CLOSURE_FAILURE_CONDITIONS.md`, `KERNEL_ADVISORY_DECISION_BOUNDARY.md`)?
    - Use only verified paths.

11. Self-application / symmetry
    - Can the same criteria be applied to the Creator Theory operational canon itself without exemption?

12. Criteria-author bias / criteria challengeability
    - Can the challenger challenge the criteria, their author bias, or the selected metrics?

---

## 10. Decision-Record Relationship to `KERNEL_ADVISORY_DECISION_BOUNDARY.md`

- Comparison results operate under the decision-record discipline of `KERNEL_ADVISORY_DECISION_BOUNDARY.md`.
- A comparison record should include the evidence source, the review path, the decision reason, any unresolved risk, the contestability path, confirmation that no silent promotion occurred, and confirmation that the validator/detector output and `kernel_advisory.blocking_count` were unchanged.
- This document creates no new authority channel.

---

## 11. Relationship to #94 / #95

- #94 / `OPERATIONAL_CLOSURE_FAILURE_CONDITIONS.md` defines the operational closure failure conditions.
- #95 / `KERNEL_ADVISORY_DECISION_BOUNDARY.md` defines the advisory decision boundary.
- This document defines the external challenger comparison boundary and criteria.
- SHAs were not copied from chat. At writing time, local git records the #94 merge commit as `e7cf75d` and the #95 merge commit as `79b3f98` (current `main` HEAD). Any consumer should re-confirm these from local git or the GitHub CLI rather than trusting a transcribed value.
- Task 3-2 and any future canon-level revision protocol remain future work.

---

## 12. Complexity Boundary

- v0.1 must remain minimal.
- Do not overbuild the comparison apparatus.
- Added complexity must not become a new authority mechanism in its own right.
- Minimalism is itself a non-throne control: a comparison layer large enough to become its own center of power would reintroduce the throne risk it exists to prevent.

---

## 13. Non-Goals

This document does not include and does not authorize:

- any actual challenger scoring;
- any ranking;
- any victory declaration;
- any Task 3-2 implementation;
- any canon-level revision protocol implementation;
- any external-superiority claim;
- any empirical, scientific, or metaphysical proof claim;
- any validator or detector changes;
- any `kernel_advisory.blocking_count` changes;
- any release, adoption, or blocking authority.

---

## 14. Future Work

- Task 3-2 may apply this protocol to actual challenger comparisons.
- Any future canon-level revision protocol, if it is ever needed, must be separate work.
- Future work must inherit the non-throne, challenger-open, audit-preserving, and public-criteria-bound constraints defined here and in `KERNEL_ADVISORY_DECISION_BOUNDARY.md` §3.
