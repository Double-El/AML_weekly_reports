import time
import re
from pathlib import Path
from typing import Optional, List, Dict, Any
from playwright.sync_api import sync_playwright

from config import SCREENSHOT_DIR


def sanitize_filename(name: str) -> str:
    """파일명으로 안전하게 사용할 수 있도록 특수문자를 제거합니다."""
    return re.sub(r'[^a-zA-Z0-9가-힣_-]', '_', name)[:40]


def capture_webpage_screenshot(
    url: str,
    output_filename: str,
    timeout_ms: int = 20000,
) -> Optional[Path]:
    """
    Playwright 브라우저를 통해 실제 출처 웹페이지에 접속하여 화면을 캡처합니다.
    원문 헤드와 공시일자가 명확히 나타나도록 페이지 렌더링 후 필요시 스크롤하여 캡처합니다.
    """
    if not url or not url.startswith("http"):
        print(f"  [스크린샷 건너뜀] 유효하지 않은 URL: {url}")
        return None

    screenshot_path = SCREENSHOT_DIR / output_filename

    try:
        with sync_playwright() as p:
            # 브라우저 실행 (안정적인 헤드리스 모드)
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": 1280, "height": 900},
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/125.0.0.0 Safari/537.36"
                ),
            )
            page = context.new_page()

            print(f"  [웹페이지 접속 및 캡처] {url}")
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
                time.sleep(2)  # 동적 콘텐츠 및 폰트 로드 대기
            except Exception as nav_e:
                print(f"  [웹페이지 로딩 대기 시간 초과, 현재 상태 캡처 진행] {nav_e}")

            # 원문 헤드 및 공시일자가 한눈에 들어오도록 적절히 스크롤 조정
            try:
                # 상단 헤더 배너가 너무 클 경우 본문 헤드와 일자가 보이도록 약간 스크롤(150px)
                page.evaluate("window.scrollBy(0, 150)")
                time.sleep(1)
            except Exception:
                pass

            page.screenshot(path=str(screenshot_path), full_page=False)
            browser.close()

        if screenshot_path.exists() and screenshot_path.stat().st_size > 0:
            print(f"  [스크린샷 저장 완료] {screenshot_path.name}")
            return screenshot_path
        else:
            return None

    except Exception as e:
        print(f"  [스크린샷 캡처 오류] URL {url} 처리 실패: {e}")
        return None


def capture_screenshots_for_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    검증 완료된 각 이슈 항목당 1개의 교차검증 출처 스크린샷을 캡처하여 매핑합니다.
    """
    print(f"\n[출처 웹페이지 스크린샷 캡처 시작] 총 {len(items)}건 대상")
    for idx, item in enumerate(items, 1):
        source_url = item.get("source_url")
        safe_title = sanitize_filename(item.get("title", f"issue_{idx}"))
        timestamp = int(time.time())
        filename = f"aml_issue_{idx}_{safe_title}_{timestamp}.png"

        if source_url:
            screenshot_file = capture_webpage_screenshot(source_url, filename)
            item["screenshot_path"] = str(screenshot_file) if screenshot_file else None
        else:
            item["screenshot_path"] = None

    return items
