from typing import List, Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

class Grade(Base):
    __tablename__ = 'Grade'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(255), comment='段位')
    Remark: Mapped[Optional[str]] = mapped_column(String(255))

    Competitor: Mapped[List['Competitor']] = relationship('Competitor', foreign_keys='[Competitor.CurrentGradeId]',
                                                          back_populates='Grade_')
    Competitor_: Mapped[List['Competitor']] = relationship('Competitor', foreign_keys='[Competitor.HighestGradeId]',
                                                           back_populates='Grade1')

