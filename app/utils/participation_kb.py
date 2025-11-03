from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def participation_keyboard(
    event_id: int, current_status: bool | None = None
) -> InlineKeyboardMarkup:
    """
    Две кнопки: Пойду / Не пойду
    current_status подсвечивает текущий выбор пользователя
    """
    yes_text = "✅ Пойду" + (" ✅" if current_status else "")
    no_text = "🚫 Не пойду" + (" ✅" if current_status is False else "")
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=yes_text, callback_data=f"participate_{event_id}_yes"
                ),
                InlineKeyboardButton(
                    text=no_text, callback_data=f"participate_{event_id}_no"
                ),
            ]
        ]
    )
