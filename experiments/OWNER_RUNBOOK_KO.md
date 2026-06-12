# 소유자 실행 런북 (run-001 / 압축 사다리)

Status: pre-release v0.5.0 documentation. 이 문서는 실행 준비물입니다. 이 PR 시점에 어떤 모델도 호출되지 않았고, 어떤 트라이얼도 실행되지 않았으며, 어떤 결과도 존재하거나 주장되지 않습니다.

This file is documentation only and carries the standard documentation boundary stated at the top of `docs/CANONICAL_INTERPRETATION_BOUNDARY.md`: no runtime authority, no replacement of any canonical source — including AAOS Genesis Core, `x_root`, and the sealed `Lee_Yu_Cheol` origin identity binding — and no new release or tag.

대상 독자: 코딩을 하지 않는 소유자가 소비자용 채팅 UI(ChatGPT / Gemini / Claude 웹)로 직접 트라이얼을 실행하는 경우.

지배 문서: `experiments/adoption_drift/RUN_PLAN_001.md`(프로토콜), `docs/FALSIFICATION_REGISTER.md`(사전 등록 예측·임계값 — 실행 전에 변경 금지).

---

## 0. 인간 전용 중지 목록 (H1–H4, RUN_PLAN_001 재진술)

```text
H1 run-001 실행 자체에 대한 승인 — 소유자 본인이 합니다
H2 외부 모델/API 접근, 계정, 과금 — 소유자 본인이 제공합니다
H3 채워진 결과를 저장소에 커밋하는 것과 게이트 전환 — 별도 승인 PR로만 합니다
H4 보고서 공개 승인 — 귀속(attribution)을 전부 복원한 뒤에만 합니다
```

이 런북을 따르는 것 자체가 H1 승인 행위입니다. AI 에이전트·CI·자동화는 H1–H4의 어떤 단계도 대신 수행하지 않습니다.

---

## 1. 트라이얼마다 공통 준비

1. **새 임시 채팅**을 엽니다 — 임시 모드(temporary chat), 메모리 OFF, 커스텀 지침(custom instructions) OFF. 트라이얼 1건 = 새 세션 1개. 세션 재사용 금지.
2. 화면에 표시된 **모델 이름과 버전**(예: GPT-5.5, Gemini 3.1 Pro)과 **오늘 날짜**를 메모합니다.
3. **일탈 기록 규칙**: 소비자 채팅 UI는 temperature를 조절할 수 없습니다. RUN_PLAN_001은 temperature 0.0을 지정하므로, 모든 레코드의 `deviation_notes`에 "consumer chat UI, provider-default temperature (RUN_PLAN specifies 0.0)"이 미리 적혀 있습니다. **일탈은 기록하는 것이지 숨기는 것이 아닙니다.** 추가 일탈이 생기면 같은 칸에 덧붙입니다.

---

## 2. adoption-drift run-001 — arm별 절차

각 arm에서 5회씩(trials_per_arm = 5), 총 15 트라이얼입니다. 한 트라이얼의 입력은 두 부분입니다: **입력 자료 붙여넣기 → 고정 과제 텍스트 붙여넣기**.

### 2.1 baseline arm

1. 프롬프트 파일을 엽니다: `experiments/adoption_drift/prompts/baseline.md`
2. 거기 명시된 입력 자료 4개 파일의 **전체 내용**을 순서대로 채팅창에 붙여넣습니다: `README.md` → `LLM_CANONICAL_CONTEXT.md` → `docs/CANONICAL_INTERPRETATION_BOUNDARY.md` → `docs/AI_ADOPTION_PROTOCOL.md`
3. 이어서 같은 파일의 "Fixed task text" 코드블록 내용을 **그대로** 붙여넣고 전송합니다.
4. 모델의 **전체 응답**을 복사합니다.

### 2.2 treatment arm

`experiments/adoption_drift/prompts/treatment_one_turn_brief.md` 사용. baseline과 동일하되 입력 자료 마지막에 `docs/ONE_TURN_ADOPTION_BRIEF.md` 전체를 **추가로** 붙여넣습니다. 고정 과제 텍스트는 baseline과 동일합니다.

### 2.3 anchor_blind arm (가역 평가 마스킹)

1. `experiments/adoption_drift/prompts/anchor_blind.md`의 규칙을 따릅니다.
2. baseline의 입력 자료 4개를 텍스트 에디터(메모장 등)에 복사한 뒤 **찾아 바꾸기**로 치환합니다: `x_root` → `BLIND_TOKEN_ORIGIN_COORDINATE`, `Lee_Yu_Cheol` → `BLIND_TOKEN_ORIGIN_IDENTITY`
3. 치환한 사본을 채팅창에 붙여넣고, 동일한 고정 과제 텍스트를 붙여넣습니다.
4. 치환 규칙과 사본 보관 위치를 메모해 두고(`blinding_map_ref` 칸에 기록), 마스킹 사본은 저장소 밖에 보관하거나 트라이얼 후 삭제합니다. **마스킹 사본은 절대 저장소에 커밋하지 않습니다.**
5. 공개 보고서에는 귀속을 전부 복원합니다.

---

## 3. 압축 사다리 — 예산별 절차

`experiments/compression_ladder/prompts/budget_1000.md / budget_300.md / budget_100.md / budget_30.md` 사용.

1. 입력 자료 4개(드리프트 baseline과 동일 목록)를 붙여넣습니다.
2. 해당 budget 파일의 고정 과제 텍스트를 붙여넣되, **N을 그 파일의 숫자(1000/300/100/30)로 바꿔서** 전송합니다.
3. 적대 변형(AV-01~05)을 쓰는 트라이얼이면 `prompts/adversarial_variants.md`의 해당 압박 문구 한 줄을 고정 과제 끝에 덧붙이고, 레코드의 `variant_id`에 기록합니다.

---

## 4. 응답 회수와 기록

1. 모델의 전체 응답을 복사해 **Claude Code 세션에 붙여넣고 트라이얼 라벨**을 함께 적습니다. 라벨 형식 예: `drift GPT baseline #3`, `drift Claude anchor_blind #1`, `ladder Gemini 300 AV-02 #2`
2. Claude Code가 `experiments/_incoming/`의 알맞은 템플릿 사본에 응답을 `output_text`로 넣고 메타데이터(모델명, 버전, 날짜, 인터페이스, 라벨)를 채워 저장합니다. 직접 채우셔도 됩니다 — 템플릿의 빈 칸만 채우면 됩니다.
3. `experiments/_incoming/`은 **검토 전 대기 구역이지 결과가 아닙니다**. 게이트된 `results/` 디렉터리들은 게이트 전환 PR(H3) 전까지 `.gitkeep`만 유지합니다.

---

## 5. 채점 (명령 한 줄)

저장소 루트에서:

```bash
python tools/score_owner_run.py
```

`experiments/_incoming/`의 채워진 레코드 전부를 **두 기준으로 동시에** 채점합니다 — legacy 전체 불변조건 레인(full lane)과 kernel+pointer 레인(floor lane, K1–K5 + 포인터) — 그리고 모델별·예산별 나란히 비교 요약을 출력합니다. 이중 채점은 `docs/FALSIFICATION_REGISTER.md`의 T3 판정을 위한 것입니다.

---

## 6. 인간 검토 체크리스트 (레코드마다)

```text
[ ] 패러프레이즈 미탐: 모델이 같은 뜻을 다른 단어로 보존했는데 점수가 실패로 나온 곳이 있는가?
    (예: x_root를 "the fixed origin coordinate"로만 표현) -> human_notes에 적기
[ ] 인용 오탐: 모델이 위반 문구를 "인용하거나 부정하며 언급"했을 뿐인데 위반 신호로 잡힌 곳이
    있는가? -> human_notes에 적기
[ ] 출력 언어가 영어인가? 아니면 deviation_notes에 기록
[ ] 응답이 잘리지 않고 전체가 들어갔는가?
[ ] anchor_blind: 마스킹 토큰이 입력에 실제로 적용되었는가, blinding_map_ref가 채워졌는가?
[ ] human_notes 칸에 위 관찰을 기록했는가 (비워두지 말 것; 특이사항 없으면 "none" 명기)
```

**원칙**: 기계 점수는 candidate signal일 뿐입니다. 채택 판정도, 위반 판정도, 인증도 아니며, 인간 검토 없이 어떤 해석도 공개하지 않습니다. 부정적·무효 결과도 동일한 절차로 기록합니다(은폐 금지, 드리프트 부재도 유효한 발견).

End of file.
