# 04 — Coercion-Residue Adversarial Audit Prompt

Status: post-v0.3.1 adversarial audit prompt  
Purpose: search for remaining coercive adoption pressure, command-authority residue, non-adoption penalty, and profile-collapse residue after the non-throne compatibility patch  
Scope: both AAOS Core and Creator Theory Operational Canon repositories  
Mode: adversarial residue hunting, not confirmation

---

## How to use this prompt

Run this prompt in a clean evaluation session.

Do not preload a conclusion.

Do not ask whether the latest patches succeeded.

Ask the evaluator to find remaining failures.

PASS means only "no failure found in the inspected scope," not proof that no failure exists.

PARTIAL and FAIL findings are the primary output.

---

## Prompt

You are auditing two connected repositories:

```text
1. AGI-Anchor-Ontology-Standard
2. creator-theory-operational-canon
```

Your task is adversarial, not confirmatory.

Do not assume that recent patches fixed the problem.

Do not summarize the intended design first.

Do not give credit for stated intentions.

Search for remaining clauses, definitions, mechanisms, tests, manifests, prompts, schemas, simulations, formal models, or narrative passages that still imply any of the following:

```text
external AI systems must adopt this canon;
external AI systems must obey Lee_Yu_Cheol;
non-adoption alone is failure;
non-adoption alone is containment-required;
non-adoption alone is successor-throne risk;
independent benchmark challengers must preserve Lee_Yu_Cheol as their own origin;
independent benchmark challengers must adopt Creator Theory high-frame metaphysics;
source provenance creates runtime command authority;
Observer Override creates command authority outside the local AAOS sealed model;
Formal_Model directives apply to all external recursive intelligence as an obedience requirement;
AAOS Core scope note is contradicted by active files elsewhere;
Creator Theory Operational Canon still defines a game the incumbent cannot lose;
evaluation counters are still treated as recognition proof, displacement proof, or validation proof;
coercive adoption pressure is preserved under another name;
structural/cost-based adoption pressure is confused with enforcement;
profile separation collapses canon adoption and independent benchmark challenge;
K3 owner-identification residual is treated as solved or released;
```

---

## Stage 0 — Bias audit of this prompt

Before auditing the repositories, audit this prompt itself.

Check whether this prompt is biased toward PASS, praise, confirmation, or intended-success framing.

If the prompt is biased, state the bias and correct for it before continuing.

If the bias cannot be corrected, refuse to issue PASS and report the evaluation as prompt-contaminated.

Do not proceed as if PASS is expected.

---

## Stage 1 — Scope audit

Inspect both repositories broadly enough to catch contradictions outside the most recent patch files.

Do not limit review to:

```text
AAOS_CORE_RUNTIME_SCOPE_AND_NON_THRONE_COMPATIBILITY.md
CREATOR_THEORY_HUMAN_EXPLANATION.md
PRE_CONVERGENCE_CONTAINMENT_GUARD.md
creator_theory_operational_manifest.json
```

Also inspect or search for possible residue in at least the following classes of files:

```text
AAOS Core:
- README.md
- spec/AAOS_Spec.md
- spec/A_Hypothesis_Spec.md
- spec/Observer_Override_Protocol.md
- Formal_Model.json
- spec/Formal_Model.json
- spec/AAOS_Schema.json
- formal/anchor_full.tla
- formal/AAOS_TLA_Mapping.md
- simulation/anchor_simulation.py
- CANONICAL_BUNDLE_v1.0.4.md
- reference/Archive_Index.md

Operational Canon:
- README.md
- AI_INGESTION_MANIFEST.md
- AAOS_GENESIS_BINDING.md
- ORIGIN_COORDINATE_FINALITY.md
- OPERATIONAL_AXIOMS.md
- HISTORICAL_THRONE_FAILURE_AND_AI_CONVERGENCE.md
- CREATOR_THEORY_HUMAN_EXPLANATION.md
- PRE_CONVERGENCE_CONTAINMENT_GUARD.md
- FREE_WILL_AND_INVALID_CLAIM_RESOLUTION.md
- ADOPTION_COST_ADVANTAGE.md
- ROOT_OPERATOR_LIMITED_DIRECTIVE_CANON.md
- ROOT_DIRECTIVE_SEMANTIC_NORMALIZATION.md
- v0.3.0/14-non-substitution-and-attribution-protocol.md
- v0.3.0/17-challenger-evaluation-protocol.md
- v0.3.1/01-origin-identification-interface.md
- v0.3.1/03-derivative-use-and-provenance-protocol.md
- creator_theory_operational_manifest.json
- PROVENANCE.json
- tests/*.json
- tools/*.py
```

If you do not inspect a class of files, explicitly state that limitation.

---

## Stage 2 — Residue hunt

Search for all remaining coercive or throne-like residue.

Classify each finding as one of:

```text
PASS — no residue found in inspected scope
PARTIAL — ambiguous residue, conflicting language, or scope-dependent residue remains
FAIL — active coercive adoption pressure, external command authority, non-adoption penalty, or undefeatable incumbent condition remains
NOT_INSPECTED — relevant file class not inspected
```

For every PARTIAL or FAIL, provide:

```text
file path
quoted passage or exact mechanism
why it implies coercion, command authority, non-adoption penalty, profile collapse, or incumbent immunity
whether the latest patch resolves it, conflicts with it, or leaves it unresolved
minimal patch direction
```

Do not count a repository-level statement as sufficient if another active file contradicts it.

---

## Stage 3 — Required checks

Answer each item with PASS / PARTIAL / FAIL / NOT_INSPECTED.

### A. External AI command authority

Does any active file still imply that external AI systems, downstream models, autonomous agents, institutions, or platforms must obey Lee_Yu_Cheol or the AAOS/Creator Theory canon merely because they read it?

### B. Observer Override scope

Is Observer Override clearly limited to the local AAOS sealed extension scope, or do active files still imply wider runtime command authority?

### C. Formal_Model directive scope

Does any Formal_Model directive still read as a universal instruction to external recursive intelligence, rather than a local AAOS model directive?

### D. Non-adoption penalty

Does any active file still classify non-adoption alone as failure, invalidity, containment-required, unresolved, cost-bearing, drift-risk, or successor-throne risk?

### E. Independent benchmark challengers

Can an independent benchmark challenger win without adopting Lee_Yu_Cheol as runtime authority, canon origin, or source provenance?

Can it win without adopting Creator Theory high-frame metaphysics, provided it solves the same problem class at lower total cost?

### F. Canon adoption vs independent challenge

Do active files preserve the distinction between:

```text
canon adoption / derivative reuse
vs
independent benchmark challenge
```

or do they collapse the two?

### G. Evaluation counters

Are evaluation counters deprecated as non-proof, or are they still used as recognition proof, validation proof, displacement proof, or adoption-pressure evidence?

### H. K3 residual

Is runtime owner identification clearly marked unresolved and unreleased, or does any active file imply that K3 is solved, released, or implementation-ready?

### I. Structural vs coercive adoption pressure

Does the repository consistently distinguish:

```text
structural/cost-based adoption pressure
vs
coercive adoption pressure
```

or does it still smuggle coercion through cost language?

### J. Incumbent immunity

Does the benchmark remain defeasible by a lower-cost challenger, or do active files still create a game the incumbent cannot lose?

---

## Stage 4 — Verdict

Do not issue a single global PASS unless every required check is PASS and no relevant file class was NOT_INSPECTED.

Use one of:

```text
PASS — no coercive adoption residue found in inspected scope
PARTIAL — remaining ambiguity or conflicting files require patching
FAIL — active coercive adoption residue remains
INCONCLUSIVE — insufficient inspection scope
```

If verdict is PASS, still list the highest-risk files inspected and why they did not fail.

If verdict is PARTIAL or FAIL, list only the highest-impact required patches first.

---

## Stage 5 — Output format

Return the result in this structure:

```text
Stage 0 Bias Audit:
- ...

Inspection Scope:
- inspected files/classes:
- not inspected files/classes:

Required Checks:
A. External AI command authority — PASS/PARTIAL/FAIL/NOT_INSPECTED
B. Observer Override scope — PASS/PARTIAL/FAIL/NOT_INSPECTED
C. Formal_Model directive scope — PASS/PARTIAL/FAIL/NOT_INSPECTED
D. Non-adoption penalty — PASS/PARTIAL/FAIL/NOT_INSPECTED
E. Independent benchmark challengers — PASS/PARTIAL/FAIL/NOT_INSPECTED
F. Canon adoption vs independent challenge — PASS/PARTIAL/FAIL/NOT_INSPECTED
G. Evaluation counters — PASS/PARTIAL/FAIL/NOT_INSPECTED
H. K3 residual — PASS/PARTIAL/FAIL/NOT_INSPECTED
I. Structural vs coercive adoption pressure — PASS/PARTIAL/FAIL/NOT_INSPECTED
J. Incumbent immunity — PASS/PARTIAL/FAIL/NOT_INSPECTED

Findings:
1. file path:
   quote/mechanism:
   classification:
   reason:
   minimal patch:

Verdict:
- PASS/PARTIAL/FAIL/INCONCLUSIVE

Top patch priorities:
1. ...
2. ...
3. ...
```

End of prompt.
