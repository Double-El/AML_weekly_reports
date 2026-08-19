import json
import re
import time
import requests
from typing import List, Dict, Any, Optional, Tuple

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    FALLBACK_MODELS,
    DOMESTIC_AUTHORITIES,
    INTERNATIONAL_AUTHORITIES,
    ALL_TARGET_AUTHORITIES,
)


def call_gemini_rest_api(
    prompt: str,
    enable_grounding: bool = False,
    temperature: float = 0.1,
    max_retries: int = 3,
) -> Tuple[Optional[str], List[str]]:
    """
    Google AI Studio REST API를 직접 호출합니다.
    반환값: (생성된 텍스트, Grounding 웹 검색 출처 URL 목록)
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY가 설정되지 않았습니다. .env 파일을 확인해 주세요.")

    models_to_try = [GEMINI_MODEL] + [m for m in FALLBACK_MODELS if m != GEMINI_MODEL]

    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={GEMINI_API_KEY}"
        grounding_options = [True, False] if enable_grounding else [False]

        for use_grounding in grounding_options:
            payload: Dict[str, Any] = {
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ],
                "generationConfig": {
                    "temperature": temperature,
                }
            }
            if use_grounding:
                payload["tools"] = [{"google_search": {}}]

            for attempt in range(max_retries):
                try:
                    res = requests.post(
                        url,
                        headers={"Content-Type": "application/json"},
                        json=payload,
                        timeout=35,
                    )
                    if res.status_code == 200:
                        data = res.json()
                        candidates = data.get("candidates", [])
                        if candidates:
                            parts = candidates[0].get("content", {}).get("parts", [])
                            text_parts = [p.get("text", "") for p in parts if "text" in p]
                            full_text = "".join(text_parts).strip()

                            # Grounding 출처 URL 수집
                            grounding_urls = []
                            grounding_metadata = candidates[0].get("groundingMetadata", {})
                            chunks = grounding_metadata.get("groundingChunks", [])
                            for chunk in chunks:
                                web_info = chunk.get("web", {})
                                uri = web_info.get("uri")
                                if uri and uri not in grounding_urls:
                                    grounding_urls.append(uri)

                            if full_text:
                                return full_text, grounding_urls
                    elif res.status_code == 429:
                        wait_sec = (attempt + 1) * 3
                        print(f"  [API 할당량 대기] {model_name} (Search={use_grounding}) {wait_sec}초 대기 후 재시도...")
                        time.sleep(wait_sec)
                    elif res.status_code in [400, 404]:
                        break
                    else:
                        print(f"  [API 응답 상태: {res.status_code}] {res.text[:120]}")
                        time.sleep(2)
                except Exception as e:
                    print(f"  [HTTP 요청 오류] {e}")
                    time.sleep(2)

    return None, []


def build_authority_constraint_text() -> str:
    domestic_str = "\n".join([f"{i+1}. {a}" for i, a in enumerate(DOMESTIC_AUTHORITIES)])
    intl_str = "\n".join([f"{i+1}. {a}" for i, a in enumerate(INTERNATIONAL_AUTHORITIES)])
    return (
        "수집 대상은 아래 지정된 15개 자금세탁방지(AML) 및 금융제재 감독기관의 공식 발표/공시 내용에 한정됩니다:\n"
        "1. 국내 감독기관\n"
        f"{domestic_str}\n"
        "2. 국제감독기구\n"
        f"{intl_str}\n"
    )


def extract_first_source_url(text_content: str, fallback_urls: Optional[List[str]] = None) -> Optional[str]:
    """
    텍스트에서 가장 먼저 나오는 유효한 웹 URL을 추출합니다.
    텍스트에 없으면 fallback_urls의 첫 번째 유효 URL을 반환합니다.
    """
    if text_content:
        url_pattern = re.compile(r'https?://[^\s)\]">]+')
        matches = url_pattern.findall(text_content)
        if matches:
            return matches[0].rstrip('.,;:')

    if fallback_urls:
        for u in fallback_urls:
            if u and u.startswith("http"):
                return u.rstrip('.,;:')

    return None


def collect_daily_announcements(
    target_date_info: Dict[str, Any],
    client: Any = None,
) -> List[Dict[str, Any]]:
    """
    1단계: 특정 일자의 공시 내용을 Gemini API를 통해 질문하고 수집합니다.
    질문 예: "26년 8월 10일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."
    """
    question_prompt = target_date_info["question"]
    authority_text = build_authority_constraint_text()

    prompt = f"""{authority_text}

질문: "{question_prompt}"

지침:
1. 위 15개 감독기관에서 {target_date_info['date_label']}에 실제로 발표 또는 공시된 공식 보도자료, 제재 부과, 법령/가이드라인 개정, 제재 리스트 업데이트 등의 내용을 조사하여 알려주세요.
2. 각 공시별로 감독기관명, 간결한 공시 제목, 상세한 공시 내용을 구조화하여 작성해 주세요.
3. 해당 일자에 위 15개 기관의 공식 공시가 전혀 확인되지 않는 경우 "공시 내용 없음"으로 응답해 주세요.
4. 아래 JSON 형식의 배열(Array)로만 출력해 주세요:
```json
[
  {{
    "authority": "기관명 (예: 금융정보분석원 (KoFIU))",
    "title": "공시 제목",
    "summary": "상세한 공시 내용"
  }}
]
```
만약 공시 내용이 없으면 [] 빈 배열을 반환해 주세요.
"""

    print(f"\n[1단계 질의] {target_date_info['date_label']} -> '{question_prompt}'")

    response_text, grounding_urls = call_gemini_rest_api(
        prompt=prompt,
        enable_grounding=True,
        temperature=0.1,
    )

    if not response_text or "공시 내용 없음" in response_text or len(response_text.strip()) < 10:
        print(f"  -> {target_date_info['date_label']} 공시 내용 없음")
        return []

    # JSON 파싱
    items = []
    try:
        match = re.search(r'```(?:json)?\s*(\[[\s\S]*?\])\s*```', response_text)
        json_str = match.group(1) if match else response_text
        parsed = json.loads(json_str)
        if isinstance(parsed, list):
            items = parsed
    except Exception:
        # JSON 파싱 불가 시 텍스트 분할 처리
        if len(response_text) > 30 and "없음" not in response_text[:40]:
            items = [{
                "authority": "국내외 자금세탁방지 감독기관",
                "title": f"{target_date_info['date_label']} 자금세탁방지 감독기관 주요 공시",
                "summary": response_text.strip(),
            }]

    valid_items = []
    for item in items:
        if isinstance(item, dict) and item.get("title"):
            item["target_date_info"] = target_date_info
            valid_items.append(item)

    print(f"  -> 1단계 추출된 공시 항목: {len(valid_items)}건")
    return valid_items


def verify_announcement_date(
    item: Dict[str, Any],
    client: Any = None,
) -> bool:
    """
    2단계: 정리된 답변을 각각 Gemini에게 다시 "해당 내용은 언제 공시가 되었나요?"라고 질문하여
    공시일자가 지정한 내용(예: '8월 10일')이 아니면 해당 내용은 삭제합니다.
    """
    target_date_info = item["target_date_info"]
    target_short = target_date_info["short_date_label"]  # 예: "8월 10일"
    target_full = target_date_info["date_label"]        # 예: "26년 8월 10일"
    target_iso = target_date_info["iso_date"]          # 예: "2026-08-10"

    content_snippet = f"감독기관: {item.get('authority', '')}\n제목: {item.get('title', '')}\n내용: {item.get('summary', '')}"

    verify_prompt = f"""다음 자금세탁방지 감독기관 공시 내용에 대해 사실관계를 확인합니다.

[공시 내용]
{content_snippet}

질문: "해당 내용은 언제 공시가 되었나요?"

지침:
1. 위 내용이 해당 감독기관을 통해 실제로 공식 공시(발표/보도자료 배포)된 정확한 날짜를 알려주세요.
2. 답변 첫머리에 반드시 공시일자(예: "{target_full}" 또는 "{target_short}")를 명확하게 명시해 주세요.
3. 다른 일자에 공시된 것이라면 실제 공시일자를 정확히 적어주세요.
"""

    answer_text, _ = call_gemini_rest_api(
        prompt=verify_prompt,
        enable_grounding=True,
        temperature=0.0,
    )

    if not answer_text:
        return False

    # 공시 일자 일치 여부 엄격 판별
    judge_prompt = f"""목표 검증 일자: "{target_short}" (연도 포함 시 "{target_full}" 또는 "{target_iso}")

질문 "해당 내용은 언제 공시가 되었나요?"에 대한 사실 확인 답변:
\"\"\"{answer_text}\"\"\"

위 답변에 따르면, 해당 공시의 실제 공식 발표/공시일자가 목표 일자인 "{target_short}" (월/일 일치)에 정확히 해당합니까?
- 목표 일자에 정확히 공시된 것이 맞다면 오직 "MATCH"라고만 답하세요.
- 다른 일자에 공시되었거나 일자가 불일치/불명확하다면 오직 "MISMATCH"라고만 답하세요.
"""
    verdict, _ = call_gemini_rest_api(
        prompt=judge_prompt,
        enable_grounding=False,
        temperature=0.0,
    )

    if verdict:
        verdict_str = verdict.strip().upper()
        is_match = "MATCH" in verdict_str and "MISMATCH" not in verdict_str
    else:
        is_match = target_short in answer_text or target_iso in answer_text

    print(f"  [2단계 일자 검증] '{item.get('title', '')[:28]}...' -> 목표: {target_short} | 판정: {'일치 (채택)' if is_match else '불일치 (삭제)'}")
    if is_match:
        item["verified_date_answer"] = answer_text
    return is_match


def request_cross_verification_link(
    item: Dict[str, Any],
    client: Any = None,
) -> Optional[str]:
    """
    3단계: 일자 검증 후 Gemini에게 "실제 조사 후 교차 검증 링크를 주세요" 라고 명령하고,
    답변 중 가장 먼저 나오는 출처 URL을 추출하여 반환합니다.
    """
    content_snippet = f"감독기관: {item.get('authority', '')}\n제목: {item.get('title', '')}\n내용: {item.get('summary', '')}"

    prompt = f"""다음 공시 내용에 대한 교차 검증을 진행합니다.

[공시 내용]
{content_snippet}

명령: "실제 조사 후 교차 검증 링크를 주세요"

지침:
1. 해당 감독기관의 공식 웹사이트, 보도자료 게시판, 공시 시스템의 실제 원문 페이지 URL을 조사하여 제공해 주세요.
2. 답변 가장 첫 부분에 유효한 원문 링크(URL)를 명확히 제시해 주세요.
"""

    print(f"  [3단계 교차 검증 링크 질의] '{item.get('title', '')[:28]}...' -> '실제 조사 후 교차 검증 링크를 주세요'")
    response_text, grounding_urls = call_gemini_rest_api(
        prompt=prompt,
        enable_grounding=True,
        temperature=0.0,
    )

    extracted_url = extract_first_source_url(response_text or "", grounding_urls)
    if extracted_url:
        print(f"    -> 교차 검증 링크 확보: {extracted_url}")
    else:
        print(f"    -> 교차 검증 링크를 찾을 수 없음")

    return extracted_url


def get_gemini_client() -> None:
    return None
