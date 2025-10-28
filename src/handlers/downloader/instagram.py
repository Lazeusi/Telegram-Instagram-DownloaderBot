from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from src.api.services.instagram import download_instagram_media
from src.utils.logger import get_logger
from src.database.modles.user import User
import os


log = get_logger()

router = Router()

@router.message(F.text & F.text.startswith("https://www.instagram.com"))
async def download_instagram_handler(message: Message):
    url = message.text.strip()
    await message.answer("📥 در حال دانلود... لطفاً کمی صبر کنید")
    user = await User.find_one(user_id=message.from_user.id)
    is_banned = user['is_banned']
    if is_banned == True:
        await message.answer("❌ شما مسدود شده‌اید. لطفاً با پشتیبانی تماس بگیرید.")
        return
    
    try:
        # دانلود و دریافت مسیر فایل
        file_path = await download_instagram_media(url)

        # آماده‌سازی فایل برای ارسال
        input_file = FSInputFile(file_path)

        # ارسال ویدیو
        await message.answer_video(input_file)

        log.info(f"Media sent to {message.from_user.id}")

    except Exception as e:
        log.error(f"Error downloading Instagram media: {e}")
        await message.answer("❌ دانلود با خطا مواجه شد. لطفاً دوباره تلاش کنید.")

    # پاک کردن فایل
    os.remove(file_path)