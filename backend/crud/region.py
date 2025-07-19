from typing import Optional
from typing import List
from sqlalchemy import Row
from sqlalchemy.orm import Session, joinedload

from backend.models.region import Region
from backend.schemas.v1.region import RegionInfoResponse


def get_all_regions(db: Session) -> List[Region]:
    return db.query(Region).options(joinedload(Region.Season)).options(joinedload(Region.User)).all()
