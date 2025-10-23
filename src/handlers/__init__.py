from .start import router as start_router
from .admin_contorol.active_admin import router as active_admin_router
from .admin_contorol.panel import router as panel_admin_router
from .admin_contorol.add_admin import router as add_admin_router
from .admin_contorol.remove_admin import router as remove_admin_router


async def setup_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(active_admin_router)
    dp.include_router(panel_admin_router)
    dp.include_router(add_admin_router)
    dp.include_router(remove_admin_router)
    