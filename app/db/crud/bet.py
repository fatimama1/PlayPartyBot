from app.db.base import AsyncSessionLocal
from app.db.models import Bet


async def save_slot_bet(tg_id: int, bet_amount: int, win: bool):
    async with AsyncSessionLocal() as session:
        new_bet = Bet(tg_id=tg_id, bet=bet_amount, win=win)
        session.add(new_bet)
        await session.commit()
