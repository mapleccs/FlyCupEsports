from typing import Optional

from pydantic import BaseModel, Field


class RegionInfoResponse(BaseModel):
    season_name: str = Field(..., description="赛季名")
    name: str = Field(..., description="赛区名")
    username: str = Field(..., description="负责人")
    logo: str = Field(..., description="logo路径")
    max_team_limit: int = Field(..., description="队伍上限")
    end_register_date: str = Field(..., description="注册截止时间")
    start_competition_date: str = Field(..., description="比赛开始时间")
    end_competition_date: str = Field(..., description="比赛结束时间")

class RegionStatisticsResponse(BaseModel):
    region_id:int=Field(...,description="赛区编号")
    region_name:str=Field(...,description="赛区名")
    team_count:int=Field(...,description="队伍数量")
    player_count:int=Field(...,description="选手数量")