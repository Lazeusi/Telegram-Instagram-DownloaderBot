from __future__ import annotations
import os
from loguru import logger
import yt_dlp
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MEDIA_DIR = BASE_DIR / "media" / "instagram"


async def download_instagram_media(url: str) -> str:
    """
    Download Instagram video using yt-dlp with Chrome cookies (anti-rate-limit).

    Args:
        url (str): Instagram post/reel URL.

    Returns:
        str: Path to downloaded video file.
    """
    try:
        date_folder = datetime.now().strftime("%Y-%m-%d")
        output_dir = MEDIA_DIR / date_folder
        output_dir.mkdir(parents=True, exist_ok=True)

        ydl_opts = {
            "outtmpl": str(output_dir / "%(id)s.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "cookiesfrombrowser": ("firefox",),  # ✅ استفاده از کوکی مرورگر برای bypass لیمیت
            "retries": 5,
            "noplaylist": True,
            "format": "best[ext=mp4]",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        logger.info(f"Downloaded Instagram media: {file_path}")
        return file_path

    except Exception as e:
        logger.error(f"Instagram fetch failed: {e}")
        raise
