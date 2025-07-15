from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.user import User

router = APIRouter()


@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
