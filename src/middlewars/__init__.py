from .register_user import RegisterUser

async def setup_middlewares(dp):
    dp.message.middleware(RegisterUser())