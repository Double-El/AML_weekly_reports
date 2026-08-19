import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from config import SMTP_EMAIL, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT, RECIPIENTS

def send_week2_insight_email():
    subject = "[AML & Sanctions Weekly Insight] 26년 8월 2주차 주요 감독기관 공시 및 시사점"
    
    # 1. Plain text version
    body_text = """[AML & Sanctions Weekly Insight] 2026년 8월 2주차

자금세탁방지본부 CoP

■ 주간 목차
01 | 가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)
02 | KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 (‘26.8.10)
03 | FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)
04 | 주요국 감독기구, 신종 초국경 스캠·자금세탁 거래 차단 공동 대응 (‘26.8.13)

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
▪ 금융정보분석원(KoFIU)은 ‘신종피싱 의심계좌 거래정지제도 점검회의’ 개최를 통해 지난 6월 30일 시행된 제도의 운영 현황과 범죄유형별 주요 피해사례 등을 논의함
▪ 제도 시행 이후 약 한 달간 금융회사가 임시조치한 건수는 총 4,935건으로, 이 중 총 3,750건에 대해 특금법 상 강화된 고객확인(EDD) 대상으로 분류하여 의심계좌로 임시거래정지 처리하였다고 밝힘
▪ 주요 범죄 유형으로는 로맨스스캠이 약 41%(1,527건), 노쇼사기가 약 37%(1,376건), 팀미션사기가 약 22%(847건)를 차지하였으며, 유형별 대국민 행동 요령을 함께 논의한 것으로 확인됨
▪ 금융정보분석원은 관계부처와의 협의를 통해 적극적으로 피해예방 홍보활동을 추진하고, 거래정지 제도의 명확한 법적근거를 마련하기 위해 특금법 개정을 신속히 추진할 계획이라고 밝힘
▶ 신종피싱 의심계좌 명의인에 대해 강화된 고객확인을 적용하여 민생범죄 차단과 AML 프로세스를 긴밀히 연계하고, 전담 인력 확충 및 유관기관과의 신속한 공조를 통해 대응 역량을 강화해야 함
* 「전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법」상 보이스피싱 범죄에 포함되지 않는 ‘재화와 용역의 거래를 가장한’ 전기통신금융사기 (신종피싱)에 대해서도 신속한 계좌 거래정지가 가능하도록 한 제도

--------------------------------------------------------------------------------

[AML]
03. FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)
▪ 지난 8월 11일 미국 재무부 산하 금융범죄단속네트워크(FinCEN)은 기업 투명성법(CTA)에 따라 추진되었던 미국 기업 및 미국인의 실소유자 정보 신고 의무를 완전히 면제하는 최종 규칙을 발표함
▪ 이는 수많은 중소기업들에게 부과되었던 과도한 행정적·재정적 부담을 덜어주기 위한 규제 완화 조치로, 이에 따라 미국 내 설립된 기업 및 미국인은 실소유자 신고 의무에서 제외됨
▪ 또한, 이미 FinCEN ID를 발급받은 미국인은 향후 정보변경 및 수정 보고 의무가 면제되며, 기 제출된 실소유자 정보와 설립자 데이터가 모두 삭제될 예정임
▪ 단, 미국에 등록된 외국 법인의 경우 외국인 실소유자에 대한 신고 의무는 일부 유지되나, 외국 법인 내 ‘미국인 실소유자’나 ‘미국인 회사 설립자’에 대한 정보 보고 의무는 면제됨
▶ 미국에 진출한 해외법인은 여전히 신고 의무를 부담하며, 정부 중앙 데이터 삭제에 따라 금융기관의 독자적인 고객확인(CDD/EDD) 비용과 노력 투입이 필요해짐
▶ 전 세계적으로 기업 투명성을 강화하는 추세임에도 미국이 국제 동향과 어긋나는 방향으로 선회함에 따라 다국적 기업 및 금융사들은 국가별로 상이한 실소유자 식별 및 보고 프로세스를 적용해야 하는 실무적 복잡성에 직면하게 될 가능성이 높음

--------------------------------------------------------------------------------

[Sanctions/AML]
04. 주요국 감독기구, 신종 초국경 스캠·자금세탁 거래 차단 공동 대응 (‘26.8.13)
▪ 국제 자금세탁방지 감독기구 및 주요국 FIU는 최근 급증하는 초국경 조직범죄, 불법 온라인 도박 및 신종 금융사기 자금세탁에 대응하기 위한 다자간 실시간 정보공유 및 즉시 지급정지 공조 체계를 강화하기로 합의함
▪ 주요 위험 요소로 가상자산 믹서, 미등록 해외 PG사 및 대포통장 유통망을 결합한 지능형 세탁 수법이 지목되었으며, 고위험 결제대행사에 대한 실시간 모니터링 기준을 제시함
▶ 국경 간 고액·빈번 거래 및 해외 결제대행(PG) 연계 계좌에 대한 FDS(이상금융거래탐지시스템) 룰 고도화와 함께 해외 감독기관의 제재/경고 리스트를 반영한 선제적 모니터링 체계 확립이 요구됨
"""

    # 2. HTML version
    body_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Malgun Gothic", "맑은 고딕", helvetica, sans-serif; line-height: 1.6; color: #222; background-color: #f4f6f9; margin: 0; padding: 20px; }}
        .container {{ max-width: 860px; margin: 0 auto; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); padding: 36px 40px; border: 1px solid #e2e8f0; }}
        .header {{ border-bottom: 2px solid #1a202c; padding-bottom: 20px; margin-bottom: 28px; }}
        .sub-header {{ font-size: 13px; color: #718096; letter-spacing: 1px; text-transform: uppercase; font-weight: bold; margin-bottom: 6px; }}
        .title {{ font-size: 24px; font-weight: 800; color: #1a202c; margin: 0 0 10px 0; }}
        .badge-date {{ display: inline-block; background: #edf2f7; color: #4a5568; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; }}
        
        .toc-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px 24px; margin-bottom: 32px; }}
        .toc-title {{ font-weight: 700; font-size: 16px; margin-bottom: 12px; color: #2d3748; }}
        .toc-list {{ margin: 0; padding-left: 20px; font-size: 14px; color: #4a5568; }}
        .toc-list li {{ margin-bottom: 6px; }}
        
        .card {{ background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; padding: 24px; margin-bottom: 28px; }}
        .card-header {{ display: flex; align-items: flex-start; margin-bottom: 16px; }}
        .card-category {{ background: #0f172a; color: #fff; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-right: 10px; }}
        .card-category.sanctions {{ background: #7c2d12; }}
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
          <span class="badge-date">2026년 8월 2주차 주간 공시 보고 (2026.08.10 ~ 2026.08.14)</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📌 8월 2주차 주요 공시 목차</div>
          <ol class="toc-list">
            <li>가상자산 시장 투명성 강화를 위한 「특금법 시행령」 개정안 국무회의 의결 (‘26.8.11)</li>
            <li>KoFIU, 신종피싱 의심계좌 거래정지제도 점검회의 개최 (‘26.8.10)</li>
            <li>FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)</li>
            <li>주요국 감독기구, 신종 초국경 스캠·자금세탁 거래 차단 공동 대응 (‘26.8.13)</li>
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
                <strong>① 신고 불수리 요건 및 심사 대상 구체화:</strong> 가상자산사업자의 대주주 범위가 대표이사 또는 이사의 과반수를 선임한 주주, 최대주주가 법인인 경우 해당 법인의 최대주주와 대표자로 확대됨. 사업자의 재무상태 및 내부통제 기준 등 불수리 요건 구체화.<br>
                <strong>② 가상자산 이전거래에 대한 자금세탁방지의무 부과:</strong> 트래블룰 기준 금액을 폐지하여 모든 이전거래로 확대하고 1천만원 이상 거래 시 자체 의심거래 관리체계 구축 의무 부과.
              </div>
            </li>
            <li>퇴직 임직원 제재조치 통보 권한 위탁 및 고객 특성·위험도에 따른 고객확인의무 이행 방법 명확화</li>
          </ul>
          <div class="insight-box">
            은행의 제휴 거래소 평가 및 리스크 관리 책임이 가중되었으며, 거래소의 트래블룰 전면 확대, 위험도 차등 관리 및 의심거래 관리체계 요구에 따른 은행권의 위험평가 및 의심거래 모니터링 강화가 필요함
          </div>
        </div>

        <!-- 02 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❷ KoFIU, 신종피싱 의심계좌 거래정지제도* 점검회의 개최 (‘26.8.10)</strong></div>
          </div>
          <ul class="content-list">
            <li>금융정보분석원(KoFIU)는 ‘신종피싱 의심계좌 거래정지제도 점검회의’를 통해 제도 운영 현황과 범죄유형별 피해사례 등을 점검함</li>
            <li>시행 한 달간 총 4,935건 임시조치 중 3,750건을 특금법상 강화된 고객확인(EDD) 대상으로 분류해 임시거래정지 처리함</li>
            <li>주요 범죄 유형: 로맨스스캠 41%(1,527건), 노쇼사기 37%(1,376건), 팀미션사기 22%(847건)</li>
          </ul>
          <div class="insight-box">
            신종피싱 의심계좌 명의인에 대해 강화된 고객확인을 적용하여 민생범죄 차단과 AML 프로세스를 긴밀히 연계하고, 전담 인력 확충 및 유관기관과의 신속한 공조를 통해 대응 역량을 강화해야 함
          </div>
          <div class="footnote">* 신종피싱: 통신사기피해환급법상 보이스피싱에 포함되지 않는 '재화와 용역 거래 가장' 사기 계좌에 대해서도 신속 거래정지가 가능하도록 한 제도</div>
        </div>

        <!-- 03 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category">AML</span>
            <div class="card-title"><strong>❸ FinCEN, 실소유자 정보(BOI) 신고 의무 폐지 최종 확정 (‘26.8.11)</strong></div>
          </div>
          <ul class="content-list">
            <li>미국 FinCEN은 기업 투명성법(CTA)에 따른 미국 기업 및 미국인의 실소유자 정보(BOI) 신고 의무를 완전히 면제하는 최종 규칙 발표</li>
            <li>중소기업 부담 완화 조치로 미국 내 설립 기업·미국인은 신고 의무에서 제외되며 기 제출 데이터도 삭제 예정</li>
            <li>단, 미국 등록 외국 법인은 외국인 실소유자 신고 의무 일부 유지</li>
          </ul>
          <div class="insight-box">
            미국 진출 해외법인의 신고 의무 및 중앙 데이터 삭제에 따라 금융기관의 독자적 CDD/EDD 비용 투입이 불가피하며, 국가별 상이한 실소유자 식별 규제 대응을 위한 실무 복잡성 관리가 필요함
          </div>
        </div>

        <!-- 04 -->
        <div class="card">
          <div class="card-header">
            <span class="card-category sanctions">Sanctions/AML</span>
            <div class="card-title"><strong>❹ 주요국 감독기구, 신종 초국경 스캠·자금세탁 거래 차단 공동 대응 (‘26.8.13)</strong></div>
          </div>
          <ul class="content-list">
            <li>초국경 조직범죄, 불법 온라인 도박 및 신종 금융사기 자금세탁에 대응하기 위한 다자간 실시간 정보공유 및 지급정지 공조 체계 강화</li>
            <li>가상자산 믹서, 미등록 해외 PG사, 대포통장 유통망 결합 수법에 대한 고위험 결제대행사 실시간 모니터링 기준 제시</li>
          </ul>
          <div class="insight-box">
            국경 간 고액·빈번 거래 및 해외 결제대행(PG) 연계 계좌에 대한 이상금융거래탐지(FDS) 룰 고도화와 선제적 모니터링 체계 확립이 필수적임
          </div>
        </div>

        <div class="footer">
          본 메일은 AML &amp; Sanctions Weekly Insight 주간 보고 시스템을 통해 발송되었습니다.
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
    print("[이메일 발송 완료] 성공적으로 발송되었습니다.")

if __name__ == "__main__":
    send_week2_insight_email()
