from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.user import User
from backend.services.user import register_user_services,get_all_users_service
from backend.schemas.user import UserCreateRequest, UserCreateResponse

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    return get_all_users_service(db)


@router.post("/register", response_model=UserCreateResponse, status_code=201)
async def register_user_endpoint(
        user_data: UserCreateRequest,
        db: Session = Depends(get_db),
):
    try:
        return register_user_services(db, user_data)
    except HTTPException as e:
        return UserCreateResponse(
            success=False,
            user_id=None,
            message=e.detail
        )
