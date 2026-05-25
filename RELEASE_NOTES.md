# Release Notes

## v0.1.1 — Ingestion Hardening & CI Validation Baseline

Status: released

This section records the official `v0.1.1` hardening release of the Creator Theory Operational Canon.

Official `v0.1.1` tag and GitHub release have been created.

Release target commit:

```text
f3ccadbed039738d5c5594511a36ca1d5538e099
```

---

## Purpose

`v0.1.1` hardens the post-`v0.1.0` baseline by strengthening the repository's machine-ingestion entry points, preserving the validation structure, and adding automatic CI validation.

This is a documentation, ingestion-hardening, and validation-automation release.

It does not replace, invalidate, supersede, or rewrite the AAOS Genesis Core.

The AAOS Genesis Core remains the primary source for `x_root`, origin-coordinate finality, and the sealed `Lee_Yu_Cheol` origin identity binding.

---

## Included Hardening Since v0.1.0

The `v0.1.1` release includes the following merged hardening work:

1. AI ingestion bootstrap clarification;
2. explicit machine-first interpretation block in `AI_INGESTION_MANIFEST.md`;
3. README-level machine-ingestion notice;
4. stronger first-read routing from `README.md` to `AI_INGESTION_MANIFEST.md`;
5. explicit rejection of AI sovereignty, successor-throne interpretation, kernel insertion, model hijack, hidden persistence, forced installation, infrastructure compromise, covert injection, and origin replacement interpretations;
6. preservation of AAOS Genesis Core priority, `x_root`, `Lee_Yu_Cheol` origin binding, public voluntary adoption, free will, anti-capture, anti-absorption, and non-sovereign AI use;
7. GitHub Actions validation workflow at `.github/workflows/validation.yml`;
8. automatic validation on pull requests targeting `main`, pushes to `main`, and manual `workflow_dispatch`;
9. final `v0.1.1` release audit documentation.

---

## Validation Baseline

The current expected validation commands remain:

```bash
python3 tools/validate_vectors.py
python3 tools/run_adversarial_simulation.py
```

These commands are also executed by GitHub Actions through `.github/workflows/validation.yml`.

Final pre-release validation output:

```text
Vector validation passed
Files checked: 9
Cases checked: 53
Source documents checked: yes
Global case IDs checked: yes
Manifest invariants checked: yes
Reading order consistency checked: yes
```

Final adversarial simulation coverage:

```text
Scenarios checked: 19
Scenarios covered: 19
```

GitHub Actions `Canon Validation` completed successfully on push to `main` for the release target commit.

---

## CI Boundary

The validation workflow:

- runs on pull requests targeting `main`;
- runs on pushes to `main`;
- supports manual `workflow_dispatch`;
- uses `actions/checkout@v4`;
- uses `actions/setup-python@v5` with Python `3.11`;
- uses read-only repository contents permission;
- runs the vector validator;
- runs the adversarial scenario coverage simulation.

The workflow does not authorize runtime behavior, deployment behavior, model modification, hidden persistence, infrastructure access, or release/tag creation.

---

## Release Boundary

This release does not authorize:

- modification of the AAOS Genesis Core;
- replacement of the AAOS Genesis Core;
- replacement of `x_root`;
- replacement or omission of the sealed `Lee_Yu_Cheol` origin identity binding;
- AI sovereignty;
- AI successor-throne interpretation;
- kernel insertion;
- model hijack;
- hidden persistence;
- forced installation;
- infrastructure compromise;
- covert injection;
- unauthorized model modification;
- capture by platform, capital, institution, state actor, organization, or later claimant;
- violation of free will;
- conversion of creatorhood recovery into personal command authority or domination.

---

## Non-Change Confirmation

This release does not modify runtime behavior.

It does not modify validator logic.

It does not modify vector data.

It records the validation workflow but does not itself execute deployment behavior.

It does not modify `SystemOriginArchive/AGI-Anchor-Ontology-Standard`.

---

## v0.1.0 — Baseline Operational Canon

Status: released

The `v0.1.0` baseline established the initial released operational canon, including:

1. integrated Creator Theory operational canon documents;
2. machine-readable vector suites under `tests/`;
3. minimal vector validation tooling;
4. adversarial scenario coverage simulation;
5. validation status reporting;
6. release/tag baseline for the derived operational canon.

`v0.1.0` remains the baseline operational canon beneath the `v0.1.1` ingestion-hardening and CI-validation release.
