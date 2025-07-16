from fastapi import HTTPException, status
from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.user_role import UserRole


def assign_role_to_user(db: Session, user_id: int, role_id: int) -> UserRole | None:
    user_role = UserRole(UserId=user_id, RoleId=role_id)
    db.add(user_role)
    db.commit()
    db.refresh(user_role)
    return user_role
