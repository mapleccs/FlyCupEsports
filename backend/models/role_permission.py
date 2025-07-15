from sqlalchemy import Table, Column, Integer, ForeignKey, Index
from backend.models.base import Base

t_RolePermission = Table(
    'RolePermission', Base.metadata,
    Column('RoleId', Integer, ForeignKey('Role.Id'), primary_key=True, nullable=False),
    Column('PermissionId', Integer, ForeignKey('Permission.Id'), primary_key=True, nullable=False),
    Index('PermissionId', 'PermissionId')
)
