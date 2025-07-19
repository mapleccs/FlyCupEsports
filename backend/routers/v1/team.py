from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.core.database import get_db
from backend.services.v1.team import register_team_services
from backend.schemas.v1.team import TeamRegisterRequest, TeamRegisterResponse

from backend.core.auth import get_token_user_id

router = APIRouter(prefix="/team", tags=["team"])


@router.post("/register", response_model=TeamRegisterResponse, status_code=201)
async def register_user_endpoint(
        user_data: TeamRegisterRequest,
        user_id: int = Depends(get_token_user_id),
        db: Session = Depends(get_db),
) -> TeamRegisterResponse:
    try:
        return register_team_services(db, user_id, user_data)
    except HTTPException as e:
        return TeamRegisterResponse(
            success=False,
            team_token=None,
            message=e.detail
        )
