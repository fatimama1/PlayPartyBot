from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TIMES = [f"{h:02d}:{m:02d}" for h in range(18, 24) for m in (0, 30)]


def time_keyboard(row_size: int = 4) -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для выбора времени с 18:00 до 00:00 с шагом 30 минут.

    :param row_size: количество кнопок в ряду
    :return: InlineKeyboardMarkup
    """
    keyboard, row = [], []
    for i, time in enumerate(TIMES, 1):
        row.append(InlineKeyboardButton(text=time, callback_data=f"time_{time}"))
        if i % row_size == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
