from sqlalchemy.future import select

from app.db.base import AsyncSessionLocal
from app.db.models import Participant, User


async def get_event_participants(event_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Participant).where(Participant.event_id == event_id)
        )
        return result.scalars().all()


async def get_all_users(exclude_tg_id: int = None):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        if exclude_tg_id:
            users = [u for u in users if u.tg_id != exclude_tg_id]
        return users
