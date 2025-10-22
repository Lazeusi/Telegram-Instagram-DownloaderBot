from aiogram import types , Router , F
from aiogram.filters import Command , CommandStart

from src.utils.logger import get_logger


log = get_logger()

router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(f'Hello, {message.from_user.first_name}!')