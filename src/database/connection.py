from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings
from src.utils.logger import get_logger

log = get_logger()
class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_DB_URI)
        self.db = self.client[settings.MONGO_DB_NAME]
        self.users = self.db['users']
    
    async def check_connection(self):
        try:
            await self.client.admin.command('ping')
            log.info("Database is connected.")            
        except Exception as e:
            log.error(f"Database connection error: {e}")
            
db = Database()