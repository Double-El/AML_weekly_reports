import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENTS

def send_july_week3_insight_email():
    subject = "[AML & Sanctions Weekly Insight] 2026년 7월 3주차 자금세탁방지 주요 공시 상세 보고서"
    
    # 1. Plain Text Version (Full Detailed)
    body_text = """[AML & Sanctions Weekly Insight] 2026년 7월 3주차

자금세탁방지본부 CoP
수집 및 분석 대상 주차: 2026년 7월 3주차 (2026.07.20 ~ 2026.07.24)

================================================================================
■ 7월 3주차 주요 공시 목차
================================================================================
01 | [AML] FATF, 탈중앙화 금융(DeFi) 규제 및 자금세탁 방지 특별 보고서 발표 (‘26.7.21)
02 | [Sanctions/AML] 美 OFAC, 멕시코 카르텔(CJNG) 및 초국경 자금세탁망 50여 개 대상 대규모 제재 단행 (‘26.7.23)
03 | [AML] 英 FCA, 자산운용사 및 대체투자 펀드 대상 금융범죄(AML) 내부통제 점검 결과 발표 (‘26.7.22)
04 | [AML] 금융위·금감원, 「가상자산이용자보호법」 시행에 따른 이상거래 상시감시 및 AML 연계 체계 가동 (‘26.7.20)

================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================

--------------------------------------------------------------------------------
[AML] 01. FATF, 탈중앙화 금융(DeFi) 규제 및 자금세탁 방지 특별 보고서 발표 (‘26.7.21)
--------------------------------------------------------------------------------
[1] 발간 배경 및 개요
▪ 국제자금세탁방지기구(FATF)는 7월 21일 급격히 팽창하는 탈중앙화 금융(DeFi) 생태계에서의 자금세탁(ML), 테러자금조달(TF) 및 대량살상무기 확산금융(PF) 위험에 대응하기 위한 「DeFi 규제 과제 특별 보고서」를 공식 발표함.

[2] 핵심 내용 및 규제 판단 기준
① '통제 또는 중대한 영향력(COSI)' 기준 확립
- 명목상 탈중앙화를 표방하더라도 프로토콜 개발자, 거버넌스 토큰 집중 보유자, 관리자 키(Admin Key) 보유자 등이 실질적인 통제력이나 중대한 영향력을 행사하는 경우 FATF 권고기준(R.15)상 가상자산사업자(VASP) 규제 대상에 포함됨을 명문화함.
② 규제 사각지대 해소 및 글로벌 이행 촉구
- 전 세계 93%의 관할권이 아직 DeFi에 대한 자금세탁방지 규율 체계를 확립하지 못했음을 지적하며, 각국 규제당국에 기능적 위험기반 접근법(RBA)을 적용해 실질 지배자를 식별·감독할 것을 강력히 권고함.
③ 불법 자금세탁 수법 차단
- 스마트 컨트랙트 취약점 공격, 믹서(Mixer) 연계, 비호스팅 지갑 간 P2P 익명 자금 이동 등 신종 자금은닉 수법에 대한 선제적 감시 체계 구축을 요구함.

▶ [시사점 및 금융권 대응 방향]
- DeFi 프로토콜 연계 온체인 트랜잭션 감시 고도화: 블록체인 분석 솔루션을 활용하여 거래소 및 은행 연계 계좌에서 DeFi 프로토콜, 유동성 풀(Liquidity Pool)로 유출입되는 고위험 자금 흐름을 실시간으로 추적해야 함.
- 실질 지배력(COSI) 보유 법인 고객 실사 강화: DeFi 관련 사업을 영위하는 법인 고객에 대해 스마트 컨트랙트 관리 권한 및 거버넌스 구조를 심층 분석하는 강화된 고객확인(EDD) 절차를 수립해야 함.


--------------------------------------------------------------------------------
[Sanctions/AML] 02. 美 OFAC, 멕시코 카르텔(CJNG) 및 초국경 자금세탁망 50여 개 대상 대규모 제재 단행 (‘26.7.23)
--------------------------------------------------------------------------------
[1] 제재 배경 및 발표 내용
▪ 미국 재무부 해외자산통제국(OFAC)은 7월 23일 행정명령 E.O. 14059 및 E.O. 13224에 근거하여 멕시코의 악명 높은 범죄조직인 할리스코 신세대 카르텔(CJNG)과 연계된 50개 이상의 개인, 페이퍼컴퍼니 및 금융 중개 네트워크에 대해 사상 최대 규모의 특별지정제재(SDN)를 단행함.

[2] 주요 제재 대상 및 범죄 수법
① 다계층 복합 자금세탁 네트워크 차단
- 타임셰어(시계열 콘도 분양) 사기, 불법 부동산 개발업체, 허위 결제대행사를 통해 미국 시민들로부터 편취한 자금을 멕시코 및 역외 페이퍼컴퍼니로 은닉·세탁한 구조를 전면 적발함.
② 가상자산 및 환전 브로커 제재
- 불법 마약 및 사기 수익금을 USDT 등 스테이블코인으로 전환하여 국경 간 송금한 암호화폐 환전 브로커 및 계좌 명의인을 SDN 목록에 대거 등재함.
③ 강력한 2차 제재(Secondary Sanctions) 경고
- 제재 대상자와 금융 거래를 수행하거나 자금세탁을 지원한 제3국 금융기관에 대해 미국 금융망 접근을 원천 차단하는 세컨더리 제재 위험을 엄중 경고함.

▶ [시사점 및 금융권 대응 방향]
- SDN 제재 필터링 리스트 실시간 동기화: OFAC 신규 제재 명단(개인 30여 명, 법인 20여 개)을 글로벌 제재 스크리닝 엔진에 즉각 반영하여 당일 결제 및 외환 송금 거래를 철저히 차단해야 함.
- 중남미 및 역외 경유 해외송금 심사 강화: 부동산 투자, 회원권 결제, 컨설팅 명목의 중남미행 외환 송금 시 수취 법인의 실소유자 및 설립 목적을 정밀 검증(EDD)해야 함.


--------------------------------------------------------------------------------
[AML] 03. 英 FCA, 자산운용사 및 대체투자 펀드 대상 금융범죄(AML) 내부통제 점검 결과 발표 (‘26.7.22)
--------------------------------------------------------------------------------
[1] 조사 배경 및 개요
▪ 영국 금융감독청(FCA)은 7월 22일 240여 개 글로벌 자산운용사, 헤지펀드 및 대체투자 펀드사를 대상으로 실시한 금융범죄(AML/CFT) 내부통제 체계 심층 점검 결과를 공개하고 업계 전반에 모범 및 미흡 사례를 통보함.

[2] 주요 지적사항 및 권고사항
① 복합 펀드 구조의 실소유자(Beneficial Ownership) 확인 부실
- 사모펀드, 역외 SPC 등 다층 지배구조 뒤에 숨은 실질 지배자에 대한 검증을 형식적인 확인서 징구에만 의존하고 독립적인 검증을 누락한 사례를 엄중 지적함.
② 고위험 고객(PEP) 및 제재 대상자 상시 스크리닝 미흡
- 온보딩 이후 고객의 정치적 주요인물(PEP) 지정 여부 및 글로벌 제재 리스트 변경 사항을 주기적으로 재검증(Ongoing Monitoring)하지 않는 취약점 발견.
③ 전사 자금세탁 위험평가(EWRA) 갱신 지연
- 신규 투자 상품 출시 및 지정학적 리스크 변화(러시아·중동 제재 등)를 전사 위험평가 모델에 적시에 반영하지 못한 운용사들에 대해 시정 조치를 요구함.

▶ [시사점 및 금융권 대응 방향]
- 사모펀드 및 신탁 상품의 실소유자(BO) 확인 체계 고도화: 자산운용 및 신탁 부문에서는 다단계 투자 구조에 대해 출자자 명부, 정관, 지배구조도를 전수 징구하여 실질 지배자를 규명해야 함.
- 자금 원천(Source of Wealth/Funds) 실사 강화: 고액 자산가 및 법인 고객의 투자 자금 형성 과정과 출처에 대한 객관적 증빙을 확보하는 프로세스를 내재화해야 함.


--------------------------------------------------------------------------------
[AML] 04. 금융위·금감원, 「가상자산이용자보호법」 시행에 따른 이상거래 상시감시 및 AML 연계 체계 가동 (‘26.7.20)
--------------------------------------------------------------------------------
[1] 제도 시행 및 추진 경과
▪ 금융위원회와 금융감독원은 「가상자산 이용자 보호 등에 관한 법률(가상자산이용자보호법)」이 본격 시행됨에 따라, 가상자산거래소의 이용자 예치금 분리 보관 및 불공정거래 상시감시 체계를 7월 20일부터 본격 가동함.

[2] 핵심 통제 체계 및 감독 방향
① 불공정거래 상시감시 및 당국 통보 핫라인 가동
- 거래소는 이상 가격 급등락, 자전거래, 미공개정보 이용 의심 거래를 24시간 실시간 감시하고, 이상 징후 포착 시 금융당국 및 KoFIU에 즉시 통보해야 함.
② 원화 예치금의 은행 분리 보관 및 신탁 관리 의무화
- 이용자 예치금은 공신력 있는 은행에 안전 자산으로 신탁 보관되며, 거래소 파산 시에도 예치금이 이용자에게 우선 지급되도록 법적 보호 장치 완비.
③ 이상거래 감시와 AML 의심거래보고(STR) 연계
- 불공정거래로 의심되는 자금 흐름에 대해 즉각 특금법상 STR(의심거래보고)을 병행 제출하도록 감독 프로세스 연계 강화.

▶ [시사점 및 금융권 대응 방향]
- 제휴 은행의 예치금 관리 실사 및 FDS 연계: 실명계좌 발급 은행은 거래소 예치금 신탁 관리의 안전성을 정기 점검하고, 거래소 FDS 통보 데이터를 활용해 은행 계좌 출금 모니터링을 강화해야 함.
- 시세조종 및 불법 자금세탁 연계 시나리오 룰셋 고도화: 단기 급증 입금 후 코인 매수, 다계좌 분산 이체 후 특정 가상자산 집중 매매 등 불공정거래와 자금세탁이 결합된 복합 시나리오를 FDS 및 STR 룰에 반영해야 함.
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
          <span class="badge-date">2026년 7월 3주차 상세 보고서 (2026.07.20 ~ 2026.07.24)</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📋 7월 3주차 주요 공시 및 핵심 의제</div>
          <ol class="toc-list">
            <li><strong>[AML]</strong> FATF, 탈중앙화 금융(DeFi) 규제 및 자금세탁 방지 특별 보고서 발표 (‘26.7.21)</li>
            <li><strong>[Sanctions/AML]</strong> 美 OFAC, 멕시코 카르텔(CJNG) 및 초국경 자금세탁망 50여 개 대상 대규모 제재 단행 (‘26.7.23)</li>
            <li><strong>[AML]</strong> 英 FCA, 자산운용사 및 대체투자 펀드 대상 금융범죄(AML) 내부통제 점검 결과 발표 (‘26.7.22)</li>
            <li><strong>[AML]</strong> 금융위·금감원, 「가상자산이용자보호법」 시행에 따른 이상거래 상시감시 및 AML 연계 체계 가동 (‘26.7.20)</li>
          </ol>
        </div>

        <!-- Card 01 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">01. FATF, 탈중앙화 금융(DeFi) 규제 및 자금세탁 방지 특별 보고서 발표 (‘26.7.21)</div>
          </div>
          
          <div class="section-subtitle">[1] 발간 배경 및 개요</div>
          <ul class="content-list">
            <li>국제자금세탁방지기구(FATF)는 7월 21일 급격히 팽창하는 <strong>탈중앙화 금융(DeFi) 생태계에서의 자금세탁(ML), 테러자금조달(TF) 위험에 대응하기 위한 특별 보고서</strong>를 공식 발표함.</li>
          </ul>

          <div class="section-subtitle">[2] 핵심 내용 및 규제 판단 기준</div>
          <ul class="content-list">
            <li><strong>'통제 또는 중대한 영향력(COSI)' 기준 확립:</strong>
              <div class="sub-bullet-box">
                <p>• 명목상 탈중앙화를 표방하더라도 프로토콜 개발자, 거버넌스 토큰 집중 보유자, 관리자 키(Admin Key) 보유자 등이 실질적인 통제력이나 중대한 영향력을 행사하는 경우 <strong>FATF 권고기준(R.15)상 가상자산사업자(VASP) 규제 대상에 포함됨</strong>을 명문화함.</p>
              </div>
            </li>
            <li><strong>규제 사각지대 해소 및 글로벌 이행 촉구:</strong>
              <div class="sub-bullet-box">
                <p>• 전 세계 93%의 관할권이 아직 DeFi에 대한 자금세탁방지 규율 체계를 확립하지 못했음을 지적하며, 각국 규제당국에 기능적 위험기반 접근법(RBA)을 적용해 실질 지배자를 식별·감독할 것을 강력히 권고함.</p>
              </div>
            </li>
            <li><strong>불법 자금세탁 수법 차단:</strong>
              <div class="sub-bullet-box">
                <p>• 스마트 컨트랙트 취약점 공격, 믹서(Mixer) 연계, 비호스팅 지갑 간 P2P 익명 자금 이동 등 신종 자금은닉 수법에 대한 선제적 감시 체계 구축을 요구함.</p>
              </div>
            </li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>DeFi 프로토콜 연계 온체인 트랜잭션 감시 고도화:</strong> 블록체인 분석 솔루션을 활용하여 거래소 및 은행 연계 계좌에서 DeFi 프로토콜, 유동성 풀(Liquidity Pool)로 유출입되는 고위험 자금 흐름을 실시간으로 추적해야 함.</li>
              <li><strong>실질 지배력(COSI) 보유 법인 고객 실사 강화:</strong> DeFi 관련 사업을 영위하는 법인 고객에 대해 스마트 컨트랙트 관리 권한 및 거버넌스 구조를 심층 분석하는 강화된 고객확인(EDD) 절차를 수립해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 02 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category sanctions">Sanctions / AML</span>
            <div class="card-title">02. 美 OFAC, 멕시코 카르텔(CJNG) 및 초국경 자금세탁망 50여 개 대상 대규모 제재 단행 (‘26.7.23)</div>
          </div>
          
          <div class="section-subtitle">[1] 제재 배경 및 발표 내용</div>
          <ul class="content-list">
            <li>미국 재무부 해외자산통제국(OFAC)은 7월 23일 행정명령 E.O. 14059 및 E.O. 13224에 근거하여 멕시코의 <strong>할리스코 신세대 카르텔(CJNG)과 연계된 50개 이상의 개인, 페이퍼컴퍼니 및 금융 중개 네트워크에 대해 사상 최대 규모의 제재(SDN)</strong>를 단행함.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 제재 대상 및 범죄 수법</div>
          <ul class="content-list">
            <li><strong>다계층 복합 자금세탁 네트워크 차단:</strong> 타임셰어(시계열 콘도 분양) 사기, 불법 부동산 개발업체, 허위 결제대행사를 통해 미국 시민들로부터 편취한 자금을 멕시코 및 역외 페이퍼컴퍼니로 은닉·세탁한 구조를 전면 적발함.</li>
            <li><strong>가상자산 및 환전 브로커 제재:</strong> 불법 마약 및 사기 수익금을 스테이블코인(USDT 등)으로 전환하여 국경 간 송금한 암호화폐 환전 브로커 및 계좌 명의인을 SDN 목록에 대거 등재함.</li>
            <li><strong>강력한 2차 제재(Secondary Sanctions) 경고:</strong> 제재 대상자와 금융 거래를 수행하거나 자금세탁을 지원한 제3국 금융기관에 대해 미국 금융망 접근을 원천 차단하는 세컨더리 제재 위험을 경고함.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>SDN 제재 필터링 리스트 실시간 동기화:</strong> OFAC 신규 제재 명단(개인 30여 명, 법인 20여 개)을 글로벌 제재 스크리닝 엔진에 즉각 반영하여 당일 결제 및 외환 송금 거래를 철저히 차단해야 함.</li>
              <li><strong>중남미 및 역외 경유 해외송금 심사 강화:</strong> 부동산 투자, 회원권 결제, 컨설팅 명목의 중남미행 외환 송금 시 수취 법인의 실소유자 및 설립 목적을 정밀 검증(EDD)해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 03 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">03. 英 FCA, 자산운용사 및 대체투자 펀드 대상 금융범죄(AML) 내부통제 점검 결과 발표 (‘26.7.22)</div>
          </div>
          
          <div class="section-subtitle">[1] 조사 배경 및 개요</div>
          <ul class="content-list">
            <li>영국 금융감독청(FCA)은 7월 22일 <strong>240여 개 글로벌 자산운용사, 헤지펀드 및 대체투자 펀드사 대상 금융범죄(AML/CFT) 내부통제 체계 심층 점검 결과</strong>를 공개하고 모범 및 미흡 사례를 통보함.</li>
          </ul>

          <div class="section-subtitle">[2] 주요 지적사항 및 권고사항</div>
          <ul class="content-list">
            <li><strong>복합 펀드 구조의 실소유자(Beneficial Ownership) 확인 부실:</strong> 사모펀드, 역외 SPC 등 다층 지배구조 뒤에 숨은 실질 지배자에 대한 검증을 형식적인 확인서 징구에만 의존하고 독립적인 검증을 누락한 사례를 엄중 지적함.</li>
            <li><strong>고위험 고객(PEP) 및 제재 대상자 상시 스크리닝 미흡:</strong> 온보딩 이후 고객의 정치적 주요인물(PEP) 지정 여부 및 글로벌 제재 리스트 변경 사항을 주기적으로 재검증(Ongoing Monitoring)하지 않는 취약점 발견.</li>
            <li><strong>전사 자금세탁 위험평가(EWRA) 갱신 지연:</strong> 신규 투자 상품 출시 및 지정학적 리스크 변화(러시아·중동 제재 등)를 전사 위험평가 모델에 적시에 반영하지 못한 운용사들에 대해 시정 조치를 요구함.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>사모펀드 및 신탁 상품의 실소유자(BO) 확인 체계 고도화:</strong> 자산운용 및 신탁 부문에서는 다단계 투자 구조에 대해 출자자 명부, 정관, 지배구조도를 전수 징구하여 실질 지배자를 규명해야 함.</li>
              <li><strong>자금 원천(Source of Wealth/Funds) 실사 강화:</strong> 고액 자산가 및 법인 고객의 투자 자금 형성 과정과 출처에 대한 객관적 증빙을 확보하는 프로세스를 내재화해야 함.</li>
            </ul>
          </div>
        </div>

        <!-- Card 04 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title">04. 금융위·금감원, 「가상자산이용자보호법」 시행에 따른 이상거래 상시감시 및 AML 연계 체계 가동 (‘26.7.20)</div>
          </div>
          
          <div class="section-subtitle">[1] 제도 시행 및 추진 경과</div>
          <ul class="content-list">
            <li>금융위원회와 금융감독원은 <strong>「가상자산 이용자 보호 등에 관한 법률(가상자산이용자보호법)」</strong>이 본격 시행됨에 따라, 가상자산거래소의 <strong>이용자 예치금 분리 보관 및 불공정거래 상시감시 체계</strong>를 7월 20일부터 본격 가동함.</li>
          </ul>

          <div class="section-subtitle">[2] 핵심 통제 체계 및 감독 방향</div>
          <ul class="content-list">
            <li><strong>불공정거래 상시감시 및 당국 통보 핫라인 가동:</strong> 거래소는 이상 가격 급등락, 자전거래, 미공개정보 이용 의심 거래를 24시간 실시간 감시하고, 이상 징후 포착 시 금융당국 및 KoFIU에 즉시 통보해야 함.</li>
            <li><strong>원화 예치금의 은행 분리 보관 및 신탁 관리 의무화:</strong> 이용자 예치금은 공신력 있는 은행에 안전 자산으로 신탁 보관되며, 거래소 파산 시에도 예치금이 이용자에게 우선 지급되도록 법적 보호 장치 완비.</li>
            <li><strong>이상거래 감시와 AML 의심거래보고(STR) 연계:</strong> 불공정거래로 의심되는 자금 흐름에 대해 즉각 특금법상 STR(의심거래보고)을 병행 제출하도록 감독 프로세스 연계 강화.</li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>제휴 은행의 예치금 관리 실사 및 FDS 연계:</strong> 실명계좌 발급 은행은 거래소 예치금 신탁 관리의 안전성을 정기 점검하고, 거래소 FDS 통보 데이터를 활용해 은행 계좌 출금 모니터링을 강화해야 함.</li>
              <li><strong>시세조종 및 불법 자금세탁 연계 시나리오 룰셋 고도화:</strong> 단기 급증 입금 후 코인 매수, 다계좌 분산 이체 후 특정 가상자산 집중 매매 등 불공정거래와 자금세탁이 결합된 복합 시나리오를 FDS 및 STR 룰에 반영해야 함.</li>
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
    
    txt_path = report_dir / "aml_report_20260720_week3.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"제목: {subject}\n\n{body_text}")
        
    html_path = report_dir / "aml_report_20260720_week3.html"
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
        print("[상세 이메일 발송 성공] 2026년 7월 3주차 보고서가 성공적으로 발송되었습니다.")
        return True
    except Exception as e:
        print(f"[이메일 발송 오류] {e}")
        return False

if __name__ == "__main__":
    send_july_week3_insight_email()
