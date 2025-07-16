from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserCreateRequest, UserCreateResponse, UserInfoResponse
from backend.crud.user import get_user_by_username, create_user, get_all_user
from backend.crud.user_role import assign_role_to_user
from backend.crud.role import get_role_by_name


def get_all_users_service(db: Session) -> List[UserInfoResponse]:
    raw_users = get_all_user(db)
    return [UserInfoResponse(id=u[0], user_name=u[1], photo_path=u[2]) for u in raw_users]


def register_user_services(db: Session, user_data: UserCreateRequest) -> UserCreateResponse:
    existing_user = get_user_by_username(db, user_data.user_name)

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
