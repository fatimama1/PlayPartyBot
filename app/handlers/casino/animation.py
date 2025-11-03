import asyncio
import random

from aiogram.types import Message

from .slots_logic import SLOTS


async def spin_animation(slot_msg: Message, rounds: int = 5, delay: float = 0.4):
    """
    Прокрутка "барабанов", возвращает финальный результат.
    """
    result = []
    for i in range(3):
        reel = random.choice(SLOTS)
        result.append(reel)
        interim_display = ["❔"] * 3
        interim_display[: i + 1] = result[: i + 1]
        await slot_msg.edit_text(" ".join(interim_display))
        await asyncio.sleep(delay)
    return result
