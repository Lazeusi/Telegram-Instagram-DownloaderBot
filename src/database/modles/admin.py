from datetime import datetime

from src.database.connection import db
from src.utils.logger import get_logger

log = get_logger()

class Admin:
    collection = db.admins
    
    @classmethod
    async def find_one(cls, user_id : int = None, username : str = None):
        if username:
            username = username.lower()
            return await cls.collection.find_one({"username" : username})
        return await cls.collection.find_one({"user_id" : user_id})
            

    @classmethod
    async def add_one(cls, user_id : int, username : str = None, is_owner : bool = None):
        if username:
            username = username.lower()
        await cls.collection.insert_one({"user_id" : user_id,
                                        "username" : username,
                                        "join_date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        "is_owner" : is_owner
                                        })
        log.info(f"Admin {username or user_id} added to admin list.")
    @classmethod 
    async def remove_one(cls, user_id : int):
        await cls.collection.delete_one({"user_id" : user_id})
        log.info(f"Admin {user_id} removed from admin list.")
    @classmethod 
    async def update_one(cls, user_id : int, username : str = None):
        if username:
            username = username.lower()
        await cls.collection.update_one({"user_id" : user_id}, {"$set" : {"username" : username}})
        
    @classmethod
    async def get_all(cls):
        return await cls.collection.find({}).to_list(length=None)
        