from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base

class Season(Base):
    __tablename__ = 'Season'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(255), comment='赛季名')
    StartDate: Mapped[datetime.datetime] = mapped_column(DateTime, comment='赛季开始日期')
    EndDate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, comment='赛季结束日期')
    Description: Mapped[Optional[str]] = mapped_column(String(255))

    Region: Mapped[List['Region']] = relationship('Region', back_populates='Season_')