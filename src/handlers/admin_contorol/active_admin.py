from aiogram import types , Router , F
from aiogram.filters import Command

from src.utils.logger import get_logger
from src.database.modles.admin import Admin

log = get_logger()

router = Router()

@router.message(Command('active_admin'))
async def active_admin(message: types.Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    
    exist_admins = await Admin.get_all()
    if not exist_admins:
        await Admin.add_one(user_id=user_id,
                            username=username,
                            is_owner=True
                            )
        return
    else:
        return