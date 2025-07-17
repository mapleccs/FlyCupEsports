from typing import List, Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

class Rank(Base):
    __tablename__ = 'Rank'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(255), comment='段位')
    Remark: Mapped[Optional[str]] = mapped_column(String(255))

    CurrentRankPlayer: Mapped[List['Player']] = relationship('Player', foreign_keys='[Player.CurrentRankId]',
                                                          back_populates='CurrentRank')
    HighestRankPlayer: Mapped[List['Player']] = relationship('Player', foreign_keys='[Player.HighestRankId]',
                                                           back_populates='HighestRank')

