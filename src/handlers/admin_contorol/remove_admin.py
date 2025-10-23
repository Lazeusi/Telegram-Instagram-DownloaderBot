from aiogram import Router , F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext



from src.database.modles.admin import Admin
from src.utils.logger import get_logger
from src.keyboards.inline.admin.panel import admin_list_remove , admin_panel , accept_remove_admin
from src.database.modles.user import User

log = get_logger()

router = Router()



@router.callback_query(F.data == "remove_admin")
async def remove_admin(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    user_is_admin = await Admin.find_one(user_id = user_id)
    user_is_owner = user_is_admin['is_owner']
    if user_is_owner == False:
        await callback.answer(f"You don't have permission to add admin. \nYou back to admin panel",
                              reply_markup=admin_panel()
                              )
        return
    await callback.message.edit_text("Select the admin you want to remove", reply_markup=await admin_list_remove())

  
@router.callback_query(F.data.startswith("remove_admin:"))
async def remove_admin(callback: CallbackQuery , state: FSMContext) -> None:

        user_id = int(callback.data.split(":")[1])
        is_owner = await Admin.find_one(user_id = user_id)
        if is_owner['is_owner'] == True:
            await callback.answer("You can't remove owner")
            return
        user = await User.find_one(user_id = user_id)
        await callback.message.edit_text(f"Are you sure you want to remove this admin?\nUserID : {user['user_id']}\nUsername : {user['username']}", 
                                        reply_markup=accept_remove_admin(user_id=user_id))

    
@router.callback_query(F.data.startswith("accept_remove_admin:"))
async def accept_remove(callback: CallbackQuery) -> None:

        user_id = int(callback.data.split(":")[1])
        await Admin.remove_one(user_id = user_id)
        await callback.message.edit_text(f"Admin removed successfully\nYou back to admin panel",
                                         reply_markup=admin_panel()
                                         )  