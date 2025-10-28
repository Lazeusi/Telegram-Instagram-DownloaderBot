from fastapi import FastAPI
from src.api.routes import instagram

app = FastAPI(title="Instagram Downloader API")

app.include_router(instagram.router)

