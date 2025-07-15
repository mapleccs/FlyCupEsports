from typing import List
from sqlalchemy import Integer, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base

class ContactType(Base):
    __tablename__ = 'ContactType'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Name: Mapped[str] = mapped_column(VARCHAR(255), comment='联系方式')

    CompetitorContact: Mapped[List['CompetitorContact']] = relationship(
        'CompetitorContact', back_populates='ContactType_'
    )
