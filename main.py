from aiogram import Bot, Dispatcher
import asyncio

from src.utils.logger import get_logger
from src.config import settings
from src.handlers import setup_handlers
from src.database.connection import db
from src.middlewars import setup_middlewares

log = get_logger()
async def main():
    
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()
    
    await setup_middlewares(dp)
    await setup_handlers(dp)
    await db.check_connection()
    
    details = await bot.get_me()
    log.info(
        f"Bot started.\n"
        f"Name: {details.first_name}\n"
        f"Username: {details.username}\n"
        f"ID: {details.id}"
    )

    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("Bot stopped.")