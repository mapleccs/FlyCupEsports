from typing import List, Optional
from sqlalchemy import Integer, VARCHAR, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.models.role_permission import t_RolePermission  # 中间表

from backend.models.base import Base

class Permission(Base):
    __tablename__ = 'Permission'

    Id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='编号')
    Code: Mapped[str] = mapped_column(VARCHAR(255), comment='权限具体功能，例如：VIEW_MATCH_PAGE、EDIT_PLAYER_API')
    Name: Mapped[str] = mapped_column(VARCHAR(255), comment='名称')
    Type: Mapped[str] = mapped_column(VARCHAR(255), comment='权限类型，例如：页面、接口、数据、按钮')
    Url: Mapped[Optional[str]] = mapped_column(VARCHAR(255), comment='API请求地址，例如：/admin/match、/api/player/{id}')
    Method: Mapped[Optional[str]] = mapped_column(VARCHAR(255), comment='标识GET还是POST请求')
    Remark: Mapped[Optional[str]] = mapped_column(TEXT, comment='描述')

    Role: Mapped[List['Role']] = relationship(
        'Role',
        secondary=t_RolePermission,
        back_populates='Permission_'
    )
    UserPermission: Mapped[List['UserPermission']] = relationship('UserPermission', back_populates='Permission_')
