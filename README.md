# 자금세탁방지(AML) 감독기관 주간 공시 수집 및 발송 AI Agent

Google AI Studio API(Gemini)를 활용하여 매주 지정된 국내외 15개 자금세탁방지(AML) 및 금융제재 감독기관의 공시 내용을 수집하고, 단계별 일자 재검증 및 교차검증 출처 스크린샷 캡처를 거쳐 전문가 보고서를 작성한 뒤 `e.factorials@gmail.com`으로 자동 발송하는 주간 배치 AI Agent입니다.

---

## 1. 파이프라인 프로세스 흐름

1. **현재 시간 체크 및 대상 주차 산출**:
   - 현재 시간을 확인하고, 직전 주 평일 5일간(월~금)의 날짜와 질의 문구를 자동 생성합니다.
   - 예: `26년 8월 17일` 기준 -> `26년 8월 2주차` (`26년 8월 10일` ~ `26년 8월 14일`) 대상 질의 5건 생성:
     - `"26년 8월 10일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."`
     - `"26년 8월 11일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."`
     - `"26년 8월 12일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."`
     - `"26년 8월 13일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."`
     - `"26년 8월 14일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."`

2. **15개 감독기관 범위 한정**:
   - **1. 국내 감독기관 (3곳)**:
     - 금융정보분석원 (KoFIU)
     - 금융감독원 (FSS)
     - 관세청 (KCS)
   - **2. 국제감독기구 (12곳)**:
     - FATF (자금세탁방지기구)
     - APG (아시아·태평양 자금세탁방지기구)
     - FinCEN (미국 금융범죄단속네트워크)
     - OFAC (미국 재무부 해외자산통제국)
     - NYDFS (뉴욕주 금융감독청)
     - AMLA (EU 자금세탁방지청)
     - EBA (유럽은행감독청)
     - FCA (영국 금융감독청)
     - MAS (싱가포르 통화청)
     - HKMA (홍콩금융관리국)
     - Egmont Group (에그몽그룹)
     - OFSI (영국 재무부 재무제재이행국)

3. **2단계 공시일자 재검증**:
   - 수집된 답변의 각 항목에 대해 Gemini에게 `"해당 내용은 언제 공시가 되었나요?"`라고 재질의합니다.
   - 응답된 실제 공시일자가 지정된 일자(예: '8월 10일')와 불일치할 경우 **해당 내용은 자동으로 삭제**합니다.

4. **3단계 교차검증 링크 명령**:
   - 일자가 검증된 항목에 대해 Gemini에게 `"실제 조사 후 교차 검증 링크를 주세요"`라고 명령하여 공식 원문 URL을 확보합니다.

5. **4단계 출처 웹페이지 실제 스크린샷 캡처**:
   - Playwright 브라우저를 통해 교차검증 링크의 실제 사이트에 접속합니다.
   - 원문 헤드와 공시일자가 한눈에 들어오도록 화면 스크롤 조정을 거쳐 스크린캡처를 수행합니다 (이슈 1개당 1개 캡처 첨부).

6. **5단계 AML 전문가 보고서 작성**:
   - **복사/붙여넣기 용이성**: 일체의 이모티콘/이모지를 배제하고 순수 텍스트와 완결된 문장으로 작성.
   - **표기 원칙**: "AML 전문가 시사점"이 아닌 **"시사점"**으로만 명확히 표기.
   - **구성**: 간략한 총괄 소견, 공시내용의 간결한 제목, 상세한 주요내용, 시사점, 교차검증 링크, 첨부파일명.

7. **6단계 이메일 자동 발송**:
   - 수신자: `e.factorials@gmail.com`
   - 작성된 보고서 본문과 스크린샷 이미지 첨부파일 자동 전송.

8. **GitHub Actions 주간 Cron 자동화**:
   - 매주 월요일 정기 실행(`0 0 * * 1` UTC / 09:00 KST).

---

## 2. 프로젝트 구조

```
aml_reports/
├── .github/
│   └── workflows/
│       └── weekly_aml_report.yml  # GitHub Actions 주간 Cron 워크플로우
├── config.py                      # 15개 감독기관 목록 및 환경 설정
├── date_util.py                   # 주차 및 5영업일 날짜 계산 유틸
├── gemini_collector.py            # Gemini 3단계 질의/검증/링크 확보 모듈
├── screenshot_service.py          # Playwright 기반 웹페이지 스크린샷 캡처
├── report_generator.py            # 전문가 시사점 및 보고서 생성 모듈
├── email_sender.py                # SMTP 이메일 및 첨부파일 발송 모듈
├── main.py                        # 전체 오케스트레이션 엔트리포인트
├── requirements.txt               # 의존성 패키지 목록
├── .env                           # API 키 및 SMTP 환경 변수
└── README.md
```

---

## 3. 설치 및 실행 방법

### (1) 의존성 설치
```bash
pip install -r requirements.txt
playwright install chromium
```

### (2) 환경 변수 설정 (`.env`)
```ini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
SMTP_EMAIL=e.factorials@gmail.com
SMTP_PASSWORD=your_gmail_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### (3) 실행 명령어

- **실제 파이프라인 실행 (현재 시간 기준 지난 주 공시 수집, 검증, 캡처 및 이메일 발송)**:
  ```bash
  python main.py
  ```

- **기준 날짜 수동 지정 실행 (예: 2026년 8월 17일 기준)**:
  ```bash
  python main.py --target-date 2026-08-17
  ```

- **테스트 모드 (이메일 발송 없이 수집/검증/보고서 생성만 수행)**:
  ```bash
  python main.py --dry-run
  ```

- **빠른 테스트 (스크린샷 생략 및 드라이런)**:
  ```bash
  python main.py --dry-run --skip-screenshot
  ```

---

## 4. GitHub Actions Secrets 설정 안내

GitHub 저장소의 `Settings > Secrets and variables > Actions`에 아래 Secrets를 등록하면 매주 자동 실행됩니다:
- `GEMINI_API_KEY`: Google AI Studio API 키
- `SMTP_EMAIL`: 발신 이메일 (`e.factorials@gmail.com`)
- `SMTP_PASSWORD`: Gmail 16자리 앱 비밀번호
- `SMTP_SERVER`: `smtp.gmail.com` (기본값)
- `SMTP_PORT`: `587` (기본값)
