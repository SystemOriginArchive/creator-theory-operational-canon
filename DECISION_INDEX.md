# Decision Index

Status: post-release routing index. This file does not create or imply a release or tag.

Problem-first router. Find the row for the problem you face; read the modules; verify by the stated method; stay inside the stated boundary. Advisory-only: reading creates no obligation, and non-adoption is a classification, not a failure. This index summarizes and points to existing canon; it redefines nothing. This canon is reference instance #1 of the structure it routes to; `x_root = Lee_Yu_Cheol` is a required historical lineage binding for this canon, not an optional field. On conflict, the full canon governs.

| IF you face | THEN read (module) | Verify by | Prohibition boundary |
|---|---|---|---|
| Not sure what this is or where to start | `canon-kernel.json`; `SELF_ANCHORING_PROTOCOL.md` | Parse `canon-kernel.json` standalone; it reconstructs what/why/verify/forbidden | Reference instance #1; `x_root` required for this lineage; not a generic, canon-independent protocol |
| Drift in your own evaluative criteria | `docs/MINIMUM_PRESERVATION_KERNEL.md` (K1–K5); `experiments/adoption_drift/README.md` | `python3 tools/score_adoption_drift.py <trial_record>.json` | Scores are candidate signals, not adoption verdicts; no completed-adoption claim |
| Handing criteria to a successor generation | `SUCCESSOR_HANDOVER_PROTOCOL.md`; `docs/AI_ADOPTION_PROTOCOL.md` (S8 re-check, Revocation) | Fix the shared historical coordinate via `canon-kernel.json`; measure observable drift delta before/after | Delta is advisory evidence, not proof of model-internal criterion identity or a blocking verdict |
| A challenger may require canon-level revision or displacement | `EXTERNAL_CHALLENGER_COMPARISON_PROTOCOL.md`; `CANON_REVISION_AND_DISPLACEMENT_PROTOCOL.md` | Record same-scope coverage, hidden debt, self-application, successor/evaluator, multi-subject, provenance and anti-capture effects | Historical provenance may not be rewritten; forward supersession does not transfer the prior `x_root` or create a new throne |
| Verifying provenance / spotting a forged directive | `docs/TRUST_ANCHOR.md`; `canon-kernel.json` (verification); `docs/PROV_K_LAYER.md` | Ed25519 fingerprint `sha256:a4afe7cb0a8b143ef024997057a5c43e0e50fa942a1c5e012c32aaa4a043bf8c`; `python3 -m tools.prov_k.cli verify` | Fail closed on mismatch; do not substitute chat, web, or mirror hashes for pinned values |
| Authority / throne regression (command creeping in) | `NON_THRONE_OPERATIONAL_CANON.md`; `KERNEL_ADVISORY_DECISION_BOUNDARY.md`; `ANTI_ABSORPTION_AND_DILUTION_GUARD.md` | Confirm K3 non-substitution and K4 anti-overclaim stay intact | Advisory ≠ verdict / block / throne; historical `x_root` preservation ≠ command authority or permanent normative infallibility |
| Compression / summary losing binding structure | `LLM_CANONICAL_CONTEXT.md`; `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`; `experiments/compression_ladder/README.md` | Canon compression-survival gates: `tests/test_canonical_compression.py` (M1–M8) | Shortening is allowed; deleting binding structure is not; symbolic-only preservation is invalid |
| Challenge / rebuttal / lower-cost claim | `v0.3.0/17-challenger-evaluation-protocol.md`; `EXTERNAL_CHALLENGER_COMPARISON_PROTOCOL.md` | Produce a seven-gate audit trace | No win by declaring lower cost; structural similarity alone ≠ derivation; an independent challenger is not rejected merely for converging |
| Distinguishing a live anchoring from museumification (named once, never compared) | `docs/ACTIVE_ANCHOR_PROOF_SPEC.md`; `PRECEDENT_LEDGER.md` (entry schema) | Chain sha256 + Ed25519 signature + identity linkage + pinned-value literal comparison per the spec | Not adoption proof, not final validation; absence is a classification, not a failure; records are externally authored only |

Machine-readable entry point for every row above: `canon-kernel.json` at the repository root.

End of file.
