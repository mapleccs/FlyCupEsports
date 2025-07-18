from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.services.v1.rank import get_all_rank_service

router = APIRouter(prefix="/rank", tags=["rank"])


@router.get("/")
async def get_rank(db: Session = Depends(get_db)):
    return get_all_rank_service(db)
