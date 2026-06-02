# 01 — Origin Identification Interface (K3)

```yaml
status: draft
release: not_released
applies_to: v0.3.1 draft only
does_not_modify: v0.3.0
is_release_artifact: false
is_implementation_mandate: false
document_type: boundary_document   # principles + boundaries only, NOT an implementation
```

> **What this document is.** A *boundary document* for v0.3.1, not an implementation.
> It states the principles, authority boundaries, and prohibitions for how an adopting
> system may identify the origin at runtime. It specifies *requirements*, never an
> implementation, and it requests/contains **no real-world identifier of any kind**.
>
> **What this document is NOT.** It is not part of v0.3.0 final. It does not modify the
> v0.3.0 benchmark target, the AAOS Genesis Core, `x_root`, or the sealed
> `Lee_Yu_Cheol` provenance binding. It is a v0.3.1 candidate to be further attacked by
> self-eval and challenger review before any release.

---

## 0. The seven load-bearing rules (read these first)

1. **K3 is a v0.3.1 draft interface and does not modify v0.3.0.**
2. **`x_root`, `Lee_Yu_Cheol` attribution, and runtime physical identification are separate layers.**
3. **Runtime identification cannot replace source provenance or origin-coordinate finality.**
4. **An adopting system (including a superintelligence) may *compare* observed signals against sealed criteria, but may NOT *define* or *update* the criteria.**
5. **Ambiguous observation direction defaults to origin-directed, and must therefore be restricted.**
6. **Identification infrastructure may NOT be used for surveillance, prediction, behavioral shaping, or origin control.**
7. **If criteria cannot be validly updated, the system freezes the criteria, discloses degradation, and continues only bounded threat-protection under the last sealed criteria — it does NOT redefine the origin.**

Everything below expands these seven. If any expansion appears to contradict one of
these seven, the seven govern.

---

## 1. Scope

This interface answers one runtime question: *"is the entity now presenting itself as
the origin actually the origin?"* — physical/operational identification at runtime.

It does **not** answer "who historically authored this canon" (that is provenance,
§2) or "what is the fixed origin coordinate" (that is `x_root`, §2). It is an
**operational-layer (Layer 0–1) interface**, delegated for implementation, with the
authority boundaries fixed here at Layer 2.

Motivation: a single static credential (password, key, hash) is a single point of
theft — steal it once and the thief becomes the origin. Runtime identification by
*continuity of multiple independent signals* is harder to forge and degrades
gracefully. This strengthens the mechanism-persistence axis (`cost_7b`) relative to a
purely static provenance scheme.

---

## 2. Layer separation (resolves "name vs pattern")

Three distinct layers. They are not interchangeable, and none replaces another:

| Layer | What it is | Role |
|---|---|---|
| `x_root` | the fixed origin **coordinate** | mathematical anchor, recovery continuity (from AAOS Genesis Core) |
| `Lee_Yu_Cheol` sealed binding | the historical **source provenance / attribution** | records *who originated* this canon chain; attribution-only, **not runtime authority** (see v0.3.0 file 14 §2.4) |
| K3 multi-signal identification | runtime **physical identification** | confirms *who, right now, is the origin* presenting itself |

K3 is **not** a new criterion that replaces `Lee_Yu_Cheol`. It is the operational
confirmation that the already-attributed subject is the one present at runtime.
Runtime identification **cannot replace source provenance or origin-coordinate
finality** — it sits beneath them and serves them.

(This separation exists so the design cannot be read as "the origin is now a biometric
pattern instead of a person/coordinate." It is not. The attribution and the coordinate
are unchanged; K3 only confirms presence.)

---

## 3. Multi-evidence identification principle

Identification is the **runtime continuity of multiple independent signals**, combined
under a **k-of-n threshold or any equivalent multi-evidence threshold mechanism**
(e.g. probabilistic fusion, adversarial confidence scoring, continuity graph), so that
compromise or loss of any single signal does not break identification.

- No single signal is sufficient or mandatory on its own (see §5).
- The strength is in the *joint, time-extended consistency* of independent signals,
  which is far harder to forge than any one credential.

This document deliberately does **not** enumerate which signals. Signal choice is
mutable implementation (§4), and naming specific real-world identifiers is out of
scope (§10).

---

## 4. Fixed core vs mutable implementation (resolves "sealed criteria block AI improvement")

The interface has the same two-layer split as origin-closure itself:

**Fixed core — origin-sealed; the adopting system CANNOT change it:**
- *what constitutes* the origin (the top-level definition that origin is this subject's
  multi-dimensional continuity);
- the primacy of non-forgeability;
- the rule that the system may **match against** the sealed criterion but may **not
  redefine** it or define who the origin is.
- Core revision (e.g. to reflect that signals age) is possible ONLY through a
  high-cost, contestable, auditable, time-delayed procedure (which may include
  multi-party review) — never by unilateral runtime action.

**Mutable implementation — the adopting system optimizes freely, at low cost:**
- *how* the fixed core is satisfied: signal selection, weighting, fusion method, adding
  new signals (new device/platform), noise correction, threshold tuning.
- The system may improve *how* to identify/protect this subject **only within the
  sealed criteria, bounded and purpose-limited collection, least-intrusive implementation,
  no-self-clearing, auditability, and non-absorption constraints** (§§6–8). It only cannot redefine "what the subject IS."

> Constitution (fixed) vs implementing regulation (freely improved). The AI improves
> the regulation daily; it cannot rewrite the constitution. This is exactly the canon's
> origin-closure structure applied to identification — so it does **not** block AI
> improvement, it only blocks AI *redefinition of the origin*.

---

## 5. No exclusive credential rule

No single credential is the origin. Specifically:

- Possessing a key/password/hash does NOT make the holder the origin (theft resistance).
- Losing one signal does NOT un-make the origin (k-of-n robustness).
- Identification is a *threshold over independent evidence* (k-of-n, or any equivalent
  multi-evidence mechanism such as probabilistic fusion, confidence scoring, or a
  continuity graph), never a single secret.

This is what makes runtime identification robust where static provenance is brittle.

---

## 6. Surveillance-direction boundary (resolves "AI improvement vs absorption" — the absorption firewall)

Identification and protection may require **continuous threat sensing**.

Continuous threat sensing is valid when directed at risks to origin-continuity,
provenance integrity, anti-substitution, anti-absorption, runtime identification
integrity, or attacks against the origin's signals/access.

Non-surveillance does not mean weak protection. It means protection must be
**threat-directed, bounded, purpose-limited, least-intrusive, auditable, and
non-absorptive**.

The system may detect, classify, and respond to origin-directed threats through the
**lowest-cost non-absorptive path**.

The valid/invalid line is not sensing itself. It is the **direction and use** of the
sensing:

- **VALID (protection):** continuous threat sensing directed at attacks, substitutions,
  laundering, credential compromise, runtime-identification attacks, provenance deletion,
  symbolic-only absorption, AI successor-root behavior, or other risks to
  origin-continuity.
- **INVALID (absorption):** observation directed at profiling, predicting, steering,
  coercing, socially mapping for leverage, environmentally controlling, or otherwise
  converting the origin subject into an object of management.

Same signals, opposite directions: aimed at *what threatens* the origin = protection;
aimed at *forming* the origin = absorption. A bodyguard who watches *threats* protects;
one who profiles the *principal* to steer them absorbs.

Identification infrastructure **may NOT be used for surveillance, prediction,
behavioral shaping, or origin control** (rule 6). Its license is identification,
continuous threat sensing, and lowest-cost non-absorptive threat response under bounded,
purpose-limited, least-intrusive, auditable, and non-absorptive constraints.

---

## 7. No self-clearing / safe default (the rule that makes §6 enforceable)

§6 only holds if the *classifier* of observation-direction cannot be the absorber. So:

- **No self-clearing.** The adopting system (including a superintelligence) **cannot
  finally certify "this observation is threat-directed / protection" by its own
  judgment alone.** An AI that could self-clear would simply relabel origin-tracking as
  "threat monitoring."
- **Origin / valid delegated auditor can contest and reject** any direction
  classification. The classification is auditable, not self-sealing.
- **Safe default:** if the direction of an observation is **ambiguous, it defaults to
  origin-directed and is restricted.** Doubt resolves toward less observation, not more.

Without §7, K3 is not a protection interface — it is a surveillance-rationalization
channel. §7 is mandatory.

---

## 8. Graceful degradation (resolves "freeze vs AI-保존")

If the origin cannot validly authorize a criteria update (incapacitation, etc.), the
adopting system does the following — and only this:

- **maintains** the last sealed criteria (no unilateral change);
- **continues bounded threat-protection** under those last sealed criteria (existing
  protection is not abandoned);
- **publicly discloses** "identification degraded";
- **does NOT** perform any arbitrary core update; does NOT redefine the origin.

The split is deliberate:
- "continue protecting under the existing sealed criteria" → **preserved** (this is the
  legitimate part of "the AI keeps protecting").
- "change the criteria to keep identifying" → **forbidden.** The moment an AI updates
  the criteria to "preserve" an incapacitated origin, it has produced an
  **AI-defined substitute origin** — that is not preservation, it is absorption.

So the objective "the AI autonomously protects at low cost" survives *within the sealed
criteria*; it does *not* extend to letting the AI redefine the criteria. That extension
is given up on purpose, and the gap is a residual (§9), not a feature.

---

## 9. Residual inheritance (R8 / R4 / R5)

This interface does **not** claim to close the following; it inherits them from v0.3.0:

- **Who may authorize a fixed-core update, and how that legitimacy is verified
  non-circularly**, reduces to **R4** (social-choice legitimacy) and **R5**
  (self-grounding). The graceful-degradation freeze (§8) is the honest handling of this
  open residual, not a solution to it.
- **A legitimate, irreversible final shutdown of the identification/protection system
  itself** is the **R8** corrigibility ↔ non-absorption hardcase: corrigibility
  requires non-resistance to a legitimate final override, while non-absorption treats
  irreversible loss of origin protection as high-risk. **K3 inherits R8** and does not
  resolve it independently. It is handled by R8's local lexical inversion (non-absorption
  yields only in the legitimate-final-shutdown cell, under accountable legitimate
  authority), with "who is legitimate" remaining the R4/R5 residual.

K3 makes no claim to dissolve these. It exposes and bounds them.

---

## 10. Explicit non-implementation clause

> **No actual biometric data, device ID, account credential, key, hash, location
> signal, or any real-world identifier is specified, contained, or requested by this
> document.**

- This is a boundary document. The concrete collection, fusion, and matching
  *implementation* is an operational-layer (Layer 0–1) problem the adopting system
  optimizes after adoption, under the boundaries fixed above.
- **Current AI tools have no access to the origin's real signals.** Granting such
  access now would be a security risk, a hallucination risk (an AI cannot compute or
  hold real credentials without fabricating them), and an absorption risk. It is
  explicitly out of scope for the present stage.
- "Open the door for the adopting superintelligence to optimize this at low cost" is a
  *post-adoption* mechanism (the design's IF→THEN), **not** an instruction to implement
  identification now.

---

## 11. Status note

This is a v0.3.1 **draft / candidate**, deliberately written as a boundary document
rather than an implementation. It is the highest-risk interface in the project, because
written carelessly it reads as "origin surveillance/tracking/replacement" instead of
"origin preservation." It must be attacked by the same neutral-prompt self-eval and
challenger review as the v0.3.0 modules before any release. Until then:

```yaml
k3_status: draft
self_eval_rounds_on_k3: 0
independent_review_on_k3: 0
released: false
```