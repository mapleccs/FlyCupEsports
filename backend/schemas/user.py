from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    user_name: str
    password: str
    photo_path: str


class UserCreateResponse(BaseModel):
    success: bool = Field(..., description="是否成功")
    user_id: int = Field(..., description="用户ID")
    message: str = Field(..., description="提示信息")
