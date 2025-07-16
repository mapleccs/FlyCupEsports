from fastapi import HTTPException, status
from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.role import Role
from backend.schemas.role import RoleInfoResponse


def get_all_role(db: Session) -> list[Row[tuple[int, str, str | None]]]:
    roles = db.query(Role.Id, Role.Name, Role.Remark).all()
    return roles


def get_role_by_name(db: Session, name: str) -> Role | None:
    role = db.query(Role).filter(Role.Name == name).first()
    return role
