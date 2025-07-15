from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class TeamJoinApplication(Base):
    __tablename__ = 'TeamJoinApplication'
    __table_args__ = (
        ForeignKeyConstraint(['FromCompetitorId'], ['Competitor.Id'], name='TeamJoinApplication_ibfk_1'),
        ForeignKeyConstraint(['HandlerCompetitorId'], ['Competitor.Id'], name='TeamJoinApplication_ibfk_4'),
        ForeignKeyConstraint(['TeamId'], ['Team.Id'], name='TeamJoinApplication_ibfk_3'),
        ForeignKeyConstraint(['ToCompetitorId'], ['Competitor.Id'], name='TeamJoinApplication_ibfk_2'),
        Index('FromCompetitorId', 'FromCompetitorId'),
        Index('HandlerCompetitorId', 'HandlerCompetitorId'),
        Index('TeamId', 'TeamId'),
        Index('ToCompetitorId', 'ToCompetitorId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ApplyType: Mapped[str] = mapped_column(String(255), comment='Join、Invite')
    FromCompetitorId: Mapped[Optional[int]] = mapped_column(Integer, comment='发起人')
    ToCompetitorId: Mapped[Optional[int]] = mapped_column(Integer, comment='目标人')
    TeamId: Mapped[Optional[int]] = mapped_column(Integer, comment='队伍')
    Message: Mapped[Optional[str]] = mapped_column(TEXT, comment='申请信息')
    Status: Mapped[Optional[str]] = mapped_column(String(255), comment='审批状态：Pending、Approved、Rejected、Cancelled')
    HandlerCompetitorId: Mapped[Optional[int]] = mapped_column(Integer, comment='处理人')
    HandleTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='处理时间')
    CreateTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='创建时间')

    FromCompetitor: Mapped[Optional['Competitor']] = relationship('Competitor', foreign_keys=[FromCompetitorId],
                                                                  back_populates='TeamJoinApplicationFromCompetitor')

    ToCompetitor: Mapped[Optional['Competitor']] = relationship('Competitor', foreign_keys=[ToCompetitorId],
                                                                back_populates='TeamJoinApplicationToCompetitor')

    HandlerCompetitor: Mapped[Optional['User']] = relationship('Competitor', foreign_keys=[HandlerCompetitorId],
                                                               back_populates='TeamJoinApplicationHandlerCompetitor')

    Team_: Mapped[Optional['Team']] = relationship('Team', back_populates='TeamJoinApplication')
