from fastapi import HTTPException, status
from sqlalchemy import Row
from sqlalchemy.orm import Session, joinedload
from backend.models.user import User
from backend.models.user_role import UserRole
from backend.schemas.user import UserCreateRequest, UserCreateResponse, UserInfoResponse, UserLoginRequest


def user_login(db: Session, login_info: UserLoginRequest) -> User | None:
    user = db.query(User).filter(
        User.Username == login_info.username,
        User.Password == login_info.password
    ).first()
    return user


def get_all_user(db: Session) -> list[UserInfoResponse]:
    users = db.query(User).options(
        joinedload(User.UserRole).joinedload(UserRole.Role_)
    ).all()

    return [
        UserInfoResponse(
            id=u.Id,
            username=u.Username,
            photo_path=u.UserPhoto,
            roles=[r.Role_.Name for r in u.UserRole]
        ) for u in users
    ]


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
