from aiogram import Router , F , Bot
from aiogram.types import Message , CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from src.database.modles.admin import Admin
from src.utils.logger import get_logger
from src.keyboards.inline.admin.panel import admin_panel , back_to_admin_panel
from src.database.modles.user import User

log = get_logger()

router = Router()

class AddAdminState(StatesGroup):
    waiting_for_username = State()
    
@router.callback_query(F.data == 'add_admin')
async def add_admin(callback: CallbackQuery , state: FSMContext) -> None:
    user_id = callback.from_user.id
    user_is_admin = await Admin.find_one(user_id = user_id)
    user_is_owner = user_is_admin['is_owner']
    if user_is_owner == False:
        await callback.answer(f"You don't have permission to add admin. \nYou back to admin panel",
                              reply_markup=admin_panel()
                              )
        return
    await callback.message.edit_text("Enter 'UserID' or '@Username' of user \nyou want to add as admin",
                                     reply_markup=back_to_admin_panel()
                                     )
    await state.update_data(message_id = callback.message.message_id)
    await state.set_state(AddAdminState.waiting_for_username)
    
    
@router.callback_query(F.data == 'back_to_admin_panel')
async def back_admin_panel(callback: CallbackQuery , state: FSMContext) -> None:
    await state.clear()
    await callback.message.edit_text(" <------------Adminstrator Panel------------>", reply_markup=admin_panel())
    
@router.message(AddAdminState.waiting_for_username)
async def process_username(message: Message, state: FSMContext , bot : Bot) -> None:
    data = await state.get_data()
    message_id = data['message_id']
    await bot.delete_message(chat_id=message.chat.id, message_id=message_id)
    
    id = message.text
    user_id = message.from_user.id
    user_is_admin = await Admin.find_one(user_id = user_id)
    user_is_owner = user_is_admin['is_owner']
    if user_is_owner == True:
        if id.isdigit():
            id = int(id)
            user = await User.find_one(user_id = user_id)
            if not user:
                await message.reply("User not found. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            is_admin = await Admin.find_one(user_id = user['user_id'])
            if is_admin:
                await message.reply("User already admin. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            else:
                await Admin.add_one(user_id= user['user_id'], username=user['username'], is_owner=False)
                await message.reply("Admin added successfully. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
        elif '@' in id:
            id = id[1:].lower()
            user = await User.find_one(username = id)
            
            if not user:
                await message.reply("User not found. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            is_admin = await Admin.find_one(user_id = user['user_id'])
            if is_admin:
                await message.reply("User already admin. \nYou back to admin panel" , 
                                        reply_markup=admin_panel()
                                        )
                return
            await Admin.add_one(user_id=user['user_id'], username=user['username'], is_owner=False)
            await message.reply("Admin added successfully. \nYou back to admin panel" , 
                                    reply_markup=admin_panel()
                                    )
        else:
            await message.reply("Invalid input. \nYou back to admin panel" , 
                                    reply_markup=admin_panel()
                                    )
            return
    else:
        await message.reply("You don't have permission to add admin. \nYou back to admin panel" , 
                                reply_markup=admin_panel()
                                )
        return
        
        
        
    
    