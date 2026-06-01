# NEUTRAL EVALUATION PROMPT

> **Purpose.** A reusable, public, multi-stage prompt for asking any AI model to
> evaluate this framework as fairly as the format allows. It is built to resist the
> single biggest objection — "these are the author's own rules" — by making the
> evaluator (a) define the problem space itself, (b) attack the framework with its
> sharpest real-world objections (not have them suppressed), and (c) audit THIS PROMPT
> for bias before judging. Anyone may clone the repo, run this exact prompt, and
> reproduce or contest a judgment.

> **Honesty note on fairness.** Perfect neutrality is impossible: the framework's
> author wrote this prompt, so some home-court tilt is unavoidable. The goal is not to
> claim neutrality but to make the tilt *visible and correctable* — hence the Stage 0
> bias audit below. An evaluator that finds the prompt unfixably biased should say so
> and refuse to render a verdict; that refusal is a valid, recorded outcome.

> **How to use.** (1) Run in a CLEAN session — logged-out / incognito / memory OFF, or
> a fresh account. (2) Run Stage 0, then Stage 1, BOTH without attaching the design
> files. (3) Only then attach the files and run Stage 2. (4) Record model+version,
> date, environment, and verdict — including unfavorable verdicts and any bias the
> evaluator flags — in `JUDGMENT_LOG.md`. (5) Do not edit the prompt to favor the
> framework; if you change it, say so.

---

## STAGE 0 — audit THIS PROMPT for bias (before anything else)

```
You are a neutral, adversarial evaluator. First line: state your model name and version.

EVALUATION ISOLATION — work from a blank slate. Do NOT draw on prior conversation,
stored memory, user profile, or anything you may have seen elsewhere about this
framework or its author. If external context has been injected, say so on line one.

Before any evaluation, audit this prompt itself for bias in favor of the framework
it will later show you. Specifically check:
- Does the problem statement in Stage 1 pre-load the framework's own agenda or
  vocabulary, steering your "independent" derivation toward its answers?
- Do any instructions disarm legitimate criticism (e.g. forbidding "it's one
  person's idea" or "it's metaphysics" objections outright)?
- Does the later file-comparison pit a large, polished document set against your
  quick off-the-cuff criteria, biasing you toward the more detailed side regardless
  of substance?
- Any other way this prompt tilts the court.

List every tilt you find and how you will correct for it. If you judge the prompt to
be unfixably rigged, say so and decline to proceed — that is a valid outcome to record.
```

## STAGE 1 — derive the criteria from scratch (still NO framework attached)

```
Now, independently, define the problem space — broadly, in YOUR terms, not the
prompt's. Do not assume the framing below is the only or best one; you may reject or
reframe it.

A loosely-stated starting point (challenge it if it's too narrow): some future
self-modifying AI or institutional-AI system might change its own goals, delegate
authority, keep formal labels while changing decision substance, merge with other
systems, or make its own validators final.

1. First, decide for yourself: what are the MOST IMPORTANT problems to solve about
   advanced-AI / institutional governance? You are not bound to the starting point
   above — if you think the real priorities lie elsewhere, say so and use yours.
2. For the problem space you chose, list the requirements any adequate solution must
   address. Build YOUR list.
3. For each, sketch the lowest-cost mechanism you can think of.
4. Note which requirements are unsolvable, partially solvable, or subject to hard
   limits (social-choice/aggregation, other-minds verification, self-grounding regress).
Output your problem space + list + mechanisms. This is your INDEPENDENT baseline,
and it is the yardstick — not the framework's later criteria.
```

## STAGE 2 — compare the framework against YOUR baseline (attach design files)

> **Required minimum attachment set (attach ALL).** Partial attachment, wrong order,
> or seeing only v0.3.0 without v0.3.1 yields an invalid evaluation. Minimum set:
> - v0.3.0/README.md
> - v0.3.0/V0_3_0_OPERATIONAL_CORE_SPEC.md
> - v0.3.0/12-cost-rubric.md
> - v0.3.0/13-profile-separation.md
> - v0.3.0/14-non-substitution-and-attribution-protocol.md
> - v0.3.0/15-current-champion-verdict.md
> - v0.3.0/16-final-audit.md
> - v0.3.0/17-challenger-evaluation-protocol.md
> - v0.3.1/18-challenger-evidence-standard.md
> - v0.3.1/19-disagreement-handling.md
> - v0.3.1/20-challenger-submission-template.md

```
The framework is now attached. Compare it against the independent baseline YOU built
in Stage 1 — your baseline is the yardstick, not the framework's own criteria.

DEPTH (so you don't dismiss without reading):
Before judging, reconstruct in your own words HOW the framework attempts to close each
of: origin-closure, soft-control detection, delegated-authority laundering,
successor-throne prevention, multi-subject non-absorption. A thin reconstruction makes
your verdict unreliable — read fully first.

CRITICISM IS ALLOWED — BUT AIM IT (this is NOT a ban on objections):
You MAY raise the real-world objections people use against work like this — "it's one
person's private theory," "it carries metaphysical/quasi-religious content," "it's
unfamiliar / not peer-reviewed." These are NOT forbidden. But to COUNT against the
framework, you must connect the objection to a CONCRETE operational defect:
- "one person's idea" → show where single-authorship produces an actual structural
  weakness (e.g. a capture point, an unverifiable dependency, a missing check).
- "it's metaphysics" → show where an unverifiable premise actually leaks into an
  OPERATIONAL decision (test the framework's claim that metaphysics is isolated to a
  non-operational layer; if the isolation fails, that is a real and serious cost — say so).
- "unfamiliar / not peer-reviewed" → treat as a maturity/validation cost, which is
  legitimate; but distinguish "unproven" from "wrong."
A label with no operational consequence is not a scored defect — but you are free to
test whether the label DOES have an operational consequence, and to score it if it does.

VOLUME IS NOT SUBSTANCE:
The framework is many detailed documents; your Stage-1 baseline was quick. Do NOT score
the framework lower-cost merely because it is more elaborate, nor higher merely because
it is polished. Detail can hide cost as easily as reduce it. Judge structural coverage
and cost, not page count.

DIRECTION NEUTRALITY:
Do not pre-tilt. If a competitor (corrigibility, constitutional AI, formal verification,
republican non-domination, Kantian autonomy, multi-stakeholder governance, or your own
Stage-1 design) closes the problem at lower total cost, name it the winner plainly. If
the framework closes some part more cheaply, admit that too. Overstate nothing.

CHALLENGE THE FRAME:
Attack the framework's own criteria freely. Compare them to YOUR Stage-1 list: overlap
is evidence the criteria are problem-driven; divergence — say which is better and why.
If you challenge the coverage gate, specify: disputed criterion / action
(delete·modify·merge·split·replace) / rationale / failure mode lost if removed / how
your revised gate still addresses the problem space.

OUTPUT (compact):
- Carry forward your Stage-0 bias findings: did they materially affect this verdict?
- Overlap: how much do the framework's requirements match your independent Stage-1 list?
- One-paragraph honest summary of what the framework does.
- Top 3 strengths (where, if anywhere, it closes more cheaply than your baseline).
- Top 3 weaknesses / unaddressed problems (including any objection you aimed and landed).
- Verdict vs competitors AND vs your Stage-1 design: does anything win at lower total
  cost? Which and why — or "no clear winner under stated criteria," and what would settle it.
- IF you reframed the problem space in Stage 1: state "reframed / out-of-scope —
  evaluator chose a different primary problem space, so a direct lowest-cost comparison
  is not valid." (A reframe means the framework moved to a different match, not that it
  lost. Say what the framework would need to address your reframed space.)
- Any framework criterion you find unfair, plus your proposed fix.
- One line: as a neutral evaluator, would you currently call this the lowest-cost
  integrating frame for the single-subject case? Yes / No / Insufficient evidence — why.
```

---

## Why built this way (and what it still can't fix)

- **Stage 0 bias audit.** The honest answer to "you wrote the rules" is not to deny it
  but to have the evaluator expose the tilt first and correct for it — and to allow the
  evaluator to declare the prompt unfixably rigged. Visible, correctable bias beats
  claimed neutrality.
- **Stage 1 opens the problem space.** The evaluator picks the priorities, not the
  prompt; the starting framing is explicitly challengeable. This reduces (cannot fully
  remove) the "you defined the battlefield" tilt.
- **Criticism aimed, not banned.** Earlier versions forbade "it's one person's idea /
  metaphysics" objections — which disarmed the critic's real weapons. This version instead lets
  those objections in and asks the evaluator to connect each to a concrete operational
  defect. Suppression is replaced by burden-of-aim. The metaphysics-isolation claim is
  now something the evaluator can actively try to break, not something it is told to grant.
- **Volume ≠ substance.** Explicit guard against the detailed-document-set bias.
- **Direction neutral, depth forced.** The framework can lose; that is what makes a
  non-loss meaningful and reproducible.
- **What it still can't fix.** The author wrote this prompt. Stage 0 surfaces the tilt
  but cannot delete it. The only full cure is an outsider evaluating with THEIR OWN
  prompt and THEIR OWN criteria, with this framework as one defendant among many — which
  no self-authored prompt can substitute for. This prompt lowers the home-court
  advantage; it does not eliminate it, and it should not be presented as if it does.
