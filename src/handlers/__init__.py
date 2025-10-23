from .start import router as start_router
from .admin_contorol.active_admin import router as active_admin_router
async def setup_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(active_admin_router)