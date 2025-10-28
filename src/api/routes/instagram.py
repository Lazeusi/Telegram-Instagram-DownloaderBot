from fastapi import APIRouter, HTTPException, Query
from loguru import logger
from src.api.services.instagram import download_instagram_media

router = APIRouter(prefix="/api/v1", tags=["Instagram Downloader"])


@router.get("/download")
async def download_instagram(url: str = Query(..., description="Instagram post/reel URL")):
    """
    Download Instagram video using yt-dlp and return file path.
    """
    try:
        file_path = await download_instagram_media(url)
        return {"status": "success", "file_path": file_path}

    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
