from typing import Optional, List

from pydantic import BaseModel, Field


class UserLoginRequest(BaseModel):
    username: str = Field(..., description="用户名")
    password: str = Field(..., description="密码")


class UserLoginResponse(BaseModel):
    success: bool = Field(..., description="是否成功")
    user_id: Optional[int] = Field(None, description="用户ID")
    message: str = Field(..., description="提示信息")


class UserInfoResponse(BaseModel):
    id: int = Field(..., description="用户编号")
    username: str = Field(..., description="用户名")
    photo_path: Optional[str] = Field(None, description="头像路径")
    roles: List[str] = Field(..., description="角色")


class UserCreateRequest(BaseModel):
    username: str = Field(..., description="用户名")
    password: str = Field(..., description="密码")
    photo_path: Optional[str] = Field(None, description="头像路径")
    role: str = Field("User", description="角色")


class UserCreateResponse(BaseModel):
    success: bool = Field(..., description="是否成功")
    user_id: Optional[int] = Field(None, description="用户ID")
    message: str = Field(..., description="提示信息")
