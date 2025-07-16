from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.schemas.v1.user import UserCreateRequest, UserCreateResponse, UserInfoResponse, UserLoginRequest, \
    UserLoginResponse
from backend.crud.user import get_user_by_username, create_user, get_all_user, user_login
from backend.crud.user_role import assign_role_to_user
from backend.crud.role import get_role_by_name


def user_login_service(db: Session, login_info: UserLoginRequest) -> UserLoginResponse | None:
    user = user_login(db, login_info)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The user name or password is incorrect.",
        )
    return UserLoginResponse(
        success=True,
        user_id=user.Id,
        message="Login successfully.",
    )


def get_all_users_service(db: Session) -> List[UserInfoResponse]:
    raw_users = get_all_user(db)
    return raw_users


def register_user_services(db: Session, user_data: UserCreateRequest) -> UserCreateResponse:
    existing_user = get_user_by_username(db, user_data.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists.",
        )

    role = get_role_by_name(db, user_data.role)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The role is not exist.",
        )
    user = create_user(db, user_data)
    user_role = assign_role_to_user(db, user.Id, role.Id)

    return UserCreateResponse(
        success=True,
        user_id=user.Id,
        message="User created successfully.",
    )
