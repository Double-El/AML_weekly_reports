import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENTS

def send_august_week3_insight_email():
    subject = "[AML & Sanctions Weekly Insight] 2026년 8월 3주차 자금세탁방지 주요 공시 상세 보고서"
    
    # 1. Plain Text Version (Full Detailed matching standard format)
    body_text = """[AML & Sanctions Weekly Insight] 2026년 8월 3주차

자금세탁방지본부 CoP
수집 및 분석 대상 주차: 2026년 8월 3주차 (2026.08.17 ~ 2026.08.21)

================================================================================
■ 8월 3주차 주요 공시 목차
================================================================================
01 | [AML] 금융위·KoFIU, 개정 「특금법 시행령」 본격 시행 및 가상자산사업자 관리 강화 (‘26.8.20)
02 | [AML] FATF, 국경 간 신속결제 투명성 제고를 위한 권고기준 16(R.16) 개정 지침 의견수렴 (‘26.8.21)
03 | [Sanctions/AML] 美 OFAC, ICC 관련 일반면허(GL 12) 발급 및 글로벌 SDN 제재 목록 갱신 (‘26.8.18)
04 | [AML] EU AMLA 및 주요 회원국, 국가 AML 종합전략 발표 및 단일규정집(Single Rulebook) 대비 (‘26.8.17)

================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================

--------------------------------------------------------------------------------
[AML] 01. 금융위·KoFIU, 개정 「특금법 시행령」 본격 시행 및 가상자산사업자 관리 강화 (‘26.8.20)
--------------------------------------------------------------------------------
[1] 개정 배경 및 추진 경과
▪ 가상자산 시장의 건전성을 제고하고 불법 자금세탁 및 범죄 수익 은닉을 차단하기 위한 「특정 금융거래정보의 보고 및 이용 등에 관한 법률(특금법) 시행령」 개정안이 2026년 8월 20일(목)부터 본격 시행됨.

[2] 주요 개정 내용 및 핵심 통제 기준
① 가상자산 이전거래(트래블룰) 전면 확대
- 기존 100만 원 이상 거래에만 적용되던 트래블룰 기준 금액이 전면 폐지되어 '모든 가상자산 이전거래'로 송·수신인 신원정보 제공 및 확인 의무가 확대됨.
- 수취 사업자는 송금 사업자로부터 필수 정보가 제공되지 않은 경우 추가 정보를 요구하거나 거래를 거절해야 하는 정보 확보 의무를 지님.
② 가상자산사업자(VASP) 대주주 적격성 심사제 도입
- 대표자 및 임원 위주의 기존 심사에서 '최대주주 및 주요주주(법인인 경우 법인의 대표자 포함)'까지 심사 대상을 대폭 확장함.
③ 재무건전성 및 신용 요건 신설
- 가상자산사업자는 부채비율 200% 이하를 유지해야 하며 최근 3년간 채무불이행 이력이 없어야 함.
- 범죄경력 심사 대상 법률을 기존 5개에서 10개(마약거래방지법, 공정거래법, 조세범처벌법, 가상자산이용자보호법 등 추가)로 대폭 확대함.

▶ [시사점 및 금융권 대응 방향]
- 실명계좌 발급 은행의 거래소 정기 실사 항목 개편: 제휴 가상자산거래소에 대한 은행의 정기 위험평가 시 대주주 적격성, 재무건전성(부채비율 200%), 내부통제 체계를 철저히 실사해야 함.
- 소액 분산 송금(스머핑) 모니터링 고도화: 트래블룰 기준 금액 폐지에 따라 규제 회피 목적의 소액 쪼개기 거래를 탐지하는 FDS 시나리오를 정밀하게 재구축해야 함.
- 가상자산-원화 연계 의심거래보고(STR) 연계: 거래소 입출금 패턴과 은행 원화 계좌 간의 단기 급증 이상 이체에 대해 즉각적인 STR 보고 프로세스를 가동해야 함.


--------------------------------------------------------------------------------
[AML] 02. FATF, 국경 간 신속결제 투명성 제고를 위한 권고기준 16(R.16) 개정 지침 의견수렴 (‘26.8.21)
--------------------------------------------------------------------------------
[1] 발간 배경 및 개요
▪ 국제자금세탁방지기구(FATF)는 국경 간 신속 결제 시스템(FPS, Fast Payment Systems)의 확산과 지급결제 현대화에 발맞추어, 전신송금 투명성을 규율하는 '권고기준 16(Recommendation 16)' 개정 지침 초안에 대한 글로벌 공청회를 8월 21일 마감함.

[2] 주요 개정 방향 및 통제 요구사항
① 지급결제 메시지 표준화 및 필수 식별정보 의무화
- ISO 20022 표준 전문 도입에 따라 송금인·수취인의 성명, 계좌번호, 고유 식별번호(주민번호/사업자번호/LEI)를 결제 체인 전 과정에서 누락 없이 전달하도록 규정.
② 신속결제망 중간 매개기관(Intermediary PSP)의 역할 명확화
- 국경 간 신속 결제 시 중간 결제대행 기관도 결제 메시지 내 필수 정보 누락 여부를 실시간 검증하고 의심거래 발생 시 즉각 보고하도록 통제 기준 신설.
③ 사기 및 자금세탁 방지를 위한 실시간 스크리닝 기준 제시
- 초국경 결제 처리 속도가 단축됨에 따라 결제 체결 전(Pre-transaction) 단계에서의 제재 및 이상거래 실시간 필터링 기술 적용을 권고함.

▶ [시사점 및 금융권 대응 방향]
- 외환 전문(ISO 20022) AML 데이터 무결성 검증: 신속 해외송금 및 외환 결제 처리 시 송수신인 식별 정보가 완전하게 포함되어 있는지 실시간 검증하는 시스템 필터를 구축해야 함.
- 실시간 FDS 및 제재 스크리닝 처리 속도 개선: 신속결제 환경에 맞추어 결제 지연 없이 제재 대상자 및 고위험 사기 계좌를 탐지할 수 있도록 스크리닝 엔진의 처리 성능을 고도화해야 함.


--------------------------------------------------------------------------------
[Sanctions/AML] 03. 美 OFAC, ICC 관련 일반면허(GL 12) 발급 및 글로벌 SDN 제재 목록 갱신 (‘26.8.18)
--------------------------------------------------------------------------------
[1] 제재 추진 경과 및 주요 발표 내용
▪ 미국 재무부 해외자산통제국(OFAC)은 8월 18일 국제형사재판소(ICC) 관련 제재 대상자와의 기존 계약 종결 및 자산 정리를 지원하기 위한 일반면허(General License 12)를 발급함.
▪ 아울러 중동 및 테러 지원 네트워크 연계 개인 및 법인을 특별지정제재(SDN) 목록에 추가 등재하고, 기존 제재 대상자의 식별 정보를 최신화함.

[2] 핵심 제재 통제 사항
- 일반면허 12(GL 12)의 허용 범위와 유예 기간을 준수하지 않은 거래에 대해 미국 금융시스템 접근을 차단하는 제재 규정 적용.
- 테러 조직 및 우회 조달망 연계 페이퍼컴퍼니와의 모든 금융 거래 금지 및 미국 내 자산 동결.

▶ [시사점 및 금융권 대응 방향]
- SDN 리스트 실시간 동기화 및 오탐 관리: OFAC의 최신 제재 리스트 갱신 데이터를 제재 스크리닝 엔진에 즉각 반영하여 당일 외환 송금 및 무역금융 거래를 철저히 차단해야 함.
- 일반면허(GL) 적용 거래의 적격성 심사: 제재 대상 연계 거래 중 일반면허(GL 12 등) 적용을 주장하는 거래에 대해 법적 요건 및 기한 충족 여부를 정밀 심사(EDD)해야 함.


--------------------------------------------------------------------------------
[AML] 04. EU AMLA 및 주요 회원국, 국가 AML 종합전략 발표 및 단일규정집(Single Rulebook) 대비 (‘26.8.17)
--------------------------------------------------------------------------------
[1] 추진 배경 및 개요
▪ 2027년 7월 전면 시행을 앞둔 EU 단일 자금세탁방지 규정집(AMLR Single Rulebook)과 신설 유럽자금세탁방지청(AMLA) 체계에 발맞추어, 아일랜드 등 EU 주요 회원국이 국가 차원의 제1차 AML/CFT 종합 전략을 8월 17일 공식 발표함.

[2] 주요 정책 방향 및 핵심 규율 사항
① 고위험 분야(가상자산·사모펀드·부동산) 집중 통제
- 현금 거래 한도 규제 강화(최대 1만 유로) 및 1천 유로 이상 가상자산 거래에 대한 전면 실사 의무화.
② 법인 실소유자(BO) 중앙 레지스트리 실시간 검증
- 페이퍼컴퍼니를 악용한 조세 회피 및 자금세탁을 방지하기 위해 EU 전역 실소유자 등록 데이터베이스의 상호 연계를 추진함.
③ 글로벌 금융회사에 대한 국경 간 통합 검사 체계 마련
- EU 역내 다국적 금융그룹에 대해 AMLA와 회원국 금융당국이 합동 검사를 실시하는 통합 감독 프레임워크 구축.

▶ [시사점 및 금융권 대응 방향]
- 유럽 진출 국내 지점 및 현지법인의 규제 조기 정합성 확보: 2027년 전면 시행되는 EU AMLR 및 AMLA 기준에 부합하도록 현지 지점의 내부통제 규정 및 고객확인 절차를 상향 표준화해야 함.
- 역외 투자 펀드 및 고위험 자산 심사 강화: 유럽계 법인 및 펀드 고객과의 거래 시 실소유자 정보(BO)를 중앙 레지스트리와 대조 검증하는 절차를 내재화해야 함.
"""

    # 2. Rich HTML Version
    body_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕", "Apple SD Gothic Neo", helvetica, sans-serif; line-height: 1.65; color: #1e293b; background-color: #f1f5f9; margin: 0; padding: 24px; }}
        .container {{ max-width: 900px; margin: 0 auto; background: #ffffff; border-radius: 14px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01); padding: 40px 48px; border: 1px solid #e2e8f0; }}
        
        .header {{ border-bottom: 2px solid #0f172a; padding-bottom: 24px; margin-bottom: 32px; }}
        .sub-header {{ font-size: 13px; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase; font-weight: 700; margin-bottom: 8px; }}
        .title {{ font-size: 26px; font-weight: 800; color: #0f172a; margin: 0 0 12px 0; letter-spacing: -0.5px; }}
        .badge-date {{ display: inline-block; background: #f8fafc; border: 1px solid #cbd5e1; color: #334155; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; }}
        
        .toc-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #0ea5e9; border-radius: 8px; padding: 22px 26px; margin-bottom: 36px; }}
        .toc-title {{ font-weight: 800; font-size: 16px; margin-bottom: 14px; color: #0f172a; display: flex; align-items: center; }}
        .toc-list {{ margin: 0; padding-left: 20px; font-size: 14px; color: #334155; }}
        .toc-list li {{ margin-bottom: 8px; line-height: 1.5; }}
        
        .card {{ background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 28px 30px; margin-bottom: 36px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }}
        .card-header {{ display: flex; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #f1f5f9; padding-bottom: 16px; }}
        .card-category {{ background: #0f172a; color: #fff; font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 6px; margin-right: 12px; letter-spacing: 0.5px; }}
        .card-category.sanctions {{ background: #991b1b; }}
        .card-title {{ font-size: 18px; font-weight: 800; color: #0f172a; line-height: 1.4; }}
        
        .section-subtitle {{ font-size: 14px; font-weight: 700; color: #475569; margin: 16px 0 8px 0; }}
        .content-list {{ list-style-type: none; padding-left: 0; margin: 0 0 18px 0; font-size: 14px; color: #334155; }}
        .content-list > li {{ margin-bottom: 12px; position: relative; padding-left: 20px; line-height: 1.65; }}
        .content-list > li::before {{ content: "▪"; position: absolute; left: 0; color: #475569; font-weight: 900; font-size: 16px; }}
        
        .sub-bullet-box {{ background: #f8fafc; border: 1px solid #f1f5f9; border-radius: 8px; padding: 14px 16px; margin-top: 10px; font-size: 13.5px; }}
        .sub-bullet-box p {{ margin: 0 0 8px 0; }}
        .sub-bullet-box p:last-child {{ margin-bottom: 0; }}
        
        .insight-card {{ background: #eff6ff; border-left: 5px solid #2563eb; padding: 18px 20px; border-radius: 0 10px 10px 0; margin-top: 22px; }}
        .insight-header {{ font-size: 14px; font-weight: 800; color: #1e40af; margin-bottom: 8px; display: flex; align-items: center; }}
        .insight-body {{ font-size: 13.5px; color: #1e3a8a; line-height: 1.6; margin: 0; padding-left: 18px; }}
        .insight-body li {{ margin-bottom: 6px; }}
        .insight-body li:last-child {{ margin-bottom: 0; }}
        
        .footer {{ text-align: center; font-size: 12px; color: #94a3b8; margin-top: 48px; padding-top: 24px; border-top: 1px solid #e2e8f0; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <div class="sub-header">자금세탁방지본부 CoP | 주간 컴플라이언스 인텔리전스</div>
          <div class="title">AML &amp; Sanctions Weekly Insight</div>
          <span class="badge-date">2026년 8월 3주차 상세 보고서 (2026.08.17 ~ 2026.08.21)</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📋 8월 3주차 주요 공시 및 핵심 의제</div>
          <ol class="toc-list">
            <li><strong>[AML]</strong> 금융위·KoFIU, 개정 「특금법 시행령」 본격 시행 및 가상자산사업자 관리 강화 (‘26.8.20)</li>
            <li><strong>[AML]</strong> FATF, 국경 간 신속결제 투명성 제고를 위한 권고기준 16(R.16) 개정 지침 의견수렴 (‘26.8.21)</li>
            <li><strong>[Sanctions/AML]</strong> 美 OFAC, ICC 관련 일반면허(GL 12) 발급 및 글로벌 SDN 제재 목록 갱신 (‘26.8.18)</li>
            <li><strong>[AML]</strong> EU AMLA 및 주요 회원국, 국가 AML 종합전략 발표 및 단일규정집(Single Rulebook) 대비 (‘26.8.17)</li>
          </ol>
        </div>

        <!-- Card 01 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">01. 금융위·KoFIU, 개정 「특금법 시행령」 본격 시행 및 가상자산사업자 관리 강화 (‘26.8.20)</div>
          </div>
          
          <div class="section-subtitle">[1] 개정 배경 및 추진 경과</div>
          <ul class="content-list">
            <li>가상자산 시장의 투명성을 대폭 강화하고 자금세탁 및 범죄 자금 은닉을 원천 차단하기 위한 <strong>「특금법 시행령」 개정안이 2026년 8월 20일(목)부터 본격 시행</strong>됨.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 개정 내용 및 핵심 통제 기준</div>
          <ul class="content-list">
            <li><strong>가상자산 이전거래(트래블룰) 전면 확대:</strong>
              <div class="sub-bullet-box">
                <p>• 기존 100만 원 이상 거래 기준을 전면 폐지하고 <strong>모든 가상자산 이전거래에 대해 송·수신인 신원정보 제공 의무를 의무화</strong>함.</p>
                <p>• 수취 사업자는 필수 정보가 누락된 경우 정보 제공을 요청하거나 거래를 거절해야 하는 확인 의무를 부담.</p>
              </div>
            </li>
            <li><strong>가상자산사업자(VASP) 대주주 적격성 심사제 도입:</strong>
              <div class="sub-bullet-box">
                <p>• 대표자·임원 위주의 심사에서 <strong>최대주주 및 주요주주(법인인 경우 대표자 포함)까지 대주주 심사 범위 확장</strong>.</p>
                <p>• 부채비율 200% 이하 유지 요건 신설 및 범죄경력 심사 대상 법률을 10개(마약거래방지법, 공정거래법, 조세범처벌법 등)로 대폭 확대.</p>
              </div>
            </li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>실명계좌 발급 은행의 거래소 정기 실사 항목 개편:</strong> 제휴 가상자산거래소에 대한 정기 위험평가 시 대주주 적격성, 부채비율 200% 충족 여부 및 내부통제 체계를 철저히 실사해야 함.</li>
              <li><strong>소액 분산 송금(스머핑) 모니터링 고도화:</strong> 트래블룰 기준 금액 폐지에 따라 규제 회피 목적의 소액 쪼개기 거래를 탐지하는 FDS 시나리오를 정밀하게 재구축해야 함.</li>
              <li><strong>가상자산-원화 연계 의심거래보고(STR) 연계:</strong> 거래소 입출금 패턴과 은행 원화 계좌 간의 단기 급증 이상 이체에 대해 즉각적인 STR 보고 프로세스를 가동해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 02 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">02. FATF, 국경 간 신속결제 투명성 제고를 위한 권고기준 16(R.16) 개정 지침 의견수렴 (‘26.8.21)</div>
          </div>
          
          <div class="section-subtitle">[1] 발간 배경 및 개요</div>
          <ul class="content-list">
            <li>국제자금세탁방지기구(FATF)는 국경 간 신속 결제 시스템(FPS) 확산에 대응하여 <strong>전신송금 투명성을 규율하는 '권고기준 16(R.16)' 개정 지침 초안 공청회를 8월 21일 마감</strong>함.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 개정 방향 및 통제 요구사항</div>
          <ul class="content-list">
            <li><strong>지급결제 메시지 표준화(ISO 20022):</strong> 송금인·수취인의 성명, 계좌번호, 고유 식별번호(주민번호/LEI)를 결제 체인 전 과정에서 누락 없이 전달하도록 규정.</li>
            <li><strong>중간 매개기관(Intermediary PSP) 통제 강화:</strong> 국경 간 신속 결제 시 중간 결제대행 기관도 필수 정보 누락 여부를 실시간 검증하고 의심거래 시 즉각 보고 의무 부과.</li>
            <li><strong>실시간 결제 전(Pre-transaction) 스크리닝 요구:</strong> 결제 체결 전 단계에서의 제재 및 이상거래 실시간 필터링 기술 적용 권고.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>외환 전문(ISO 20022) AML 데이터 무결성 검증:</strong> 신속 해외송금 및 외환 결제 처리 시 송수신인 식별 정보가 완전하게 포함되어 있는지 실시간 검증하는 시스템 필터를 구축해야 함.</li>
              <li><strong>실시간 FDS 및 제재 스크리닝 처리 속도 개선:</strong> 신속결제 환경에 맞추어 결제 지연 없이 제재 대상자 및 고위험 사기 계좌를 탐지할 수 있도록 스크리닝 엔진 성능을 고도화해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 03 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category sanctions">Sanctions / AML</span>
            <div class="card-title">03. 美 OFAC, ICC 관련 일반면허(GL 12) 발급 및 글로벌 SDN 제재 목록 갱신 (‘26.8.18)</div>
          </div>
          
          <div class="section-subtitle">[1] 제재 추진 경과 및 주요 발표 내용</div>
          <ul class="content-list">
            <li>미국 재무부 해외자산통제국(OFAC)은 8월 18일 <strong>국제형사재판소(ICC) 관련 제재 대상자와의 거래 정리를 지원하기 위한 일반면허(GL 12)를 발급</strong>함.</li>
            <li>아울러 중동 및 테러 지원 네트워크 연계 개인 및 법인을 특별지정제재(SDN) 목록에 추가 등재하고 최신 식별정보를 갱신함.</li>
          </ul>

          <div class="section-subtitle">[2] 핵심 제재 통제 사항</div>
          <ul class="content-list">
            <li><strong>일반면허 유예 조건 준수:</strong> GL 12의 허용 범위와 유예 기간을 충족하지 않은 거래에 대해 미국 금융망 접근을 원천 차단.</li>
            <li><strong>테러 지원 및 우회 조달망 차단:</strong> 제재 대상자와 연계된 페이퍼컴퍼니와의 모든 금융 거래 금지 및 미국 내 자산 동결 조치.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>SDN 리스트 실시간 동기화 및 오탐 관리:</strong> OFAC의 최신 제재 리스트 갱신 데이터를 제재 스크리닝 엔진에 즉각 반영하여 당일 외환 송금 및 무역금융 거래를 철저히 차단해야 함.</li>
              <li><strong>일반면허(GL) 적용 거래의 적격성 심사:</strong> 제재 대상 연계 거래 중 일반면허(GL 12 등) 적용을 주장하는 거래에 대해 법적 요건 및 기한 충족 여부를 정밀 심사(EDD)해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 04 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">04. EU AMLA 및 주요 회원국, 국가 AML 종합전략 발표 및 단일규정집(Single Rulebook) 대비 (‘26.8.17)</div>
          </div>
          
          <div class="section-subtitle">[1] 추진 배경 및 개요</div>
          <ul class="content-list">
            <li>2027년 7월 전면 시행되는 <strong>EU 단일 자금세탁방지 규정집(AMLR Single Rulebook)과 신설 AMLA 체계</strong>에 발맞추어, 아일랜드 등 EU 주요 회원국이 국가 차원의 <strong>제1차 AML/CFT 종합 전략을 8월 17일 공식 발표</strong>함.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 정책 방향 및 핵심 규율 사항</div>
          <ul class="content-list">
            <li><strong>고위험 분야(가상자산·사모펀드·부동산) 집중 통제:</strong> 현금 거래 한도 규제 강화(최대 1만 유로) 및 1천 유로 이상 가상자산 거래에 대한 전면 실사 의무화.</li>
            <li><strong>법인 실소유자(BO) 중앙 레지스트리 실시간 검증:</strong> 페이퍼컴퍼니를 악용한 조세 회피 및 자금세탁 방지를 위한 EU 전역 데이터베이스 상호 연계 추진.</li>
            <li><strong>글로벌 금융회사 대상 국경 간 통합 검사:</strong> EU 역내 다국적 금융그룹에 대해 AMLA와 회원국 당국 간 합동 검사 프레임워크 구축.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>유럽 진출 국내 지점의 규제 조기 정합성 확보:</strong> 2027년 전면 시행되는 EU AMLR 및 AMLA 기준에 부합하도록 현지 지점의 내부통제 규정 및 고객확인 절차를 상향 표준화해야 함.</li>
              <li><strong>역외 투자 펀드 및 고위험 자산 심사 강화:</strong> 유럽계 법인 및 펀드 고객과의 거래 시 실소유자 정보(BO)를 중앙 레지스트리와 대조 검증하는 절차를 내재화해야 함.</li>
            </ul>
          </div>
        </div>

        <div class="footer">
          본 상세 보고서는 AML &amp; Sanctions Weekly Insight 시스템을 통해 생성 및 발송되었습니다.
        </div>
      </div>
    </body>
    </html>
    """

    # 로컬 보고서 파일 저장 (TXT 및 HTML)
    report_dir = Path(__file__).resolve().parent / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    
    txt_path = report_dir / "aml_report_20260817_week3.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"제목: {subject}\n\n{body_text}")
        
    html_path = report_dir / "aml_report_20260817_week3.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(body_html)
        
    print(f"로컬 보고서 저장 완료 ->\n  - TXT: {txt_path}\n  - HTML: {html_path}")

    # 이메일 메시지 구성 및 전송
    msg = MIMEMultipart("mixed")
    msg["From"] = f"자금세탁방지본부 CoP <{SMTP_EMAIL}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject

    msg_body = MIMEMultipart("alternative")
    part1 = MIMEText(body_text, "plain", "utf-8")
    part2 = MIMEText(body_html, "html", "utf-8")
    msg_body.attach(part1)
    msg_body.attach(part2)
    msg.attach(msg_body)

    print(f"[SMTP 전송 시작] 대상: {', '.join(RECIPIENTS)}")
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, RECIPIENTS, msg.as_string())
        server.quit()
        print("[상세 이메일 발송 성공] 2026년 8월 3주차 보고서가 성공적으로 발송되었습니다.")
        return True
    except Exception as e:
        print(f"[이메일 발송 오류] {e}")
        return False

if __name__ == "__main__":
    send_august_week3_insight_email()
