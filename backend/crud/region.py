from typing import Optional
from typing import List
from sqlalchemy import Row, distinct
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

from backend.models.region import Region
from backend.models.team import Team
from backend.models.player import Player
from backend.schemas.v1.region import RegionInfoResponse


def get_all_regions(db: Session) -> List[Region]:
    return db.query(Region).options(joinedload(Region.Season)).options(joinedload(Region.User)).all()


# 返回 List[Row(region_id, team_count)]
def get_region_team_counts(db: Session):
    return db.query(
        Region.Id.label("region_id"),
        func.count(distinct(Team.Id)).label("team_count")
    ).outerjoin(Team, Team.RegionId == Region.Id) \
     .group_by(Region.Id) \
     .all()

# 返回 List[Row(region_id, player_count)]
def get_region_player_counts(db: Session):
    return db.query(
        Region.Id.label("region_id"),
        func.count(distinct(Player.Id)).label("player_count")
    ).outerjoin(Player, Player.RegionId == Region.Id) \
     .group_by(Region.Id) \
     .all()
