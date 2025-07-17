from typing import List, Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

class Position(Base):
    __tablename__ = 'Position'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255), comment='游戏位置：Top、Jungle')
    Remark: Mapped[Optional[str]] = mapped_column(String(255))

    PrimaryPositionPlayer: Mapped[List['Player']] = relationship('Player', foreign_keys='[Player.PrimaryPositionId]', back_populates='PrimaryPosition')
    SecondaryPositionPlayer: Mapped[List['Player']] = relationship('Player', foreign_keys='[Player.SecondaryPositionId]', back_populates='SecondaryPosition')
