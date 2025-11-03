from aiogram import Router, types

router = Router()


@router.message()
async def log_all_messages(message: types.Message):
    # Асинхронный вывод в консоль через стандартный print не блокирует event loop, можно оставить
    print(
        f"[DEBUG] Got message from {message.from_user.id} ({message.from_user.full_name}): {message.text}"
    )

    # Асинхронная отправка ответа
    await message.answer("Сообщение получено (debug)")
