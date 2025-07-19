from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text, \
    UniqueConstraint
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class Team(Base):
    __tablename__ = 'Team'
    __table_args__ = (
        # 同一个赛区中不能有相同名称和简称的队伍
        UniqueConstraint("TeamName", "TeamShortName","RegionId", name="uq_team_name_short_region"),

        # 一个玩家只能在一个赛区创建一个战队
        UniqueConstraint("CreatePlayerId","RegionId", name="uq_create_player_region"),
        ForeignKeyConstraint(["RegionId"], ["Region.Id"], name="Team_ibfk_1"),
        ForeignKeyConstraint(["CreatePlayerId"], ["Player.Id"], name="Team_ibfk_2"),
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    TeamName: Mapped[str] = mapped_column(VARCHAR(255))
    TeamShortName: Mapped[str] = mapped_column(VARCHAR(255))
    TeamLogo: Mapped[Optional[str]] = mapped_column(VARCHAR(255), comment='队伍LOGO文件路径')
    TeamSlogan: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    CreatePlayerId: Mapped[int] = mapped_column(Integer, comment='队伍创建人编号')
    RegionId: Mapped[int] = mapped_column(Integer, comment="报名赛区")
    RegisterCost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='队伍创建费用')
    RegisterTime: Mapped[datetime.datetime] = mapped_column(DateTime, comment='赛区报名时间')


    CreatePlayer: Mapped['Player'] = relationship('Player', back_populates='CreatedTeams')
    Region: Mapped['Region'] = relationship('Region', back_populates='Teams')
    TeamJoinApplication: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                            back_populates='Team_')
    TeamPlayer: Mapped[List['TeamPlayer']] = relationship('TeamPlayer', back_populates='Team')
