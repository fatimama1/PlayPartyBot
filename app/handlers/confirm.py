from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.db.crud import get_event, get_participant_status, set_participation
from app.utils import main_menu, participation_keyboard

router = Router()


@router.callback_query(F.data.startswith("participate_"))
async def set_participation_callback(callback: CallbackQuery):
    try:
        _, event_id_str, choice = callback.data.split("_")
        event_id = int(event_id_str)
        is_going = choice == "yes"
    except ValueError:
        return await callback.answer("Некорректные данные", show_alert=True)

    event = await get_event(event_id)
    if not event:
        return await callback.answer("Событие не найдено", show_alert=True)

    await set_participation(callback.from_user.id, event_id, is_going=is_going)

    current_status = await get_participant_status(callback.from_user.id, event_id)

    await callback.message.edit_reply_markup(
        reply_markup=participation_keyboard(event_id, current_status=current_status)
    )


@router.callback_query(F.data == "main_menu")
async def return_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=main_menu())
    await callback.answer()
