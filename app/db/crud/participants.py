from sqlalchemy.future import select

from app.db.base import AsyncSessionLocal
from app.db.models import Participant


async def set_participation(tg_id: int, event_id: int, is_going: bool) -> Participant:
    async with AsyncSessionLocal() as session:
        participant = (
            await session.execute(
                select(Participant).where(
                    Participant.tg_id == tg_id, Participant.event_id == event_id
                )
            )
        ).scalar_one_or_none()

        if participant:
            participant.is_going = is_going
        else:
            participant = Participant(tg_id=tg_id, event_id=event_id, is_going=is_going)
            session.add(participant)

        await session.commit()
        await session.refresh(participant)
        return participant


async def get_participants_by_status(
    event_id: int, is_going: bool
) -> list[Participant]:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Participant).where(
                Participant.event_id == event_id, Participant.is_going == is_going
            )
        )
        return result.scalars().all()


async def get_participant_status(tg_id: int, event_id: int) -> bool | None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Participant.is_going).where(
                Participant.tg_id == tg_id, Participant.event_id == event_id
            )
        )
        return result.scalar_one_or_none()
