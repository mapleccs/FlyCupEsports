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
        Index('CurrentGradeId', 'CurrentGradeId'),
        Index('HighestGradeId', 'HighestGradeId'),
        Index('PrimaryLocationId', 'PrimaryLocationId'),
        Index('SecondaryLocationId', 'SecondaryLocationId'),
        Index('UserId', 'UserId')
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
    RegisterCost: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2), comment='报名押金')
    RegisterDate: Mapped[datetime.datetime] = mapped_column(DateTime, comment='报名日期')
    IsApproved: Mapped[int] = mapped_column(TINYINT(1), comment='是否通过申请')
    Reason: Mapped[Optional[str]] = mapped_column(Text, comment='未通过申请原因')

    Grade_: Mapped['Grade'] = relationship('Grade', foreign_keys=[CurrentGradeId], back_populates='Competitor')
    Grade1: Mapped['Grade'] = relationship('Grade', foreign_keys=[HighestGradeId], back_populates='Competitor_')
    Location_: Mapped['Location'] = relationship('Location', foreign_keys=[PrimaryLocationId], back_populates='Competitor')
    Location1: Mapped['Location'] = relationship('Location', foreign_keys=[SecondaryLocationId], back_populates='Competitor_')
    User_: Mapped['User'] = relationship('User', back_populates='Competitor')
    CompetitorContact: Mapped[List['CompetitorContact']] = relationship('CompetitorContact', back_populates='Competitor_')

