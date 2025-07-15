from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class CompetitorContact(Base):
    __tablename__ = 'CompetitorContact'
    __table_args__ = (
        ForeignKeyConstraint(['CompetitorId'], ['Competitor.Id'], name='CompetitorContact_ibfk_1'),
        ForeignKeyConstraint(['ContactTypeId'], ['ContactType.Id'], name='CompetitorContact_ibfk_2'),
        Index('CompetitorId', 'CompetitorId'),
        Index('ContactTypeId', 'ContactTypeId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    CompetitorId: Mapped[int] = mapped_column(Integer, comment='选手编号')
    ContactTypeId: Mapped[int] = mapped_column(Integer, comment='联系类型')
    ContactNumber: Mapped[str] = mapped_column(VARCHAR(20), comment='联系号码')

    Competitor_: Mapped['Competitor'] = relationship('Competitor', back_populates='CompetitorContact')
    ContactType_: Mapped['ContactType'] = relationship('ContactType', back_populates='CompetitorContact')
