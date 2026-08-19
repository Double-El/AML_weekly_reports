import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENTS

def send_july_week4_insight_email():
    subject = "[AML & Sanctions Weekly Insight] 2026년 7월 4주차 자금세탁방지 주요 공시 상세 보고서"
    
    # 1. Plain Text Version (Full Detailed)
    body_text = """[AML & Sanctions Weekly Insight] 2026년 7월 4주차

자금세탁방지본부 CoP
수집 및 분석 대상 주차: 2026년 7월 4주차 (2026.07.27 ~ 2026.07.31)

================================================================================
■ 7월 4주차 주요 공시 목차
================================================================================
01 | [AML] KoFIU, FATF 아시아·태평양 지역기구(APG) 제28차 연차총회 참석 및 초국경 금융범죄 대응 논의 (‘26.7.27~7.31)
02 | [AML] 금융위·금감원, '가상자산 대여 서비스 가이드라인' 마련 민관 합동 TF 출범 (‘26.7.31)
03 | [Sanctions/AML] 美 OFAC, 제재 현대화 이니셔티브 2차 발표 및 대 이란 제재망 집중 지정 (‘26.7.27, ‘26.7.29~7.30)
04 | [AML] MAS(싱가포르 통화청), 디지털 결제 토큰(DPT) 서비스 제공자 대상 AML/CFT 규정 및 지침 개정 (‘26.7.31)

================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================

--------------------------------------------------------------------------------
[AML] 01. KoFIU, FATF 아시아·태평양 지역기구(APG) 제28차 연차총회 참석 및 초국경 금융범죄 대응 논의 (‘26.7.27~7.31)
--------------------------------------------------------------------------------
[1] 회의 배경 및 개요
▪ 금융정보분석원(KoFIU)은 7월 27일부터 31일까지 브루나이에서 개최된 국제자금세탁방지기구(FATF) 산하 아시아·태평양 지역기구(APG) 제28차 연차총회에 참석하여 역내 41개 회원국 및 국제기구 대표단과 함께 초국경 금융범죄 대응 및 FATF 제5차 상호평가 체계 대응 방향을 논의함.

[2] 주요 논의 사항 및 성과
① 초국경 조직범죄 및 신종 사이버 스캠 대응 공조 강화
- 역내 회원국들은 사이버 사기, 인신매매 결합 스캠, 무역기반 자금세탁(TBML) 등 고도화되는 초국경 조직범죄 수익을 조기에 차단하고 몰수하기 위한 다자간 실시간 정보공유 및 수사공조를 대폭 강화하기로 합의함.
② 국내 신종피싱 거래정지제도 우수 사례 공유
- 한국 대표단은 지난 6월 30일부터 시행 중인 '신종피싱 의심계좌 임시거래정지제도'의 운영 성과와 범죄수익 조기 동결 프로세스를 소개하여 회원국들로부터 높은 평가를 받음.
③ FATF 제5차 상호평가 체계(Round 5) 대비
- 제5차 상호평가는 단순한 법령 구축 여부를 넘어 '실제 자금세탁 위험 차단 성과 및 감독의 실효성(Effectiveness)'을 중점 평가하므로, 금융회사의 실질적인 의심거래 탐지 역량과 위험기반 접근법(RBA) 내재화가 필수적임을 재확인함.

▶ [시사점 및 금융권 대응 방향]
- 초국경 사기·스캠 연계 자금 이동 모니터링 고도화: 해외 송금 및 환전 거래 중 고위험 스캠 의심 패턴(단기 급증, 다계좌 분산 송금 등)을 실시간 감지하는 FDS 시나리오를 정교화해야 함.
- RBA(위험기반접근법) 기반 실효성 입증 준비: 향후 FATF 상호평가 및 당국 수검에 대비해 형식적 규정 준수를 넘어 실제 이상거래 탐지·보고(STR) 및 조치 실적을 입증할 수 있는 통계 및 내부통제 증적 관리 체계를 확립해야 함.
- 유관기관과의 신속 공조 체계 구축: 초국경 범죄수익 은닉 차단을 위해 FIU 및 수사당국의 정보 제공 요청에 24시간 대응할 수 있는 전담 프로세스를 정비해야 함.


--------------------------------------------------------------------------------
[AML] 02. 금융위·금감원, '가상자산 대여 서비스 가이드라인' 마련 민관 합동 TF 출범 (‘26.7.31)
--------------------------------------------------------------------------------
[1] 추진 배경 및 개요
▪ 금융위원회와 금융감독원은 디지털자산거래소공동협의체(DAXA) 및 5대 원화 가상자산거래소와 함께 가상자산 대여(Lending)·예치 서비스의 건전한 시장 질서 확립과 이용자 피해 예방을 위한 '가상자산 대여 서비스 가이드라인' 민관 합동 TF를 출범하고 첫 회의를 개최함.

[2] 핵심 규율 방향 및 논의 내용
① 불공정 거래 및 과도한 레버리지 차단
- 가상자산 대여 서비스가 무분별한 레버리지 투자를 부추기거나 차명·불법 자금의 세탁 통로로 악용되는 것을 방지하기 위해 대여 한도 및 적정 담보비율 기준을 신설함.
② 사업자 건전성 및 이용자 자산 보호 기준 표준화
- 대여 자산의 분리 보관, 무단 재예치(Re-hypothecation) 제한, 사업자의 자산 건전성 공시 의무화를 추진함.
③ 자금출처 및 거래 목적 확인(EDD) 체계 마련
- 대여 서비스를 이용하는 고액 거래자에 대해 자금 원천 및 대여 목적 소명 절차를 의무화하여 미신고 파생상품 거래 및 불법 자금 유입을 선제적으로 차단함.

▶ [시사점 및 금융권 대응 방향]
- 가상자산 대여·파생 연계 계좌 모니터링 강화: 실명계좌 발급 은행은 제휴 거래소의 가상자산 대여 서비스 이용 고객 중 이상 고액 입출금 거래자에 대해 강화된 고객확인(EDD)을 실시하고 자금 흐름의 투명성을 점검해야 함.
- 제휴 거래소 내부통제 실사 항목 반영: 거래소에 대한 정기 위험평가 시 대여 자산 분리 보관 및 담보 관리 시스템의 적정성을 실사 평가 항목에 즉시 반영해야 함.
- 불법 자금세탁 우회 경로 차단: 가상자산 대여를 가장한 편법 증여, 조세 회피 및 불법 외화유출 시나리오를 FDS 및 STR 룰셋에 반영하여 이상거래 감시를 강화해야 함.


--------------------------------------------------------------------------------
[Sanctions/AML] 03. 美 OFAC, 제재 현대화 이니셔티브 2차 발표 및 대 이란 제재망 집중 지정 (‘26.7.27, ‘26.7.29~7.30)
--------------------------------------------------------------------------------
[1] 제재 추진 경과 및 주요 발표 내용
▪ 미국 재무부 해외자산통제국(OFAC)은 7월 27일 제재의 정확도와 실효성을 높이기 위한 '제재 현대화 이니셔티브(Sanctions Modernization Initiative)' 2차 조치를 단행하여 SDN 리스트에서 84개 대상(사망자, 해산 법인 등)을 정비하고 최신 식별정보를 갱신함.
▪ 이어 7월 29~30일 호르무즈 해협 불법 유류 갈취 및 밀수 네트워크, 마한 항공(Mahan Air) 및 이란 혁명수비대(IRGC) 연계 글로벌 조달망·자금세탁 네트워크에 속한 다수의 선박, 유령회사 및 금융 중개인을 대거 SDN으로 지정함.

[2] 핵심 제재 통제 사항
- 이란산 석유화학 제품 및 원유의 불법 해상 환적(STS Transfer), 선박 자동식별장치(AIS) 조작 행위와 연계된 해운사, 선박 및 제3국 페이퍼컴퍼니 자산 동결.
- 2차 제재(Secondary Sanctions) 경고: 제재 대상자와의 거래를 중개하거나 결제 서비스를 제공한 외국 금융기관에 대해 미국 금융망 접근 차단 등 강력한 세컨더리 제재 경고.

▶ [시사점 및 금융권 대응 방향]
- 제재 스크리닝(Sanctions Screening) 엔진 즉각 최신화: OFAC의 SDN 리스트 정비 및 신규 지정 데이터를 실시간 반영하여 오탐(False Positive)을 줄이고 정탐(True Match) 필터링 정확도를 제고해야 함.
- 해상 무역금융 및 선박 검증(Vessel Screening) 고도화: 수출입 선적서류(B/L) 심사 시 선박의 IMO 번호, 과거 기항지, 선박명 변경 이력 및 AIS 조작 여부를 철저히 검증해야 함.
- 제3국 경유 우회 결제 모니터링: 중동·동남아 소재 중개 무역상을 경유하는 외환 송금 거래 시 최종 실수요자(End-user) 및 원산지 증명서 검증을 강화하여 2차 제재 리스크를 사전에 차단해야 함.


--------------------------------------------------------------------------------
[AML] 04. MAS(싱가포르 통화청), 디지털 결제 토큰(DPT) 서비스 제공자 대상 AML/CFT 규정 및 지침 개정 (‘26.7.31)
--------------------------------------------------------------------------------
[1] 개정 배경 및 개요
▪ 싱가포르 통화청(MAS)은 결제서비스법(Payment Services Act, PSA) 개정에 따른 후속 조치로, 디지털 결제 토큰(DPT) 송금 및 수탁(Custody) 서비스를 제공하는 사업자 대상 AML/CFT 규정 및 지침을 7월 31일 개정 공표함.

[2] 주요 개정 내용
① 고객 실사(CDD) 및 지속적 모니터링 의무 대폭 강화
- DPT 서비스 제공자는 고객 온보딩 시 실소유자(Beneficial Owner) 식별뿐만 아니라 거래 목적 및 자금 원천에 대한 실질적 검증을 의무적으로 수행해야 함.
② 트래블룰(Travel Rule) 이행 요건 및 상대방 실사 의무 구체화
- 송금 VASP는 수취 VASP의 적격성을 사전에 평가해야 하며, 비신고 VASP 또는 개인지갑(Unhosted Wallet)으로의 이전 시 위험도에 따라 거래를 제한하거나 추가 본인인증을 적용해야 함.
③ 다자간 가상자산 믹싱 및 고위험 거래 통제
- 프라이버시 코인 및 믹서(Mixer)와 연계된 지갑 주소와의 거래를 엄격히 금지하고, 의심스러운 패턴 발생 시 즉각 싱가포르 금융정보분석원(STRO)에 STR을 제출하도록 규정함.

▶ [시사점 및 금융권 대응 방향]
- 동남아 주요 금융 허브 연계 외환·디지털자산 결제 심사 강화: 싱가포르 등 현지 규제 강화에 발맞추어 싱가포르 소재 VASP 및 핀테크 결제대행사와의 거래 시 상대방 실사(Counterparty Due Diligence) 체계를 정비해야 함.
- 트래블룰 및 블록체인 온체인 모니터링 연동: 가상자산 송수신 시 트래블룰 솔루션과 온체인 분석 툴(Chainalysis 등)을 연동하여 불법 믹서 경유 지갑 및 고위험 거래를 실시간 차단해야 함.
- 글로벌 규제 정합성 유지: 아시아 주요국 감독기관(한국 KoFIU, 싱가포르 MAS, 홍콩 HKMA 등)의 가상자산 규제 공조 강화에 대비하여 국내외 지점의 컴플라이언스 기준을 상향 표준화해야 함.
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
        .insight-body {{ font-size: 13.5px; color: #1e3a8a; line-height: 1.6; margin: 0; }}
        .insight-body li {{ margin-bottom: 6px; }}
        .insight-body li:last-child {{ margin-bottom: 0; }}
        
        .footnote {{ font-size: 12px; color: #64748b; margin-top: 16px; padding-top: 10px; border-top: 1px dashed #e2e8f0; line-height: 1.5; }}
        .footer {{ text-align: center; font-size: 12px; color: #94a3b8; margin-top: 48px; padding-top: 24px; border-top: 1px solid #e2e8f0; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <div class="sub-header">자금세탁방지본부 CoP | 주간 컴플라이언스 인텔리전스</div>
          <div class="title">AML &amp; Sanctions Weekly Insight</div>
          <span class="badge-date">2026년 7월 4주차 상세 보고서 (2026.07.27 ~ 2026.07.31)</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📋 7월 4주차 주요 공시 및 핵심 의제</div>
          <ol class="toc-list">
            <li><strong>[AML]</strong> KoFIU, FATF 아시아·태평양 지역기구(APG) 제28차 연차총회 참석 및 초국경 금융범죄 대응 논의 (‘26.7.27~7.31)</li>
            <li><strong>[AML]</strong> 금융위·금감원, '가상자산 대여 서비스 가이드라인' 마련 민관 합동 TF 출범 (‘26.7.31)</li>
            <li><strong>[Sanctions/AML]</strong> 美 OFAC, 제재 현대화 이니셔티브 2차 발표 및 대 이란 제재망 집중 지정 (‘26.7.27, ‘26.7.29~7.30)</li>
            <li><strong>[AML]</strong> MAS(싱가포르 통화청), 디지털 결제 토큰(DPT) 서비스 제공자 대상 AML/CFT 규정 및 지침 개정 (‘26.7.31)</li>
          </ol>
        </div>

        <!-- Card 01 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">01. KoFIU, FATF 아시아·태평양 지역기구(APG) 제28차 연차총회 참석 및 초국경 금융범죄 대응 논의 (‘26.7.27~7.31)</div>
          </div>
          
          <div class="section-subtitle">[1] 회의 배경 및 개요</div>
          <ul class="content-list">
            <li>금융정보분석원(KoFIU)은 7월 27일부터 31일까지 브루나이에서 개최된 국제자금세탁방지기구(FATF) 산하 <strong>아시아·태평양 지역기구(APG) 제28차 연차총회</strong>에 참석하여 역내 41개 회원국 및 국제기구 대표단과 함께 <strong>초국경 금융범죄 대응 및 FATF 제5차 상호평가 체계 대응 방향</strong>을 논의함.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 논의 사항 및 성과</div>
          <ul class="content-list">
            <li><strong>초국경 조직범죄 및 신종 사이버 스캠 대응 공조 강화:</strong>
              <div class="sub-bullet-box">
                <p>• 역내 회원국들은 사이버 사기, 인신매매 결합 스캠, 무역기반 자금세탁(TBML) 등 고도화되는 초국경 조직범죄 수익을 조기에 차단하고 몰수하기 위한 다자간 실시간 정보공유 및 수사공조를 대폭 강화하기로 합의함.</p>
              </div>
            </li>
            <li><strong>국내 신종피싱 거래정지제도 우수 사례 공유:</strong>
              <div class="sub-bullet-box">
                <p>• 한국 대표단은 지난 6월 30일부터 시행 중인 '신종피싱 의심계좌 임시거래정지제도'의 운영 성과와 범죄수익 조기 동결 프로세스를 소개하여 회원국들로부터 높은 평가를 받음.</p>
              </div>
            </li>
            <li><strong>FATF 제5차 상호평가 체계(Round 5) 대비:</strong>
              <div class="sub-bullet-box">
                <p>• 제5차 상호평가는 단순한 법령 구축 여부를 넘어 <strong>'실제 자금세탁 위험 차단 성과 및 감독의 실효성(Effectiveness)'</strong>을 중점 평가하므로, 금융회사의 실질적인 의심거래 탐지 역량과 위험기반 접근법(RBA) 내재화가 필수적임을 재확인함.</p>
              </div>
            </li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>초국경 사기·스캠 연계 자금 이동 모니터링 고도화:</strong> 해외 송금 및 환전 거래 중 고위험 스캠 의심 패턴(단기 급증, 다계좌 분산 송금 등)을 실시간 감지하는 FDS 시나리오를 정교화해야 함.</li>
              <li><strong>RBA(위험기반접근법) 기반 실효성 입증 준비:</strong> 향후 FATF 상호평가 및 당국 수검에 대비해 형식적 규정 준수를 넘어 실제 이상거래 탐지·보고(STR) 및 조치 실적을 입증할 수 있는 통계 및 내부통제 증적 관리 체계를 확립해야 함.</li>
              <li><strong>유관기관과의 신속 공조 체계 구축:</strong> 초국경 범죄수익 은닉 차단을 위해 FIU 및 수사당국의 정보 제공 요청에 24시간 대응할 수 있는 전담 프로세스를 정비해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 02 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">02. 금융위·금감원, '가상자산 대여 서비스 가이드라인' 마련 민관 합동 TF 출범 (‘26.7.31)</div>
          </div>
          
          <div class="section-subtitle">[1] 추진 배경 및 개요</div>
          <ul class="content-list">
            <li>금융위원회와 금융감독원은 디지털자산거래소공동협의체(DAXA) 및 5대 원화 가상자산거래소와 함께 가상자산 대여(Lending)·예치 서비스의 건전한 시장 질서 확립과 이용자 피해 예방을 위한 <strong>'가상자산 대여 서비스 가이드라인' 민관 합동 TF를 출범</strong>하고 첫 회의를 개최함.</li>
          </ul>

          <div class="section-subtitle">[2] 핵심 규율 방향 및 논의 내용</div>
          <ul class="content-list">
            <li><strong>불공정 거래 및 과도한 레버리지 차단:</strong>
              <div class="sub-bullet-box">
                <p>• 가상자산 대여 서비스가 무분별한 레버리지 투자를 부추기거나 차명·불법 자금의 세탁 통로로 악용되는 것을 방지하기 위해 대여 한도 및 적정 담보비율 기준을 신설함.</p>
              </div>
            </li>
            <li><strong>사업자 건전성 및 이용자 자산 보호 기준 표준화:</strong>
              <div class="sub-bullet-box">
                <p>• 대여 자산의 분리 보관, 무단 재예치(Re-hypothecation) 제한, 사업자의 자산 건전성 공시 의무화를 추진함.</p>
              </div>
            </li>
            <li><strong>자금출처 및 거래 목적 확인(EDD) 체계 마련:</strong>
              <div class="sub-bullet-box">
                <p>• 대여 서비스를 이용하는 고액 거래자에 대해 자금 원천 및 대여 목적 소명 절차를 의무화하여 미신고 파생상품 거래 및 불법 자금 유입을 선제적으로 차단함.</p>
              </div>
            </li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>가상자산 대여·파생 연계 계좌 모니터링 강화:</strong> 실명계좌 발급 은행은 제휴 거래소의 가상자산 대여 서비스 이용 고객 중 이상 고액 입출금 거래자에 대해 강화된 고객확인(EDD)을 실시하고 자금 흐름의 투명성을 점검해야 함.</li>
              <li><strong>제휴 거래소 내부통제 실사 항목 반영:</strong> 거래소에 대한 정기 위험평가 시 대여 자산 분리 보관 및 담보 관리 시스템의 적정성을 실사 평가 항목에 즉시 반영해야 함.</li>
              <li><strong>불법 자금세탁 우회 경로 차단:</strong> 가상자산 대여를 가장한 편법 증여, 조세 회피 및 불법 외화유출 시나리오를 FDS 및 STR 룰셋에 반영하여 이상거래 감시를 강화해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 03 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category sanctions">Sanctions / AML</span>
            <div class="card-title">03. 美 OFAC, 제재 현대화 이니셔티브 2차 발표 및 대 이란 제재망 집중 지정 (‘26.7.27, ‘26.7.29~7.30)</div>
          </div>
          
          <div class="section-subtitle">[1] 제재 추진 경과 및 주요 발표 내용</div>
          <ul class="content-list">
            <li>미국 재무부 해외자산통제국(OFAC)은 7월 27일 제재의 정확도와 실효성을 높이기 위한 <strong>'제재 현대화 이니셔티브(Sanctions Modernization Initiative)' 2차 조치</strong>를 단행하여 SDN 리스트에서 84개 대상(사망자, 해산 법인 등)을 정비하고 최신 식별정보를 갱신함.</li>
            <li>이어 7월 29~30일 <strong>호르무즈 해협 불법 유류 갈취 및 밀수 네트워크</strong>, <strong>마한 항공(Mahan Air) 및 이란 혁명수비대(IRGC) 연계 글로벌 조달망·자금세탁 네트워크</strong>에 속한 다수의 선박, 유령회사 및 금융 중개인을 대거 SDN으로 지정함.</li>
          </ul>

          <div class="section-subtitle">[2] 핵심 제재 통제 사항</div>
          <ul class="content-list">
            <li><strong>해상 불법 환적 및 제재 회피 수법 차단:</strong> 이란산 석유화학 제품 및 원유의 불법 해상 환적(STS Transfer), 선박 자동식별장치(AIS) 조작 행위와 연계된 해운사, 선박 및 제3국 페이퍼컴퍼니 자산 동결.</li>
            <li><strong>2차 제재(Secondary Sanctions) 경고:</strong> 제재 대상자와의 거래를 중개하거나 결제 서비스를 제공한 외국 금융기관에 대해 미국 금융망 접근 차단 등 강력한 세컨더리 제재 경고.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>제재 스크리닝(Sanctions Screening) 엔진 즉각 최신화:</strong> OFAC의 SDN 리스트 정비 및 신규 지정 데이터를 실시간 반영하여 오탐(False Positive)을 줄이고 정탐(True Match) 필터링 정확도를 제고해야 함.</li>
              <li><strong>해상 무역금융 및 선박 검증(Vessel Screening) 고도화:</strong> 수출입 선적서류(B/L) 심사 시 선박의 IMO 번호, 과거 기항지, 선박명 변경 이력 및 AIS 조작 여부를 철저히 검증해야 함.</li>
              <li><strong>제3국 경유 우회 결제 모니터링:</strong> 중동·동남아 소재 중개 무역상을 경유하는 외환 송금 거래 시 최종 실수요자(End-user) 및 원산지 증명서 검증을 강화하여 2차 제재 리스크를 사전에 차단해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 04 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">04. MAS(싱가포르 통화청), 디지털 결제 토큰(DPT) 서비스 제공자 대상 AML/CFT 규정 및 지침 개정 (‘26.7.31)</div>
          </div>
          
          <div class="section-subtitle">[1] 개정 배경 및 개요</div>
          <ul class="content-list">
            <li>싱가포르 통화청(MAS)은 결제서비스법(Payment Services Act, PSA) 개정에 따른 후속 조치로, <strong>디지털 결제 토큰(DPT) 송금 및 수탁(Custody) 서비스를 제공하는 사업자 대상 AML/CFT 규정 및 지침</strong>을 7월 31일 개정 공표함.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 개정 내용</div>
          <ul class="content-list">
            <li><strong>고객 실사(CDD) 및 지속적 모니터링 의무 대폭 강화:</strong> DPT 서비스 제공자는 고객 온보딩 시 실소유자(Beneficial Owner) 식별뿐만 아니라 거래 목적 및 자금 원천에 대한 실질적 검증을 의무적으로 수행해야 함.</li>
            <li><strong>트래블룰(Travel Rule) 이행 요건 및 상대방 실사 의무 구체화:</strong> 송금 VASP는 수취 VASP의 적격성을 사전에 평가해야 하며, 비신고 VASP 또는 개인지갑(Unhosted Wallet)으로의 이전 시 위험도에 따라 거래를 제한하거나 추가 본인인증을 적용해야 함.</li>
            <li><strong>다자간 가상자산 믹싱 및 고위험 거래 통제:</strong> 프라이버시 코인 및 믹서(Mixer)와 연계된 지갑 주소와의 거래를 엄격히 금지하고, 의심스러운 패턴 발생 시 즉각 싱가포르 금융정보분석원(STRO)에 STR을 제출하도록 규정함.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>동남아 주요 금융 허브 연계 외환·디지털자산 결제 심사 강화:</strong> 싱가포르 등 현지 규제 강화에 발맞추어 싱가포르 소재 VASP 및 핀테크 결제대행사와의 거래 시 상대방 실사(Counterparty Due Diligence) 체계를 정비해야 함.</li>
              <li><strong>트래블룰 및 블록체인 온체인 모니터링 연동:</strong> 가상자산 송수신 시 트래블룰 솔루션과 온체인 분석 툴(Chainalysis 등)을 연동하여 불법 믹서 경유 지갑 및 고위험 거래를 실시간 차단해야 함.</li>
              <li><strong>글로벌 규제 정합성 유지:</strong> 아시아 주요국 감독기관(한국 KoFIU, 싱가포르 MAS, 홍콩 HKMA 등)의 가상자산 규제 공조 강화에 대비하여 국내외 지점의 컴플라이언스 기준을 상향 표준화해야 함.</li>
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

    # 로컬 보고서 파일 저장
    report_dir = Path(__file__).resolve().parent / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "aml_report_20260727_week4.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"제목: {subject}\n\n{body_text}")
    print(f"로컬 보고서 저장 완료 -> {report_path}")

    # 이메일 메시지 구성 및 전송
    msg = MIMEMultipart("alternative")
    msg["From"] = f"자금세탁방지본부 CoP <{SMTP_EMAIL}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject

    part1 = MIMEText(body_text, "plain", "utf-8")
    part2 = MIMEText(body_html, "html", "utf-8")
    msg.attach(part1)
    msg.attach(part2)

    print(f"[SMTP 전송 시작] 대상: {', '.join(RECIPIENTS)}")
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, RECIPIENTS, msg.as_string())
        server.quit()
        print("[상세 이메일 발송 성공] 2026년 7월 4주차 보고서가 성공적으로 발송되었습니다.")
        return True
    except Exception as e:
        print(f"[이메일 발송 오류] {e}")
        return False

if __name__ == "__main__":
    send_july_week4_insight_email()
