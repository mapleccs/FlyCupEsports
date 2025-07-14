from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from .base import Base


class RegionTeam(Base):
    __tablename__ = 'RegionTeam'
    __table_args__ = (
        ForeignKeyConstraint(['RegionId'], ['Region.Id'], name='RegionTeam_ibfk_2'),
        ForeignKeyConstraint(['TeamId'], ['Team.Id'], name='RegionTeam_ibfk_1'),
        Index('RegionId', 'RegionId')
    )

    TeamId: Mapped[int] = mapped_column(Integer, primary_key=True)
    RegionId: Mapped[int] = mapped_column(Integer, primary_key=True)
    RegisterTime: Mapped[datetime.datetime] = mapped_column(DateTime, comment='赛区报名时间')
    AuditStatus: Mapped[str] = mapped_column(String(255), comment='查看审核状态:Pending,Approved,Rejected')

    Region_: Mapped['Region'] = relationship('Region', back_populates='RegionTeam')
    Team_: Mapped['Team'] = relationship('Team', back_populates='RegionTeam')
