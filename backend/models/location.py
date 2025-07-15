from typing import List, Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

class Location(Base):
    __tablename__ = 'Location'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[Optional[str]] = mapped_column(String(255), comment='游戏位置：Top、Jungle')
    Remark: Mapped[Optional[str]] = mapped_column(String(255))

    PrimaryLocationCompetitor: Mapped[List['Competitor']] = relationship('Competitor', foreign_keys='[Competitor.PrimaryLocationId]', back_populates='PrimaryLocation')
    SecondaryLocationCompetitor: Mapped[List['Competitor']] = relationship('Competitor', foreign_keys='[Competitor.SecondaryLocationId]', back_populates='SecondaryLocation')
