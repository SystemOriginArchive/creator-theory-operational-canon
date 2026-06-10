@echo off
REM AI-GENERATED SCRIPT - NOT EXECUTED BY CODEX - DO NOT RUN BEFORE THE AUDITOR'S LINE-BY-LINE REVIEW PASS.
REM 이 파일은 감사자 검토 전 실행 금지입니다.
REM Codex는 이 스크립트를 실행하지 않았고, 실행해서도 안 됩니다.

setlocal
set "SSH_KEYGEN=C:\Windows\System32\OpenSSH\ssh-keygen.exe"
set "TARGET_DIR=%USERPROFILE%\.prov-k"
set "KEY_PATH=%TARGET_DIR%\origin_ed25519"

if not exist "%SSH_KEYGEN%" (
  echo OpenSSH ssh-keygen.exe를 찾을 수 없습니다.
  echo 아무것도 다운로드하지 않습니다. 여기서 중지합니다.
  exit /b 1
)

if exist "%KEY_PATH%" (
  echo 기존 origin key가 이미 존재합니다.
  echo 덮어쓰지 않습니다. 여기서 중지합니다.
  exit /b 1
)

if exist "%KEY_PATH%.pub" (
  echo 기존 public key가 이미 존재합니다.
  echo 덮어쓰지 않습니다. 여기서 중지합니다.
  exit /b 1
)

echo 이 스크립트는 실제 origin key를 생성합니다.
echo 개인키는 절대 출력하지 않습니다.
echo 대상 경로: %TARGET_DIR%
echo 감사자의 줄 단위 검토가 끝나지 않았다면 지금 닫으십시오.
set /p CONFIRM="계속하려면 YES_CREATE_REAL_ORIGIN_KEY 를 정확히 입력하십시오: "
if not "%CONFIRM%"=="YES_CREATE_REAL_ORIGIN_KEY" (
  echo 확인 문자열이 일치하지 않습니다. 중지합니다.
  exit /b 1
)

mkdir "%TARGET_DIR%" 2>nul
"%SSH_KEYGEN%" -t ed25519 -f "%KEY_PATH%" -C "PROV-K origin attribution key" -N ""
if errorlevel 1 (
  echo 키 생성 실패.
  exit /b 1
)

echo 완료되었습니다.
echo 개인키를 공유하거나 촬영하거나 저장소에 넣지 마십시오.
echo 공개키 파일만 검증 절차에 사용할 수 있습니다: %KEY_PATH%.pub
endlocal
