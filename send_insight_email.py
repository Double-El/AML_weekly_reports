import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENTS

def send_weekly_insight_email():
    subject = "[AML & Sanctions Weekly Insight] 8월 1주차 주요 감독기관 공시 및 시사점"
    
    # 1. Plain text version
    body_text = """[AML & Sanctions Weekly Insight] 8월 1주차

자금세탁방지본부 CoP

■ 목차
01 | 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)
02 | KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 (‘26.8.10)
03 | KoFIU, 아시아·태평양 지역기구(APG*) 연차 총회 참석 (‘26.8.3)
04 | FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)
05 | 금감원, 네이버·토스·카카오에 해외결제 자금세탁 관리 부실로 ‘경영유의’ (‘26.8.7)
06 | FinCEN, 은행비밀보호법 위반 혐의로 UBS에 1억 2,500만 달러 벌금 부과 (‘26.8.3)
07 | OFAC, 대 테러 · 이란 관련 가상자산 거래소 및 자금세탁 네트워크 제재 (‘26.8.7)

================================================================================

[AML]
01. 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)
▪ 가상자산사업자의 신고제를 강화하고, 가상자산 이전거래 관련 자금세탁방지 의무를 강화하기 위한 「특금법 시행령」 개정안이 국무회의에서 의결되어, 2026.8.20(목)부터 시행될 예정임
▪ 금번 개정안의 주요 내용은 다음과 같음
① 신고 불수리 요건 및 심사 대상 구체화
: 가상자산사업자의 대주주 범위가 대표이사 또는 이사의 과반수를 선임한 주주, 최대주주가 법인인 경우 해당 법인의 최대주주와 대표자로 확대됨
또한, 사업자의 재무상태 및 사회적 신용, 임원·대주주의 자격 요건과 전문인력·전산설비 등 내부통제 기준을 마련하는 등 신고 불수리 요건을 구체화함
② 가상자산 이전거래에 대한 자금세탁방지의무 부과
: 트래블룰의 기준 금액을 폐지하여 모든 가상자산 이전거래로 적용대상을 확대하였으며, 해외 가상자산사업자 또는 지갑 거래는 위험도에 따라 허용범위를 차등화함
또한, 1천만원 이상 거래에 대해서는 자체 의심거래 관리 체계를 구축·운영할 의무가 부과됨
▪ 이외에도 퇴직 임직원의 제재조치 통보 권한을 검사수탁기관에 위탁하고, 고객 특성과 위험도에 따른 고객확인의무 이행 방법을 명확히 규정함
▶ 은행의 제휴 거래소 평가 및 리스크 관리 책임이 가중되었으며, 거래소의 트래블룰 전면 확대, 위험도 차등 관리 및 의심거래 관리체계 요구에 따른 은행권의 위험평가 및 의심거래 모니터링 강화가 필요함

--------------------------------------------------------------------------------

[AML]
02. KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 (‘26.8.10)
▪ 금융정보분석원(KoFIU)는 ‘신종피싱 의심계좌 거래정지제도 점검회의’ 개최를 통해 지난 6월 30일 시행된 제도의 운영 현황과 범죄유형별 주요 피해사례 등을 논의함
▪ 제도 시행 이후 약 한 달간 금융회사가 임시조치한 건수는 총 4,935건으로, 이 중 총 3,750건에 대해 특금법 상 강화된 고객확인 대상으로 분류하여 의심계좌로 임시거래정지 처리하였다고 밝힘
▪ 주요 범죄 유형으로는 로맨스스캠이 약 41%(1,527건), 노쇼사기가 약 37%(1,376건), 팀미션사기가 약 22%(847건)를 차지하였으며, 유형별 대국민 행동 요령을 함께 논의한 것으로 확인됨
▪ 금융정보분석원은 관계부처와의 협의를 통해 적극적으로 피해예방 홍보활동을 추진하고, 거래정지 제도의 명확한 법적근거를 마련하기 위해 특금법 개정을 신속히 추진할 계획이라고 밝힘
▶ 신종피싱 의심계좌 명의인에 대해 강화된 고객확인을 적용하여 민생범죄 차단과 AML 프로세스를 긴밀히 연계하고, 전담 인력 확충 및 유관기관과의 신속한 공조를 통해 대응 역량을 강화해야 함
* 「전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법」상 보이스피싱 범죄에 포함되지 않는 ‘재화와 용역의 거래를 가장한’ 전기통신금융사기 (신종피싱)에 대해서도 신속한 계좌 거래정지가 가능하도록 한 제도

--------------------------------------------------------------------------------

[AML]
03. KoFIU, 아시아·태평양 지역기구(APG*) 연차 총회 참석 (‘26.8.3)
▪ 금융정보분석원(KoFIU)은 2026년 아시아·태평양 자금세탁방지기구(APG) 연차총회에 참석해 역내 주요 자금세탁 및 테러자금조달 위험과 FATF 제5차 상호평가 대응 방향에 대해 논의함
▪ APG 회원국들은 사이버 스캠, 초국경 조직범죄, 무역기반 자금세탁 등 최근 증가하고 있는 금융범죄 위험에 대해 국가 간 신속한 정보공유와 수사협력이 필요하다는 점을 확인함
▪ 우리나라는 최근 신종스캠 범죄 대응을 위해 시행중인 지급정지제도를 소개하며, 불법자금 흐름을 조기에 차단하는 것이 중요하다고 강조함
▪ 또한, 제5차 FATF 상호평가를 조기에 수검한 말레이시아, 싱가폴, 캐나다 등은 평가 준비 및 결함 해소 경험을 공유하면서, 국가위험평가를 기반으로 한 위험기반 정책을 수립·운영해야 하며, 신속한 정보 공유와 협력을 통해 실질적 성과를 창출하는 것이 중요하다는 점을 재확인함
▶ 신종 금융범죄 사례와 자금 이동 방식을 지속적으로 분석함으로써 자금세탁방지 체계도 사후 적발을 넘어 범죄 자금의 이동을 조기에 탐지하고 차단하는 방향으로 강화가 필요해짐
▶ 제도 구축이나 규정 준수 뿐만 아니라 실제 자금세탁 위험을 식별·관리하고, 범죄자금 흐름을 차단하는 구체적인 운영성과 효과성을 입증하는 것이 중요해짐
* 국제자금세탁방지기구(FATF)의 기준을 전파·이행하는 9개 지역기구 중 하나로, 아세안·태평양 41개 회원국으로 구성

--------------------------------------------------------------------------------

[AML]
04. FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)
▪ 지난 8월 11일 미국 재무부 산하 금융범죄단속네트워크(FinCEN)은 기업 투명성법(CTA)에 따라 추진되었던 미국 기업 및 미국인의 실소유자 정보 신고 의무를 완전히 면제하는 최종 규칙을 발표함
▪ 이는 수많은 중소기업들에게 부과되었던 과도한 행정적·재정적 부담을 덜어주기 위한 규제 완화 조치로, 이에 따라 미국 내 설립된 기업 및 미국인은 실소유자 신고 의무에서 제외됨
▪ 또한, 이미 FinCEN ID를 발급받은 미국인은 향후 정보변경 및 수정 보고 의무가 면제되며, 기 제출된 실소유자 정보와 설립자 데이터가 모두 삭제될 예정임
▪ 단, 미국에 등록된 외국 법인의 경우 외국인 실소유자에 대한 신고 의무는 일부 유지되나, 외국 법인 내 ‘미국인 실소유자’나 ‘미국인 회사 설립자’에 대한 정보 보고 의무는 면제됨
▶ 미국에 진출한 해외법인은 여전히 신고 의무를 부담하며, 정부 중앙 데이터 삭제에 따라 금융기관의 독자적인 고객확인(CDD/EDD) 비용과 노력 투입이 필요해짐
▶ 전 세계적으로 기업 투명성을 강화하는 추세임에도 미국이 국제 동향과 어긋나는 방향으로 선회함에 따라 다국적 기업 및 금융사들은 국가별로 상이한 실소유자 식별 및 보고 프로세스를 적용해야 하는 실무적 복잡성에 직면하게 될 가능성이 높음

--------------------------------------------------------------------------------

[AML]
05. 금감원, 네이버·토스·카카오에 해외결제 자금세탁 관리 부실로 ‘경영유의’ (‘26.8.7)
▪ 금융감독원이 국경 간 거래 급증에 대응하는 자금세탁방지 및 내부통제 체계가 미흡하다는 사유로, 네이버파이낸셜·토스페이먼츠·카카오페이에 경영유의 조치를 부과함
▪ 주요 지적사항은 다음과 같음
① 해외 PG사 고객확인 및 자금세탁 감시 소홀 (카카오페이·토스페이먼츠)
: 해외 고객의 국내 가맹점 정산 업무를 대행하는 해외 PG사와의 계약을 체결하고 대금을 정산 받는 과정에서 해외 PG사에 대한 별도 자금세탁방지 의무 이행 여부 및 고객확인 절차 이행이 미흡함
② 온·오프라인 가맹점 관리 부실 및 거래품목 확인 누락 (네이버파이낸셜·토스페이먼츠)
: 정산대금의 해외송금 시 단순히 해외 가맹점의 결제 건수와 총액만 확인하고, 실제 거래 품목을 형식적으로 받거나 적절히 확인하지 않아 이상거래 여부를 파악하지 못함
③ 주기적 고객확인 미이행 및 정보 입력 오류 방치 (네이버파이낸셜·토스페이먼츠)
: 외국인 대표자의 주민등록번호 입력 오류 등을 장기간 방치하거나, 고객확인 재이행 주기가 도래하였음에도 절차를 이행하지 않음
▶ 해외 PG사에 대한 강화된 고객확인과 정산대금의 실거래 품목 검증 등 모니터링 체계를 고도화하고, 고객확인 정보 및 주기적 고객확인 이행 여부 점검 등 내부통제 프로세스의 정합성 유지가 필요함

--------------------------------------------------------------------------------

[AML]
06. FinCEN, 은행비밀보호법 위반 혐의로 UBS에 1억 2,500만 달러 벌금 부과 (‘26.8.3)
▪ 美 재무부 산하 금융범죄단속네트워크(FinCEN)는 지난 8월 3일 UBS Financial Services Inc.에 은행비밀보호법(BSA)*을 위반한 혐의로 1억 2,500만 달러(한화 약 1,700억원)의 벌금을 부과함
▪ FinCEN이 밝힌 주요 지적사항은 다음과 같음
① 외화 송금 모니터링 체계 미비
: 2018년 동일 항목 제재(450만 달러) 이후에도 모니터링 시스템 결함을 방치하여 6만 건 이상의 외화 송금 이상거래 모니터링에 실패함
② 고위험 고객 및 제재 위험 관리 소홀
: 러시아, 베네수엘라 등 고위험 지역 연계 고객에 대해 자금 원천, 제재 연관성, 부정적 뉴스 등을 검토하지 않아 고객확인 및 거래 모니터링이 제대로 수행되지 않음
③ 의심거래보고(SAR)의 누락 및 지연 보고
: 수백 건의 의심거래에 대해 의심거래보고(SAR)를 누락하거나, 법정 기한을 넘겨 지연 제출했으며, 일부 보고의 경우 핵심 정보가 누락되거나 부실하게 작성되었음
▶ 과거 적발된 결함이 지속된 점을 중대한 가중 처벌 요소로 평가한 사례로, 감독당국 지적 사항에 대한 개선의 적시성, 완결성이 중요한 판단 지표임을 시사함
* Bank Secrecy Act의 약자로, 금융기관의 자금세탁 및 테러자금조달 방지를 위한 미국의 주요 법률

--------------------------------------------------------------------------------

[Sanctions]
07. OFAC, 대 테러 · 이란 관련 가상자산 거래소 및 자금세탁 네트워크 제재 (‘26.8.7)
▪ 지난 8월 7일, 미 재무부 산하 해외자산통제국(OFAC)이 이란 정권 및 이란혁명수비대(IRGC)의 자금세탁 및 제재 회피를 지원한 가상자산 거래소 2곳 및 관련 개인·법인을 제재 대상으로 지정함
▪ 이번 조치는 이란 측이 미등록 가상자산 거래소, 다국적 네트워크 및 온라인 도박사업 등을 활용해 디지털 자산을 대규모로 이동·세탁하고, 이를 IRGC와 관련 인물들에게 제공한 데 따른 것임
▪ 구체적으로 이란과 연계된 가상자산 거래소인 ‘Shelbit Exchange’, ‘Aban Teher’ 및 이란 국적의 시아바시 카이반포르(Siavash Kaivanpour) 등이 제재 대상 목록에 올라감
▪ 제재 지정에 따라 해당 개인 및 법인의 미국 내 모든 자산은 동결될 뿐만 아니라, 이들과 거래하는 미국 및 제3국의 금융기관이나 개인 역시 2차 제재(Secondary Sanctions) 위험에 노출될 가능성이 있음
▶ 제3국 및 복수의 해외 법인을 경유해 제재를 회피할 가능성이 있으므로, 제재 대상과의 직접 거래뿐만 아니라 거래상대방, 자금흐름 및 지분관계 등을 종합적으로 고려할 필요가 있음
▶ 가상자산 등이 제재회피 및 자금세탁의 주요 통로로 적극 활용되고 있으므로, 가상자산, 고위험 업종 등 복수 위험 요인이 결합된 거래에 대해 모니터링 강화가 필요함
"""

    # 2. Rich HTML version matching PDF styling
    body_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕", helvetica, "Apple SD Gothic Neo", sans-serif; line-height: 1.6; color: #222; background-color: #f4f6f9; margin: 0; padding: 20px; }}
        .container {{ max-width: 860px; margin: 0 auto; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); padding: 36px 40px; border: 1px solid #e2e8f0; }}
        .header {{ border-bottom: 2px solid #1a202c; padding-bottom: 20px; margin-bottom: 28px; }}
        .sub-header {{ font-size: 13px; color: #718096; letter-spacing: 1px; text-transform: uppercase; font-weight: bold; margin-bottom: 6px; }}
        .title {{ font-size: 24px; font-weight: 800; color: #1a202c; margin: 0 0 10px 0; }}
        .badge-date {{ display: inline-block; background: #edf2f7; color: #4a5568; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; }}
        
        .toc-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px 24px; margin-bottom: 32px; }}
        .toc-title {{ font-weight: 700; font-size: 16px; margin-bottom: 12px; color: #2d3748; display: flex; align-items: center; }}
        .toc-list {{ margin: 0; padding-left: 20px; font-size: 14px; color: #4a5568; }}
        .toc-list li {{ margin-bottom: 6px; }}
        
        .card {{ background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 24px; margin-bottom: 28px; position: relative; }}
        .card-header {{ display: flex; align-items: flex-start; margin-bottom: 16px; }}
        .card-category {{ background: #0f172a; color: #fff; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-right: 10px; }}
        .card-category.sanctions {{ background: #7c2d12; }}
        .card-num {{ background: #000; color: #fff; width: 22px; height: 22px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; margin-right: 8px; flex-shrink: 0; }}
        .card-title {{ font-size: 16px; font-weight: 700; color: #0f172a; line-height: 1.4; }}
        
        .content-list {{ list-style-type: none; padding-left: 0; margin: 0 0 16px 0; font-size: 14px; color: #334155; }}
        .content-list li {{ margin-bottom: 10px; position: relative; padding-left: 18px; line-height: 1.6; }}
        .content-list li::before {{ content: "▪"; position: absolute; left: 0; color: #475569; font-weight: bold; }}
        .content-sublist {{ margin-top: 6px; margin-bottom: 6px; padding-left: 14px; color: #475569; }}
        
        .insight-box {{ background: #eff6ff; border-left: 4px solid #2563eb; padding: 12px 16px; border-radius: 0 6px 6px 0; font-size: 14px; font-weight: 600; color: #1e3a8a; line-height: 1.5; margin-top: 14px; }}
        .insight-box::before {{ content: "▶ "; color: #2563eb; }}
        
        .footnote {{ font-size: 12px; color: #64748b; margin-top: 12px; padding-top: 8px; border-top: 1px dashed #e2e8f0; }}
        .footer {{ text-align: center; font-size: 12px; color: #94a3b8; margin-top: 40px; padding-top: 20px; border-top: 1px solid #e2e8f0; }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="header">
          <div class="sub-header">자금세탁방지본부 CoP</div>
          <div class="title">AML &amp; Sanctions Weekly Insight</div>
          <span class="badge-date">8월 1주차 주간 공시 보고</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📌 주간 주요 공시 목차</div>
          <ol class="toc-list">
            <li>가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)</li>
            <li>KoFIU, 신종피싱 의심계좌 거래정지제도 점검회의 개최 (‘26.8.10)</li>
            <li>KoFIU, 아시아·태평양 지역기구(APG) 연차 총회 참석 (‘26.8.3)</li>
            <li>FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)</li>
            <li>금감원, 네이버·토스·카카오에 해외결제 자금세탁 관리 부실로 ‘경영유의’ (‘26.8.7)</li>
            <li>FinCEN, 은행비밀보호법 위반 혐의로 UBS에 1억 2,500만 달러 벌금 부과 (‘26.8.3)</li>
            <li>OFAC, 대 테러 · 이란 관련 가상자산 거래소 및 자금세탁 네트워크 제재 (‘26.8.7)</li>
          </ol>
        </div>

        <!-- 01 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❶ 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)</strong></div>
          </div>
          <ul class="content-list">
            <li>가상자산사업자의 신고제를 강화하고, 가상자산 이전거래 관련 자금세탁방지 의무를 강화하기 위한 <strong>「특금법 시행령」 개정안</strong>이 국무회의에서 의결되어, <strong>2026.8.20(목)부터 시행</strong>될 예정임</li>
            <li>금번 개정안의 주요 내용은 다음과 같음
              <div class="content-sublist">
                <strong>① 신고 불수리 요건 및 심사 대상 구체화:</strong> 가상자산사업자의 대주주 범위가 대표이사 또는 이사의 과반수를 선임한 주주, 최대주주가 법인인 경우 해당 법인의 최대주주와 대표자로 확대됨. 또한 사업자의 재무상태 및 사회적 신용, 임원·대주주의 자격 요건과 전문인력·전산설비 등 내부통제 기준을 마련함.<br>
                <strong>② 가상자산 이전거래에 대한 자금세탁방지의무 부과:</strong> 트래블룰의 기준 금액을 폐지하여 모든 가상자산 이전거래로 적용대상을 확대하였으며, 해외 가상자산사업자/지갑 거래는 위험도에 따라 차등화함. 1천만원 이상 거래는 자체 의심거래 관리체계 구축·운영 의무 부과.
              </div>
            </li>
            <li>이외에도 퇴직 임직원의 제재조치 통보 권한을 검사수탁기관에 위탁하고, 고객 특성과 위험도에 따른 고객확인의무 이행 방법을 명확히 규정함</li>
          </ul>
          <div class="insight-box">
            은행의 제휴 거래소 평가 및 리스크 관리 책임이 가중되었으며, 거래소의 트래블룰 전면 확대, 위험도 차등 관리 및 의심거래 관리체계 요구에 따른 은행권의 위험평가 및 의심거래 모니터링 강화가 필요함
          </div>
        </div>

        <!-- 02 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❷ KoFIU, 신종피싱 의심계좌 거래정지제도 점검회의 개최 (‘26.8.10)</strong></div>
          </div>
          <ul class="content-list">
            <li>금융정보분석원(KoFIU)는 ‘신종피싱 의심계좌 거래정지제도 점검회의’ 개최를 통해 지난 6월 30일 시행된 제도의 운영 현황과 범죄유형별 주요 피해사례 등을 논의함</li>
            <li>제도 시행 이후 약 한 달간 금융회사가 임시조치한 건수는 총 4,935건으로, 이 중 총 3,750건에 대해 특금법 상 강화된 고객확인 대상으로 분류하여 의심계좌로 임시거래정지 처리함</li>
            <li>주요 범죄 유형으로는 로맨스스캠이 약 41%(1,527건), 노쇼사기가 약 37%(1,376건), 팀미션사기가 약 22%(847건)를 차지함</li>
            <li>금융정보분석원은 관계부처 협의를 통해 피해예방 홍보활동을 추진하고, 거래정지 제도의 명확한 법적근거 마련을 위해 특금법 개정을 신속 추진할 계획임</li>
          </ul>
          <div class="insight-box">
            신종피싱 의심계좌 명의인에 대해 강화된 고객확인을 적용하여 민생범죄 차단과 AML 프로세스를 긴밀히 연계하고, 전담 인력 확충 및 유관기관과의 신속한 공조를 통해 대응 역량을 강화해야 함
          </div>
          <div class="footnote">* 신종피싱: 통신사기피해환급법상 보이스피싱에 포함되지 않는 '재화와 용역의 거래를 가장한' 사기에 대해서도 신속한 계좌 거래정지가 가능하도록 한 제도</div>
        </div>

        <!-- 03 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❸ KoFIU, 아시아·태평양 지역기구(APG) 연차 총회 참석 (‘26.8.3)</strong></div>
          </div>
          <ul class="content-list">
            <li>금융정보분석원(KoFIU)은 2026년 APG 연차총회에 참석해 역내 주요 자금세탁 및 테러자금조달 위험과 FATF 제5차 상호평가 대응 방향에 대해 논의함</li>
            <li>APG 회원국들은 사이버 스캠, 초국경 조직범죄, 무역기반 자금세탁 등 최근 증가하는 금융범죄 위험에 대해 국가 간 신속한 정보공유와 수사협력이 필요함을 확인</li>
            <li>우리나라는 신종스캠 범죄 대응을 위해 시행 중인 지급정지제도를 소개하며, 불법자금 흐름의 조기 차단 중요성을 강조함</li>
            <li>FATF 제5차 상호평가 수검국(말레이시아, 싱가포르, 캐나다 등) 경험 공유를 통해 국가위험평가 기반의 위험기반 정책(RBA) 수립·운영 및 실질적 성과 창출 중요성 재확인</li>
          </ul>
          <div class="insight-box">
            신종 금융범죄 사례와 자금 이동 방식을 지속적으로 분석하여 사후 적발을 넘어 범죄자금 조기 탐지·차단으로 고도화하고, 규정 준수를 넘어 실질적 위험 관리 효과성을 입증하는 체계 구축이 필수적임
          </div>
        </div>

        <!-- 04 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❹ FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)</strong></div>
          </div>
          <ul class="content-list">
            <li>미국 FinCEN은 기업 투명성법(CTA)에 따라 추진되었던 미국 기업 및 미국인의 실소유자 정보(BOI) 신고 의무를 완전히 면제하는 최종 규칙을 발표함</li>
            <li>중소기업의 과도한 행정·재정적 부담 경감을 위한 규제 완화 조치로 미국 내 설립 기업 및 미국인은 신고 의무에서 제외되며 기존 제출 데이터도 삭제 예정임</li>
            <li>미국 등록 외국 법인은 외국인 실소유자 신고 의무가 일부 유지되나 미국인 실소유자 관련 정보 보고는 면제됨</li>
          </ul>
          <div class="insight-box">
            미국 진출 해외법인의 신고 의무 및 중앙 데이터 삭제에 따라 금융기관의 독자적 CDD/EDD 역량 투입이 불가피하며, 국가별 상이한 실소유자 식별 규제에 따른 실무 복잡성 대응이 필요함
          </div>
        </div>

        <!-- 05 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❺ 금감원, 네이버·토스·카카오에 해외결제 자금세탁 관리 부실로 ‘경영유의’ (‘26.8.7)</strong></div>
          </div>
          <ul class="content-list">
            <li>금융감독원이 국경 간 거래 급증에 대응하는 자금세탁방지 및 내부통제 체계 미흡으로 네이버파이낸셜·토스페이먼츠·카카오페이에 경영유의 조치를 부과함</li>
            <li><strong>주요 지적사항:</strong>
              <div class="content-sublist">
                <strong>① 해외 PG사 고객확인 및 자금세탁 감시 소홀:</strong> 해외 PG사 계약 정산 과정에서 AML 의무 이행 및 고객확인 소홀<br>
                <strong>② 가맹점 관리 부실 및 거래품목 확인 누락:</strong> 총액만 확인하고 실거래 품목 검증 미흡으로 이상거래 미탐지<br>
                <strong>③ 주기적 고객확인 미이행 및 정보 오류 방치:</strong> 외국인 대표자 주민번호 오류 장기 방치 및 재이행 주기 미준수
              </div>
            </li>
          </ul>
          <div class="insight-box">
            해외 PG사에 대한 강화된 고객확인과 정산대금 실거래 품목 검증 모니터링 체계를 고도화하고, 주기적 고객확인 등 내부통제 프로세스의 정합성을 철저히 유지해야 함
          </div>
        </div>

        <!-- 06 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❻ FinCEN, 은행비밀보호법 위반 혐의로 UBS에 1억 2,500만 달러 벌금 부과 (‘26.8.3)</strong></div>
          </div>
          <ul class="content-list">
            <li>미 FinCEN은 UBS Financial Services Inc.에 은행비밀보호법(BSA) 위반 혐의로 1억 2,500만 달러(약 1,700억원) 벌금을 부과함</li>
            <li><strong>주요 지적사항:</strong>
              <div class="content-sublist">
                <strong>① 외화 송금 모니터링 체계 미비:</strong> 과거 제재 이후에도 결함을 방치해 6만 건 이상의 외화송금 이상거래 모니터링 실패<br>
                <strong>② 고위험 고객 및 제재 위험 관리 소홀:</strong> 러시아·베네수엘라 등 고위험 지역 연계 고객에 대한 자금원천 및 제재 연관성 검토 소홀<br>
                <strong>③ 의심거래보고(SAR) 누락 및 지연:</strong> 수백 건의 SAR 누락 및 법정기한 초과 지연 제출
              </div>
            </li>
          </ul>
          <div class="insight-box">
            과거 적발된 결함이 지속된 점을 중대 가중처벌 요소로 평가한 사례로, 감독당국 지적사항에 대한 개선의 적시성 및 완결성이 핵심 판단 지표임을 시사함
          </div>
        </div>

        <!-- 07 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category sanctions">Sanctions</span>
            <div class="card-title"><strong>❼ OFAC, 대 테러 · 이란 관련 가상자산 거래소 및 자금세탁 네트워크 제재 (‘26.8.7)</strong></div>
          </div>
          <ul class="content-list">
            <li>미 OFAC은 이란 정권 및 이란혁명수비대(IRGC)의 자금세탁·제재회피를 지원한 가상자산 거래소 2곳(Shelbit Exchange, Aban Teher) 및 관련 개인·법인을 제재 대상으로 지정함</li>
            <li>이란 측이 미등록 가상자산 거래소, 도박사업 등을 통해 디지털 자산을 대규모 이동·세탁한 정황 확인</li>
            <li>제재 대상과 거래하는 제3국 금융기관/개인 역시 2차 제재(Secondary Sanctions)에 노출될 위험 존재</li>
          </ul>
          <div class="insight-box">
            제3국 및 다국적 법인을 경유한 우회 거래 가능성을 고려하여 거래상대방, 자금흐름, 지분관계를 종합 분석하고 가상자산·고위험 업종 복합 거래 모니터링을 강화해야 함
          </div>
        </div>

        <div class="footer">
          본 메일은 AML &amp; Sanctions Weekly Insight 주간 보고 시스템을 통해 발송되었습니다.<br>
          상세 보고서 PDF 원본이 첨부되어 있습니다.
        </div>
      </div>
    </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["From"] = f"자금세탁방지본부 CoP <{SMTP_EMAIL}>"
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject

    # Attach both plain text and HTML
    part1 = MIMEText(body_text, "plain", "utf-8")
    part2 = MIMEText(body_html, "html", "utf-8")
    msg.attach(part1)
    msg.attach(part2)

    # Attach PDF file
    pdf_path = Path(r"c:\Users\efact\Desktop\aml_reports\AML&amp_Sanctions Weekly Insight_8월 1주차.pdf")
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            pdf_part = MIMEBase("application", "pdf")
            pdf_part.set_payload(f.read())
        encoders.encode_base64(pdf_part)
        pdf_filename = "AML_Sanctions_Weekly_Insight_8월_1주차.pdf"
        pdf_part.add_header("Content-Disposition", f"attachment; filename={pdf_filename}")
        msg.attach(pdf_part)
        print(f"  [PDF 첨부 완료] {pdf_path.name}")

    print(f"[SMTP 전송 시작] 대상: {', '.join(RECIPIENTS)}")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_EMAIL, SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL, RECIPIENTS, msg.as_string())
    server.quit()
    print("[이메일 발송 완료] 성공적으로 발송되었습니다.")

if __name__ == "__main__":
    send_weekly_insight_email()
