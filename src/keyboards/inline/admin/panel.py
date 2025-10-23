from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.database.modles.admin import Admin




def admin_panel() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Add Admin" , callback_data="add_admin"),
                InlineKeyboardButton(text="Remove Admin" , callback_data="remove_admin"),
            ],
            [
                InlineKeyboardButton(text="Ban User" , callback_data="ban_user"),
                InlineKeyboardButton(text="Unban User" , callback_data="unban_user"),
            ],
            [
                InlineKeyboardButton(text="Force join" , callback_data="force_join"),
            ]
        ]
    )
    
def back_to_admin_panel() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔙 Back" , callback_data="back_to_admin_panel")
            ]
        ]
    )
    
async def admin_list_remove() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    admins = await Admin.get_all()
    for admin in admins:
        keyboard.button(text=f"{admin['username']}" , callback_data=f"remove_admin:{admin['user_id']}")     
    keyboard.button(text="🔙 Back" , callback_data="back_to_admin_panel")
    keyboard.adjust(1)
    return keyboard.as_markup()

def accept_remove_admin(user_id : int) -> InlineKeyboardMarkup:

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [             
                InlineKeyboardButton(text="✅ Accept" , callback_data=f"accept_remove_admin:{user_id}"),
                InlineKeyboardButton(text="❌ Decline" , callback_data=f"decline_remove_admin:{user_id}"),
            ]
        ]
        
    )
    
    