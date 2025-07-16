from typing import List, Optional

from sqlalchemy import Column, DECIMAL, DateTime, ForeignKeyConstraint, Index, Integer, String, Table, Text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal
from backend.models.base import Base

class TeamRole(Base):
    __tablename__ = 'TeamRole'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(String(255))

    TeamCompetitor: Mapped[List['TeamCompetitor']] = relationship('TeamCompetitor', back_populates='TeamRole')
