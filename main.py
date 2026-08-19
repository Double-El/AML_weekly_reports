import argparse
import sys
import os
from datetime import datetime
from pathlib import Path

# UTF-8 콘솔 출력 지원 (Windows 환경 대응)
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


from config import RECIPIENTS
from date_util import get_target_dates, get_week_info
from gemini_collector import (
    get_gemini_client,
    collect_daily_announcements,
    verify_announcement_date,
    request_cross_verification_link,
)
from screenshot_service import capture_screenshots_for_items
from report_generator import generate_expert_report
from email_sender import send_aml_report_email


def run_aml_pipeline(
    base_date: datetime = None,
    dry_run: bool = False,
    skip_screenshot: bool = False,
) -> None:
    """
    자금세탁방지(AML) 감독기관 공시 수집, 일자 재검증, 교차검증 링크 확보,
    스크린샷 캡처, 전문가 보고서 생성 및 이메일 발송 파이프라인을 실행합니다.
    """
    if base_date is None:
        base_date = datetime.now()

    print("=" * 75)
    print(" 자금세탁방지(AML) 감독기관 주간 공시 수집 및 발송 AI Agent")
    print("=" * 75)
    print(f"기준(현재) 시간: {base_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # 1. 대상 주차 및 5영업일 날짜 계산
    week_title, date_range = get_week_info(base_date)
    target_dates = get_target_dates(base_date)
    print(f"수집 대상 주차: {week_title} ({date_range})")
    print("수집 대상 일자 및 질의 문구:")
    for d in target_dates:
        print(f"  - {d['date_label']}: \"{d['question']}\"")

    client = get_gemini_client()

    # 2. 일자별 1단계 수집 & 2단계 일자 재검증 & 3단계 교차검증 링크 질의
    verified_items = []
    print("\n" + "-" * 60)
    print("1단계: 일자별 질의 / 2단계: 공시일자 재검증 / 3단계: 교차검증 링크 확보")
    print("-" * 60)

    for target_d in target_dates:
        # 1단계 수집 질의
        raw_items = collect_daily_announcements(target_d, client)
        
        # 2단계 검증 질의: "해당 내용은 언제 공시가 되었나요?"
        for item in raw_items:
            print(f"\n[2단계 공시일자 검증] 기관: {item.get('authority')} | 제목: {item.get('title')}")
            is_valid = verify_announcement_date(item, client)
            if is_valid:
                # 3단계 교차검증 링크 질의: "실제 조사 후 교차 검증 링크를 주세요"
                verified_url = request_cross_verification_link(item, client)
                item["source_url"] = verified_url or item.get("source_url", "")
                verified_items.append(item)
            else:
                print(f"  -> 지정된 공시일자({target_d['short_date_label']})와 불일치하여 해당 내용은 삭제(제외)합니다.")

    print("\n" + "-" * 60)
    print(f"검증 완료된 최종 유효 공시 건수: 총 {len(verified_items)}건")
    print("-" * 60)

    # 4. 검증된 공시 항목의 출처 웹페이지 스크린샷 캡처 (이슈 1개당 1개 첨부)
    if not skip_screenshot and verified_items:
        verified_items = capture_screenshots_for_items(verified_items)

    # 5. 전문가 시각의 보고서 생성 (이모티콘 없이, '시사점' 표기)
    print("\n" + "-" * 60)
    print("4단계: AML 전문가 시각 보고서 작성")
    print("-" * 60)
    subject, report_body = generate_expert_report(
        verified_items,
        week_title,
        date_range,
        client,
    )

    # 로컬 보고서 파일 저장
    report_dir = Path(__file__).resolve().parent / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_filename = f"aml_report_{base_date.strftime('%Y%m%d_%H%M%S')}.txt"
    report_path = report_dir / report_filename
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"제목: {subject}\n\n{report_body}")
    print(f"로컬 보고서 저장 완료 -> {report_path}")

    # 보고서 미리보기 출력
    print("\n[보고서 미리보기]\n" + "=" * 60)
    print(report_body)
    print("=" * 60)

    # 6. 이메일 발송
    attachment_paths = [
        item["screenshot_path"]
        for item in verified_items
        if item.get("screenshot_path")
    ]

    if dry_run:
        print("\n[DRY RUN 모드] 실제 이메일 발송을 건너뜁니다.")
        print(f"수신 예정자: {', '.join(RECIPIENTS)}")
        print(f"첨부 예정 파일 수: {len(attachment_paths)}개")
    else:
        print("\n" + "-" * 60)
        print("5단계: 보고서 및 스크린샷 이메일 발송")
        print("-" * 60)
        success = send_aml_report_email(
            subject=subject,
            body_text=report_body,
            attachment_paths=attachment_paths,
            recipients=RECIPIENTS,
        )
        if success:
            print("\nAML 주간 공시 보고서 파이프라인이 성공적으로 완료되었습니다.")
        else:
            print("\n이메일 발송 중 오류가 발생했습니다. 로그를 확인해 주세요.")


def main():
    parser = argparse.ArgumentParser(description="AML 감독기관 공시 수집 및 발송 AI Agent")
    parser.add_argument(
        "--target-date",
        type=str,
        help="기준 날짜 지정 (형식: YYYY-MM-DD, 예: 2026-08-17). 미지정시 현재 시스템 시간 사용",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="이메일 발송 없이 수집 및 보고서 생성만 수행",
    )
    parser.add_argument(
        "--skip-screenshot",
        action="store_true",
        help="스크린샷 캡처 단계를 건너뜀 (빠른 테스트용)",
    )

    args = parser.parse_args()

    base_date = None
    if args.target_date:
        try:
            base_date = datetime.strptime(args.target_date, "%Y-%m-%d")
        except ValueError:
            print(f"[오류] 잘못된 날짜 형식입니다: {args.target_date}. YYYY-MM-DD 형식으로 입력하세요.")
            sys.exit(1)

    run_aml_pipeline(
        base_date=base_date,
        dry_run=args.dry_run,
        skip_screenshot=args.skip_screenshot,
    )


if __name__ == "__main__":
    main()
