from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from .base import Base



class UserPermission(Base):
    __tablename__ = 'UserPermission'
    __table_args__ = (
        ForeignKeyConstraint(['PermissionId'], ['Permission.Id'], name='UserPermission_ibfk_2'),
        ForeignKeyConstraint(['UserId'], ['User.Id'], name='UserPermission_ibfk_1'),
        Index('PermissionId', 'PermissionId'),
        Index('UserId', 'UserId')
    )

    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='编号')
    UserId: Mapped[int] = mapped_column(Integer, comment='用户编号')
    PermissionId: Mapped[int] = mapped_column(Integer, comment='权限编号')
    IsAllow: Mapped[int] = mapped_column(TINYINT(1), comment='是否可以使用')

    Permission_: Mapped['Permission'] = relationship('Permission', back_populates='UserPermission')
    User_: Mapped['User'] = relationship('User', back_populates='UserPermission')
