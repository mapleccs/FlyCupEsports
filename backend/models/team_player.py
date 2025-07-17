from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class TeamPlayer(Base):
    __tablename__ = 'TeamPlayer'
    __table_args__ = (
        ForeignKeyConstraint(['TeamId'], ['Team.Id'], name='TeamPlayer_ibfk_1'),
        ForeignKeyConstraint(['TeamRoleId'], ['TeamRole.Id'], name='TeamPlayer_ibfk_3'),
        ForeignKeyConstraint(['PlayerId'], ['Player.Id'], name='TeamPlayer_ibfk_2'),
        Index('TeamId', 'TeamId'),
        Index('TeamRoleId', 'TeamRoleId'),
        Index('PlayerId', 'PlayerId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    TeamId: Mapped[int] = mapped_column(Integer, comment='队伍')
    PlayerId: Mapped[int] = mapped_column(Integer, comment='选手')
    TeamRoleId: Mapped[int] = mapped_column(Integer, comment='队内角色')
    JoinDate: Mapped[datetime.datetime] = mapped_column(DateTime)

    Team: Mapped['Team'] = relationship('Team', back_populates='TeamPlayer')
    TeamRole: Mapped['TeamRole'] = relationship('TeamRole', back_populates='TeamPlayer')
    Player: Mapped['Player'] = relationship('Player', back_populates='TeamPlayers')
