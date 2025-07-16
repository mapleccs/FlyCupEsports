from fastapi import HTTPException, status
from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreateRequest, UserCreateResponse, UserLoginRequest


def user_login(db: Session, login_info: UserLoginRequest) -> User | None:
    user = db.query(User).filter(
        User.Username == login_info.username,
        User.Password == login_info.password
    ).first()
    return user


def get_all_user(db: Session) -> list[Row[tuple[int, str, str | None]]]:
    users = db.query(User.Id, User.Username, User.UserPhoto).all()
    return users


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.Username == username).first()


def create_user(db: Session, user: UserCreateRequest) -> User | None:
    db_user = User(
        Username=user.username,
        Password=user.password,
        UserPhoto=user.photo_path,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
