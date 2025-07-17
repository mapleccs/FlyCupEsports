from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.position import Position
from backend.schemas.v1.position import PositionInfoResponse


def get_all_position(db: Session) -> list[PositionInfoResponse]:
    positions = db.query(Position).all()

    requests = [
        PositionInfoResponse(
            id=pos.Id,
            name=pos.Name,
            remark=pos.Remark
        )
        for pos in positions
    ]
    return requests
