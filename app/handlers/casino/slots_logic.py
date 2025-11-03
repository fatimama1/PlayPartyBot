from app.db.crud import get_balance, save_slot_bet, update_balance

SLOTS = ["🍒", "🍋", "🍊", "💎", "7️⃣"]


async def process_slot_result(tg_id: int, bet: int, result: list):
    await update_balance(tg_id, -bet)

    counts = {s: result.count(s) for s in result}
    max_count = max(counts.values())

    if max_count == 3:
        win_amount = bet * 5
        text = f"{' '.join(result)}\n🎉 Джекпот! Вы выиграли {win_amount}💰"
        won = True
    elif max_count == 2:
        win_amount = bet * 2
        text = f"{' '.join(result)}\n🎉 Вы выиграли {win_amount}💰"
        won = True
    else:
        win_amount = 0
        text = f"{' '.join(result)}\n😢 Вы проиграли {bet}💰"
        won = False

    if won:
        await update_balance(tg_id, win_amount)

    await save_slot_bet(tg_id, bet, won)

    balance = await get_balance(tg_id)
    text += f"\nВаш баланс: {balance}💰"
    return text, balance
