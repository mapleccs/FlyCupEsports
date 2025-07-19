from typing import List

from fastapi import HTTPException, status, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.core.database import logger
from backend.crud.rank import *
from backend.schemas.v1.team import TeamRegisterResponse, TeamRegisterRequest
from backend.crud.team import create_team
from backend.crud.position import get_position_by_name
from backend.crud.rank import get_rank_by_name
from backend.core.auth import create_access_token
from backend.services.v1.player import get_player_by_user_id_region_id_service


def register_team_services(db: Session, user_id: int,
                           team_data: TeamRegisterRequest) -> TeamRegisterResponse:
    try:
        player = get_player_by_user_id_region_id_service(db, user_id, team_data.region_id)
        if player is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="在此赛区并未找到您已注册的选手.",
            )

        team = create_team(db, player.Id, team_data)

        db.commit()
        db.refresh(team)

        token = create_access_token({
            "team_id": team.Id,
        })

        return TeamRegisterResponse(
            success=True,
            team_token=token,
            message="队伍创建成功.",
        )

    except IntegrityError as e:
        if "uq_team_name_short_region" in str(e.orig):
            raise HTTPException(status_code=400, detail="同一个大区中不能有相同名称和简称的队伍")
        elif "uq_create_player_region" in str(e.orig):
            raise HTTPException(status_code=400, detail="一个玩家只能在一个赛区创建一个战队")
        else:
            logger.error(e)
            raise HTTPException(status_code=400, detail="创建信息有误")
