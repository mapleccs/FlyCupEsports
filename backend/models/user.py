from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class User(Base):
    __tablename__ = 'User'
    __table_args__ = (
        ForeignKeyConstraint(['RoleId'], ['Role.Id'], name='User_ibfk_1'),
    )
    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='用户编号')
    Username: Mapped[str] = mapped_column(String(20), unique=True, comment='用户名称')
    Password: Mapped[str] = mapped_column(String(20), comment='密码')
    RoleId: Mapped[int] = mapped_column(Integer, comment="用户角色")
    UserPhoto: Mapped[Optional[str]] = mapped_column(String(255), comment='用户头像路径')

    Competitor: Mapped[List['Competitor']] = relationship('Competitor', back_populates='User_')

    Regions: Mapped[List['Region']] = relationship('Region', back_populates='User')

    Role: Mapped['Role'] = relationship('Role', foreign_keys=[RoleId], back_populates='Users')
