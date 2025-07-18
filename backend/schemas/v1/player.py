from typing import Optional

from pydantic import BaseModel, Field


class PlayerRegisterRequest(BaseModel):
    personal_name: str = Field(..., description="选手名")
    gameId: str = Field(..., description="游戏名")
    main_position: str = Field(..., description="主位置")
    secondary_position: str = Field(..., description="副位置")
    highest_rank: str = Field(..., description="最高段位")
    current_rank: str = Field(..., description="当前段位")
    QQ: str = Field(..., description="QQ号")
    contact: Optional[str] = Field(None, description="联系方式")
    region: int = Field(..., description="赛区ID")
    payment_method: str = Field(..., description="支付方式")


class PlayerRegisterResponse(BaseModel):
    success: bool = Field(..., description="是否成功")
    player_token: Optional[str] = Field(None, description="玩家编号token")
    message: str = Field(..., description="提示信息")
