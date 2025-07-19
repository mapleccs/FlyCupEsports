from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.services.v1.region import get_all_region_service, get_region_statistics_service

router = APIRouter(prefix="/region", tags=["region"])


@router.get("/")
async def get_regions(db: Session = Depends(get_db)):
    return get_all_region_service(db)


@router.get("/statistics")
async def get_region_statistics(db: Session = Depends(get_db)):
    return get_region_statistics_service(db)
