from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class User(Base):
    __tablename__ = 'User'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='用户编号')
    UserName: Mapped[str] = mapped_column(VARCHAR(20), comment='用户名称')
    Password: Mapped[str] = mapped_column(VARCHAR(20), comment='密码')
    UserPhoto: Mapped[str] = mapped_column(VARCHAR(255), nullable=True, comment='用户头像路径')

    Competitor: Mapped[List['Competitor']] = relationship('Competitor', back_populates='User_')
    Region: Mapped[List['Region']] = relationship('Region', back_populates='User_')
    TeamJoinApplication: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                            foreign_keys='[TeamJoinApplication.FromUserId]',
                                                                            back_populates='User_')
    TeamJoinApplication_: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                             foreign_keys='[TeamJoinApplication.HandlerUserId]',
                                                                             back_populates='User1')
    TeamJoinApplication1: Mapped[List['TeamJoinApplication']] = relationship('TeamJoinApplication',
                                                                             foreign_keys='[TeamJoinApplication.ToUserId]',
                                                                             back_populates='User2')
    TeamUser: Mapped[List['TeamUser']] = relationship('TeamUser', back_populates='User_')
    UserPermission: Mapped[List['UserPermission']] = relationship('UserPermission', back_populates='User_')
    UserRole: Mapped[List['UserRole']] = relationship('UserRole', back_populates='User_')
