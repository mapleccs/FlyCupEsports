from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base

class UserRole(Base):
    __tablename__ = 'UserRole'
    __table_args__ = (
        ForeignKeyConstraint(['RoleId'], ['Role.Id'], name='UserRoleRole'),
        ForeignKeyConstraint(['UserId'], ['User.Id'], name='UserRoleUser'),
        Index('UserRoleRole', 'RoleId'),
        Index('UserRoleUser', 'UserId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='编号')
    UserId: Mapped[int] = mapped_column(Integer, comment='用户编号')
    RoleId: Mapped[int] = mapped_column(Integer, comment='角色编号')

    Role_: Mapped['Role'] = relationship('Role', back_populates='UserRole')
    User_: Mapped['User'] = relationship('User', back_populates='UserRole')

