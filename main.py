from aiogram import Bot, Dispatcher
import asyncio
import uvicorn

from src.utils.logger import get_logger
from src.config import settings
from src.handlers import setup_handlers
from src.database.connection import db
from src.middlewars import setup_middlewares
from src.api.main import app

log = get_logger()


async def start_api():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, reload=False)
    server = uvicorn.Server(config)
    await server.serve()


async def start_bot():
    
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
async def main():
    await asyncio.gather(
        start_api(),
        start_bot()
    )
    
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("Bot stopped.")