from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from app.utils import main_menu

from .animation import spin_animation
from .slots_logic import process_slot_result
from .states import SlotStates

router = Router()


@router.message(F.text == "🎰 Слоты")
async def slots_start(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    from app.db.crud import get_balance

    balance = await get_balance(tg_id)
    if balance <= 0:
        await message.answer(
            "Ваш баланс пуст. Пополните его, чтобы играть.", reply_markup=main_menu()
        )
        return

    await message.answer(
        f"Ваш баланс: {balance}💰\nВведите вашу ставку (или 0 чтобы выйти):",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(SlotStates.waiting_for_bet)


@router.message(SlotStates.waiting_for_bet)
async def process_bet(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Введите число!")
        return

    bet = int(message.text)
    tg_id = message.from_user.id

    from app.db.crud import get_balance

    balance = await get_balance(tg_id)

    # Выход в главное меню
    if bet == 0:
        await state.clear()
        await message.answer("Возврат в главное меню:", reply_markup=main_menu())
        return

    if bet < 0:
        await message.answer("❌ Ставка должна быть положительным числом!")
        return

    if balance < bet:
        await message.answer(f"Недостаточно средств! Ваш баланс: {balance}💰")
        if balance == 0:
            await state.clear()
            await message.answer(
                "Баланс кончился. Возврат в главное меню:", reply_markup=main_menu()
            )
        return

    # Сообщение для анимации
    anim_msg = await message.answer("🎰 Крутим...")

    # Анимация (будет редактировать только anim_msg)
    final_result = await spin_animation(anim_msg)

    # Финальный результат — отдельное сообщение
    text, balance = await process_slot_result(tg_id, bet, final_result)
    await message.answer(text)
    # Отдельное сообщение с результатом и балансом

    # Если баланс кончился
    if balance == 0:
        await state.clear()
        await message.answer(
            "Баланс кончился. Возврат в главное меню:", reply_markup=main_menu()
        )
    else:
        await message.answer("Введите следующую ставку (или 0 чтобы выйти):")
