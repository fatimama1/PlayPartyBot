from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(
        Integer, ForeignKey("users.tg_id"), nullable=False
    )  # 🔗 связь с User
    bet = Column(Integer, nullable=False)
    win = Column(Boolean, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="bets")  # 🔄 связь обратно
