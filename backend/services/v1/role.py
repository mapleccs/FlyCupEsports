from typing import List

from sqlalchemy.orm import Session
from backend.schemas.v1.role import RoleInfoResponse
from backend.crud.role import get_all_role


def get_all_roles_service(db: Session) -> List[RoleInfoResponse]:
    roles = get_all_role(db)
    return [RoleInfoResponse(id=u[0], name=u[1], remark=u[2]) for u in roles]
