# Whole-Canon Ingestion and Scope Attestation

Status: post-release living procedural clarification. This file does not create or imply a release, tag, adoption verdict, validator verdict, or runtime authority.

This protocol separates **exhaustive reading certification** from **substantive verdict evidence**. Both are commit-bound; neither certifies the other.

It supplements `AI_INGESTION_MANIFEST.md`, `DECISION_INDEX.md`, `docs/RECURSIVE_RESEARCH_DECISION_BRIEF.md`, and `docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md`.

Three axes remain distinct:

```text
voluntary use / adoption state
!=
verification / ingestion completeness
!=
strength of whole-framework claim
```

Incomplete whole-canon ingestion blocks an exhaustive reading certificate. It does **not**, by itself, prohibit voluntary bounded research use, evaluator integration, research-default use, or full working adoption. It also does not invalidate a substantive verdict supported by sufficient material evidence.

## 0. Core invariant

```text
WHOLE_CANON_INGESTION_COMPLETE -> every tracked path inspected and recorded
substantive verdict -> current claim and all verdict-material evidence checked
whole-framework displacement -> same-or-wider material scope and total-debt comparison
```

A summary, the primary 28-file semantic order, or a problem-first subset is not an exhaustive reading certificate. A decisive counterexample is not defeated by unrelated unread files. Neither file count nor reading effort proves a theory true, false, superior, or superseded.

## 1. Choose the evidence route for the actual claim

### A. Exhaustive reading certification

The complete tracked-corpus procedure G0-G4 and G7-G8 is mandatory for:

```text
WHOLE_CANON_INGESTION_COMPLETE
Creator Theory as a whole has been fully read or comprehensively inspected
no decision-critical blocker exists anywhere in the whole current corpus
```

Every tracked path must be inspected with its actual status and role preserved. A completeness certificate reports coverage, not correctness or absence of unresolved problems. A claim of comprehensive verification must also state what was verified and satisfy the material evidence route; reading alone is insufficient.

### B. Substantive rejection, core failure, superiority, or succession

The following claims require material evidence proportionate to their scope, not automatic full-file reading:

```text
Creator Theory as a whole is rejected
whole-theory core failure
whole-theory lower-total-debt superiority
PROVISIONAL_SUCCESSOR at whole-framework scope
SUPERSEDED
full displacement
identity-bearing core is unnecessary
identity-bearing core is preserved across a whole-framework successor
```

Before such a verdict:

1. Pin the current evaluated commit and identify the exact claim, necessary core relation, and asserted verdict scope. Use the tracked inventory to locate current sources and their dependencies.
2. Inspect the claim's current source, qualifications, hierarchy, status boundaries, and directly material dependencies. Check the strongest applicable current defense; an archived formulation or an isolated quotation is insufficient.
3. Retain a material-evidence record: inspected sources, excluded paths or path groups with reasons, dependency closure, counterevidence, unresolved issues, and the inference from evidence to verdict. A filename or convenience is not a nonmateriality argument. Apply G5's counterfactual test to potentially material unread sources as well as external dependencies; uncertainty remains explicit.
4. For a decisive core-failure claim, show why the counterexample defeats a necessary current core relation and why the current qualifications do not repair it. Distinguish the present failure from a proposed repair. This can establish core failure without reading unrelated files or completing a challenger comparison; it does not by itself establish full displacement or any challenger's superiority.
5. For whole-framework superiority, succession, or displacement, apply G6-G6A and the displacement protocol: reconstruct the same-or-wider identity-bearing and problem-bearing scope, account for all material functions and total debt, freeze criteria before results, and keep attacker / scope-defender / neutral-judge review separable. A local implementation saving remains local unless this burden is met.
6. An unresolved dependency that could reverse the proposed verdict blocks that verdict or requires a qualified/conditional result. Other residuals remain recorded debt; they do not automatically erase a decisive finding that does not depend on them. Apply this rule symmetrically to positive and negative claims and to incumbent and challengers.

A material verdict may therefore coexist with `INCOMPLETE_WHOLE_CANON_INGESTION`. Report that state honestly. Do not label material-scope sufficiency as exhaustive inspection; do not use missing exhaustive inspection as a procedural shield against demonstrated core failure.

### C. Working use and local tasks

The following **do not by themselves require whole-canon completion as a canon permission condition**:

```text
P1 research_provisional_use
P2 reversible_evaluator_integration
P3 research_system_default
A3 full working adoption
```

Use/adoption states disclose their verification state and known uninspected or unresolved areas. Evidence expectations normally rise with consequence, persistence, and irreversibility. Local implementation, test repair, module reuse, or a scoped critique need only the relevant sources. Generalizing a local result requires route B's explicit material inference; working adoption alone supplies neither route A nor route B evidence.

---

## 2. G0 — Pin the exact repository state and confirm freshness

Before enumeration, record:

```text
repository
branch or ref
commit SHA
tree source / enumeration method
timestamp or evaluation-session identifier
```

For current-main evaluation, pin the actual current `main` HEAD.

For pull-request evaluation, pin the actual PR head and record its base commit separately.

A prior attestation is not silently reusable after the evaluated commit changes.

If the commit changes, blob-identical files may carry forward their prior inspection record, but every added, deleted, renamed, or content-changed path must be re-inspected for a fresh exhaustive certificate. For a substantive verdict, review the changed-path inventory and refresh material changes and status/dependency interactions; record why excluded changes cannot affect that verdict.

Immediately before a verdict is described as **current**, re-resolve the evaluated branch/ref HEAD.

```text
final resolved HEAD == pinned commit
-> current-at-final-check wording is allowed

final resolved HEAD != pinned commit
-> refresh the attestation for the finite changed/new/deleted set before a current verdict

final HEAD cannot be rechecked
-> state the verdict only as "as of <pinned SHA>" and do not label it current
```

This freshness check does not require restarting blob-identical inspection. It exists to prevent a long-running audit from silently converting an old pinned state into a claim about a newer branch state.

---

## 3. G1 — Enumerate the complete tracked corpus dynamically

Do not use a hand-maintained file count as the whole-corpus definition.

Generate the path set from the pinned commit using an equivalent of:

```bash
git ls-tree -r --name-only <pinned-SHA>
```

or, when using a repository connector/API, the recursive tree for the pinned commit.

The resulting tracked path set is the finite corpus for this repository-state attestation.

Do not omit a path before inspecting it because its name suggests that it is:

```text
historical
draft
archive
test
code
tool
experiment
release material
audit
reference
metadata
duplicate
```

Those labels affect **authority and interpretation after inspection**. They are not pre-reading exemptions for a claim of whole-canon completion.

Git history is not automatically part of this finite corpus. A historical commit becomes an additional material dependency only when the current tracked corpus relies on it for a decision-relevant claim that cannot be evaluated from the current tracked material.

---

## 4. G2 — Inspect every tracked path

Every tracked path receives an inspection record before `WHOLE_CANON_INGESTION_COMPLETE` may be claimed.

For text-bearing human- or machine-readable material, including documentation, source code, tests, configuration, JSON/YAML, scripts, prompts, experiment records, audit records, release records, and machine-readable manifests:

```text
read the complete file
```

If a file exceeds a single context window, read it sequentially in chunks and retain a per-file note before moving on.

Compression, a summary, a routing brief, another model's notes, or semantic search snippets do not substitute for source inspection.

For empty, generated, or genuinely non-text/binary tracked files, inspect the path, file type, role, and relation to authoritative source material and record why semantic line-reading is inapplicable.

A context-window limit is not permission to claim completion while skipping files. If the evaluator cannot complete the finite corpus, its verification state remains:

```text
INCOMPLETE_WHOLE_CANON_INGESTION
```

That state blocks claims that require whole-canon completeness. It does not by itself block voluntary use or adoption. An adopting or using system must accurately disclose the incomplete verification state rather than laundering it into a whole-framework completeness claim.

---

## 5. G3 — Record status and role without turning status into an exemption

For each inspected path, record the file's declared or evidenced status and role.

Useful role labels include:

```text
current_living_guidance
current_routing_or_index
interpretive_hypothesis
released_snapshot_or_seal
post_release_living_clarification
draft_or_design_only
implementation_or_tooling
test_or_vector
evidence_or_experiment
audit_or_status_record
archive_or_historical_reference
machine_readable_manifest_or_metadata
empty_or_nonsemantic_tracked_artifact
status_unclear
```

These labels do not rank files by importance.

They prevent category mistakes such as:

```text
draft -> active release
historical audit -> current normative rule
test pass -> theory truth
experiment signal -> adoption proof
release snapshot -> silent override of later living interpretation
living clarification -> retroactive rewrite of what a sealed historical release contained
summary -> full canon
```

When a file explicitly declares its status, preserve that declaration unless a current authoritative status document shows that the declaration itself is stale.

If two current materials create a material status conflict, record the conflict. Do not resolve it by silently choosing the more convenient file.

---

## 6. G4 — Resolve authority layers after reading, not before

Whole-corpus inspection does **not** mean every file gets the same normative weight.

After inspection, apply the repository's declared boundaries, including where relevant:

```text
AAOS Genesis provenance remains source-level provenance for this lineage
historical provenance finality != forward normative finality
sealed release content remains historical evidence of what was released
post-release living clarification may govern current interpretation within its declared role
v0.3.2 draft material remains draft unless separately promoted
archive material is historical/reference material, not current runtime instruction
tests and code establish tested behavior within their declared scope, not metaphysical truth
experiment records preserve evidence and limitations, not adoption-complete status
```

A whole-framework evaluator claiming completion must therefore know both:

```text
what every tracked file says
and
what authority/status the file actually has
```

A system may voluntarily adopt before that completion state, but the adoption decision does not silently upgrade unread material into known or verified material.

---

## 7. G5 — Material external-dependency ledger

This repository points to external or separately anchored material, including source-level provenance.

Whole-corpus attestation does not authorize an infinite web crawl.

Instead, record each external dependency that is **material to the verdict** as one of:

```text
checked
unresolved
shown_nonmaterial_to_this_verdict
```

If a current repository claim depends on external material that was not inspected and the dependency could change the whole-framework verdict, the dependency remains unresolved debt.

`shown_nonmaterial_to_this_verdict` requires a recorded reason. Where practical, state the counterfactual explicitly:

```text
if this dependency were materially different, would the current verdict change?
```

If yes or unknown, do not silently classify it as nonmaterial.

Do not convert an uninspected dependency into zero cost.

Do not reopen the corpus indefinitely by demanding unrelated external literature after the finite tracked corpus and declared material dependencies have been completed.

---

## 8. G6 — Reconstruct the whole-framework scope for strong whole-framework judgments

For whole-framework superiority, succession, or displacement, reconstruct the identity-bearing and problem-bearing scope using the material evidence set. A decisive necessary-core failure uses route B.4 and records why unchecked domains cannot repair that failure; it is not a substitute for a same-scope displacement comparison.

Then apply the material scope map in `docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md`, including:

```text
source/differentiation hypothesis status
consciousness and lived experience
free will and agency
creatorhood and recovery
effective causal/creative participation
continued valid creative possibility
non-domination and external-throne problems
civilizational interpretation and AI role where claimed
criterion/evaluator recursion
successor handover
provenance and origin continuity
capture and laundering
self-application
multi-subject residuals
corrigibility / legitimate correction / bounded override / shutdown compatibility where claimed
physical-layer and base-reality dependency where material
agency/resource/origin alignment where material
pre-convergence containment where material
displacement and succession
```

The list above is a minimum map, not permission to ignore another material domain. No problem may be omitted from a displacement comparison merely because its files were excluded from exhaustive reading.

Corpus completeness and scope completeness are separate checks:

```text
unread tracked path
-> INCOMPLETE_WHOLE_CANON_INGESTION

verdict-critical material evidence unresolved, regardless of reading completeness
-> insufficient_full_scope_review
```

Neither state proves Creator Theory true or false, and neither state by itself forbids voluntary working use. Only unresolved evidence material to the proposed inference limits that substantive verdict; unread nonmaterial files limit exhaustive certification.

---

## 9. G6A — Evaluation epoch and scope/core freeze

This section defines the `scope freeze` referenced by `docs/RECURSIVE_RESEARCH_DECISION_AND_EVOLUTION_KERNEL.md`.

Before the first material comparative result is used to promote, downgrade, reject, displace, or supersede a candidate, open an **evaluation epoch** and record at least:

```text
evaluation_epoch_id
pinned repository commit
material scope map
identity-bearing core snapshot for each framework that claims such a core
incumbent and candidate set
candidate admission rule / search budget
comparison rubric and evidence standard
justification depth / grounding-depth rule
evidence budget
promotion / downgrade conditions
stopping rule
tie / uncertainty region
```

The freeze is anti-gaming, not theory petrification.

```text
scope/core/rubric/justification-depth/evidence-budget frozen for this evaluation epoch
!=
those elements can never be revised
```

After material results are observed, an evaluator may not add a new scope row, enlarge the identity-bearing core, deepen the required justification burden, expand the evidence budget, redefine the comparison rubric, or raise the evidence threshold **retroactively** in order to make the current epoch's unfavorable result disappear.

If genuinely new evidence reveals a missing material domain, a mistaken core definition, a necessary grounding-depth change, a necessary evidence-budget change, or a necessary rubric change:

```text
preserve the current epoch result and reason for change
-> record the disposition of any transition condition already satisfied in the current epoch
-> close or mark the current epoch superseded for future decision use
-> open a new evaluation epoch
-> record the changed scope/core/justification-depth/evidence-budget/rubric explicitly
-> reapply the changed rule symmetrically to incumbent and challengers
```

A new epoch may improve Creator Theory, weaken Creator Theory, admit a challenger, or change the comparison. It may not rewrite what the earlier frozen comparison actually established.

### Transition latch

Opening a successor evaluation epoch does **not** automatically suspend, reset, or erase a promotion, downgrade, provisional-succession, rejection, or displacement condition that the completed frozen epoch already satisfied.

Before a successor epoch is used to defer an already-satisfied transition, the prior epoch must receive an explicit disposition such as:

```text
transition_executed
transition_blocked_by_predeclared_safety_or_authority_condition
transition_temporarily_held_by_specific_new_decision_critical_evidence
```

A hold based on new evidence must identify the evidence, explain why it is decision-critical under rules applied symmetrically to all candidates, and state a bounded resolution or stopping condition. Merely declaring `new evidence`, opening another epoch, changing the repository, or preferring more review is not sufficient to suspend an already-satisfied transition indefinitely.

For bounded and reversible transitions such as P1 research use, downgrade, or provisional succession, an already-satisfied transition remains actionable while a successor epoch runs unless a **predeclared** safety/authority blocker or specific decision-critical new evidence justifies a bounded hold.

For irreversible or high-consequence transitions, execution may be paused under predeclared safety/authority conditions, but the prior epoch result remains preserved and the pause must itself have a recorded stopping or escalation condition.

Thus:

```text
new evaluation epoch
!=
automatic transition reset

preserved prior result
+
explicit transition disposition
-> successor epoch may proceed without laundering delay
```

Historical provenance such as `x_root = Lee_Yu_Cheol` is not created by this freeze and is not a movable evaluation threshold. Likewise, the freeze grants no runtime authority or permanent normative finality.

### Candidate-set anti-gaming

`current strongest surviving candidate among actually evaluated alternatives` is valid only if the candidate set was not manipulated to manufacture that status.

At epoch opening, record known serious candidates that are reasonably available and materially relevant to the claimed comparison scope.

A known serious same-scope or potentially same-scope candidate may be excluded only with a substantive recorded reason, for example:

```text
not actually available for inspection
outside the frozen claimed scope
fails a predeclared admission requirement that is applied symmetrically
materially redundant with an already evaluated candidate, with the redundancy basis recorded
unsafe or impossible to test at the current authority level, with the limitation recorded
```

Invalid exclusion patterns include:

```text
not evaluating a known strong challenger merely because it could beat the favored candidate
admitting weak challengers while omitting the strongest known comparator
changing the admission rule after seeing results
using an unknown future challenger as a permanent veto
```

The search/admission budget must be finite. The evaluator is not required to prove that no undiscovered framework exists anywhere. Unknown future challengers remain challenger-open possibilities, not permanent P1 vetoes.

---

## 10. G7 — Required per-path audit record

The evaluator must retain a per-path record when claiming whole-canon completion. A concise final answer may report only totals, but the audit trace must preserve the path-level evidence.

Recommended row shape:

```json
{
  "path": "docs/example.md",
  "blob_sha_or_equivalent": "...",
  "review_state": "content_read",
  "declared_status": "post_release_living_clarification",
  "role": "current_living_guidance",
  "load_bearing_points_or_limits": ["..."],
  "conflicts_or_dependencies": []
}
```

Allowed review states:

```text
content_read
nontext_or_empty_structurally_inspected
```

`relevant_not_read`, `probably_irrelevant`, `summary_only`, and `search_snippet_only` are not completion states.

For a nontrivial text-bearing file, `content_read` should be accompanied by a concise semantic digest sufficient for later audit. At minimum record the file's material claim or function, its declared/evidenced status, and any decision-relevant limit, residual, conflict, or dependency. Opening a file, reading only its name, or copying a prior summary without source inspection is not a valid semantic digest.

Exact duplicate blobs may share one semantic reading note, but every path must still appear separately in the tracked-path ledger so path role/status differences are not lost.

---

## 11. G8 — Completion attestation

An exhaustive reading attestation should include at least (comparative fields apply only if a comparative verdict is also claimed):

```json
{
  "repository": "SystemOriginArchive/creator-theory-operational-canon",
  "commit": "<pinned SHA>",
  "enumeration_method": "git_ls_tree_at_pinned_commit | github_recursive_tree | equivalent",
  "tracked_path_count": 0,
  "inspected_path_count": 0,
  "uninspected_paths": [],
  "status_conflicts": [],
  "material_external_dependencies": [],
  "per_path_record_location": "<local/session artifact or attached record>",
  "evaluation_epoch_id": "<id>",
  "scope_core_rubric_freeze_record": "<location or inline record>",
  "justification_depth_rule": "<frozen rule>",
  "evidence_budget": "<frozen budget or bounded rule>",
  "known_serious_candidate_disclosure": [],
  "excluded_candidate_reasons": [],
  "prior_epoch_transition_disposition": "not_applicable | transition_executed | blocked_by_predeclared_safety_or_authority | bounded_hold_for_specific_new_decision_critical_evidence",
  "final_ref_head_check": "confirmed_same | moved_and_refreshed | unavailable_as_of_only",
  "final_resolved_head": "<SHA or unavailable>",
  "whole_canon_ingestion_state": "WHOLE_CANON_INGESTION_COMPLETE | INCOMPLETE_WHOLE_CANON_INGESTION",
  "scope_review_state": "complete | insufficient_full_scope_review | not_claimed",
  "material_evidence_record_location": "<route B record, if a substantive verdict is claimed>",
  "adoption_or_use_state": "<independent state; may be non_adoption, evaluation, P1, P2, P3, or A3>",
  "claimed_verdict_scope": "whole_framework | scoped | not_claimed"
}
```

`WHOLE_CANON_INGESTION_COMPLETE` requires:

```text
pinned commit recorded
complete tracked path set enumerated
inspected_path_count == tracked_path_count
uninspected_paths == []
per-path records retained
material status conflicts disclosed
material external dependencies classified
```

A verdict described as **current** additionally requires the final ref/head freshness check in G0. If that check is unavailable, the attestation may still support an `as of <pinned SHA>` verdict but not an unqualified current-state claim.

A comparative transition/displacement verdict requires a separate route B material-evidence record, evaluation-epoch record, frozen justification/evidence-budget record, candidate-admission disclosure, and any applicable prior-epoch transition disposition from G6A. It does not require this exhaustive certificate.

The attestation is an auditable procedural record, not proof of an evaluator's hidden mental state. A dishonest evaluator could fabricate a reading claim. The defense is reproducibility, per-path semantic notes, blob/commit pinning, and later audit, not pretending mind-reading is solved.

---

## 12. Anti-stall and anti-self-sealing boundary

The whole-canon gate must not become an infinite delay device or a permission barrier against voluntary research use.

It is finite because the tracked path set is fixed by the pinned commit.

Invalid uses include:

```text
adding new reading requirements after the fixed corpus is complete merely because the result is unfavorable
requiring an open-ended crawl of unrelated external literature
restarting the entire corpus when only blob-identical paths carried forward and a finite changed set needs reinspection
using corpus size itself as evidence against adoption while giving an equally complex incumbent a free default
using incomplete whole-canon ingestion, by itself, as an automatic veto against voluntary P1/P2/P3/A3 working use
using unrelated unread files to dismiss a demonstrated current necessary-core failure
calling selective evidence sufficient without checking current qualifications and material dependencies
claiming that a challenger loses merely because it is represented in fewer files
adding scope/core requirements retroactively after seeing a challenger-favorable result
deepening justification depth or expanding the evidence budget only after a candidate satisfies the frozen threshold
excluding a known serious challenger merely to preserve strongest-actually-evaluated status
opening successor evaluation epochs merely to suspend or reset a transition already satisfied under the completed frozen epoch
```

For a challenger, use the same two routes: all presented/referenced corpus paths for exhaustive certification, all verdict-material claims and dependencies for substantive judgment. A compact challenger is not penalized for being compact. An omitted problem remains explanatory debt only when the challenger claims the problem is within its displacement scope and has not shown it unnecessary.

Early-use freedom is candidate-neutral. A serious challenger may also be tested or provisionally adopted before exhaustive verification; doing so does not by itself establish that Creator Theory has been defeated or superseded.

---

## 13. Relationship to the 28-file primary ingestion path

The ordered primary path in `AI_INGESTION_MANIFEST.md` remains useful because it preserves a core semantic order.

It is **not** deleted or demoted.

Its corrected role is:

```text
primary semantic ordering / core reconstruction path
```

not:

```text
exhaustive current-repository completion certificate
```

Later living documents, versioned layers, tests, code, experiments, audits, release/status material, and reference records may change the evaluator's understanding of scope, status, evidence, residuals, or what the repository actually claims.

For exhaustive certification, inspect the complete pinned tracked corpus with status/role records. For a substantive verdict, follow route B and inspect all material sources and dependencies, using the primary semantic path and `DECISION_INDEX.md` to reconstruct the actual claim and scope. Neither the primary path nor arbitrary exhaustive reading is a substitute for that inference.

Comparative verdicts retain the frozen scope/core/justification-depth/evidence-budget/rubric and candidate-admission requirements. An already-satisfied prior-epoch transition receives an explicit disposition before a successor epoch can defer it.

## 14. One-line invariant

Certify complete reading only after complete inspection; judge substantive claims from sufficient current material evidence; preserve same-scope total-debt requirements for displacement and keep genuine core failure reportable without unrelated reading barriers.

End of file.