from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.config import settings
from app.db.crud import create_event, get_all_users
from app.utils import main_menu, participation_keyboard, time_keyboard

router = Router()


@router.message(Command("create_event"))
async def cmd_create_event(message: Message):
    await message.answer("🕓 Выберите время:", reply_markup=time_keyboard())


@router.callback_query(F.data.startswith("time"))
async def choose_time(callback: CallbackQuery):
    time_str = callback.data.split("_")[1]

    # Создаем событие
    event = await create_event(time_str, callback.from_user.id)

    # Рассылаем всем пользователям кроме создателя
    users = await get_all_users(exclude_tg_id=callback.from_user.id)
    for user in users:
        try:
            await callback.message.bot.send_message(
                user.tg_id,
                f"📢 {settings.EVENT_NAME} в {time_str}!",
                reply_markup=participation_keyboard(event.id),
            )
        except Exception as e:
            print(f"Не удалось отправить {user.tg_id}: {e}")

    # Обновляем сообщение создателя только текстом
    await callback.message.edit_text(
        f"Событие {settings.EVENT_NAME} создано на {time_str} и разослано всем ✅"
    )

    # Отправляем главное меню отдельным сообщением
    await callback.message.answer("Главное меню:", reply_markup=main_menu())

    await callback.answer()
