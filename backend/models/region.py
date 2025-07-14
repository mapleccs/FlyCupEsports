from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from .base import Base


class Region(Base):
    __tablename__ = 'Region'
    __table_args__ = (
        ForeignKeyConstraint(['SeasonId'], ['Season.Id'], name='Region_ibfk_1'),
        ForeignKeyConstraint(['UserId'], ['User.Id'], name='Region_ibfk_2'),
        Index('SeasonId', 'SeasonId'),
        Index('UserId', 'UserId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    SeasonId: Mapped[int] = mapped_column(Integer, comment='所属赛季')
    Name: Mapped[str] = mapped_column(String(255))
    UserId: Mapped[int] = mapped_column(Integer, comment='赛区负责人')
    MaxTeamLimit: Mapped[int] = mapped_column(Integer, comment='最大战队上限')
    EndRegisterDate: Mapped[datetime.datetime] = mapped_column(DateTime, comment='报名截止日期')
    StartCompetitionDate: Mapped[datetime.datetime] = mapped_column(DateTime, comment='比赛开始日期')
    EndCompetitionDate: Mapped[datetime.datetime] = mapped_column(DateTime, comment='比赛结束日期')

    Season_: Mapped['Season'] = relationship('Season', back_populates='Region')
    User_: Mapped['User'] = relationship('User', back_populates='Region')
    RegionTeam: Mapped[List['RegionTeam']] = relationship('RegionTeam', back_populates='Region_')
