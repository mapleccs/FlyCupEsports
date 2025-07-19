from typing import Optional

from pydantic import BaseModel, Field


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    refresh_token: str
    access_token: str
