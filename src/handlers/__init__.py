from .start import router as start_router
from .admin_contorol.active_admin import router as active_admin_router
from .admin_contorol.panel import router as panel_admin_router
from .admin_contorol.add_admin import router as add_admin_router
from .admin_contorol.remove_admin import router as remove_admin_router
from .admin_contorol.ban_user import router as ban_user_router
from .admin_contorol.unban_user import router as unban_user_router
from .downloader.instagram import router as instagram_downloader_router


async def setup_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(active_admin_router)
    dp.include_router(panel_admin_router)
    dp.include_router(add_admin_router)
    dp.include_router(remove_admin_router)
    dp.include_router(ban_user_router)
    dp.include_router(unban_user_router)
    dp.include_router(instagram_downloader_router)
    