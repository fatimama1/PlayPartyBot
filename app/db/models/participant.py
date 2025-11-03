from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, ForeignKey("users.tg_id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    is_going = Column(Boolean, default=True)

    user = relationship("User", back_populates="participants")
    event = relationship("Event", back_populates="participants")
