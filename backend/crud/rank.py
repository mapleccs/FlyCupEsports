from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.rank import Rank
from backend.schemas.v1.rank import RankInfoResponse


def get_rank_by_name(db: Session, name: str) -> Rank | None:
    return db.query(Rank).filter(Rank.Name == name).first()


def get_all_rank(db: Session) -> list[RankInfoResponse]:
    ranks = db.query(Rank).all()

    requests = [
        RankInfoResponse(
            id=r.Id,
            name=r.Name,
            remark=r.Remark
        )
        for r in ranks
    ]
    return requests
