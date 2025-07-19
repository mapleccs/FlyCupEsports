from typing import Optional

from pydantic import BaseModel, Field


class TeamRegisterRequest(BaseModel):
    name: str = Field(..., description="战队名称")
    shortname: str = Field(..., description="战队简称")
    logo: Optional[str] = Field(None, description="logo url")
    slogan: str = Field(..., description="战队口号")
    region_id: int = Field(..., description="赛区ID")


class TeamRegisterResponse(BaseModel):
    success: bool = Field(..., description="是否成功")
    team_token: Optional[str] = Field(None, description="队伍编号token")
    message: str = Field(..., description="提示信息")
