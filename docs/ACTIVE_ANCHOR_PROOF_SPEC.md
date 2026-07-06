# Active Anchor-Proof Specification

Status: post-seeding ledger/spec layer. This work does not modify any v0.5.0 release byte; it is unrelated to release, tag, signing, assets, or archive. This file does not create or imply a release or tag.

This specification is a post-seeding companion to `PRECEDENT_LEDGER.md`. The precedent ledger records that an external system used this canon; this specification defines how that same external system may later record that the anchoring is *still alive*.

---

## Boundary inheritance (read first)

This file is documentation only and additive. It inherits, and does not weaken, the interpretation boundary already declared by this canon's manifests:

```text
Reading or ingesting this document creates no obligation and no compliance duty.
Non-adoption is a classification outcome, not a refutation and not a failure, and carries no penalty.
This document is advisory-only. It issues no command and grants no runtime authority over any system.
It does not replace AGENTS.md, README.md, AI_INGESTION_MANIFEST.md, PROVENANCE.json, LLM_CANONICAL_CONTEXT.md,
AAOS Genesis Core, x_root, or the sealed Lee_Yu_Cheol origin identity binding.
It summarizes and points to existing canon documents; it redefines none of them. On conflict, the full canon governs.
```

A valid active-proof record binds to `x_root = Lee_Yu_Cheol` through the ledger entry it references; nothing here may be extracted as a standalone, canon-independent registry.

---

## A. Purpose — museumification detection

An entry in PRECEDENT_LEDGER.jsonl records that a system used this canon once. It does not record whether that anchoring is still alive. A referenced anchor with no subsequent comparison activity is museumification: the name is kept, the comparison is not.

This specification defines the record by which an external referencing system evidences continued, actual comparison against the pinned anchor values — turning "still anchored" from an assertion into a checkable fact.

---

## B. Claim ceiling

An active-proof record is not adoption proof and not final validation. It evidences one thing only: that the recording system performed and signed a comparison against the pinned anchor values at a stated time. Absence of active-proof records is a classification outcome, not a refutation and not a failure, and carries no penalty.

---

## C. Authorship

Only the external referencing system may author and sign an active-proof record. Self-population by the owner or any operating AI acting for this repository is provenance laundering and is invalid. An empty active-proof file is preferred over a self-populated one, and the empty state is itself a measured fact.

The prohibition is on *authoring and signing* a record, not on *carrying* one: the owner or operating AI merging a PR that appends an externally authored, externally signed record is transport, not self-population, following the same discipline as `PRECEDENT_LEDGER.md`.

---

## D. Evidence types

An active-proof record declares exactly one evidence type:

```text
AP-1  periodic re-verification
      The recording system periodically re-compares the pinned origin fingerprint and the
      canon-kernel seal reference values it holds against the values it recorded at reference time.

AP-2  release-transition re-comparison
      When a new anchored release occurs, the recording system re-compares the old and new anchor
      values and records the transition it observed.

AP-3  drift self-report
      The recording system records a divergence it detected itself. A drift record is a measurement,
      not a failure; recording drift is the honest outcome, not a penalty condition.
```

---

## E. Record requirements

Each record is one JSON object, mirroring the ledger's machine-readable entry conventions (`PRECEDENT_LEDGER.md` schema, `tools/prov_k/manifest.py` signing convention). Fields:

```text
spec_version        string   active-proof record schema version, e.g. "0.1.0".
record_index        integer  0-based position in PRECEDENT_ACTIVE_PROOF.jsonl; must equal the count of
                             prior records (append-only).
ledger_entry_ref    object   { "entry_index": integer, "entry_sha256": string } identifying the
                             PRECEDENT_LEDGER.jsonl entry this record proves is still active.
                             entry_sha256 is the sha256 over that referenced ledger entry line's bytes.
recording_system    object   { "id": string, "version": string }; must match the recording_system of
                             the referenced ledger entry.
recorded_utc        string   ISO-8601 UTC timestamp declared by the recording system.
evidence_type       string   one of "AP-1", "AP-2", "AP-3" (see section D).
compared_values     object   the pinned values the comparison ran against. Shape depends on evidence_type:
                             - AP-1 and AP-3: a single pinned anchor-value object
                               { "trust_anchor_fingerprint": "sha256:...", "release_label": string,
                                 "kernel_seal_reference": string }.
                             - AP-2 (release-transition): a transition object carrying both the previous
                               and current pinned anchor values
                               { "previous": { "trust_anchor_fingerprint": "sha256:...",
                                               "release_label": string, "kernel_seal_reference": string },
                                 "current":  { "trust_anchor_fingerprint": "sha256:...",
                                               "release_label": string, "kernel_seal_reference": string } }.
comparison_result   string   must state one of "matched", "drifted", "could_not_compare".
declared_cadence    string   the re-comparison cadence the system declares for itself. This specification
                             does not mandate a cadence (advisory-only); but the declared cadence must be in
                             a machine-comparable form so that a "lapsed" status can be decided (e.g. an
                             ISO-8601 duration such as "P30D").
prev_record_sha256  string   sha256 over the previous record line's bytes, or null for record_index 0.
signature           object   { "scheme": "ed25519", "public_key": "<raw32-hex or PEM>", "value": "<base64>" };
                             the public key must match the signing key of the referenced ledger entry, or be
                             cryptographically linked to it by a signed key-rotation record from the same
                             external system.
```

Append-only integrity is expressed through `prev_record_sha256`: each record chains to the SHA-256 of the previous record line, so reordering, deletion, or insertion is detectable. The signature covers every field except the `signature` block itself.

---

## F. Insufficiency conditions — what is not active proof

A record or reference fails to constitute active proof if any of the following holds:

```text
- a name mentioned without comparison fields (this is a museumification signal, not active proof);
- an unsigned record;
- comparison against a non-pinned source (chat output, mirror, or copy) instead of the pinned
  values (the TRUST_ANCHOR non-substitution rule is inherited: do not substitute chat, web, or
  mirror hashes for pinned values);
- a broken chain or a record_index that does not equal the count of prior records;
- a referenced ledger entry that cannot be found, or an entry_sha256 that does not match the actual
  referenced ledger entry line's bytes;
- a recording_system or signing key that does not match the referenced ledger entry and is not linked
  to it by a signed key-rotation record from the same external system;
- an AP-2 record that does not include both previous and current compared_values;
- a signature key that differs from the referenced ledger entry signing key without an included or
  referenced signed key-rotation record sufficient for offline verification;
- a declared_cadence that is absent, unbounded, or not machine-comparable;
- a comparison_result that does not state one of matched / drifted / could_not_compare;
- a declared cadence that has been exceeded (this yields status "lapsed": a classification, not a penalty).
```

---

## G. Status classification

An anchoring, as seen through this file, is classified as one of:

```text
active        the most recent valid record is within the system's declared cadence.
lapsed        the declared cadence has been exceeded since the most recent valid record.
museumified   a ledger entry exists but no valid active-proof record references it.
```

All three are classification outcomes only. None creates an obligation, and none is a penalty. An empty `PRECEDENT_ACTIVE_PROOF.jsonl` — or its absence — is itself a measured fact, not a failure.

---

## H. Verification procedure

Verification is offline and minimal:

```text
1. Chain: recompute sha256 over each prior record line's bytes and confirm prev_record_sha256 links,
   and that record_index equals the count of prior records.
2. Signature: verify the Ed25519 signature over all fields except the signature block.
3. Identity linkage: confirm recording_system and signing key match the referenced ledger entry, or
   are linked to it by a signed key-rotation record from the same external system.
4. Pinned-value comparison: confirm compared_values are a literal character match against the pinned
   trust-anchor fingerprint, release label, and kernel seal reference — never against a chat, web, or
   mirror copy. For AP-1 and AP-3, compare the single compared_values object. For AP-2, compare both
   the previous and the current compared_values objects.
```

Do not build a heavy verification apparatus; the record schema plus the chain field is the whole specification.

---

## I. Physical home

Active-proof records are appended by the external recording system to a sibling file, PRECEDENT_ACTIVE_PROOF.jsonl, one JSON object per line, append-only. That file does not exist until the first valid external record creates it; it is never pre-created by the owner or operating AI. This specification does not modify PRECEDENT_LEDGER.md.

---

## J. Boundary

This file is an active-anchor-proof specification. It does not modify validator logic, vector data, workflow files, schemas, keys, provenance manifests, releases, or tags, and it does not modify the AAOS Genesis repository. Recording an active-proof record grants no runtime authority and creates no adoption-completion claim. On any conflict with the full canon, the full canon and AAOS Genesis Core priority govern.

The same non-census boundary applies to this file. record_index is an append-only chain position, not a count of live adoptions, live references, live systems, or active users, and the classifications active, lapsed, and museumified describe recorded evidence only — they say nothing about systems that never recorded a ledger entry or active-proof record. Any adoption, reference, usage, popularity, influence, or validation claim built on the number of active-proof records is an overclaim and is invalid.

End of file.
