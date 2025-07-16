from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.services.role import get_all_roles_service

router = APIRouter(prefix="/role", tags=["role"])


@router.get("/")
async def get_roles(db: Session = Depends(get_db)):
    return get_all_roles_service(db)
