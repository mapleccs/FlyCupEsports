from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base

class Team(Base):
    __tablename__ = 'Team'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    TeamName: Mapped[str] = mapped_column(VARCHAR(255))
    TeamLogo: Mapped[str] = mapped_column(VARCHAR(255), comment='队伍LOGO文件路径')
    CreateUserId: Mapped[int] = mapped_column(Integer, comment='队伍创建人编号')
    CreateCost: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), comment='队伍创建费用')

    TeamJoinApplication: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication', back_populates='Team_')
    TeamUser: Mapped[List['TeamUser']] = relationship('TeamUser', back_populates='Team_')
    RegionTeam: Mapped[List['RegionTeam']] = relationship('RegionTeam', back_populates='Team_')