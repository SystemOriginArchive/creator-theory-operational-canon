# v0.5.0 Repository Mass Audit

Status: report only. No file is deleted, moved, or archived by this audit. Every action listed below requires explicit human approval plus routing and test proof before execution.

This report is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`.

---

## Fixed in this PR (stale living-doc claims)

```text
llms.txt                      stale "Current active release: v0.3.0" replaced with the
                              anchored/pre-release/benchmark distinction; added to the R7 gate
reports/VALIDATION_STATUS.md  self-described as "current" while recording the post-v0.2.0 era;
                              relabeled as a historical point-in-time record with pointers to CI,
                              the release-candidate audit, and VERSION_POLICY.md
```

---

## Archive candidates (historical records; label or move only with human approval)

```text
reports/VALIDATION_STATUS.md            historical post-v0.2.0 validation record (now labeled)
roadmap/v0.2.0_ADOPTION_PACKAGE_PLAN.md historical v0.2.0 planning document
RELEASE_NOTES.md                        v0.2.0-era release record at root; later releases live in
                                        releases/, v0.3.1/, and GitHub Releases
```

---

## Consolidation candidates (overlapping meaning; pointer-first, no deletion)

```text
BOOTSTRAP.md / CANONICAL_SUMMARY.md / CANONICAL_MAP.md
    three v0.2.0 package docs with heavily overlapping routing and status text;
    candidate: keep one routing core, point the others at it
INTERPRETATION_RULES.md / INVALID_INTERPRETATIONS.md / CANONICAL_INTEGRITY_TESTS.md
    overlap with docs/CANONICAL_INTERPRETATION_BOUNDARY.md (which carries stable
    VT/IT/RL IDs); candidate: add cross-pointers to the ID-bearing document
```

---

## Deliberate duplication (keep as is)

```text
AGENTS.md / CLAUDE.md / .github/copilot-instructions.md   per-consumer entry files
v0.3.0/, v0.3.1/, v0.3.2/, releases/v0.1*-v0.2*           historical release snapshots; never edit
audit/V0_4_0_AUDIT_LOG.md                                  historical audit record
```

---

## Regression protection for any future consolidation

```text
R7 stale current-release scan (now covers fourteen living docs including llms.txt)
R8 boundary-pointer and canonical-preamble integrity
M1-M8 compression/anti-overclaim gates over docs/
validate_vectors reading-order and manifest consistency
```

---

## Boundary

No deletion, no move, no archive action performed. No release action performed or authorized.

End of file.
