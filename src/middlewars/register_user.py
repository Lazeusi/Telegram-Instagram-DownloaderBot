from aiogram import BaseMiddleware, types
from typing import Callable, Awaitable, Dict, Any


from src.database.modles.user import User
from src.database.modles.admin import Admin



class RegisterUser(BaseMiddleware):
    """Middleware برای ثبت خودکار کاربر در دیتابیس"""

    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any],
    ) -> Any:
        
        user_id = event.from_user.id
        username = event.from_user.username

        # جستجو یا ساخت کاربر
        user = await User.find_one(user_id = user_id)
        if not user:
            await User.insert_one(user_id = user_id,
                                  username = username
                                  )

        else:
            await User.update_one(user_id = user_id,
                                  username = username
                                  )
            
        exist_admin = await Admin.find_one(user_id = user_id,
                                           username = username
                                           )
        if exist_admin:
            await Admin.update_one(user_id = user_id,
                                   username = username
                                   )

        # عبور به هندلر بعدی
        return await handler(event, data)

        