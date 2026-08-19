from datetime import datetime, timedelta
from typing import List, Dict, Tuple


def get_target_dates(base_date: datetime = None) -> List[Dict[str, any]]:
    """
    기준 날짜(base_date, 기본값: 현재 시스템 시간)를 기준으로
    직전 주 월요일부터 금요일까지 5일간의 날짜 목록 및 질의 문구를 반환합니다.

    예: base_date가 2026-08-17 (월)인 경우 ->
        2026-08-10 (월), 2026-08-11 (화), 2026-08-12 (수), 2026-08-13 (목), 2026-08-14 (금)
    """
    if base_date is None:
        base_date = datetime.now()

    # 기준 날짜의 요일 (월요일: 0, 화요일: 1, ..., 일요일: 6)
    weekday = base_date.weekday()
    
    # 직전 주 월요일 계산:
    current_week_monday = base_date - timedelta(days=weekday)
    last_week_monday = current_week_monday - timedelta(days=7)

    start_d = last_week_monday
    end_d = last_week_monday + timedelta(days=4)
    week_range_label = f"{start_d.strftime('%Y-%m-%d')} ~ {end_d.strftime('%Y-%m-%d')}"
    week_short_label = f"{start_d.month}월 {start_d.day}일 ~ {end_d.month}월 {end_d.day}일"

    target_dates = []
    for i in range(5):  # 월, 화, 수, 목, 금
        d = last_week_monday + timedelta(days=i)
        
        # 2자리 연도 (예: 26), 1~2자리 월 (예: 8), 1~2자리 일 (예: 10)
        yy_str = d.strftime("%y")
        m_str = str(d.month)
        d_str = str(d.day)
        
        # 질문 형식: "{YY}년 {M}월 {D}일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."
        question = f"{yy_str}년 {m_str}월 {d_str}일에 국내외 자금세탁방지 감독기관의 공시된 내용을 알려주세요."
        date_label = f"{yy_str}년 {m_str}월 {d_str}일"
        short_date_label = f"{m_str}월 {d_str}일"
        
        target_dates.append({
            "datetime": d,
            "iso_date": d.strftime("%Y-%m-%d"),
            "yy": yy_str,
            "month": d.month,
            "day": d.day,
            "date_label": date_label,
            "short_date_label": short_date_label,
            "question": question,
            "week_start": start_d,
            "week_end": end_d,
            "week_range": week_range_label,
            "week_short_range": week_short_label,
        })

    return target_dates


def get_week_info(base_date: datetime = None) -> Tuple[str, str]:
    """
    수집 대상 주차 정보 문자열을 반환합니다.
    예: 2026-08-17 기준 -> ("2026년 8월 2주차", "2026-08-10 ~ 2026-08-14")
    """
    if base_date is None:
        base_date = datetime.now()

    dates = get_target_dates(base_date)
    start_d = dates[0]["datetime"]
    end_d = dates[-1]["datetime"]
    
    # 해당 월의 첫 번째 월요일을 기준으로 주차 계산
    first_day_of_month = datetime(start_d.year, start_d.month, 1)
    first_monday_offset = (7 - first_day_of_month.weekday()) % 7
    first_monday = first_day_of_month + timedelta(days=first_monday_offset)

    if start_d >= first_monday:
        week_number = ((start_d - first_monday).days // 7) + 1
    else:
        week_number = 1
    
    week_title = f"{start_d.year}년 {start_d.month}월 {week_number}주차"
    date_range = f"{start_d.strftime('%Y-%m-%d')} ~ {end_d.strftime('%Y-%m-%d')}"
    
    return week_title, date_range
