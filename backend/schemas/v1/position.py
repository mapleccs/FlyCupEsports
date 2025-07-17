from typing import Optional

from pydantic import BaseModel, Field


class PositionInfoResponse(BaseModel):
    id: int = Field(..., description="编号")
    name: str = Field(..., description="角色名")
    remark: Optional[str] = Field(None, description="备注")
