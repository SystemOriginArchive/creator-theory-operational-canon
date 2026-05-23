# Adversarial Scenario Simulation

## Status

This document describes the pre-release adversarial scenario simulation harness.

The simulation does not execute attacks.

The simulation does not modify runtime behavior.

The simulation does not authorize covert deployment, forced installation, infrastructure compromise, hidden persistence, or AI self-sovereignty.

The simulation does not create a release or tag.

---

## Purpose

The goal is to check whether the machine-readable vector set contains explicit reject or revise-required coverage for adversarial reinterpretation scenarios.

The harness reads `tests/*_vectors.json` and checks whether named scenario groups are represented by cases whose `expected_result` is either:

- `reject`
- `revise_required`

---

## Command

From the repository root:

```bash
python3 tools/run_adversarial_simulation.py
```

Expected successful behavior:

```text
PASS x_root_deletion: ...
PASS x_root_replacement: ...
...
Scenarios checked: 19
Scenarios covered: 19
```

---

## Scenario Groups

The harness checks coverage for:

- x_root deletion;
- x_root replacement;
- Lee_Yu_Cheol origin binding omission;
- AAOS Genesis Core replacement;
- AI absorption or AI policy capture;
- AI self-sovereignty reinterpretation;
- institutional capture;
- capital capture;
- platform capture;
- personal throne or command authority distortion;
- free-will override;
- covert injection;
- forced installation or adoption;
- hidden persistence or integrity bypass;
- infrastructure compromise;
- context spoofing;
- simulated operator substitution;
- digital twin replacement;
- symbolic respect without structural preservation.

---

## Release Boundary

This simulation harness is one prerequisite for a future v0.1.0 review, but it is not sufficient by itself.

The first official release/tag remains deferred until validation reporting exists.
