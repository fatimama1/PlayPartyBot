import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from app.config import settings
from app.handlers import router
from app.handlers.casino.slots import router as slots_router
from app.handlers.create_event import cmd_create_event
from app.handlers.who_coming import who_coming
from app.utils import main_menu

BOT_TOKEN = settings.BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)
dp.include_router(slots_router)


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Выберите действие:",
        reply_markup=main_menu(),
    )


@dp.message(F.text == "Создать событие")
async def create_event_button(message: Message):
    await cmd_create_event(message)


@dp.message(F.text == "Кто придет?")
async def who_coming_button(message: Message):
    await who_coming(message)


async def main():
    print("🚀 Bot is starting...")
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
