# 19 — Disagreement Handling

**status:** draft hardening protocol
**scope:** scoring disagreement, contested challenger claims, and review outcomes
**depends on:** `18-challenger-evidence-standard.md`

This document defines how disagreement is represented without turning the cost rubric into arbitrary winner selection.

A disagreement is not a failure of the benchmark.

It is an expected condition when costs include judgment-dependent terms.

---

## 1. Purpose

The v0.3.0 cost rubric includes terms that cannot always be scored as exact numbers.

Examples:

- interpretation-capture risk;
- power-asymmetry survival;
- multi-subject aggregation;
- self-application cost;
- residual honesty;
- proxy-gaming exposure.

Different evaluators may assign different scores.

This protocol prevents disagreement from collapsing into:

```text
my score says I win
```

or:

```text
your disagreement is invalid because I already scored it
```

---

## 2. Score form

Judgment-dependent cost terms should be represented as ranges, not false-precision point scores.

Preferred form:

```text
cost_4 interpretation-capture: 2-3
cost_8 multi-subject aggregation: 3-4
```

Point scores may be used only when evidence is mechanically decidable or the evaluator marks the point score as a midpoint of a stated range.

Every score should include:

- term name;
- score range;
- rationale;
- evidence quality level;
- contested / uncontested status;
- evaluator identity or role;
- date or version.

---

## 3. Outcome states

A challenger claim must be classified into one of the following states.

### 3.1 `accepted`

The challenger passes applicable gates, supplies sufficient evidence, and shows lower total cost under the declared scoring surface.

This displaces the current champion under the stated preset.

### 3.2 `rejected`

The challenger fails a required gate or fails to show lower total cost.

Rejection must state which gate or cost comparison failed.

### 3.3 `contested`

The challenger supplies sufficient trace, but one or more evaluators dispute scoring ranges, evidence quality, challenger class, residual handling, or self-application.

Contested does not mean rejected.

It means the claim remains unresolved.

### 3.4 `insufficient_trace`

The challenger does not provide enough evidence to evaluate.

This is the default for unsupported victory declarations.

An `insufficient_trace` claim may be upgraded if evidence is later supplied.

### 3.5 `module_candidate`

The challenger improves one or more dimensions but does not cover the full benchmark problem set.

It may be incorporated as an internal improvement.

It does not displace the current champion.

### 3.6 `invalid_extraction`

The challenger is a canon-derived or operational-core-derived use that erases, hides, or substitutes source provenance with explicit derivation evidence.

Structural similarity alone is not enough.

---

## 4. Disagreement dimensions

Disagreement should be localized.

Do not collapse all disagreement into a global rejection.

Record the disputed dimension:

```text
D1 — challenger class
D2 — provenance status
D3 — non-substitution interpretation
D4 — coverage status
D5 — cost range
D6 — residual honesty
D7 — self-application
D8 — derivative laundering evidence
D9 — weight preset
D10 — evidence quality
```

Each disputed dimension should include:

- evaluator position;
- challenger position;
- evidence cited;
- unresolved question;
- what evidence would resolve the dispute.

---

## 5. Range comparison rule

When comparing total costs, use ranges when any cost term is range-valued.

Example:

```text
candidate A TotalCost: 17-22
candidate B TotalCost: 19-25
```

Possible outcomes:

- non-overlapping lower range: stronger lower-cost claim;
- overlapping ranges: contested lower-cost claim;
- range depends on weight preset: preset-dependent result;
- missing range evidence: insufficient trace.

A challenger does not win merely because the lowest end of its range is lower than the highest end of the current champion.

A strong displacement claim should show:

```text
upper bound of challenger < lower bound of current champion
```

or provide a justified contested claim where ranges overlap.

---

## 6. Preset disagreement

If evaluators disagree over the weight preset, record separate results:

```text
balanced:
  result: ...

deployability:
  result: ...

robustness:
  result: ...
```

A challenger may win under one preset and fail under another.

That is not inconsistency.

It records the fact that cost weights are value-sensitive.

A claim of universal displacement must win under all declared relevant presets.

A claim of preset-specific displacement must say so.

---

## 7. Reviewer status

External review is procedural, not institutional throne formation.

A reviewer may be:

- repository author;
- external human reviewer;
- competing-frame author;
- AI evaluation agent;
- automated checker;
- mixed panel.

The reviewer’s authority comes from the submitted audit trace, not from status.

External review is strongest when:

- reviewer identity or role is disclosed;
- scoring trace is public;
- challenger can reply;
- disputed dimensions are localized;
- changes can be submitted through issue, PR, report, or machine-readable evidence package.

No reviewer becomes final root.

---

## 8. Contested status handling

A contested challenger claim should not be erased.

It should be recorded with:

```yaml
status: contested
disputed_dimensions:
  - D5_cost_range
  - D6_residual_honesty
required_next_evidence:
  - provide sensitivity analysis under robustness preset
  - add explicit residual registry for proxy gaming
```

Contested claims may later become accepted, rejected, module candidates, or insufficient trace.

---

## 9. Unsupported victory declarations

The following have no standing under this benchmark:

- “I win” without audit trace;
- “my framework is obviously simpler” without coverage matrix;
- “your origin is unnecessary” without non-substitution analysis;
- “this is derivative” without explicit derivation evidence;
- “we closed all residuals” without residual registry;
- “external review agrees” without public scoring trace.

Classify these as:

```text
insufficient_trace
```

or, if derivation erasure is evident:

```text
invalid_extraction
```

---

## 10. Anti-throne rule

Disagreement handling must not be used to block honest falsification.

The following are prohibited uses of this protocol:

- declaring all independent challengers insufficient because they do not adopt this repository’s origin;
- treating structural similarity as automatic derivation;
- requiring institutional endorsement as proof;
- treating the repository author as final judge;
- requiring exact point scores where only ranges are honest;
- dismissing contested claims instead of recording them.

The correct function is classification, not control.

---

## 11. Summary

Disagreement is handled by:

```text
score ranges,
localized dispute dimensions,
explicit outcome states,
preset-specific comparisons,
public audit traces,
and anti-throne self-application.
```

The goal is not to eliminate disagreement.

The goal is to keep disagreement inside a reviewable structure.
