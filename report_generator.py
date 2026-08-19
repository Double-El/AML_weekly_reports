import re
from typing import List, Dict, Any, Tuple

from gemini_collector import call_gemini_rest_api


def generate_expert_report(
    verified_items: List[Dict[str, Any]],
    week_title: str,
    date_range: str,
    client: Any = None,
) -> Tuple[str, str]:
    """
    엄선된 공시 항목들을 바탕으로 자금세탁방지(AML) 전문가 시각의 보고서를 작성합니다.
    - 복사해서 붙여 넣을 수 있게 이모티콘 없이 순수 텍스트만으로 완결된 문장 작성
    - 전문가 시각을 유지하되 항목명은 "시사점"으로만 표기
    - 간략한 총괄 소견, 공시내용의 간결한 제목, 상세한 주요내용, 시사점, 교차검증 링크, 첨부파일 명시
    """
    email_subject = f"[AML 주간 공시 보고서] {week_title} 자금세탁방지 감독기관 주요 공시 및 시사점"

    if not verified_items:
        no_data_body = f"""자금세탁방지(AML) 주간 감독기관 공시 동향 보고서

수집 대상 주차: {week_title} ({date_range})
모니터링 대상 기관: 금융정보분석원(KoFIU), 금융감독원(FSS), 관세청(KCS) 및 FATF, FinCEN, OFAC, NYDFS, AMLA, EBA, FCA, MAS, HKMA, Egmont Group, OFSI 등 15개 국내외 감독기관

1. 총괄 소견
금주 모니터링 대상인 국내외 15개 자금세탁방지 감독기관의 공식 공시 내역을 수집하고 공시일자를 교차 검증한 결과, 해당 주차에 공식 발표된 신규 공시 내용이 없음을 확인하였습니다. 주요 감독기관의 추가적인 제재 및 가이드라인 발표 여부를 지속적으로 모니터링하겠습니다.

2. 세부 공시 내역
- 해당 기간 내 보고 대상 공식 공시 내역 없음.
"""
        return email_subject, no_data_body

    # 프롬프트 입력 데이터 구성
    items_context = ""
    for idx, item in enumerate(verified_items, 1):
        target_d = item.get("target_date_info", {})
        date_str = target_d.get("date_label", "일자 미상")
        authority = item.get("authority", "감독기관")
        title = item.get("title", "")
        summary = item.get("summary", "")
        source_url = item.get("source_url", "링크 없음")
        screenshot_file = item.get("screenshot_path", "")
        screenshot_name = screenshot_file.split("\\")[-1].split("/")[-1] if screenshot_file else "첨부파일 없음"

        items_context += f"""
[공시 항목 {idx}]
- 공시일자: {date_str}
- 감독기관: {authority}
- 공시 제목: {title}
- 주요 내용: {summary}
- 교차검증 링크: {source_url}
- 첨부파일명: {screenshot_name}
"""

    prompt = f"""당신은 자금세탁방지(AML) 및 글로벌 금융 컴플라이언스 전문가입니다.
다음 검증된 국내외 감독기관 공시 목록을 바탕으로, 금융회사 경영진과 AML 실무 부서에서 즉시 업무에 활용할 수 있는 주간 공시 보고서를 작성해 주세요.

수집 대상 주차: {week_title} ({date_range})

검증 완료된 공시 데이터:
{items_context}

[작성 원칙 및 필수 준수 규칙]
1. [이모티콘 사용 엄격 금지] 이모티콘, 이모지(예: 🚨, 📌, 💡, 📅 등)는 일체 사용하지 마세요. 공식 문서에 바로 복사하여 붙여넣을 수 있도록 오직 표준 텍스트 기호(-, 1., [ ], .)와 완결된 한글 문장만 사용하세요.
2. [표기 규칙] 시사점 항목을 작성할 때는 반드시 "AML 전문가 시사점"이 아니라 오직 "시사점"으로만 표기하세요.
3. [문장 스타일] 모든 문장은 전문성을 갖춘 완결된 경어체(~합니다, ~하여야 합니다) 또는 명확한 명사형 종결 문장으로 작성하세요.
4. [보고서 구성]:
   - 맨 처음에 전체 주간 동향을 요약하는 "1. 총괄 소견"을 3~5문장으로 간략하게 작성하세요.
   - 이어서 "2. 주요 공시별 상세 분석" 아래에 각 공시별로 다음 순서대로 명확히 작성하세요:
     가. 간결한 제목
     나. 감독기관 및 공시일자
     다. 상세한 주요내용
     라. 시사점 (자금세탁방지 전문가의 시각에서 거래 모니터링, 고객확인제도(CDD/EDD), 내부통제, 제재 필터링 등에 미치는 영향과 대응 방향 서술)
     마. 교차검증 링크 (제공된 URL 기재)
     바. 첨부파일 (제공된 첨부파일명 기재)

위 원칙을 철저히 지켜 완성된 보고서 전문을 출력해 주세요.
"""

    response_text, _ = call_gemini_rest_api(
        prompt=prompt,
        enable_grounding=False,
        temperature=0.2,
    )

    if response_text:
        # 혹시 모를 유니코드 이모지 제거
        clean_text = re.sub(r'[\U00010000-\U0010ffff]', '', response_text.strip())
        # "AML 전문가 시사점"을 "시사점"으로 치환 보장
        clean_text = re.sub(r'AML\s*전문가\s*시사점', '시사점', clean_text)
        return email_subject, clean_text

    # 폴백 텍스트
    fallback_body = f"""자금세탁방지(AML) 주간 감독기관 공시 동향 보고서

수집 대상 주차: {week_title} ({date_range})

1. 총괄 소견
금주 수집 및 검증된 국내외 자금세탁방지 감독기관의 주요 공시 내역을 아래와 같이 정리하여 보고합니다.

2. 주요 공시별 상세 분석
"""
    for idx, item in enumerate(verified_items, 1):
        target_d = item.get("target_date_info", {})
        date_str = target_d.get("date_label", "일자 미상")
        screenshot_file = item.get("screenshot_path", "")
        screenshot_name = screenshot_file.split("\\")[-1].split("/")[-1] if screenshot_file else "첨부파일 없음"

        fallback_body += f"""
[{idx}] {item.get('title', '')}
- 감독기관 및 공시일자: {item.get('authority', '')} ({date_str})
- 상세한 주요내용: {item.get('summary', '')}
- 시사점: 해당 감독기관의 공시 및 제재 기준을 반영하여 거래 모니터링 시스템의 시나리오 및 고객확인 절차를 점검하고 내부통제 체계를 강화할 필요가 있습니다.
- 교차검증 링크: {item.get('source_url', '')}
- 첨부파일: {screenshot_name}
"""
    return email_subject, fallback_body
