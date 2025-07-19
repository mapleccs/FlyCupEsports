from datetime import timedelta
from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.schemas.v1.user import UserCreateRequest, UserCreateResponse, UserInfoResponse, UserLoginRequest, \
    UserLoginResponse, UserUpdateRoleResponse
from backend.crud.user import get_user_by_username, create_user, get_all_user, user_login, change_user_type
from backend.crud.role import get_role_by_name
from backend.core.auth import create_access_token, create_refresh_token


def user_login_service(db: Session, login_info: UserLoginRequest) -> UserLoginResponse:
    user = user_login(db, login_info)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误.",
        )

    access_token = create_access_token({"user_id": user.Id})
    refresh_token = create_refresh_token({"user_id": user.Id})

    return UserLoginResponse(
        success=True,
        user_token=access_token,
        refresh_token=refresh_token,
        user_role_id=user.RoleId,
        user_role_name=user.Role.Name if user.Role else None,
        message="登录成功.",
    )


def get_all_users_service(db: Session) -> List[UserInfoResponse]:
    raw_users = get_all_user(db)
    return raw_users


def register_user_services(db: Session, user_data: UserCreateRequest) -> UserCreateResponse:
    role_capitalized = user_data.role.capitalize()
    existing_user = get_user_by_username(db, user_data.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="此用户已存在.",
        )

    role = get_role_by_name(db, role_capitalized)

    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="此角色不存在.",
        )
    user = create_user(db, user_data, role.Id)
    db.commit()
    db.refresh(user)

    token = create_access_token({
        "user_id": user.Id,
    })

    return UserCreateResponse(
        success=True,
        user_token=token,
        message="用户创建成功.",
    )
