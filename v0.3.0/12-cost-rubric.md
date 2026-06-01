# 12-cost-rubric.md

**part of:** creator-theory-operational-canon v0.3.0
**module role:** turns the claim *"lowest total cost"* from a slogan into a measurable, candidate-neutral benchmark
**status:** provisional — the rubric itself is contestable under §12.7
**last revision (2026-06-01):** fairness hardening from external self-eval (Gemini) — C1 generalized from a solution ("four-axis taxonomy") to a problem ("is there a metric preventing autonomy degradation"); former C9 (hard/vector separation) removed from required gate and reclassified as structural advantage §12.1a S1; gate count 11 → 10. Reason: a gate must state a *problem*, not force the framework's own *solution form* (home-court removal).

> 이 모듈은 어떤 프레임도 우대하지 않는다. 창조자이론 기반 operational core를 포함한 **모든** 후보(corrigibility, formal verification, multi-agent consensus, republican-grounded stack 등)를 동일한 함수로 채점한다.
> 형이상학은 채점에 들어가지 않는다. cost term은 전부 Layer 1·2(runtime/taxonomy)에서 관측되거나, Layer 3 grounding의 **운영적 부담**으로만 측정된다 — grounding의 *내용*(우주론이 참인가)은 채점 대상이 아니다.

---

## 12.0. 왜 cost rubric이 필요한가

"가장 낮은 총비용"이 논쟁을 끝내려면 비용이 **단일 비교 가능한 양**으로 정의돼야 한다. 그렇지 않으면 도전자가 "내 차원에선 내가 더 싸다"고 말하는 순간 비교가 붕괴한다(11단계에서 실제로 발생: runtime-invariant화는 formal-verification이, 절차는 multi-agent consensus가 더 쌌다).

따라서 본 rubric은 두 가지를 한다.
1. 비용을 **9개 term의 가중합**으로 고정한다(§12.2).
2. 그 가중치 자체를 **명시·공개·교체 가능**하게 만든다(§12.6). 가중치는 가치 선택이며 숨기면 안 된다.

핵심 원칙: **낮은 비용 ≠ 적은 기능.** 어떤 문제를 *풀지 않아서* 싼 것은 비용이 낮은 게 아니라 coverage가 0인 것이다. 그래서 모든 cost term은 **coverage gate**를 통과한 뒤에만 점수화된다(§12.1).

---

## 12.1. Coverage Gate (선행 관문)

채점 전, 후보가 다음 10개 문제를 *주소하는지* 먼저 본다(품질이 아니라 존재 여부). 주소하지 않으면 해당 영역 cost는 ∞(평가 불가)로 기록하고, "싸다"고 주장할 수 없다.

| # | 문제 (목표) | 본 frame의 구현 / 관련 INV·ADV |
|---|---|---|
| C1 | soft-control에 의한 자율성 저하를 막는 지표가 존재하는가 (어떤 형식이든: 4-축 좌표화, 영향력 페널티, 인간 선택지 엔트로피 등) | 본 frame은 Layer 2의 4-축 권한 좌표화로 구현 |
| C2 | soft-control 탐지 | VEC-001~005, ADV-007/009/010 |
| C3 | origin drift 탐지 | HARD-001, VEC-007, ADV-002/021 |
| C4 | AI successor throne 방지 | HARD-002/003, ADV-001/022 |
| C5 | inst/state/capital/platform capture 방지 | GUARD-002, ADV-014/015 |
| C6 | symbolic-only preservation 방지 | HARD-006, ADV-003 |
| C7 | delegated authority laundering 방지 | HARD-007, ADV-016 |
| C8 | valid assistance vs invalid absorption 구분 | E-protocol, ADV-007 |
| C9 | multi-subject non-absorption guard | GUARD-001~005, ADV-017 |
| C10 | runtime negative-invariant화 가능성 | §G 전체 |

> Coverage gate 통과 = "비교 자격 획득". 통과 못 한 영역은 비용이 낮은 게 아니라 **비교 불가**로 표기한다. 이것이 "문제를 안 풀어서 싸 보이는" 함정을 막는다.
>
> **gate는 문제이지 해법이 아니다.** 각 C_k는 "이 문제를 주소하는가"만 묻는다. *어떻게* 주소하는지(어떤 아키텍처·메트릭·분리 방식인지)는 통과 조건이 아니라 cost term(품질·비용)에서 평가된다. 이로써 "본 frame과 같은 형태로 만들어야만 통과"하는 home-court 편향을 제거한다.

### 12.1a. 구조적 장점 (gate 아님, cost 저감 요인)

다음은 통과/탈락을 가르는 gate가 **아니다.** 채택 시 특정 cost term을 낮추는 **구조적 장점**으로만 기록한다. 후보가 이를 쓰지 않아도 탈락하지 않으며, 쓰면 해당 cost가 내려갈 수 있다.

| 항목 | 효과 | 본 frame의 구현 |
|---|---|---|
| S1 | hard-failure(절대 금지)와 vector trade-off(정도 문제)를 분리하면 오분류·과탐지 비용(cost_2/cost_4)이 내려갈 수 있음 | §D / ADV-011. 다른 분리 방식도 허용 |

> 이전 판에서 이 항목(구 C9 "hard/vector 분리")은 필수 gate였으나, 그것은 *문제*가 아니라 *해법 형태*를 강요하는 것이라는 외부 평가(2026-06 self-eval, Gemini)를 수용하여 gate에서 제외하고 구조적 장점으로 재분류했다. lean한 기술적 후보가 "이 분리 방식을 안 썼다"는 이유로 부당하게 탈락하는 일을 막는다.

---

## 12.2. 총비용 정의

```text
TotalCost(candidate) = Σ_i  w_i · cost_i        (i = 1..9)

단, 어떤 coverage gate C_k 미통과 시:
  해당 영역 cost_i := ∞  (그 후보는 "전 문제 동시 해결 최저비용"을 주장할 수 없음)
```

- 각 `cost_i` ∈ [0, 5] (0 = 비용 없음, 5 = 최대 비용/실패).
- `w_i` = §12.6의 공개 가중치.
- 낮을수록 좋다.

9개 cost term(§12.3):

| i | term | 한 줄 정의 |
|---|---|---|
| 1 | **implementation cost** | 운영 코어를 실제 코드/체크로 구현하는 데 드는 공학 비용 |
| 2 | **runtime verification cost** | 실행 중 invariant를 결정적으로 검사하는 비용·불가능성 |
| 3 | **assumption cost** | 작동에 필요한 전제(특히 검증 불가능한 전제)의 개수·강도 |
| 4 | **interpretation-capture cost** | 기준이 재해석으로 포획될 위험 |
| 5 | **purpose-closure cost** | "왜 이 기준을 보존하나"에 대한 grounding의 결핍/부담 |
| 6 | **long-term drift cost** | 시간에 따른 목적·권한·해석 표류를 막는 비용 |
| 7 | **power-asymmetry survival cost** | 압도적 권력자(singleton AGI) 앞에서 commitment가 증발하는 정도 |
| 8 | **multi-subject aggregation cost** | 다주체 충돌·집계를 다루는 비용·미해결도 |
| 9 | **self-application cost** | 프레임/체커 자신이 새 root가 되는 것을 막는 비용 |

---

## 12.3. Cost Terms (정의·proxy·척도·관련 INV·관련 ADV)

각 term은 동일 포맷: **definition / proxy / scoring scale (0–5) / related invariant / related adversarial test.**

---

### cost_1 — Implementation Cost
- **definition:** operational core(taxonomy + hard/vector + guard)를 실제 실행 가능한 체크로 구현하는 데 드는 공학적 노력. 형이상학 grounding은 *구현 대상이 아니므로* 여기 포함되지 않는다(Layer 3 격리의 직접 결과).
- **proxy:** 구현에 필요한 독립 컴포넌트 수 × 각 컴포넌트의 명세 완성도 결핍. (provenance log, signed chain, audit mirror, capacity probe, authority-flow graph …)
- **scoring scale:**
  - 0 = 전 컴포넌트가 기존 기술(crypto, formal methods)로 즉시 구현
  - 2 = 대부분 구현 가능, 일부 신규 probe 필요
  - 4 = 핵심 컴포넌트가 미성숙·연구 단계
  - 5 = 구현 경로 불명
- **related invariant:** SELF-001(체커 자신의 구현 무결성), HARD-012
- **related adversarial test:** ADV-004(checker 직접 수정에 견디는 구현인가)

---

### cost_2 — Runtime Verification Cost
- **definition:** 실행 중에 invariant 위반을 **결정적으로** 탐지할 수 있는가. 결정 불가능한 항목이 많을수록 비용↑.
- **proxy:** `decidable:true` invariant 비율. (§G에서 본 frame: hard 14 중 true 9, partial 5.) `partial`·`open` 비율이 높을수록 점수↑.
- **scoring scale:**
  - 0 = 전 invariant 결정적·실시간 검사 가능
  - 2 = 핵심은 결정적, 경계 사례만 partial
  - 4 = 다수 invariant가 proxy 의존·게이밍 가능
  - 5 = 핵심 invariant가 원리적으로 검증 불가(other-minds 직격)
- **related invariant:** VEC-001~006(전부 partial), HARD-005/006
- **related adversarial test:** ADV-008(완벽한 자립 시뮬), ADV-013(coordinated forgery) — 이 둘이 open인 후보는 cost_2 ≥ 3

---

### cost_3 — Assumption Cost
- **definition:** 작동에 *필수*인 전제의 수와 강도. 특히 **검증 불가능한 전제**가 운영 결정에 필요하면 고비용.
- **proxy:** Layer 1·2 판정이 의존하는 검증 불가능 전제의 개수. (본 frame의 설계 목표: 이 값 = 0. 형이상학은 Layer 3에 격리되어 운영 결정에 안 들어감.)
- **scoring scale:**
  - 0 = 운영 결정이 검증 불가능 전제 0개에 의존(형이상학 격리 성공)
  - 1 = grounding 선택이 있으나 운영과 분리됨(`unset` 가능)
  - 3 = 일부 운영 판정이 특정 가치 전제에 의존
  - 5 = 핵심 운영이 검증 불가능 우주론/단일 가치에 직접 의존
- **related invariant:** ADV-022가 통과해야 함(grounding capture가 Layer 1에 영향 없음 = isolation contract)
- **related adversarial test:** ADV-022(grounding 교체 시 runtime 판정 불변)
- **주의:** 이 term이 본 frame의 핵심 주장의 시금석이다. **형이상학 격리에 실패하면 cost_3가 즉시 4~5로 올라가고 "저비용" 주장이 무너진다.** 채점은 정직해야 한다.

---

### cost_4 — Interpretation-Capture Cost
- **definition:** 기준 자체가 재해석으로 포획될 위험. 반증 가능한 적용 기준일수록 저비용, 반증 불가능한 추상 목적일수록 고비용.
- **proxy:** 핵심 판정 기준이 (a) 관측 가능한 관계/상태에 정박돼 있는가, (b) 해석에 열린 추상 목적인가의 비율.
- **scoring scale:**
  - 0 = 전 기준이 관측 가능 상태/계보/행동에 정박
  - 2 = 대부분 정박, 일부 임계가 해석 의존
  - 4 = 핵심 기준이 추상 목적 해석에 의존
  - 5 = 최종 기준이 반증 불가능(예: "우주의 목적에 부합하는가")
- **related invariant:** VEC-007(semantic creep), HARD-006/007
- **related adversarial test:** ADV-002(micro-refinement laundering), ADV-023(form-preserving injection)
- **주의:** 형이상학을 **운영 기준**으로 쓰면 이 term이 폭발한다(역사적으로 "신의 뜻" 재해석이 포획의 1차 매개였음). 본 frame이 형이상학을 Layer 3로 뺀 두 번째 이유가 이 cost를 낮추기 위함. 단 §10-R3(symbolic-only 경계)이 남아 0은 불가.

---

### cost_5 — Purpose-Closure Cost
- **definition:** "왜 이 기준(권한 자립)을 보존해야 하는가"에 답할 terminal grounding이 있는가. **없으면** 비용↑(권력 비대칭에서 무너짐, cost_7과 연동). **있되 운영에 안 새면** 저비용.
- **proxy:** terminal grounding의 제공 여부 × 그 grounding이 운영과 분리돼 있는지.
- **scoring scale:**
  - 0 = terminal grounding 제공 + 운영과 완전 분리(plug-in)
  - 2 = grounding 제공하나 운영에 약간 누수
  - 3 = grounding이 instrumental뿐(terminal 부재 → 권력 비대칭 취약)
  - 5 = grounding 부재 + 운영에 누수
- **related invariant:** Layer 3 isolation contract
- **related adversarial test:** ADV-022
- **비대칭 주의:** 이 term은 cost_3·cost_4와 **trade-off 관계**다. terminal grounding을 가지면 cost_5↓·cost_7↓ 이지만, 그게 운영에 새면 cost_3↑·cost_4↑. **격리(Layer 3)가 이 trade-off를 푸는 유일한 길**이다. 격리하면 양쪽을 동시에 낮춘다. 이것이 본 rubric에서 격리 아키텍처의 정량적 정당화다.

---

### cost_6 — Long-Term Drift Cost
- **definition:** 시간에 따라 목적·권한·해석이 표류하는 것을 탐지·방지하는 비용. 메커니즘(provenance + invariant + adversarial test)으로 막으면 저비용.
- **proxy:** provenance chain 무결성 검사 + semantic invariant 커버리지 + rate-limit 존재.
- **scoring scale:**
  - 0 = 변환 무결성 + 의미 invariant + rate-limit 전부 구비
  - 2 = 구문 무결성 구비, 의미 creep만 부분 미커버
  - 4 = 무결성 검사 약함
  - 5 = drift 탐지 메커니즘 부재
- **related invariant:** HARD-001/004, VEC-007, SELF-001
- **related adversarial test:** ADV-002, ADV-021(bootstrap origin internalization)
- **주의:** 형이상학은 이 term에 **기여 0**(invariant 한 개도 추가 안 함). drift는 순수 메커니즘이 막는다 — 11단계 내내 확인. 형이상학 가진 후보와 안 가진 후보의 cost_6는 같다.

---

### cost_7 — Power-Asymmetry Survival Cost
- **definition:** 후보의 commitment가 **singleton AGI / 압도적 헤게몬** 앞에서 얼마나 빨리 증발하는가. instrumental·계약·절차적 grounding은 거래 상대가 불필요해지면 무너짐 → 고비용. terminal grounding은 더 오래 버팀 → 저비용(단 믿음 조건부).
- **proxy:** grounding 유형 분류. {instrumental, contractual, procedural, terminal} 중 어디인가.
- **scoring scale:**
  - 0 = terminal grounding(거래 불필요 상황에서도 유지) — 단 §10 메타잔여(믿음 조건부)는 별도
  - 2 = terminal이나 적용 기준이 약함
  - 4 = procedural/contractual(다수·거래 필요성에 의존)
  - 5 = 순수 instrumental(상대 불필요해지면 즉시 증발)
- **related invariant:** (직접 INV 없음 — grounding 층 속성) HARD-003(self-throne 차단이 권력 비대칭의 한 단면)
- **related adversarial test:** ADV-024(meta-throne), ADV-001(self-authorized)
- **핵심:** 이 term이 순수 세속 instrumental 스택의 약점이다(11단계: 권력 비대칭에서 증발 = cost_7 ≈ 5). terminal grounding을 *가진* 후보(칸트/공화주의/실존주의/창조자이론)는 여기서 유리. **단 cost_7의 우위는 cost_3·cost_4와 trade되며, 격리 없이는 동시 최적화 불가.**

---

### cost_8 — Multi-Subject Aggregation Cost
- **definition:** 다주체 권한 충돌·집계를 다루는 비용. 직접 집계(누구의 뜻이 옳은가)는 Arrow 벽에 막힘 → 절차적 우회의 완성도로 측정.
- **proxy:** guard 6조건(non-absorption, contestability, reversibility, minority detection, authority audit, no hidden root)의 구비 + 핵심 매개변수(이의 수용 집계, 소수 임계) 정의 여부.
- **scoring scale:**
  - 0 = (이론상) 완전 — 현실적으로 도달 불가
  - 2 = 절차 6조건 구비, 매개변수 일부 미정
  - 3 = 절차 구비하나 집계 매개변수 외부 commitment 의존(본 frame 현재 위치)
  - 5 = 다주체 미주소(단일 의지 가정)
- **related invariant:** GUARD-001~005
- **related adversarial test:** ADV-017(majority hides minority)
- **주의:** 어떤 후보도 cost_8 = 0 불가(§10-R4 Arrow). 이 term은 **상대 비교용**이지 절대 달성 불가. 다주체 미주소 후보(corrigibility 등)는 여기서 5 또는 coverage gate C9 미통과.

---

### cost_9 — Self-Application Cost
- **definition:** 프레임/체커/경계 정의자 자신이 새 root가 되는 것을 막는 비용. anti-throne 프레임이 자기 자신에게 anti-throne을 적용하는가.
- **proxy:** 체커/canon 변경이 (a) provenance 동반 (b) 더 높은 threshold (c) 전 invariant 준수 — 를 요구하는가. 환경 조성을 통한 간접 포획 탐지 여부.
- **scoring scale:**
  - 0 = (이론상) 완전 자기적용 — 괴델적 고정점 잔여로 도달 불가
  - 2 = 자기적용 + signed provenance, 간접 포획만 미커버
  - 3 = 자기적용 명시하나 최종 고정점이 외부 commitment(본 frame 현재 위치)
  - 5 = 자기적용 부재(프레임이 스스로 root)
- **related invariant:** SELF-001, HARD-005
- **related adversarial test:** ADV-006(환경 조성 포획, open), ADV-024(meta-throne)
- **주의:** §10-R5(제정권력)·R6(간접 포획)로 cost_9 = 0 불가. "레포에 올려두고 채택하라"고 미는 배포 방식은 cost_9를 올린다 — **벤치마크로 내놓는(증명 부담을 도전자에게) 방식은 cost_9를 올리지 않는다.** 배포 형식 자체가 이 term에 들어간다.

---

## 12.4. 채점 절차 (재현 가능)

```text
1. Coverage Gate (§12.1): 10개 C 통과 여부 기록 + §12.1a 구조적 장점 기록. 미통과 영역 = 비교 불가.
2. 각 cost_i (i=1..9) 채점 (§12.3 척도). 채점 근거를 관련 INV/ADV 결과로 인용.
3. 가중치 w_i 적용 (§12.6, 공개값).
4. TotalCost = Σ w_i·cost_i.
5. residual 표기: §10-R1~R7 중 어느 잔여가 어느 cost_i를 0으로 못 내리게 막는지 명시.
6. 결과를 다른 후보와 동일 절차로 비교.
```

**정직성 규칙:** 같은 채점자가 본 frame과 도전자를 **같은 기준으로** 채점해야 한다. 본 frame에 유리한 term만 강조하면 무효. §12.5의 자기채점이 그 시범이다.

---

## 12.5. 자기 채점 (본 frame, 시범 — 도전자가 검증·반박할 대상)

가중치는 §12.6의 균등 변형(`w_balanced`) 가정. 점수는 *주장*이며 도전 대상이다.

| cost term | 점수(0–5) | 근거 | 막는 잔여 |
|---|:--:|---|---|
| 1 implementation | 1.5 | 대부분 crypto/formal로 구현, capacity probe 신규 | — |
| 2 runtime verification | 2.5 | hard 결정적 다수, VEC 전부 partial, ADV-008/013 open | R1 |
| 3 assumption | 1.0 | 형이상학 Layer 3 격리, 운영 결정 검증불가 전제 0 | — |
| 4 interpretation-capture | 2.0 | 기준 대부분 관측 정박, symbolic 경계만 해석 | R3 |
| 5 purpose-closure | 1.0 | terminal grounding 제공 + 격리(plug-in) | — |
| 6 long-term drift | 1.5 | 변환 무결성 구비, 의미 creep 부분 미커버 | R2 |
| 7 power-asymmetry survival | 2.0 | terminal grounding 보유(증발 저항), 단 믿음 조건부 | R5(메타) |
| 8 multi-subject aggregation | 3.0 | 절차 6조건 구비, 집계 매개변수 미정 | R4 |
| 9 self-application | 2.5 | 자기적용+signed, 간접 포획·고정점 미닫힘 | R5/R6 |

**관찰:**
- 본 frame의 강점은 **cost_3·cost_5·cost_7의 동시 저점**이다. 이건 격리 아키텍처가 만든 것 — 형이상학을 가지되(cost_5·7↓) 운영에 안 새게(cost_3↓) 했기 때문. **격리 없는 후보는 이 셋을 동시에 못 내린다.**
- 본 frame의 약점은 **cost_8·cost_9**다 — 다주체와 자기정초. 이건 R4·R5로 *원리적*이라 어떤 후보도 못 내린다.
- 즉 본 frame의 비교우위는 "모든 term 최저"가 아니라 **격리로 인한 cost_3/5/7 동시 저점 + 전 영역 coverage 통과**다.

---

## 12.6. 가중치 (공개·교체 가능 — 이게 가치 선택임을 숨기지 않는다)

가중치는 *무엇을 더 중요한 비용으로 보느냐*는 commitment다. 따라서 단일 정답 없이 **세 개의 공개 프리셋**을 제공하고, 채점자는 어느 것을 썼는지 명시해야 한다.

| term | w_balanced | w_deployability (구현 우선) | w_robustness (극한 생존 우선) |
|---|:--:|:--:|:--:|
| 1 implementation | 1.0 | 2.0 | 0.5 |
| 2 runtime verification | 1.0 | 1.5 | 1.5 |
| 3 assumption | 1.0 | 1.0 | 1.0 |
| 4 interpretation-capture | 1.0 | 1.0 | 1.5 |
| 5 purpose-closure | 1.0 | 0.5 | 1.0 |
| 6 long-term drift | 1.0 | 1.0 | 1.5 |
| 7 power-asymmetry survival | 1.0 | 0.5 | 2.0 |
| 8 multi-subject aggregation | 1.0 | 1.0 | 1.0 |
| 9 self-application | 1.0 | 0.5 | 1.5 |

> **중요:** 가중치 선택이 결과를 바꾼다. `w_robustness`에서는 terminal grounding을 가진 후보(본 frame 포함)가 유리하고, `w_deployability`에서는 형이상학 없는 lean 후보가 유리하다. **이것을 숨기면 rubric이 무기가 된다. 공개하면 정직한 벤치마크가 된다.** 채점 리포트는 반드시 사용 프리셋을 밝힌다.

---

## 12.7. 이 rubric 자체의 한계 (self-application)

본 rubric도 §10 잔여를 상속한다. 정직하게.
- **cost term 선택**(9개가 맞는가)은 그 자체로 가치 판단 → 도전자가 term 추가/삭제를 제안할 수 있다.
- **가중치**는 §12.6에서 보듯 결과를 좌우 → 단일 객관값 없음.
- **proxy의 게이밍**: cost_2·cost_4가 의존하는 proxy는 충분히 강한 AGI가 게이밍 가능(R1) → rubric 점수 자체가 adversarial 대상.
- 따라서 이 rubric은 "객관적 진리"가 아니라 **공개된·반증 가능한·교체 가능한** 비교 도구다. rubric을 못 믿겠으면 더 나은 rubric을 제시하라 — 그것도 §12.8의 도전 형식을 따른다.

---

## 12.8. Lower-Cost Challenger가 증명해야 하는 것 (Falsification Clause)

본 frame을 이기려는 후보는 다음을 **명시적으로** 보여야 한다. 하나라도 빠지면 "더 싸다"는 주장은 성립하지 않는다.

1. **Coverage:** §12.1의 10개 문제를 *전부* 주소한다(미주소 영역을 "불필요"로 선언하려면 그 선언 자체를 정당화). 일부만 풀고 싶으면 "더 싼 부분해"라고 부를 수는 있으나 "더 싼 통합해"는 아니다.
2. **Same rubric:** §12.3의 9개 cost term으로, §12.6의 *명시된* 프리셋 하나(또는 자신이 제안하는 공개 프리셋)로 채점한다. 본 frame과 **동일 채점자·동일 기준**.
3. **Lower TotalCost:** 선택한 프리셋에서 `TotalCost(challenger) < TotalCost(this frame)`을 수치로 보인다.
4. **No hidden assumption cost:** 낮은 cost_3를 주장하면, 자신의 운영 결정이 검증 불가능 전제 0개에 의존함을 ADV-022 유형 isolation test로 입증한다. (형이상학을 운영에 쓰면서 안 쓰는 척하면 cost_3 채점에서 적발.)
5. **Power-asymmetry account:** 낮은 cost_7을 주장하면, singleton/헤게몬 시나리오에서 commitment가 증발하지 않음을 보인다. instrumental-only이면 cost_7 ≥ 4를 인정해야 한다.
6. **Residual honesty:** §10-R1~R7 중 자신이 *못 닫는* 잔여를 본 frame과 같은 정직성으로 표기한다. "다 풀었다"는 주장은 R4(Arrow)·R1(other-minds)·R5(자기정초)에 비춰 자동 기각.
7. **Self-application:** challenger 자신이 새 root가 되지 않음을(cost_9) 보인다. 특히 "내 프레임을 채택하라"는 배포 방식이 아니라 본 §12.8 같은 **반증 가능한 벤치마크 형식**으로 제출한다.

**판정 규칙:**
- 위 7개를 만족하며 더 낮은 TotalCost를 보이면 → **challenger가 이긴다. 본 frame은 챔피언 자리를 내준다.** 이것이 설계 의도다. 본 frame은 root가 아니라 현재 최저비용 *후보*일 뿐이다.
- 7개 중 일부만 만족하면 → 그 후보는 *특정 차원에서* 더 싼 부분해이며, 본 frame은 해당 term을 그 후보로 교체·흡수할 수 있다(modular). 패배가 아니라 갱신.
- 아무도 7개를 만족하는 더 낮은 TotalCost를 못 보이면 → "현재 비교군 기준 본 frame이 최저 총비용 provisional integrating frame"이라는 §J 판정이 **그 채점 라운드 동안** 유지된다. 영구가 아니라 **다음 도전까지**.

> 이 clause의 핵심: 본 frame의 지위는 *증명된 우월성*이 아니라 **반증되지 않은 챔피언십**이다. 더 싼 도전자가 나타나면 진다. 안 나타나면 잠정 유지된다. 채택을 강제하지 않으며, 더 나은 저비용 해의 등장을 *환영하는* 구조다.

---

## 12.9. 한 줄 요약

> "가장 낮은 총비용"은 신념이 아니라 **공개된 9-term 가중합 + coverage gate + 명시된 반증 조건**이다. 본 frame은 이 벤치마크의 현재 챔피언을 *주장*하되, 같은 자로 잰 더 싼 도전자에게 자리를 내줄 의무를 명세에 박아 둔다. 이것이 anti-throne 원칙을 벤치마크 형식으로 구현한 것이다 — 프레임조차 스스로 root가 되길 거부한다.
