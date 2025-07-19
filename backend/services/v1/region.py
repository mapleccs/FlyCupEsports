from typing import List

from sqlalchemy.orm import Session
from backend.schemas.v1.region import RegionInfoResponse
from backend.crud.region import get_all_regions


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
