import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENTS

def send_detailed_week2_insight_email():
    subject = "[AML & Sanctions Weekly Insight] 2026년 8월 2주차 자금세탁방지 주요 공시 상세 보고서"
    
    # 1. Plain Text Version (Full Detailed)
    body_text = """[AML & Sanctions Weekly Insight] 2026년 8월 2주차

자금세탁방지본부 CoP
수집 및 분석 대상 주차: 2026년 8월 2주차 (2026.08.10 ~ 2026.08.14)

================================================================================
■ 8월 2주차 주요 공시 목차
================================================================================
01 | [AML] 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)
02 | [AML] KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 및 운영 현황 분석 (‘26.8.10)
03 | [AML] FinCEN, 기업 투명성법에 따른 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)
04 | [Sanctions/AML] 글로벌 감독기구(FATF/OFAC/EBA), 초국경 금융사기 및 자금세탁 차단 공동 가이드라인 발표 (‘26.8.13)

================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================

--------------------------------------------------------------------------------
[AML] 01. 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)
--------------------------------------------------------------------------------
[1] 개정 배경 및 개요
▪ 가상자산사업자(VASP)의 진입 장벽을 정비하고 가상자산을 악용한 자금세탁 및 불법 자금 유출을 방지하기 위한 「특정 금융거래정보의 보고 및 이용 등에 관한 법률(특금법) 시행령」 개정안이 국무회의에서 의결되어 2026년 8월 20일(목)부터 본격 시행될 예정임.

[2] 주요 개정 내용
① 대주주 적격성 심사 대상 및 신고 불수리 요건 대폭 강화
- 기존 최대주주 및 주요 주주 중심 심사에서 '대표이사 또는 이사의 과반수를 선임한 주주', '최대주주가 법인인 경우 해당 법인의 최대주주 및 대표자'까지 심사 대상 범위를 획기적으로 확대함.
- 사업자의 재무건전성 및 사회적 신용(금융관련 법령 위반 여부), 임원 및 대주주의 결격사유, 전산 설비 및 내부통제 기준 마련 여부를 명문화하여 부적격 사업자의 시장 진입을 원천 차단함.

② 가상자산 이전거래(트래블룰) 전면 확대 및 자체 의심거래 관리체계 의무화
- 현행 100만원 이상 거래에만 적용되던 트래블룰 기준 금액을 전면 폐지하여, '모든 가상자산 이전거래'로 송수신인 신원정보 제공 의무를 확대함.
- 해외 비신고 가상자산사업자 및 개인지갑(Unhosted Wallet)과의 거래는 위험도 평가에 따라 입출금 허용 범위 및 추가 본인확인을 차등화함.
- 건당 1천만원 이상 가상자산 이전거래에 대해서는 실시간 이상패턴 감지 등 자체 의심거래(STR) 관리체계를 구축·운영하도록 법적 의무를 부과함.

③ 감독·제재 실효성 제고 및 고객확인의무 명확화
- 금융정보분석원장의 퇴직 임직원에 대한 제재조치 통보 권한을 금융감독원 등 검사수탁기관에 위탁하여 검사 처리의 신속성을 확보함.
- 고객의 거래 목적, 실명계좌 보유 여부, 자금 원천 등 고객 특성과 위험도에 따른 강화된 고객확인(EDD) 절차 및 이행 방식을 구체적으로 규정함.

▶ [시사점 및 금융권 대응 방향]
- 실명확인계좌 발급 은행의 책임 가중: 제휴 가상자산거래소에 대한 은행 측 정기 위험평가 시 대주주 적격성, 내부통제 적정성 및 전산 인프라 실사 항목을 전면 개편해야 함.
- 트래블룰 솔루션 및 소액 쪼개기 거래 감시 강화: 트래블룰 기준 금액 폐지에 따라 소액 분산 송금(스머핑)을 통한 규제 회피를 차단하고, 개인지갑 화이트리스트 검증 로직을 고도화해야 함.
- 의심거래 모니터링(STR) 시나리오 재설계: 거래소 연계 가상자산 입출금 패턴과 은행 원화 계좌 간의 이상 이체(단기 급증, 다계좌 분산 등)를 실시간 연계 탐지하는 룰셋 구축이 시급함.


--------------------------------------------------------------------------------
[AML] 02. KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 및 운영 현황 (‘26.8.10)
--------------------------------------------------------------------------------
[1] 회의 배경 및 개요
▪ 금융정보분석원(KoFIU)은 경찰청, 금융감독원, 은행연합회 및 주요 금융회사와 함께 지난 6월 30일 도입된 '신종피싱 의심계좌 임시거래정지제도'의 1개월간 운영 실적을 점검하고 범죄유형별 피해 차단 성과를 공유하는 회의를 개최함.

[2] 1개월간 주요 성과 및 범죄 유형 통계
① 임시조치 및 거래정지 실적
- 제도 시행 후 약 한 달간 금융회사가 모니터링을 통해 임시조치한 건수는 총 4,935건에 달함.
- 이 중 3,750건(약 76%)에 대해 특금법상 '강화된 고객확인(EDD)' 대상으로 분류하여 선제적 임시거래정지를 단행함으로써 약 수백억 원 규모의 2차 피해 확산을 차단함.

② 신종 금융범죄 유형별 분석
- 로맨스스캠(투자유인형 사기): 41% (1,527건)로 가장 큰 비중 차지 (SNS 친분 형성 후 가짜 코인/선물 투자 유도)
- 노쇼·대리구매 사기: 37% (1,376건) (소상공인 대상 대량 주문 가장 사기 및 가짜 결제대행 링크 유포)
- 팀미션·부업 알바 사기: 22% (847건) (단순 리뷰 작성/미션 수행 후 포인트 환전 빙자 자금 편취)

③ 향후 제도 정착 계획
- 전기통신금융사기 특별법 개정을 통해 통신사기피해환급법과의 법적 사각지대를 해소하고, 금융권-수사기관 간 24시간 실시간 이상계좌 정보공유 핫라인을 고도화할 방침임.

▶ [시사점 및 금융권 대응 방향]
- FDS(이상금융거래탐지시스템) 룰셋 즉시 업데이트: 비대면 계좌 개설 직후 단기 고액 입금, SNS 기반 투자 권유 이체, 단시간 다수 소액 입금 후 일괄 인출 등 신종 스캠 시나리오를 FDS 룰에 즉각 반영해야 함.
- AML 프로세스와 민생범죄 차단 연계: FDS 탐지 계좌에 대해 즉시 강화된 고객확인(EDD)을 적용하고 자금 원천 및 거래 목적 소명 요구, 불응 시 즉각 STR(의심거래보고)을 제출하는 유기적 협업 체계 확립 필요.
- 고객 소명 대응 프로세스 표준화: 정당한 거래자의 불편을 최소화하고 민원을 방어하기 위한 신속 소명 확인 및 거래정지 해제 매뉴얼 정비가 요구됨.

* [각주] 신종피싱 거래정지제도: 통신사기피해환급법상 보이스피싱에 해당하지 않는 재화·용역 거래 가장 사기(로맨스스캠, 쇼핑몰 사기 등)에 대해서도 신속하게 계좌 지급정지가 가능하도록 특금법상 고객확인 권한을 연계한 제도.


--------------------------------------------------------------------------------
[AML] 03. FinCEN, 기업 투명성법에 따른 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)
--------------------------------------------------------------------------------
[1] 추진 경과 및 최종 규칙 발표
▪ 미국 재무부 산하 금융범죄단속네트워크(FinCEN)는 기업 투명성법(Corporate Transparency Act, CTA)에 따라 시행되던 미국 기업 및 미국인의 실소유자 정보(BOI, Beneficial Ownership Information) 신고 의무를 완전히 면제하는 최종 규칙(Final Rule)을 8월 11일 확정 발표함.

[2] 핵심 결정 사항
① 미국 내 설립 기업 및 미국인 대상 전면 면제
- 3천만 개 이상의 미국 중소기업 및 스타트업에 부과되었던 행정적·재정적 부담과 위헌 소송 논란을 해소하기 위해 미국 법인 및 미국인에 대한 BOI 보고 의무를 완전 폐지함.
- 이미 FinCEN ID를 발급받은 미국인의 정보 변경/수정 보고 의무가 면제되며, 기 제출된 실소유자 데이터베이스는 영구 파기될 예정임.

② 외국 법인에 대한 차등 적용
- 미국 내 사업자 등록을 마친 외국 법인(Foreign Entities)의 외국인 실소유자 신고 의무는 일부 유지되나, 외국 법인 내 미국인 지분권자나 미국인 회사 설립자에 대한 정보 보고 의무는 면제됨.

▶ [시사점 및 금융권 대응 방향]
- 미국 중앙 BOI 레지스트리 활용 불가에 따른 자체 CDD/EDD 역량 확충: 미국 정부의 공식 실소유자 데이터베이스를 통한 검증이 불가능해짐에 따라, 미국계 법인 고객에 대해 금융기관이 주주명부, 정관, 실질지배자 확인서를 직접 징구하여 검증하는 독자적 확인 비용이 대폭 증가함.
- 글로벌 규제 불일치(Regulatory Arbitrage) 대응: FATF 및 EU, 한국 등 전 세계적인 실소유자 투명성 강화 기조와 미국의 규제 완화 간 괴리로 인해 다국적 기업 고객 실사 시 국가별 상이한 기준을 적용해야 하는 실무적 복잡성 심화.
- 역외 유령회사(페이퍼컴퍼니) 자금세탁 위험 재부각: 델라웨어, 와이오밍 등 미국 역외 법인을 악용한 자금은닉 위험이 다시 높아지므로, 미국계 법인과의 고액 국경 간 거래 시 강화된 고객확인(EDD)을 철저히 집행해야 함.


--------------------------------------------------------------------------------
[Sanctions/AML] 04. 글로벌 감독기구(FATF/OFAC/EBA), 초국경 금융사기 및 자금세탁 차단 공동 가이드라인 발표 (‘26.8.13)
--------------------------------------------------------------------------------
[1] 글로벌 공조 배경
▪ 국제자금세탁방지기구(FATF), 유럽은행감독청(EBA), 미국 해외자산통제국(OFAC) 및 주요국 FIU는 최근 동남아 및 중동 거점 초국경 조직범죄단의 사이버 스캠, 불법 온라인 도박, 가상자산 믹싱을 결합한 대규모 자금세탁에 대응하기 위해 다자간 실시간 공조 및 규제 기준을 발표함.

[2] 핵심 권고 및 통제 기준
- 가상자산 믹서(Mixer) 및 프라이버시 코인 취급 거래소와의 직간접 거래 차단 및 거래 거절 권고.
- 국경 간 전자상거래 정산 시 해외 결제대행(PG) 업체의 하위 가맹점 실거래 품목 및 대금 흐름 전수 검증 의무화.
- 2차 제재(Secondary Sanctions) 대상국(러시아, 이란 등)과 연계된 우회 결제망 및 제3국 페이퍼컴퍼니 경유 거래에 대한 실시간 모니터링 기준 제시.

▶ [시사점 및 금융권 대응 방향]
- 해외 송금 및 결제대행(PG) 정산 FDS 모니터링 고도화: 해외 가맹점 실거래 품목과 송금 총액의 정합성을 검증하고, 해외 PG사 정산금의 불법 외화유출 이상징후 점검을 강화해야 함.
- 제재 스크리닝 시스템의 우회 경로 탐지력 제고: 복합 지분구조(50% Rule) 및 제3국 위장 법인을 통한 우회 거래를 실시간으로 스크리닝할 수 있도록 제재 필터링 엔진을 최신화해야 함.
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
          <span class="badge-date">2026년 8월 2주차 상세 보고서 (2026.08.10 ~ 2026.08.14)</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📋 8월 2주차 주요 공시 및 핵심 의제</div>
          <ol class="toc-list">
            <li><strong>[AML]</strong> 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)</li>
            <li><strong>[AML]</strong> KoFIU, 신종피싱 의심계좌 거래정지제도 점검회의 개최 및 성과 분석 (‘26.8.10)</li>
            <li><strong>[AML]</strong> FinCEN, 기업 투명성법(CTA)에 따른 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)</li>
            <li><strong>[Sanctions/AML]</strong> 글로벌 감독기구(FATF/OFAC/EBA), 초국경 금융사기 및 자금세탁 차단 공동 가이드라인 발표 (‘26.8.13)</li>
          </ol>
        </div>

        <!-- Card 01 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">01. 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)</div>
          </div>
          
          <div class="section-subtitle">[1] 개정 배경 및 개요</div>
          <ul class="content-list">
            <li>가상자산사업자(VASP)의 진입 심사를 대폭 강화하고 가상자산 이전거래의 투명성을 제고하기 위한 <strong>「특금법 시행령」 개정안이 국무회의에서 의결</strong>되어, <strong>2026.8.20(목)부터 본격 시행</strong>됨.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 개정 내용 상세</div>
          <ul class="content-list">
            <li><strong>대주주 적격성 심사 대상 확대 및 신고 불수리 요건 구체화:</strong>
              <div class="sub-bullet-box">
                <p>• <strong>심사 대상 확대:</strong> 대표이사 또는 이사의 과반수를 선임한 주주, 최대주주가 법인인 경우 해당 법인의 최대주주 및 대표자까지 대주주 범위로 확장.</p>
                <p>• <strong>불수리 요건 명문화:</strong> 사업자의 재무건전성 및 사회적 신용(금융관계법령 위반 여부), 임원·대주주 자격 요건, 전문인력·전산보안 등 내부통제 체계 구축 기준 신설.</p>
              </div>
            </li>
            <li><strong>가상자산 이전거래(트래블룰) 전면 확대 및 자체 의심거래 관리체계 구축:</strong>
              <div class="sub-bullet-box">
                <p>• <strong>트래블룰 기준 폐지:</strong> 기존 100만원 이상 거래 기준을 전면 폐지하여 <strong>모든 이전거래에 대해 송·수신인 정보 제공 의무화</strong>.</p>
                <p>• <strong>개인지갑 거래 차등화:</strong> 해외 비신고 사업자 및 개인지갑(Unhosted Wallet) 거래는 위험평가 결과에 따라 허용 범위 차등 적용.</p>
                <p>• <strong>1천만원 이상 거래 관리:</strong> 건당 1천만원 이상 거래 시 자체 이상거래 감지 및 의심거래(STR) 관리체계를 의무적으로 구축·운영.</p>
              </div>
            </li>
            <li><strong>감독·제재 권한 위탁 및 고객확인(CDD) 기준 정교화:</strong> 퇴직 임직원 제재조치 통보 권한을 검사수탁기관(금감원 등)에 위탁하고, 고객 특성과 위험도에 따른 고객확인의무 이행 기준을 명확히 규정.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>실명계좌 발급 은행의 리스크 평가 강화:</strong> 제휴 가상자산거래소에 대한 은행의 정기 위험평가 시 대주주 적격성 및 내부통제 체계 실사 기준을 대폭 강화해야 함.</li>
              <li><strong>소액 쪼개기(스머핑) 회피 차단:</strong> 트래블룰 전면 확대에 따라 소액 분산 거래를 탐지하는 모니터링 로직을 구축하고, 개인 지갑 출금 시 화이트리스트 주소 검증을 강화해야 함.</li>
              <li><strong>원화-가상자산 연계 FDS 모니터링:</strong> 은행 원화 계좌와 거래소 간 이상 입출금(단기 급증 이체 후 즉시 코인 매수 등)을 실시간 연계 탐지하는 시나리오 설계가 필수적임.</li>
            </ul>
          </div>
        </div>

        <!-- Card 02 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">02. KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 및 성과 분석 (‘26.8.10)</div>
          </div>
          
          <div class="section-subtitle">[1] 제도 운영 경과 및 1개월간 실적</div>
          <ul class="content-list">
            <li>금융정보분석원(KoFIU)은 지난 6월 30일 시행된 '신종피싱 의심계좌 거래정지제도'의 1개월 운영 실적을 점검함.</li>
            <li>시행 이후 금융회사가 임시조치한 <strong>총 4,935건 중 3,750건(약 76%)</strong>에 대해 특금법상 강화된 고객확인(EDD) 대상으로 분류하여 <strong>선제적 임시거래정지 조치</strong> 완료.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 범죄 유형별 분포</div>
          <ul class="content-list">
            <li><strong>로맨스스캠(투자사기형):</strong> 약 41% (1,527건) 차지 (SNS 친분 형성 후 가짜 투자 플랫폼 입금 유도)</li>
            <li><strong>노쇼·대리구매 사기:</strong> 약 37% (1,376건) 차지 (소상공인 대상 대량 주문 가장 후 결제대행 링크 유도)</li>
            <li><strong>팀미션·부업 사기:</strong> 약 22% (847건) 차지 (단순 미션 수행 후 고수익 미끼 자금 편취)</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>신종 사기 특화 FDS 룰셋 고도화:</strong> 비대면 개설 직후 고액 입금, SNS 투자 유인형 이체, 단시간 다수 소액 입금 후 일괄 출금 패턴을 FDS에 즉시 반영.</li>
              <li><strong>FDS 탐지-EDD 적용-STR 보고의 유기적 연계:</strong> 의심계좌 탐지 시 즉시 거래 목적 소명을 요청하고, 불응 시 STR을 즉각 보고하는 협업 프로세스 확립.</li>
              <li><strong>선의의 피해자 방어 및 소명 매뉴얼 정비:</strong> 정당한 거래 고객의 민원 예방을 위한 신속 해제 검증 가이드라인 마련 필요.</li>
            </ul>
          </div>
          <div class="footnote">* 신종피싱 거래정지제도: 통신사기피해환급법상 보이스피싱에 해당하지 않는 '재화·용역 거래 가장 사기'에 대해서도 특금법상 고객확인 권한을 연계해 신속 거래정지가 가능하도록 한 제도.</div>
        </div>

        <!-- Card 03 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">03. FinCEN, 기업 투명성법에 따른 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)</div>
          </div>
          
          <div class="section-subtitle">[1] 개정 배경 및 핵심 발표 내용</div>
          <ul class="content-list">
            <li>미국 FinCEN은 기업 투명성법(CTA)에 따라 시행되던 미국 기업 및 미국인의 실소유자 정보(BOI) 신고 의무를 완전히 면제하는 최종 규칙(Final Rule)을 확정 발표함.</li>
            <li>중소기업 및 스타트업의 과도한 행정·비용 부담 경감을 위한 조치로, <strong>미국 내 설립된 기업 및 미국인은 실소유자 신고 의무에서 전면 제외</strong>됨.</li>
            <li>기 제출된 미국인 실소유자 정보 및 설립자 데이터는 영구 삭제 예정이며, 미국 등록 외국 법인의 외국인 실소유자 신고 의무만 일부 유지됨.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>미국 중앙 DB 활용 불가에 따른 독자적 CDD/EDD 역량 확충:</strong> 미국 정부의 중앙 BOI 레지스트리 조회가 불가능해짐에 따라, 미국계 법인 고객에 대해 주주명부·정관을 직접 징구하여 실소유자를 자체 검증해야 함.</li>
              <li><strong>글로벌 규제 불일치 대응:</strong> FATF/EU/한국 등 실소유자 투명성을 강화하는 글로벌 기조와 미국의 규제 완화 간 괴리에 따른 다국적 기업 실무 복잡성 관리 필요.</li>
              <li><strong>미국 역외 유령회사(페이퍼컴퍼니) 자금세탁 리스크 경계:</strong> 델라웨어 등 미국 역외 법인을 악용한 자금은닉에 대비해 미국계 법인과의 국경 간 거래 시 강화된 고객확인(EDD) 집행.</li>
            </ul>
          </div>
        </div>

        <!-- Card 04 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category sanctions">Sanctions / AML</span>
            <div class="card-title">04. 글로벌 감독기구(FATF/OFAC/EBA), 초국경 금융사기 및 자금세탁 차단 공동 가이드라인 발표 (‘26.8.13)</div>
          </div>
          
          <div class="section-subtitle">[1] 주요 권고 및 통제 기준</div>
          <ul class="content-list">
            <li>FATF, EBA, OFAC 및 주요국 FIU는 초국경 조직범죄, 불법 온라인 도박 및 가상자산 믹싱을 결합한 대규모 자금세탁 차단을 위한 다자간 실시간 공조 기준을 발표함.</li>
            <li>가상자산 믹서(Mixer) 및 프라이버시 코인 취급 거래소와의 직간접 거래 차단 권고.</li>
            <li>해외 결제대행(PG) 업체의 하위 가맹점 실거래 품목 검증 의무화 및 2차 제재(Secondary Sanctions) 대상국 우회 결제망 실시간 필터링 요구.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>해외 송금 및 외화 결제 FDS 필터링 고도화:</strong> 해외 PG사 정산금의 실거래 품목 검증과 무역대금 가장 불법 외화유출 이상징후 점검 강화.</li>
              <li><strong>제재 스크리닝 시스템의 우회 경로 탐지력 제고:</strong> 복합 지분구조(50% Rule) 및 제3국 위장 법인을 통한 우회 거래를 실시간으로 탐지할 수 있도록 스크리닝 엔진 고도화.</li>
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

    msg = MIMEMultipart("alternative")
    msg["From"] = f"자금세탁방지본부 CoP <{SMTP_EMAIL}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject

    part1 = MIMEText(body_text, "plain", "utf-8")
    part2 = MIMEText(body_html, "html", "utf-8")
    msg.attach(part1)
    msg.attach(part2)

    print(f"[SMTP 전송 시작] 대상: {', '.join(RECIPIENTS)}")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_EMAIL, SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL, RECIPIENTS, msg.as_string())
    server.quit()
    print("[상세 이메일 발송 완료] 성공적으로 발송되었습니다.")

if __name__ == "__main__":
    send_detailed_week2_insight_email()
