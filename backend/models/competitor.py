from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class Competitor(Base):
    __tablename__ = 'Competitor'
    __table_args__ = (
        ForeignKeyConstraint(['CurrentGradeId'], ['Grade.Id'], name='Competitor_ibfk_2'),
        ForeignKeyConstraint(['HighestGradeId'], ['Grade.Id'], name='Competitor_ibfk_3'),
        ForeignKeyConstraint(['PrimaryLocationId'], ['Location.Id'], name='Competitor_ibfk_4'),
        ForeignKeyConstraint(['SecondaryLocationId'], ['Location.Id'], name='Competitor_ibfk_5'),
        ForeignKeyConstraint(['UserId'], ['User.Id'], name='Competitor_ibfk_1'),
        ForeignKeyConstraint(['RegionId'], ['Region.Id'], name='Competitor_ibfk_6'),
        Index('CurrentGradeId', 'CurrentGradeId'),
        Index('HighestGradeId', 'HighestGradeId'),
        Index('PrimaryLocationId', 'PrimaryLocationId'),
        Index('SecondaryLocationId', 'SecondaryLocationId'),
        Index('UserId', 'UserId'),
        Index('RegionId', 'RegionId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserId: Mapped[int] = mapped_column(Integer, comment='绑定的用户')
    Name: Mapped[str] = mapped_column(VARCHAR(255), comment='用户称呼')
    GameNameWithNumber: Mapped[str] = mapped_column(VARCHAR(255), comment='游戏名以及编号')
    CurrentGradeId: Mapped[int] = mapped_column(Integer, comment='当前段位')
    HighestGradeId: Mapped[int] = mapped_column(Integer, comment='最高段位')
    PrimaryLocationId: Mapped[int] = mapped_column(Integer, comment='主位置')
    SecondaryLocationId: Mapped[int] = mapped_column(Integer, comment='副位置')
    QQ: Mapped[str] = mapped_column(VARCHAR(20), comment='QQ号')
    Contact: Mapped[str] = mapped_column(VARCHAR(20), comment='联系方式')

    RegionId: Mapped[int] = mapped_column(Integer, comment="报名赛区")
    RegisterCost: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), comment='报名押金')
    RegisterTime: Mapped[datetime.datetime] = mapped_column(DateTime, comment='赛区报名时间')

    IsApproved: Mapped[int] = mapped_column(TINYINT(1), comment='是否通过申请')
    Reason: Mapped[Optional[str]] = mapped_column(Text, comment='未通过申请原因')

    CurrentGrade: Mapped['Grade'] = relationship('Grade', foreign_keys=[CurrentGradeId],
                                                 back_populates='CurrentGradeCompetitor')
    HighestGrade: Mapped['Grade'] = relationship('Grade', foreign_keys=[HighestGradeId],
                                                 back_populates='HighestGradeCompetitor')

    PrimaryLocation: Mapped['Location'] = relationship('Location', foreign_keys=[PrimaryLocationId],
                                                       back_populates='PrimaryLocationCompetitor')
    SecondaryLocation: Mapped['Location'] = relationship('Location', foreign_keys=[SecondaryLocationId],
                                                         back_populates='SecondaryLocationCompetitor')

    User_: Mapped['User'] = relationship('User', back_populates='Competitor')
    Regions: Mapped['Region'] = relationship('Region', back_populates='Competitor')

    TeamCompetitors: Mapped[List['TeamCompetitor']] = relationship('TeamCompetitor', back_populates='Competitor')

    TeamJoinApplicationFromCompetitor: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                            foreign_keys='[TeamJoinApplication.FromCompetitorId]',
                                                                            back_populates='FromCompetitor')

    TeamJoinApplicationToCompetitor: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                             foreign_keys='[TeamJoinApplication.ToCompetitorId]',
                                                                             back_populates='ToCompetitor')

    TeamJoinApplicationHandlerCompetitor: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                             foreign_keys='[TeamJoinApplication.HandlerCompetitorId]',
                                                                             back_populates='HandlerCompetitor')
