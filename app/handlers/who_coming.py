from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.config import settings
from app.db.crud import get_last_event, get_participants_by_status
from app.utils import main_menu

router = Router()


@router.message(Command("who_coming"))
async def who_coming(message: Message):
    event = await get_last_event()
    if not event:
        await message.answer("❌ Событий ещё не было", reply_markup=main_menu())
        return

    going = await get_participants_by_status(event.id, True)
    not_going = await get_participants_by_status(event.id, False)

    async def format_names(participants):
        lines = []
        for p in participants:
            try:
                chat = await message.bot.get_chat(p.tg_id)
                name = (
                    getattr(chat, "full_name", None)
                    or getattr(chat, "username", None)
                    or str(p.tg_id)
                )
                lines.append(f"• {name}")
            except Exception:
                lines.append(f"• {p.tg_id}")
        return "\n".join(lines) if lines else "—"

    text = (
        f"🎲 {settings.EVENT_NAME} в {event.time}\n\n"
        f"✅ Идут:\n{await format_names(going)}\n\n"
        f"🚫 Не идут:\n{await format_names(not_going)}"
    )

    await message.answer(text, reply_markup=main_menu())
