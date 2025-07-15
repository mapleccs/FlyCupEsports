from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base


class SystemLog(Base):
    __tablename__ = 'SystemLog'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='日志主键，自增')
    Level: Mapped[str] = mapped_column(VARCHAR(255), comment="日志级别，例如：（'Trace', 'Debug', 'Info', 'Warning', 'Error', 'Critical'）")
    Message: Mapped[str] = mapped_column(VARCHAR(255), comment='简洁明了的提示语')
    CreateTime: Mapped[datetime.datetime] = mapped_column(DateTime, comment='生成时间')
    Detail: Mapped[Optional[str]] = mapped_column(TEXT, comment='异常堆栈、调试信息等')
    Source: Mapped[Optional[str]] = mapped_column(VARCHAR(255), comment='哪个模块或功能写的日志')
    ServerIp: Mapped[Optional[str]] = mapped_column(VARCHAR(255), comment='哪台服务器/容器记录的')
    TraceId: Mapped[Optional[int]] = mapped_column(Integer, comment='分布式系统中的请求链路标识')
