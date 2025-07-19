from typing import List

from sqlalchemy.orm import Session
from backend.schemas.v1.position import PositionInfoResponse
from backend.crud.position import get_all_position


def get_all_position_service(db: Session) -> List[PositionInfoResponse]:
    res=get_all_position(db)

    requests = [
        PositionInfoResponse(
            id=pos.Id,
            name=pos.Name,
            remark=pos.Remark
        )
        for pos in res
    ]
    return requests
