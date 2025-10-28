import time
from aiogram import BaseMiddleware
from aiogram.types import Message

class RateLimiter(BaseMiddleware):
    def __init__(self, delay: int = 15):
        self.delay = delay
        self.user_timestamps = {}

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        now = time.time()

        if user_id in self.user_timestamps:
            diff = now - self.user_timestamps[user_id]
            if diff < self.delay:
                await event.answer(f"⏳ لطفاً {int(self.delay - diff)} ثانیه صبر کنید.")
                return

        self.user_timestamps[user_id] = now
        return await handler(event, data)
