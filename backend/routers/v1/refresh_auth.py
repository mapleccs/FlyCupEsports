from fastapi import APIRouter, Request, Response, Cookie, HTTPException, Body
from backend.core.auth import create_access_token, verify_refresh_token, create_refresh_token
from backend.schemas.v1.refresh_auth import RefreshTokenRequest, RefreshTokenResponse

router = APIRouter(prefix="/refresh-token", tags=["refresh"])


@router.post("/")
def refresh_access_token(data: RefreshTokenRequest) -> RefreshTokenResponse:
    refresh_token = data.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=400, detail="Missing refresh token")

    payload = verify_refresh_token(refresh_token)
    user_id = payload.get("user_id")

    new_access_token = create_access_token({"user_id": user_id})
    new_refresh_token = create_refresh_token({"user_id": user_id})
    return RefreshTokenResponse(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
    )
