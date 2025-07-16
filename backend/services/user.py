from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreateRequest, UserCreateResponse


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.UserName == username).first()


def create_user(db: Session, user_data: UserCreateRequest) -> UserCreateResponse:
    existing_user = get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists.",
        )
    # 创建用户对象
    db_user = User(
        UserName=user_data.username,
        Password=user_data.password,
        UserPhoto=user_data.photo,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserCreateResponse(
        success=True,
        userId=db_user.Id,
        message="User created successfully.",
    )
