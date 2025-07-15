from typing import List, Optional
from sqlalchemy import Integer, VARCHAR, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.models.base import Base
from backend.models.role_permission import t_RolePermission  # 中间表

class Role(Base):
    __tablename__ = 'Role'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='角色编号')
    Name: Mapped[str] = mapped_column(VARCHAR(255), comment='角色名称')
    Remark: Mapped[Optional[str]] = mapped_column(TEXT, comment='角色备注')

    Permission_: Mapped[List['Permission']] = relationship(
        'Permission',
        secondary=t_RolePermission,
        back_populates='Role'
    )
    UserRole: Mapped[List['UserRole']] = relationship('UserRole', back_populates='Role_')
