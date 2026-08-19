import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import List, Optional

from config import (
    SMTP_EMAIL,
    SMTP_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT,
    RECIPIENTS,
)


def send_aml_report_email(
    subject: str,
    body_text: str,
    body_html: Optional[str] = None,
    attachment_paths: Optional[List[str]] = None,
    recipients: Optional[List[str]] = None,
) -> bool:
    """
    작성된 AML 주간 공시 보고서(텍스트 및 반응형 HTML)와 스크린샷 첨부파일을 이메일로 발송합니다.
    """
    target_recipients = recipients or RECIPIENTS

    if not SMTP_EMAIL or not SMTP_PASSWORD:
        print("[이메일 발송 실패] SMTP_EMAIL 또는 SMTP_PASSWORD가 설정되어 있지 않습니다.")
        return False

    print(f"\n[이메일 발송 준비] 수신자: {', '.join(target_recipients)}")

    # 이메일 메시지 구성 (alternative + mixed)
    msg = MIMEMultipart("mixed")
    msg["From"] = f"자금세탁방지본부 CoP <{SMTP_EMAIL}>"
    msg["To"] = ", ".join(target_recipients)
    msg["Subject"] = subject

    # 본문 컨테이너 (텍스트 + HTML 멀티파트)
    msg_body = MIMEMultipart("alternative")
    part_text = MIMEText(body_text, "plain", "utf-8")
    msg_body.attach(part_text)

    if body_html:
        part_html = MIMEText(body_html, "html", "utf-8")
        msg_body.attach(part_html)

    msg.attach(msg_body)

    # 스크린샷 이미지 첨부파일 추가
    attached_count = 0
    if attachment_paths:
        for path_str in attachment_paths:
            if not path_str:
                continue
            path = Path(path_str)
            if not path.exists():
                print(f"  [첨부 건너뜀] 파일 없음: {path_str}")
                continue

            try:
                with open(path, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={path.name}",
                )
                msg.attach(part)
                attached_count += 1
                print(f"  [첨부파일 추가] {path.name}")
            except Exception as e:
                print(f"  [첨부파일 오류] {path_str}: {e}")

    # SMTP 서버 연결 및 전송
    try:
        print(f"  [SMTP 접속] {SMTP_SERVER}:{SMTP_PORT}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        
        server.sendmail(SMTP_EMAIL, target_recipients, msg.as_string())
        server.quit()
        print(f"[이메일 발송 성공] 총 {len(target_recipients)}명에게 발송 완료 (HTML 템플릿 적용, 첨부파일 {attached_count}개)")
        return True
    except Exception as e:
        print(f"[이메일 발송 오류] SMTP 전송 실패: {e}")
        return False
