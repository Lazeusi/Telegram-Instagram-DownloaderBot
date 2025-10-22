from loguru import logger
from pathlib import Path
import sys

# مسیر پوشه‌ی لاگ‌ها
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# مسیر فایل لاگ اصلی
LOG_FILE = LOG_DIR / "bot.log"

# حذف هندلر پیش‌فرض
logger.remove()

# لاگ به کنسول با رنگ و فرمت زیبا
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    level="INFO"
)

# لاگ به فایل با rotation و retention
logger.add(
    LOG_FILE,
    rotation="10 MB",       # هر 10 مگابایت یک فایل جدید بساز
    retention="10 days",    # لاگ‌های قدیمی‌تر از 10 روز حذف می‌شن
    compression="zip",      # فایل‌های قدیمی zip می‌شن
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG"
)


def get_logger(name: str = None):
    """
    برمی‌گردونه یه instance از logger برای ماژول خاص
    """
    return logger.bind(module=name or "main")
