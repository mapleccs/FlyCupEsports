from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from .base import Base


class OperationLog(Base):
    __tablename__ = 'OperationLog'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    UserId: Mapped[int] = mapped_column(Integer, comment='执行者ID（外键可指向 User.Id）')
    ActionType: Mapped[str] = mapped_column(String(255), comment='操作类型（如：RegisterTeam、ChangeCaptain、QuitTeam）')
    TargetType: Mapped[str] = mapped_column(String(255), comment='操作对象类型（如：Team、Region、User）')
    IsSensitive: Mapped[int] = mapped_column(TINYINT(1), comment='是否敏感操作（如权限变更、删人）')
    TargetId: Mapped[Optional[int]] = mapped_column(Integer, comment='操作目标主键ID')
    Description: Mapped[Optional[str]] = mapped_column(Text, comment='自然语言或JSON说明（如：{"oldCaptain":1001,"newCaptain":1002}）')
    IpAddress: Mapped[Optional[str]] = mapped_column(String(45), comment='操作者IP')
    UserAgent: Mapped[Optional[str]] = mapped_column(Text, comment='浏览器或客户端标识')
    Source: Mapped[Optional[str]] = mapped_column(String(50), comment='来源（Web、API、Admin等）')
    CreateTime: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='发生时间')