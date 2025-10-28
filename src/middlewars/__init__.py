from .register_user import RegisterUser
from .rate_limiter import RateLimiter

async def setup_middlewares(dp):
    dp.message.middleware(RegisterUser())
    dp.message.middleware(RateLimiter(delay=30))