import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGO_DB_URI = os.getenv("MONGO_DB_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    API_URL: str = "http://localhost:8000/api/v1"
    
settings = Settings()