from typing import List

from sqlalchemy.orm import Session
from backend.schemas.v1.region import RegionInfoResponse, RegionStatisticsResponse
from backend.crud.region import get_all_regions, get_region_team_counts, get_region_player_counts


def get_all_region_service(db: Session) -> List[RegionInfoResponse]:
    regions = get_all_regions(db)

    return [
        RegionInfoResponse(
            season_name=region.Season.Name,
            name=region.Name,
            username=region.User.Username,
            logo=region.RegionLogo,
            max_team_limit=region.MaxTeamLimit,
            end_register_date=region.EndRegisterDate.strftime("%Y-%m-%d"),
            start_competition_date=region.StartCompetitionDate.strftime("%Y-%m-%d"),
            end_competition_date=region.EndCompetitionDate.strftime("%Y-%m-%d"),
        ) for region in regions
    ]

def get_region_statistics_service(db: Session) -> list[RegionStatisticsResponse]:
    # 获取所有赛区（用于名字和 ID）
    regions = get_all_regions(db)  # 返回包含 Id 和 Name 的 Region 列表

    # 获取每个赛区的队伍数
    team_counts = get_region_team_counts(db)
    player_counts = get_region_player_counts(db)

    # 转成字典便于合并
    team_count_map = {row.region_id: row.team_count for row in team_counts}
    player_count_map = {row.region_id: row.player_count for row in player_counts}

    # 构造最终响应列表
    statistics = [
        RegionStatisticsResponse(
            region_id=region.Id,
            region_name=region.Name,
            team_count=team_count_map.get(region.Id, 0),
            player_count=player_count_map.get(region.Id, 0),
        ) for region in regions
    ]
    return statistics