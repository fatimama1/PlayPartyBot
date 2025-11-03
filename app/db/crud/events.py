from sqlalchemy.future import select

from app.db.base import AsyncSessionLocal
from app.db.models import Event, Participant


async def create_event(time: str, creator_tg_id: int):
    async with AsyncSessionLocal() as session:
        event = Event(time=time)
        session.add(event)
        await session.commit()
        await session.refresh(event)

        creator = Participant(tg_id=creator_tg_id, event_id=event.id)
        session.add(creator)
        await session.commit()

        return event


async def get_last_event():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Event).order_by(Event.id.desc()))
        return result.scalars().first()


async def get_event(event_id: int) -> Event | None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Event).where(Event.id == event_id))
        return result.scalar_one_or_none()
