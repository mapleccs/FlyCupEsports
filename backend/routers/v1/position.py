from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.services.v1.position import get_all_position_service

router = APIRouter(prefix="/position", tags=["role"])


@router.get("/")
async def get_positions(db: Session = Depends(get_db)):
    return get_all_position_service(db)
