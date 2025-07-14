from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from .base import Base


class TeamUser(Base):
    __tablename__ = 'TeamUser'
    __table_args__ = (
        ForeignKeyConstraint(['TeamId'], ['Team.Id'], name='TeamUser_ibfk_1'),
        ForeignKeyConstraint(['TeamRoleId'], ['TeamRole.Id'], name='TeamUser_ibfk_3'),
        ForeignKeyConstraint(['UserId'], ['User.Id'], name='TeamUser_ibfk_2'),
        Index('TeamId', 'TeamId'),
        Index('TeamRoleId', 'TeamRoleId'),
        Index('UserId', 'UserId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    TeamId: Mapped[int] = mapped_column(Integer, comment='队伍')
    UserId: Mapped[int] = mapped_column(Integer, comment='选手')
    TeamRoleId: Mapped[int] = mapped_column(Integer, comment='队内角色')
    JoinDate: Mapped[datetime.datetime] = mapped_column(DateTime)

    Team_: Mapped['Team'] = relationship('Team', back_populates='TeamUser')
    TeamRole_: Mapped['TeamRole'] = relationship('TeamRole', back_populates='TeamUser')
    User_: Mapped['User'] = relationship('User', back_populates='TeamUser')
