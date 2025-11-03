from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Создать событие")],
            [KeyboardButton(text="Кто придет?")],
            [KeyboardButton(text="🎰 Слоты")],
        ],
        resize_keyboard=True,
    )
