from aiogram import Router
from .sentiment import router as sentiment_router
from .history import router as history_router
from .start import router as start_router


def register_all_handlers(dp:Router):
    dp.include_router(start_router)
    dp.include_router(sentiment_router)
    dp.include_router(history_router)
