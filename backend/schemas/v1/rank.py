from typing import Optional

from pydantic import BaseModel, Field


class RankInfoResponse(BaseModel):
    id: int = Field(..., description="编号")
    name: str = Field(..., description="段位")
    remark: Optional[str] = Field(None, description="备注")
