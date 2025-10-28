from aiogram import types , Router , F
from aiogram.filters import Command , CommandStart

from src.utils.logger import get_logger


log = get_logger()

router = Router()

@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(f'سلام با این ربات میتونید هر مدیایی از اینستاگرام و دانلود کنید بصورت کاملا رایگان \n فقط لینک اون مدیا رو برام بفرست! \n مثال : https://www.instagram.com/p/CF3Tl7oL3Q2' , reply_markup=types.ReplyKeyboardRemove())