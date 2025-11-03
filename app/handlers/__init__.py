from aiogram import Router

from .confirm import router as callback_router
from .create_event import router as create_event_router
from .who_coming import router as who_coming_router

router = Router()


router.include_router(create_event_router)  # команды вроде /create_event
router.include_router(who_coming_router)  # команды вроде /who_coming
router.include_router(callback_router)  # callback-кнопки
