from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.user import User
from backend.services.user import create_user, get_user_by_username
from backend.schemas.user import UserCreateRequest, UserCreateResponse

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/register", response_model=UserCreateResponse, status_code=201)
async def register_user(
        user_data: UserCreateRequest,
        db: Session = Depends(get_db)
):
    try:
        return create_user(db, user_data)
    except HTTPException as e:
        # 捕获并重新抛出异常以保持统一响应格式
        raise HTTPException(
            status_code=e.status_code,
            detail={
                "success": False,
                "userId": None,
                "message": e.detail
            }
        )
