from aiogram import types , Router , F
from aiogram.filters import Command
from src.database.modles.admin import Admin

from src.utils.logger import get_logger
from src.keyboards.inline.admin.panel import admin_panel

log = get_logger()

router = Router()


@router.message(F.text == 'panel')
async def panel(message: types.Message) -> None:
    is_admin = await Admin.find_one(message.from_user.id)
    if is_admin:
        await message.reply(f' <--------Adminstrator Panel--------->'
        , reply_markup=admin_panel()
                            )
        
    return