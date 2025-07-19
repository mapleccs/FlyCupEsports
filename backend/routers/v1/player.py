from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.core.database import get_db
from backend.services.v1.player import register_player_services
from backend.schemas.v1.player import PlayerRegisterRequest, PlayerRegisterResponse

from backend.core.auth import get_token_user_id

router = APIRouter(prefix="/player", tags=["player"])


@router.post("/register", response_model=PlayerRegisterResponse, status_code=201)
async def register_user_endpoint(
        user_data: PlayerRegisterRequest,
        user_id: int = Depends(get_token_user_id),
        db: Session = Depends(get_db),

) -> PlayerRegisterResponse:
    try:
        return register_player_services(db, user_id, user_data)
    except HTTPException as e:
        return PlayerRegisterResponse(
            success=False,
            player_token=None,
            player_id=None,
            message=e.detail
        )
