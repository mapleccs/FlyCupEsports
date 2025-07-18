from typing import List

from sqlalchemy.orm import Session
from backend.schemas.v1.rank import RankInfoResponse
from backend.crud.rank import get_all_rank


def get_all_rank_service(db: Session) -> List[RankInfoResponse]:
    res = get_all_rank(db)
    return res
