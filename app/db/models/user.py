from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    balance = Column(Integer, nullable=False, default=500)

    participants = relationship(
        "Participant", back_populates="user", cascade="all, delete-orphan"
    )

    bets = relationship("Bet", back_populates="user", cascade="all, delete-orphan")
