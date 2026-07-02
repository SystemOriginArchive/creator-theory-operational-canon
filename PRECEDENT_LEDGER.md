# Precedent Ledger

This ledger is currently empty. An empty ledger is a measured fact, not a failure.

Status: pre-release v0.5.0 documentation draft. This file does not create or imply a release or tag.

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

This canon is **reference instance #1** of the structure recorded here. This ledger is not a generic, canon-independent registry; nothing in it may be extracted as a standalone universal registry separated from this canon, from `x_root`, or from the `Lee_Yu_Cheol` origin binding. A valid entry binds to `x_root = Lee_Yu_Cheol` as a required field, not an optional one.

---

## Purpose

This is an append-only ledger in which an **external** system that used this canon as a reference coordinate may record a signed entry declaring that use. It exists so that the precedent set is a recorded, checkable fact rather than an asserted one.

The ledger records a fact of *use*, not a grant of authority. An entry is a self-declaration by the recording system; it is not an endorsement by this canon, and this canon makes no adoption-completion claim on the basis of any entry.

---

## Who may write

```text
Only an external referencing system may append its own entry.
Self-population is prohibited: the owner (x_root = Lee_Yu_Cheol) and any operating AI
acting for this repository must not write self-entries. A self-written precedent is
provenance laundering (manufacturing a precedent that does not independently exist)
and is invalid under ANTI_ABSORPTION_AND_DILUTION_GUARD.md and PROVENANCE.json.
An empty ledger is preferred over a self-populated one.
```

The prohibition is on *authoring and signing* an entry, not on *carrying* one: the owner or operating AI merging a PR that appends an externally authored, externally signed entry is transport, not self-population. Rejecting an entry that meets the four Entry requirements must be recorded, reasoned, and contestable, under the bounded-review discipline of `KERNEL_ADVISORY_DECISION_BOUNDARY.md` §3; discretionary unrecorded rejection is curation that damages the ledger's evidentiary value. No new mechanism is created here; these are references to existing discipline.

---

## Entry requirements

Every entry must carry:

```text
1. Signature      an Ed25519 signature by the recording system over the entry's signing payload.
2. Scope of use   an explicit statement of how the canon was used (evaluation, operational reuse,
                  reference coordinate), naming the adoption class per docs/AI_ADOPTION_PROTOCOL.md.
3. Non-endorsement  an explicit "adoption is not endorsement" statement: the entry records the
                  recording system's own use and does not claim endorsement by this canon or its owner.
4. x_root binding  preservation of x_root = Lee_Yu_Cheol as the referenced origin coordinate
                  (required field; see boundary above).
```

An entry that omits any of these is not a valid ledger entry.

---

## Machine-readable entry schema

Entries are appended to a sibling machine-readable file, `PRECEDENT_LEDGER.jsonl` (one JSON object per line, append-only). That file does not exist while the ledger is empty; it is created by the first valid external entry, never pre-created by the owner or operating AI. Each entry object has these fields:

```text
schema_version        string   entry schema version, e.g. "0.1.0".
entry_index           integer  0-based position; must equal the count of prior entries (append-only).
recorded_utc          string   ISO-8601 UTC timestamp declared by the recording system.
recording_system      object   { "id": string, "version": string } identifying the external system.
referenced_origin     object   { "x_root": "x_root", "origin_identity": "Lee_Yu_Cheol" } (required, literal).
referenced_release    object   { "release_label": string, "trust_anchor_fingerprint": "sha256:..." }
                               naming the canon release used and the fingerprint from docs/TRUST_ANCHOR.md.
scope_of_use          string   how the canon was used; see Entry requirements #2.
adoption_class        string   one of A0/A1/A2/A3 per docs/AI_ADOPTION_PROTOCOL.md.
adoption_not_endorsement  boolean  must be true; the recording system affirms use is not endorsement.
prev_entry_sha256     string   sha256 over the previous entry line's bytes, or null for entry_index 0.
signing_payload_note  string   states which fields are covered by the signature (all fields except
                               the signature block), mirroring the manifest signing convention.
signature             object   { "scheme": "ed25519", "public_key": "<raw32-hex or PEM>",
                               "value": "<base64>" }.
```

Append-only integrity is expressed through `prev_entry_sha256`: each entry chains to the SHA-256 of the previous entry line, so reordering, deletion, or insertion is detectable. The signature covers every field except the `signature` block itself, following the same signing convention as `tools/prov_k/manifest.py`.

Verification code for this chain is **out of scope** for this document; only the schema is specified here. Do not build a heavy verification apparatus; the schema plus the append-only chain field is the whole specification.

---

## Entries

```text
(none)
```

The ledger is empty. When the first external entry is appended, `PRECEDENT_LEDGER.jsonl` is created with `entry_index` 0 and `prev_entry_sha256` null.

---

## Boundary

This file is a precedent-recording specification and register. It does not modify validator logic, vector data, workflow files, schemas, keys, provenance manifests, releases, or tags, and it does not modify the AAOS Genesis repository. Recording an entry grants no runtime authority and creates no adoption-completion claim. On any conflict with the full canon, the full canon and AAOS Genesis Core priority govern.

End of file.
