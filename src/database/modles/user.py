from datetime import datetime

from src.database.connection import db
from src.utils.logger import get_logger

log = get_logger()

class User:
    
    collection = db.users
    
    @classmethod
    async def find_one(cls, user_id : int = None, username : str = None):
        if username:
            username = username.lower()
            return await cls.collection.find_one({"username" : username})
        if user_id:
            return await cls.collection.find_one({"user_id" : user_id})

    
    @classmethod
    async def insert_one(cls, user_id : int, username : str = None):
        if username:
            username = username.lower()
        else:
            username = "unknown"
        await cls.collection.insert_one({"user_id" : user_id,
                                                "username" : username,
                                                "join_date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                })
        log.info(f"User {username or user_id} joined the bot.")
        
    @classmethod
    async def update_one(cls, user_id : int, username : str = None):
        if username:
            username = username.lower()
        await cls.collection.update_one({"user_id" : user_id}, {"$set" : {"username" : username}})
        
        