# backend/core/auth.py
from datetime import datetime, timedelta

from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError

from backend.core.config import settings

security = HTTPBearer()

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token 已过期")
    except JWTError:
        raise HTTPException(status_code=401, detail="无效的 Token")

def get_token_field(field_name: str):
    def dependency(credentials: HTTPAuthorizationCredentials = Security(security)):
        token = credentials.credentials
        payload = decode_token(token)
        value = payload.get(field_name)
        if value is None:
            raise HTTPException(status_code=401, detail=f"无效的 token，缺少 {field_name}")
        if not isinstance(value, int):
            raise HTTPException(status_code=401, detail=f"Token 中 {field_name} 类型错误，应为整数")
        return value
    return dependency

get_token_user_id = get_token_field("user_id")
get_token_player_id = get_token_field("player_id")
