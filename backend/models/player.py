from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class Player(Base):
    __tablename__ = 'Player'
    __table_args__ = (
        ForeignKeyConstraint(['CurrentRankId'], ['Rank.Id'], name='Player_ibfk_2'),
        ForeignKeyConstraint(['HighestRankId'], ['Rank.Id'], name='Player_ibfk_3'),
        ForeignKeyConstraint(['PrimaryPositionId'], ['Position.Id'], name='Player_ibfk_4'),
        ForeignKeyConstraint(['SecondaryPositionId'], ['Position.Id'], name='Player_ibfk_5'),
        ForeignKeyConstraint(['UserId'], ['User.Id'], name='Player_ibfk_1'),
        ForeignKeyConstraint(['RegionId'], ['Region.Id'], name='Player_ibfk_6'),
        Index('CurrentRankId', 'CurrentRankId'),
        Index('HighestRankId', 'HighestRankId'),
        Index('PrimaryPositionId', 'PrimaryPositionId'),
        Index('SecondaryPositionId', 'SecondaryPositionId'),
        Index('UserId', 'UserId'),
        Index('RegionId', 'RegionId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserId: Mapped[int] = mapped_column(Integer, comment='绑定的用户')
    Name: Mapped[str] = mapped_column(VARCHAR(255), comment='用户称呼')
    GameNameWithNumber: Mapped[str] = mapped_column(VARCHAR(255), comment='游戏名以及编号')
    CurrentRankId: Mapped[int] = mapped_column(Integer, comment='当前段位')
    HighestRankId: Mapped[int] = mapped_column(Integer, comment='最高段位')
    PrimaryPositionId: Mapped[int] = mapped_column(Integer, comment='主位置')
    SecondaryPositionId: Mapped[int] = mapped_column(Integer, comment='副位置')
    QQ: Mapped[str] = mapped_column(VARCHAR(20), comment='QQ号')
    Contact: Mapped[str] = mapped_column(VARCHAR(20), comment='联系方式')

    RegionId: Mapped[int] = mapped_column(Integer, comment="报名赛区")
    RegisterCost: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), comment='报名押金')
    RegisterTime: Mapped[datetime.datetime] = mapped_column(DateTime, comment='赛区报名时间')

    IsApproved: Mapped[int] = mapped_column(TINYINT(1), comment='是否通过申请')
    Reason: Mapped[Optional[str]] = mapped_column(Text, comment='未通过申请原因')

    CurrentRank: Mapped['Rank'] = relationship('Rank', foreign_keys=[CurrentRankId],
                                                 back_populates='CurrentRankPlayer')
    HighestRank: Mapped['Rank'] = relationship('Rank', foreign_keys=[HighestRankId],
                                                 back_populates='HighestRankPlayer')

    PrimaryPosition: Mapped['Position'] = relationship('Position', foreign_keys=[PrimaryPositionId],
                                                       back_populates='PrimaryPositionPlayer')
    SecondaryPosition: Mapped['Position'] = relationship('Position', foreign_keys=[SecondaryPositionId],
                                                         back_populates='SecondaryPositionPlayer')

    User_: Mapped['User'] = relationship('User', back_populates='Player')
    Regions: Mapped['Region'] = relationship('Region', back_populates='Player')

    TeamPlayers: Mapped[List['TeamPlayer']] = relationship('TeamPlayer', back_populates='Player')

    TeamJoinApplicationFromPlayer: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                            foreign_keys='[TeamJoinApplication.FromPlayerId]',
                                                                            back_populates='FromPlayer')

    TeamJoinApplicationToPlayer: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                             foreign_keys='[TeamJoinApplication.ToPlayerId]',
                                                                             back_populates='ToPlayer')

    TeamJoinApplicationHandlerPlayer: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                             foreign_keys='[TeamJoinApplication.HandlerPlayerId]',
                                                                             back_populates='HandlerPlayer')
