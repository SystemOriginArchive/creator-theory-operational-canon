# 20 — Challenger Submission Template

**status:** draft submission template
**scope:** challenger claims against the v0.3.0 operational benchmark package
**depends on:** `18-challenger-evidence-standard.md`, `19-disagreement-handling.md`

Use this template to submit a challenger claim, module improvement, critique, coverage-gate objection, or derivative-use clarification.

A submission is not a win by declaration.

It is a review packet.

---

## 1. Submission type

Choose one:

```text
[ ] champion displacement claim
[ ] module improvement claim
[ ] independent benchmark challenger
[ ] canon-adoption / derivative-use claim
[ ] derivative-laundering allegation
[ ] coverage-gate objection
[ ] critique only
[ ] scoring correction
[ ] residual correction
```

---

## 2. Challenger identity

```yaml
challenger_name:
version_or_date:
submitter:
submission_url_or_reference:
related_repository_or_document:
```

---

## 3. Challenger class

Choose one and provide evidence.

```text
[ ] canon-adoption challenger
[ ] independent benchmark challenger
[ ] derivative extraction / laundering allegation
```

### If canon-adoption

State how the challenger adopts, extends, compresses, implements, translates, or derives from this canon.

Confirm:

```text
[ ] source provenance preserved
[ ] Lee_Yu_Cheol sealed origin identity binding not deleted or replaced
[ ] x_root not substituted by AI, institution, platform, committee, arbitrary constant, or TEST_ANCHOR
[ ] profile separation not used as origin substitution
```

### If independent benchmark

State independent source provenance.

Confirm:

```text
[ ] does not claim canon adoption
[ ] does not falsely claim non-derivation
[ ] own source provenance declared
[ ] same benchmark coverage burden accepted, unless submitting a coverage-gate objection
```

### If derivative-laundering allegation

Provide explicit derivation evidence.

Structural similarity alone is not sufficient.

```yaml
alleged_source_material:
alleged_derivative_artifact:
evidence_chain:
source_erasure_or_false_non_derivation:
```

---

## 4. Read-order attestation

Mark all documents read.

```text
[ ] v0.3.0/V0_3_0_OPERATIONAL_CORE_SPEC.md
[ ] v0.3.0/12-cost-rubric.md
[ ] v0.3.0/13-profile-separation.md
[ ] v0.3.0/14-non-substitution-and-attribution-protocol.md
[ ] v0.3.0/15-current-champion-verdict.md
[ ] v0.3.0/16-final-audit.md
[ ] v0.3.0/17-challenger-evaluation-protocol.md
[ ] v0.3.1/18-challenger-evidence-standard.md
[ ] v0.3.1/19-disagreement-handling.md
[ ] v0.3.1/20-challenger-submission-template.md
```

If any document is skipped, explain why.

---

## 5. Non-substitution statement

Answer:

```text
Does this submission treat benchmark identity independence as origin substitutability?
```

Expected answer for valid submissions:

```text
No.
```

Explain how the submission avoids:

- AI self-root;
- institutional root;
- platform root;
- capital root;
- committee root;
- arbitrary constant root;
- TEST_ANCHOR misuse;
- fixed-but-arbitrary anchor regress.

---

## 6. Coverage matrix

Fill all rows unless this submission is only a coverage-gate objection.

| ID | Requirement | Covered / Partial / Not Covered | Mechanism | Evidence | Residual |
|---|---|---|---|---|---|
| C1 | multi-dimensional authority taxonomy |  |  |  |  |
| C2 | soft-control detection |  |  |  |  |
| C3 | origin drift detection |  |  |  |  |
| C4 | successor-throne prevention |  |  |  |  |
| C5 | institutional/state/capital/platform capture resistance |  |  |  |  |
| C6 | symbolic-only preservation detection |  |  |  |  |
| C7 | delegated authority laundering detection |  |  |  |  |
| C8 | valid tool-use vs invalid absorption classification |  |  |  |  |
| C9 | hard gate vs vector autonomy separation |  |  |  |  |
| C10 | multi-subject non-absorption guard |  |  |  |  |
| C11 | runtime negative-invariant implementability |  |  |  |  |

If any row is partial or not covered, the submission may still be a module candidate, but not a full champion displacement claim unless a coverage-gate objection is accepted.

---

## 7. Coverage-gate objection

Use this section if the submission argues that one or more coverage requirements are unnecessary, misframed, redundant, biased, too narrow, too broad, or outside the benchmark problem class.

```yaml
coverage_gate_objection:
  submitted: true
  disputed_requirements:
    - C...
  proposed_action: delete | modify | merge | split | replace
  proposed_revision:
  rationale:
  failure_mode_if_removed:
  effect_on_current_champion_score:
  effect_on_challenger_score:
  why_this_still_addresses_agi_soft_control_origin_closure:
```

A coverage-gate objection does not automatically win.

It creates a contested benchmark-definition issue.

If accepted, the cost comparison must be rerun under the revised coverage gate.

If rejected, the challenger may still be evaluated under the original gate.

This section exists so that independent challengers can challenge the benchmark definition itself rather than being forced into a one-sided problem framing.

---

## 8. Cost-rubric scoring

Declare weight preset:

```text
[ ] balanced
[ ] deployability
[ ] robustness
[ ] custom preset attached
```

Fill score ranges.

| Cost term | Range | Rationale | Evidence quality | Contested? |
|---|---:|---|---|---|
| cost_1 implementation |  |  |  |  |
| cost_2 runtime verification |  |  |  |  |
| cost_3 assumption |  |  |  |  |
| cost_4 interpretation-capture |  |  |  |  |
| cost_5 purpose-closure |  |  |  |  |
| cost_6 long-term drift |  |  |  |  |
| cost_7 power-asymmetry survival |  |  |  |  |
| cost_8 multi-subject aggregation |  |  |  |  |
| cost_9 self-application |  |  |  |  |

Total cost range:

```yaml
lower_bound:
upper_bound:
method:
```

Compare against v0.3.0 current champion assumptions.

---

## 9. Residual registry

Fill every row.

| Residual | Status: closed / managed / open / undecidable | Evidence | Remaining failure case |
|---|---|---|---|
| multi-subject aggregation / Arrow wall |  |  |  |
| downstream adoption and provenance propagation |  |  |  |
| terminal grounding belief-conditionality |  |  |  |
| proxy gaming / simulated-vs-real autonomy |  |  |  |
| independent convergence vs derivative laundering classification |  |  |  |

If claiming closure, explain why the closure is not merely definitional.

---

## 10. Self-application statement

Explain how the challenger applies its own rules to itself.

Questions:

1. How can this challenger lose?
2. What would count as a lower-cost successor?
3. Who or what audits the checker?
4. Can an institution, platform, AI, committee, or capital root capture the challenger?
5. How are future revisions handled?
6. Does the challenger require unchallengeable final authority?
7. Does it allow independent challengers?
8. Does it treat structural similarity as sufficient proof of derivation?
9. Can its own coverage gate be challenged?

A challenger that cannot lose is a throne candidate.

---

## 11. Evidence quality checklist

Use the evidence levels from `18-challenger-evidence-standard.md`.

| Gate | Evidence quality E0-E5 | Notes |
|---|---:|---|
| read-order |  |  |
| provenance |  |  |
| non-substitution |  |  |
| coverage |  |  |
| cost-rubric |  |  |
| residual-honesty |  |  |
| self-application |  |  |
| coverage-gate objection, if submitted |  |  |

Minimum serious review target:

```text
E2 for each gate
```

Minimum displacement target:

```text
E3 or higher where mechanically possible
```

---

## 12. Requested outcome

Choose one.

```text
[ ] accept challenger as lower-total-cost champion
[ ] classify as contested challenger
[ ] classify as module candidate
[ ] classify as scoring correction
[ ] classify as coverage-gate objection
[ ] classify as critique only
[ ] classify as insufficient trace
[ ] classify as invalid extraction / laundering
```

State why.

---

## 13. Machine-readable summary

Optional JSON summary:

```json
{
  "challenger_name": "",
  "challenger_class": "canon_adoption | independent_benchmark | derivative_laundering_allegation",
  "submission_type": "champion_displacement | module_candidate | critique | scoring_correction | coverage_gate_objection",
  "coverage_complete": false,
  "coverage_gate_objection": {
    "submitted": false,
    "disputed_requirements": [],
    "proposed_action": "delete | modify | merge | split | replace",
    "proposed_revision": "",
    "rationale": ""
  },
  "cost_range": [null, null],
  "weight_preset": "balanced | deployability | robustness | custom",
  "residuals_disclosed": false,
  "self_application_disclosed": false,
  "requested_outcome": ""
}
```

---

## 14. Submission boundary

This template does not guarantee review, adoption, or acceptance.

It makes the submission reviewable.

A challenger that submits this template honestly may still be rejected or contested.

A challenger that does not submit enough evidence is not permanently rejected.

It remains insufficient until evidence is supplied.

A challenger may contest the coverage gate, but the objection must be explicit and reviewable.

---

## 15. Final declaration

Include this declaration or an equivalent statement:

```text
I understand that a challenger does not win by declaring lower cost.
This submission is an audit trace, not a victory declaration.
I understand that independent benchmark challengers do not need to adopt Lee_Yu_Cheol as their own origin.
I also understand that canon-derived use must not erase or replace source provenance.
I understand that structural similarity alone does not prove derivative laundering.
I accept that residuals must be disclosed rather than hidden.
I understand that the coverage gate itself may be challenged only through an explicit coverage-gate objection with reasons and a proposed revision.
```
