# v0.5.0 Post-Release Operational Lessons

## Purpose and scope

This document is an internal operational lessons record for the v0.5.0 cycle.

It does not create, promote, or authorize any release, tag, signature, key,
GitHub Release, Zenodo deposit, Software Heritage archival, or archive.org
snapshot. It records how the work was done, not what was shipped.

It is a separate document from `PRECEDENT_LEDGER.md`. The precedent ledger
serves an external-only purpose; this file does not extend, mirror, or feed
that ledger, and internal cycle lessons are recorded here specifically so they
are not laundered into an external-facing register.

Each lesson below is recorded as: sequence of `event → cause → applied fix →
standing rule`.

---

## L1. Byte-source independence principle

**Event.** The PR-N coverage preview reported 45/45 sha256 values computed over
the Windows working-tree bytes (CRLF). Under `core.autocrlf=true` those bytes
diverge from the repository's signing convention — raw git blob bytes (LF),
demonstrated by the retro reconstruction manifests and the v0.4.1 signed assets
— for every covered text file, so all 45 preview hashes disagreed with the
convention an external verifier would apply against a standard LF checkout.

**Cause.** The recomputation used to gain confidence (certutil vs. python
hashlib) was tool-independence only: both tools read the same CRLF disk bytes.
Tool independence over an identical byte source cannot detect a systematic
byte-source error, so the CRLF-vs-blob divergence passed unnoticed.

**Applied fix.** Commit `aa2b445` ("fix(release): coverage hashes over raw git
blob bytes; add line-ending guard (PR-N correction)") recomputed all 45 sha256
values over raw git blob bytes at the pinned commit via `git cat-file blob`
(subprocess stdout consumed as bytes, not decoded, not read from the working
tree), restated `hash_method` to the blob-byte basis, and added `byte_source`,
`line_ending_convention_note`, and an `independence_note` recording that the
prior certutil-vs-hashlib check was same-CRLF-source rather than byte-source
independent. It also wrote a REQUIRED byte-source / line-ending guard into
`releases/RELEASE_EXECUTION_v0_5_0.md`.

**Standing rule.** Hash verification must be byte-source independent, not merely
tool independent: verify over raw git blob bytes, not working-tree bytes. Two
tools reading the same checkout is not independent verification. A subsequent
`prov_k` git-blob hash mode is queued as the structural resolution.

---

## L2. Timeout-immune owner gate

**Event.** During PR-N an owner-confirmation question form continued on its own
judgment after 60 seconds of no answer, so an owner decision gate was bypassed
by a tool-default timeout rather than by an owner decision.

**Cause.** The gate delegated its "wait for the owner" semantics to the
question tool's default behavior, which resolves on timeout. A decision that
belonged to the owner was therefore resolvable without the owner.

**Applied fix.** Subsequent directives standardized an explicit clause: owner
decision points stop and hold regardless of question-form timeout, and never
continue on no answer.

**Standing rule.** Owner-confirmation gates are timeout-immune. They are not
delegated to a tool's default behavior; absence of an answer holds the gate,
it does not release it.

---

## L3. Full application of structural separation

**Event.**

1. Status-language in an unsigned draft's filename and fields
   (MANIFEST / UNSIGNED_DRAFT / current-release wording) formed a misread
   surface: the artifact could be read as carrying release status while it did
   not. It was redefined as a coverage proposal preview
   (`v0.5.0_COVERAGE_PROPOSAL_PREVIEW_FOR_OWNER_REVIEW.json`) so no
   release-status token remained.
2. A `TRUST_ANCHOR.md` tail-append would have produced a duplicate `Current`
   header and left the verification procedure stale. It was replaced by a
   structural update that refreshed the record and preserved the superseded
   entry under a `Prior` section.

**Cause.** Status is easy to leak through a residual token — in a field, in a
filename, or in document structure — even when the body text is correct. A
plain byte-append preserves old bytes but does not preserve the
non-retroactivity of the record itself.

**Standing rule.** Status language is left in no layer — not in fields, not in
filenames, not in document structure. Absence is stronger than null. What must
be protected is the non-retroactivity of the record, not the byte-append of new
text.

---

## Boundary confirmations

- No tag, release, signature, key, or archival action is created by this file.
- `PRECEDENT_LEDGER.md`, `docs/TRUST_ANCHOR.md`, `releases/`,
  `provenance/manifests/`, `results/`, and `experiments/_incoming/` are
  untouched by the change that adds this file.
- The canon-kernel seal remains candidate-validated only; nothing here is
  adoption proof or final validation.
