from aiogram import F , Router , Bot
from aiogram.types import CallbackQuery , Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from src.database.modles.admin import Admin
from src.database.modles.user import User
from src.utils.logger import get_logger
from src.keyboards.inline.admin.panel import back_to_admin_panel , admin_panel

log = get_logger()

router = Router()

class UnbanUserState(StatesGroup):
    waiting_for_username = State()
    
@router.callback_query(F.data == 'unban_user')
async def unban_user(callback: CallbackQuery , state : FSMContext) -> None:
    await callback.message.edit_text("Enter 'UserID' or '@Username' of user \nyou want to unban",
                                     reply_markup=back_to_admin_panel()
                                     )
    await state.update_data(message_id = callback.message.message_id)
    await state.set_state(UnbanUserState.waiting_for_username)
    
@router.message(UnbanUserState.waiting_for_username)
async def process_username(message: Message, state: FSMContext , bot : Bot) -> None:
    data = await state.get_data()
    message_id = data['message_id']
    await bot.delete_message(chat_id=message.chat.id, message_id=message_id)
    
    id = message.text
    user_id = message.from_user.id
    user_is_admin = await Admin.find_one(user_id = user_id)
    if user_is_admin:
        if id.isdigit():
            id = int(id)
            user = await User.find_one(user_id = user_id)
            if not user:
                await message.reply("User not found. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            is_banned = user['is_banned']
            if is_banned == False:
                await message.reply("User not banned. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            else:
                await User.unban_user(user_id = user['user_id'])
                await message.reply("User unbanned successfully. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
        elif '@' in id:
            user = await User.find_one(username = id[1:])
            if not user:
                await message.reply("User not found. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            is_banned = user['is_banned']
            if is_banned == False:
                await message.reply("User not banned. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            else:
                await User.unban_user(user_id = user['user_id'])
                await message.reply("User unbanned successfully. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
        else:
            await message.reply("Invalid input. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
            return
        
    else:
        await message.reply("You don't have permission to unban user. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
        return
            
                