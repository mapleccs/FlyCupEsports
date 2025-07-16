from fastapi import HTTPException, status
from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreateRequest, UserCreateResponse


def get_all_user(db: Session) -> list[Row[tuple[int, str, str | None]]]:
    users = db.query(User.Id, User.UserName, User.UserPhoto).all()
    return users


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.UserName == username).first()


def create_user(db: Session, user: UserCreateRequest) -> User | None:
    db_user = User(
        UserName=user.user_name,
        Password=user.password,
        UserPhoto=user.photo_path,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
