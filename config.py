import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from current directory or project root
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


# Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
FALLBACK_MODELS = ["gemini-3.1-flash-lite", "gemini-flash-latest", "gemini-3.6-flash"]


# SMTP Configuration
SMTP_EMAIL = os.getenv("SMTP_EMAIL", "").strip()
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "").strip()
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com").strip()
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

# Email Recipients
RECIPIENTS = [
    "e.factorials@gmail.com",
]

# Monitored AML Regulatory Authorities
DOMESTIC_AUTHORITIES = [
    "금융정보분석원 (KoFIU)",
    "금융감독원 (FSS)",
    "관세청 (KCS)",
]

INTERNATIONAL_AUTHORITIES = [
    "FATF (자금세탁방지기구)",
    "APG (아시아·태평양 자금세탁방지기구)",
    "FinCEN (미국 금융범죄단속네트워크)",
    "OFAC (미국 재무부 해외자산통제국)",
    "NYDFS (뉴욕주 금융감독청)",
    "AMLA (EU 자금세탁방지청)",
    "EBA (유럽은행감독청)",
    "FCA (영국 금융감독청)",
    "MAS (싱가포르 통화청)",
    "HKMA (홍콩금융관리국)",
    "Egmont Group (에그몽그룹)",
    "OFSI (영국 재무부 재무제재이행국)",
]

ALL_TARGET_AUTHORITIES = DOMESTIC_AUTHORITIES + INTERNATIONAL_AUTHORITIES

# Directory for storing screenshots
SCREENSHOT_DIR = Path(__file__).resolve().parent / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
