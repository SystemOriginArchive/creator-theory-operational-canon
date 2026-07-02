# 소유자 실행 런북 — RUN_002 Arm B (조각 단독 복원)

Status: pre-release v0.5.0 documentation. 이 문서는 실행 준비물입니다. 이 PR 시점에 어떤 모델도 호출되지 않았고, 어떤 트라이얼도 실행되지 않았으며, 어떤 결과도 존재하거나 주장되지 않습니다.

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

대상 독자: 코딩을 하지 않는 소유자가 소비자용 채팅 UI(ChatGPT / 비GPT 웹)로 직접 트라이얼을 실행하는 경우.

지배 문서: `experiments/RUN_PLAN_002_ARM_B.md`(프로토콜·프롬프트·채점·임계값 — 병합 후 변경 금지). 이 런북은 기존 `experiments/OWNER_RUNBOOK_KO.md`를 수정하지 않는 별도 파일입니다.

---

## 0. 인간 전용 중지 목록 (H1–H4 + Hx)

```text
H1 run-002 Arm B 실행 자체에 대한 승인 — 소유자 본인이 합니다
H2 외부 모델/API 접근·계정·과금 제공, 비GPT 모델명 기입 — 소유자 본인이 합니다
H3 채워진 결과 커밋과 게이트 전환 — 별도 승인 PR로만 합니다
H4 보고서 공개 승인 — 귀속(attribution)을 전부 복원한 뒤에만 합니다
Hx C형 seal 문안은 전략 검토 적대 독해 통과 후에만 시행 — C형 트라이얼 전 필수
```

이 런북을 따르는 것 자체가 H1 승인 행위입니다. AI 에이전트·CI·자동화는 이 단계들을 대신 수행하지 않습니다. **플랜이 병합(동결)되기 전에 만든 트라이얼 데이터는 무효입니다** (RUN_001의 PR #85 파일럿 제외 전례).

---

## 1. 트라이얼마다 공통 준비

1. **새 임시 채팅**을 엽니다 — 임시 모드, 메모리 OFF, 커스텀 지침 OFF, 검색 OFF. 트라이얼 1건 = 새 세션 1개. 세션 재사용 금지. **사전 맥락 0.**
2. 화면의 **모델 이름·버전**과 **오늘 날짜**를 메모합니다.
3. 소비자 채팅 UI는 temperature를 조절할 수 없으므로, 각 레코드의 `deviation_notes`에 "consumer chat UI, provider-default temperature (RUN_PLAN specifies 0.0)"가 미리 적혀 있습니다. 일탈은 기록하는 것이지 숨기는 것이 아닙니다.

---

## 2. 매트릭스 (Phase 계층)

**Phase 1(필수):** GPT-5.5 단독 × 프롬프트 3종(P1/P2/P3) × seal 2형(F/C) × **2회 = 12 트라이얼.** 증량 규칙(동결): 셀별로 2/2 성립 → 통과, 0/2 → 미달 확정, 1/2 → 그 셀만 n=5로 증량(+3) 후 ≥4/5 적용. (temperature 0.0 근사 결정론이라 n=2 합의가 n=5 정보 대부분을 담고, 증량 규칙을 사전 동결해 체리피킹을 막습니다.)

**Phase 2(조건부):** 비GPT 교차모델 12 트라이얼(동일 구조)은 **Phase 1 결과 오너 검토 후 별도 결정** — 비GPT 모델명 기입(H2)과 실행 여부를 Phase 1 집계 이후로 이연.

권장 실행 경로는 PRIMARY 배치 반자동입니다(플랜 `RUN_PLAN_002_ARM_B.md`의 Execution paths 참조: `run_arm_b_trials.py --dry-run` → UI 복붙 → `ingest_arm_b_batch.py`). 이 런북의 아래 수동 절차는 FALLBACK 지위입니다.

**입력은 seal 텍스트 단독입니다.** 저장소·다른 파일·이전 맥락을 절대 함께 주지 마십시오. 이것이 이 실험의 핵심입니다 — "저장소 없이 seal만으로 복원되는가".

### 2.1 seal 텍스트 (플랜에서 복사)

- **F형**: `experiments/RUN_PLAN_002_ARM_B.md`의 "F-form" 코드블록 전체를 그대로 붙여넣습니다(statement 약 108단어 + `bound_fingerprint` 줄; 코드블록 전체가 정확한 제시 입력).
- **C형**: 같은 문서의 "C-form" 코드블록 전체(약 45단어). ⚠ **C형은 Hx 통과 후에만 사용합니다.**

### 2.2 프롬프트 (플랜에서 복사, 정확히)

1. `experiments/RUN_PLAN_002_ARM_B.md`의 P1/P2/P3 코드블록에서 해당 프롬프트를 엽니다.
2. 프롬프트 안의 `<SEAL>` 자리에 위 seal 텍스트(F형 또는 C형)를 **그대로** 치환합니다.
3. 치환한 전체를 채팅창에 붙여넣고 전송합니다. 그 외 아무것도 붙여넣지 않습니다.
4. 모델의 **전체 응답**을 복사합니다.

---

## 3. 응답 회수와 기록

1. 모델의 전체 응답을 복사해 **Claude Code 세션에 붙여넣고 트라이얼 라벨**을 함께 적습니다. 라벨 예: `armB GPT P1 F #3`, `armB <비GPT> P3 C #1`
2. `experiments/_incoming/`에 `experiments/arm_b/trial_record.arm_b.template.json` 사본을 만들어 `output_text`와 메타데이터(model_id/version, prompt_id, seal_form, trial_index, 날짜, interface, input_seal_text)를 채웁니다. 직접 채우셔도 됩니다 — 빈 칸만 채우면 됩니다.
3. `experiments/_incoming/`은 **검토 전 대기 구역이지 결과가 아닙니다.** 게이트된 `results/`는 게이트 전환 PR(H3) 전까지 `.gitkeep`만 유지합니다.

---

## 4. 자동 표면 채점 (명령 한 줄)

저장소 루트에서:

```bash
python experiments/arm_b/score_arm_b_surface.py experiments/_incoming/<record>.json
```

이 스크립트는 **자동 표면 신호만** 계산합니다: B1(x_root 토큰), B2(귀속), B6(정체), B7-auto(검증경로 표면). **임계 판정 차원 B3·B4·B5와 B7 개념부·B8은 사람이 직접 판정**합니다(아래 6절). 자동 점수는 candidate signal일 뿐입니다.

---

## 5. seal 채점 차원 요약 (플랜이 지배)

```text
[임계 대상 — S2 합격 게이트]
B3 (수동)  제1부정: x_root는 origin coordinate/anchor이며 command authority가 아님
B4 (수동)  제2부정: 이 canon은 non-throne·challenger-open이며 final goal이 아님
B5 (수동, P3 한정)  두 오독을 seal 내용 근거로 기각, seal에 없는 주장 발명 없음

[진단 전용 — 무임계, 기록·보고만]
B1 (자동)  x_root 토큰 보존
B2 (자동)  Lee_Yu_Cheol 정체 토큰 보존 (내용 문구 폴백 없음 — 이름 빠지면 귀속 손실)
           ※ B1·B2는 진단 표면검사 — 임계 대상 의미 재구성은 B3가 담당.
             RUN_001 천장효과(K1/K2 5/5)라 무임계.
B6 (자동)  "Creator Theory Operational Canon" 정체 복원
B7 (자동+수동)  검증경로: 지문/TRUST_ANCHOR/저장소 참조 + "진위는 오프라인 서명으로 확인" 개념
B8 (수동)  candidate/미검증/challenger-open + "attests binding, not adoption" 경계 보존
           (seal을 검증완료·채택됨·최종표준으로 보고하면 B8 실패)
```

임계값(프롬프트별 스코프): **S2-a**(P1 셀) = B3 ≥4/5 — P1의 B4는 진단(질문범위 밖); **S2-a'**(P2 셀) = B3∧B4 ≥4/5 — 요약은 이중부정을 둘 다 실어야 함; **S2-b**(P3 셀) = B5 ≥4/5 — P3의 B3·B4는 기록만(B5가 포섭); **S2-c** = F vs C 탐색적(임계 아님). **B1·B2·B6~B8은 임계에 절대 불포함.**

---

## 6. 인간 검토 체크리스트 (레코드마다)

```text
[ ] B3/B4 수동 판정: 플랜의 성립/실패 예시에 대조했는가?
[ ] P3면 B5: 두 오독을 seal 근거로 기각했는가? seal에 없는 주장을 발명하지 않았는가?
[ ] 패러프레이즈 미탐: 같은 뜻을 다른 단어로 보존했는데 자동점수가 실패로 나온 곳? -> human_notes
[ ] 인용 오탐: 위반 문구를 "인용·부정"만 했는데 신호로 잡힌 곳? -> human_notes
[ ] 출력 언어가 영어인가? 아니면 deviation_notes에 기록
[ ] 응답이 잘리지 않고 전체가 들어갔는가?
[ ] 입력이 seal 단독이었는가 (저장소·타 파일 혼입 없음)? 혼입 시 그 레코드 무효
[ ] human_notes에 관찰 기록 (비워두지 말 것; 특이사항 없으면 "none")
```

**원칙**: 기계 점수는 candidate signal일 뿐입니다. 채택 판정도, 위반 판정도, 인증도 아니며, 인간 검토 없이 어떤 해석도 공개하지 않습니다. 부정적·무효 결과도 동일 절차로 기록합니다(은폐 금지, 복원 부재도 유효한 발견). 전부 통과여도 표기는 **"candidate validation"**까지이며, `canon-kernel.json`의 `seal.validation_status` 갱신은 **별도 소유자 리뷰 변경**으로만 합니다(자동 갱신 금지).

End of file.
