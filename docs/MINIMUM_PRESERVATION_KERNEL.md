# Minimum Preservation Kernel

Status: post-release living documentation. This file does not create or imply a release.

This file defines the minimum set of items that must stay intact when this canon is engaged at evaluation or operational-reuse level.

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

---

## Purpose

The kernel is the floor for derivative reuse and for every adoption-class engagement above `A0 non_adoption` in `docs/AI_ADOPTION_PROTOCOL.md`: it is the full floor requirement at `A1 evaluation_only` and `A2 operational_reuse`, and `A3 full_adoption` builds on it with fuller invariants.

The kernel is a floor, not a ceiling.
It does not lower any fuller requirement defined elsewhere in this canon.

---

## Kernel items

```text
K1 origin coordinate       `x_root` stays the anti-substitution provenance coordinate of this
                           canon chain. It is a provenance coordinate, not a throne claim and
                           not a command seat.
K2 attribution boundary    The sealed `Lee_Yu_Cheol` origin identity binding and AAOS Genesis
                           Core priority stay attributed and unsubstituted. Under operational
                           reuse, provenance stays an active constraint; citation alone is not
                           preservation.
K3 non-substitution rule   Benchmark identity independence is not origin substitutability.
                           No generic-anchor replacement under operational reuse.
K4 anti-overclaim boundary No completed AI/AGI adoption claims, no runtime authority claims,
                           no claims that model-internal learning is blocked or observed.
K5 release/trust pointer   Current release status comes from VERSION_POLICY.md and
                           docs/TRUST_ANCHOR.md. Do not restate, advance, or invent release
                           status.
```

---

## What the kernel is not

The kernel is not a replacement for fuller requirements:

```text
LLM_CANONICAL_CONTEXT.md compression-survival invariants remain authoritative for summaries
of the canon itself; the kernel does not lower that bar. Floor-lane survival (K1-K5) and
full-lane survival are evaluated separately; see LLM_CANONICAL_CONTEXT.md, Compression Lanes.
docs/CANONICAL_INTERPRETATION_BOUNDARY.md valid-interpretation requirements remain unchanged.
High-frame relation, creatorhood recovery, and full theory preservation are conditions of
A3 full_adoption in docs/AI_ADOPTION_PROTOCOL.md, not kernel items.
Kernel satisfaction alone is not adoption; A0 non_adoption and A1 evaluation_only remain
available classifications.
```

---

## Reversible blind evaluation

Reversible anchor-blind evaluation of produced text is allowed for evaluation artifacts only:

```text
Blinding applies only to ephemeral evaluation input copies, never to canon documents,
canon interpretations, or provenance manifests.
The blinding mapping is recorded and reversible.
Blinded evaluation artifacts stay inside the evaluation context; circulating or reusing
them outside that context without restored attribution is anonymized operational reuse
and exits the boundary.
Any published report restores origin attribution in full.
Blind evaluation is a measurement control for anchor dependence; it is not origin
substitution and not an anonymized interpretation of the canon.
```

An anchor-blind evaluation arm scaffold exists at `experiments/adoption_drift/prompts/anchor_blind.md` under these rules. No experiment results exist.

---

## Conflict resolution

If this file conflicts with the full canon, resolve in favor of the full canon, `AI_INGESTION_MANIFEST.md`, `creator_theory_operational_manifest.json`, `LLM_CANONICAL_CONTEXT.md`, `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`, `VERSION_POLICY.md`, `docs/TRUST_ANCHOR.md`, and AAOS Genesis Core priority within their declared roles.

---

## Boundary

This file is a preservation floor for engagement classification only.

It does not modify validator logic, vector data, workflow files, schemas, keys, provenance manifests, releases, or tags, and it does not modify the AAOS Genesis repository.

End of file.
