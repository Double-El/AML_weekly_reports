import re
import html
from typing import List, Dict, Any, Tuple

from gemini_collector import call_gemini_rest_api


def build_responsive_html_report(
    verified_items: List[Dict[str, Any]],
    week_title: str,
    date_range: str,
) -> str:
    """
    고품질 반응형 HTML 주간 보고서 템플릿을 생성합니다.
    """
    toc_items = ""
    cards_html = ""

    if not verified_items:
        cards_html = f"""
        <div class="card">
          <div class="card-header">
            <span class="card-category">안내</span>
            <div class="card-title">주간 공시 내역 확인 결과</div>
          </div>
          <p style="font-size: 14.5px; color: #475569; line-height: 1.7; margin: 0;">
            금주 모니터링 대상인 국내외 15개 자금세탁방지 감독기관(KoFIU, 금감원, 관세청, FATF, FinCEN, OFAC, AMLA, MAS 등)의 공식 공시 내역을 수집하고 교차 검증한 결과, 해당 주차에 공식 발표된 신규 공시 내용이 없음을 확인하였습니다. 주요 감독기관의 추가적인 제재 및 가이드라인 발표 여부를 지속적으로 모니터링하겠습니다.
          </p>
        </div>
        """
        toc_items = "<li>해당 기간 내 보고 대상 공식 공시 내역 없음</li>"
    else:
        for idx, item in enumerate(verified_items, 1):
            target_d = item.get("target_date_info", {})
            date_str = target_d.get("date_label", target_d.get("short_date_label", "일자 미상"))
            authority = item.get("authority", "감독기관")
            title = item.get("title", "")
            summary = item.get("summary", "")
            source_url = item.get("source_url", "")
            
            is_sanction = "제재" in authority or "OFAC" in authority or "OFSI" in authority or "제재" in title or "Sanctions" in title
            category_class = "card-category sanctions" if is_sanction else "card-category"
            category_name = "Sanctions / AML" if is_sanction else "AML"

            toc_items += f"<li><strong>[{category_name}]</strong> {html.escape(title)} (‘{html.escape(date_str)})</li>\n"

            link_html = f'<div style="margin-top: 14px; font-size: 13px; color: #64748b; padding-top: 8px; border-top: 1px dashed #e2e8f0;">🔗 출처 링크: <a href="{html.escape(source_url)}" target="_blank" style="color: #2563eb; word-break: break-all;">{html.escape(source_url)}</a></div>' if source_url else ""

            cards_html += f"""
        <!-- Card {idx:02d} -->
        <div class="card">
          <div class="card-header">
            <span class="{category_class}">{category_name}</span>
            <div class="card-title">{idx:02d}. {html.escape(title)} (‘{html.escape(date_str)})</div>
          </div>
          
          <div class="section-subtitle">[1] 배경 및 개요 ({html.escape(authority)})</div>
          <ul class="content-list">
            <li>{html.escape(summary)}</li>
          </ul>

          <div class="section-subtitle">[2] 주요 내용 및 세부 분석</div>
          <ul class="content-list">
            <li><strong>감독·제재 요건 및 기준 준수:</strong>
              <div class="sub-bullet-box">
                <p>• {html.escape(authority)}의 공식 발표 및 규제 지침에 따라 관련 금융거래의 투명성과 내부통제 요건이 강화됨.</p>
                <p>• 신종 금융범죄 수법 및 글로벌 제재 리스크 차단을 위한 다각적 감시 프로세스 요구.</p>
              </div>
            </li>
          </ul>

          <div class="insight-card">
            <div class="insight-header">▶ AML 전문가 시사점 및 금융권 대응 방향</div>
            <ul class="insight-body">
              <li><strong>거래 모니터링(FDS/STR) 시나리오 점검:</strong> 공시된 제재 대상, 고위험 거래 유형 및 이상 결제 패턴을 모니터링 시스템 룰셋에 즉시 반영해야 합니다.</li>
              <li><strong>고객확인(CDD/EDD) 및 내부통제 고도화:</strong> 관련 거래 상대방 및 법인 실소유자(BO) 검증 절차를 강화하고 전사 자금세탁 위험평가(EWRA) 모델에 반영해야 합니다.</li>
            </ul>
          </div>
          {link_html}
        </div>
        """

    return f"""
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
          <span class="badge-date">{week_title} 상세 보고서 ({date_range})</span>
        </div>

        <div class="toc-box">
          <div class="toc-title">📋 {week_title} 주요 공시 및 핵심 의제</div>
          <ol class="toc-list">
            {toc_items}
          </ol>
        </div>

        {cards_html}

        <div class="footer">
          본 상세 보고서는 AML &amp; Sanctions Weekly Insight 시스템을 통해 생성 및 발송되었습니다.
        </div>
      </div>
    </body>
    </html>
    """


def generate_expert_report(
    verified_items: List[Dict[str, Any]],
    week_title: str,
    date_range: str,
    client: Any = None,
) -> Tuple[str, str, str]:
    """
    엄선된 공시 항목들을 바탕으로 전문가 시각의 텍스트 및 HTML 보고서를 작성합니다.
    (aml_report_20260720_week3.txt 표준 템플릿과 100% 동일한 구조와 전문성 준수)
    반환값: (이메일 제목, 일반 텍스트 본문, 반응형 HTML 본문)
    """
    email_subject = f"[AML & Sanctions Weekly Insight] {week_title} 자금세탁방지 주요 공시 상세 보고서"

    if not verified_items:
        no_data_body = f"""[AML & Sanctions Weekly Insight] {week_title}

자금세탁방지본부 CoP
수집 및 분석 대상 주차: {week_title} ({date_range})

================================================================================
■ {week_title} 주요 공시 목차
================================================================================
- 해당 기간 내 보고 대상 공식 공시 내역 없음

================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================
금주 모니터링 대상인 국내외 15개 자금세탁방지 감독기관의 공식 공시 내역을 수집하고 공시일자를 교차 검증한 결과, 해당 주차에 공식 발표된 신규 공시 내용이 없음을 확인하였습니다. 주요 감독기관의 추가적인 제재 및 가이드라인 발표 여부를 지속적으로 모니터링하겠습니다.
"""
        html_body = build_responsive_html_report([], week_title, date_range)
        return email_subject, no_data_body, html_body

    # 프롬프트 입력 데이터 구성
    items_context = ""
    for idx, item in enumerate(verified_items, 1):
        target_d = item.get("target_date_info", {})
        date_str = target_d.get("date_label", target_d.get("short_date_label", "일자 미상"))
        authority = item.get("authority", "감독기관")
        title = item.get("title", "")
        summary = item.get("summary", "")
        source_url = item.get("source_url", "링크 없음")

        items_context += f"""
[공시 항목 {idx}]
- 공시일자: {date_str}
- 감독기관: {authority}
- 공시 제목: {title}
- 주요 내용: {summary}
- 교차검증 링크: {source_url}
"""

    prompt = f"""당신은 자금세탁방지(AML) 및 글로벌 금융 컴플라이언스 최고 전문가입니다.
다음 검증된 국내외 감독기관 공시 목록을 바탕으로, 금융회사 경영진과 AML 실무 부서에서 즉시 업무에 활용할 수 있는 주간 공시 보고서를 작성해 주세요.

수집 대상 주차: {week_title} ({date_range})

검증 완료된 공시 데이터:
{items_context}

[작성 형식 및 필수 준수 규칙 - 엄격 준수]
1. [이모티콘 사용 엄격 금지] 이모티콘, 이모지(예: 🚨, 📌, 💡, 📅 등)는 일체 사용하지 마세요. 오직 표준 텍스트 기호(=, -, ▪, ①, ②, ▶)와 완결된 한글 문장만 사용하세요.
2. [전체 문서 구조]:
[AML & Sanctions Weekly Insight] {week_title}

자금세탁방지본부 CoP
수집 및 분석 대상 주차: {week_title} ({date_range})

================================================================================
■ {week_title} 주요 공시 목차
================================================================================
01 | [AML 또는 Sanctions/AML] 공시 제목 (‘일자)
...

================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================

--------------------------------------------------------------------------------
[AML 또는 Sanctions/AML] 번호. 공시 제목 (‘일자)
--------------------------------------------------------------------------------
[1] 배경 및 개요 (또는 제재 배경 및 발표 내용 / 발간 배경 및 개요)
▪ 상세 서술...

[2] 주요 내용 및 세부 분석 (또는 주요 제재 대상 및 범죄 수법 / 주요 논의 사항 및 성과)
① 세부 소항목 명칭
- 구체적 내용...
② 세부 소항목 명칭
- 구체적 내용...
③ 세부 소항목 명칭
- 구체적 내용...

▶ [시사점 및 금융권 대응 방향]
- 모니터링/FDS/STR 관련 실무 대응 방향 서술...
- 고객확인(CDD/EDD)/제재 필터링/내부통제 실무 대응 방향 서술...

3. 각 공시별로 위 템플릿 구조를 완벽하게 유지하여 전문가 시각의 전문을 작성하세요.
"""

    response_text, _ = call_gemini_rest_api(
        prompt=prompt,
        enable_grounding=False,
        temperature=0.2,
    )

    clean_text = ""
    if response_text:
        # 혹시 모를 유니코드 이모지 제거
        clean_text = re.sub(r'[\U00010000-\U0010ffff]', '', response_text.strip())
        # "제목: " 중복 제거
        clean_text = re.sub(r'^제목:\s*.*?\n\n', '', clean_text)
    else:
        # Fallback 텍스트 생성
        clean_text = f"""[AML & Sanctions Weekly Insight] {week_title}

자금세탁방지본부 CoP
수집 및 분석 대상 주차: {week_title} ({date_range})

================================================================================
■ {week_title} 주요 공시 목차
================================================================================
"""
        for idx, item in enumerate(verified_items, 1):
            target_d = item.get("target_date_info", {})
            date_str = target_d.get("date_label", target_d.get("short_date_label", "일자 미상"))
            authority = item.get("authority", "")
            is_sanction = "제재" in authority or "OFAC" in authority or "OFSI" in authority or "제재" in item.get("title", "")
            cat = "Sanctions/AML" if is_sanction else "AML"
            clean_text += f"{idx:02d} | [{cat}] {item.get('title', '')} (‘{date_str})\n"

        clean_text += """
================================================================================
■ 세부 공시 분석 및 전문가 시사점
================================================================================
"""
        for idx, item in enumerate(verified_items, 1):
            target_d = item.get("target_date_info", {})
            date_str = target_d.get("date_label", target_d.get("short_date_label", "일자 미상"))
            authority = item.get("authority", "감독기관")
            is_sanction = "제재" in authority or "OFAC" in authority or "OFSI" in authority or "제재" in item.get("title", "")
            cat = "Sanctions/AML" if is_sanction else "AML"

            clean_text += f"""
--------------------------------------------------------------------------------
[{cat}] {idx:02d}. {item.get('title', '')} (‘{date_str})
--------------------------------------------------------------------------------
[1] 배경 및 개요 ({authority})
▪ {item.get('summary', '')}

[2] 주요 내용 및 세부 분석
① 감독기관 공식 지침 및 규제 기준 강화
- {authority}의 공식 공시 및 세부 기준에 따라 관련 금융거래 및 컴플라이언스 절차를 정비할 필요가 있음.
② 불법 자금세탁 및 이상거래 차단 체계
- 신종 금융범죄 수법 및 국경 간 자금 이동에 대한 선제적 모니터링 요구.

▶ [시사점 및 금융권 대응 방향]
- 해당 감독기관의 공시 및 제재 기준을 반영하여 거래 모니터링 시스템(FDS/STR) 시나리오를 점검하고 고객확인(CDD/EDD) 절차를 강화해야 합니다.
- 교차검증 링크: {item.get('source_url', '링크 없음')}
"""

    html_body = build_responsive_html_report(verified_items, week_title, date_range)
    return email_subject, clean_text, html_body
