# v0.3.1 — Challenger Evidence and Submission Hardening

**status:** draft hardening package
**scope:** post-v0.3.0-rc.1 challenger evaluation workflow
**depends on:** `v0.3.0/17-challenger-evaluation-protocol.md`

This directory hardens the challenger path opened by the v0.3.0 release-candidate package.

The v0.3.0 package defines the current operational benchmark, cost rubric, profile separation, non-substitution protocol, current champion verdict, final audit, and challenger evaluation protocol.

The v0.3.1 package does not change that benchmark verdict.

It adds submission discipline around challenger claims:

1. what evidence a challenger must submit;
2. how scoring disagreement is classified;
3. how a challenger package should be formatted for review.

---

## Read order

Read v0.3.0 first:

1. `v0.3.0/V0_3_0_OPERATIONAL_CORE_SPEC.md`
2. `v0.3.0/12-cost-rubric.md`
3. `v0.3.0/13-profile-separation.md`
4. `v0.3.0/14-non-substitution-and-attribution-protocol.md`
5. `v0.3.0/15-current-champion-verdict.md`
6. `v0.3.0/16-final-audit.md`
7. `v0.3.0/17-challenger-evaluation-protocol.md`

Then read v0.3.1:

1. `18-challenger-evidence-standard.md`
2. `19-disagreement-handling.md`
3. `20-challenger-submission-template.md`

---

## File roles

### `18-challenger-evidence-standard.md`

Defines the minimum evidence required for each challenger audit gate.

A challenger must submit evidence, not just assertions.

### `19-disagreement-handling.md`

Defines how scoring disagreement is represented without collapsing into arbitrary winner claims.

It introduces outcome states such as `accepted`, `rejected`, `contested`, and `insufficient_trace`.

### `20-challenger-submission-template.md`

Provides a structured template for challenger submissions.

It is designed for issue, PR, external report, or automated evaluator use.

---

## Boundary

v0.3.1 is hardening, not a new benchmark core.

It does not:

- create v0.4.0;
- create a final v0.3.0 release;
- change validator behavior;
- change cost-rubric logic;
- change profile separation logic;
- change non-substitution logic;
- run live model evaluation;
- modify AAOS Genesis Core.

It only makes challenger claims more reviewable.
