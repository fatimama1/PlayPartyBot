from sqlalchemy import select, update

from app.db.base import AsyncSessionLocal
from app.db.models.user import User


async def get_balance(tg_id: int) -> int:
    async with AsyncSessionLocal() as session:
        res = await session.execute(select(User.balance).where(User.tg_id == tg_id))
        user = res.scalar_one_or_none()
        return user or 0


async def update_balance(tg_id: int, amount: int):
    async with AsyncSessionLocal() as session:
        await session.execute(
            update(User)
            .where(User.tg_id == tg_id)
            .values(balance=User.balance + amount)
        )
        await session.commit()
