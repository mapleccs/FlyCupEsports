from typing import List, Optional

from fastapi import HTTPException, status, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.core.database import logger
from backend.crud.rank import *
from backend.models import Player
from backend.schemas.v1.player import PlayerRegisterRequest, PlayerRegisterResponse
from backend.crud.player import create_player, get_player_by_user_id_region_id
from backend.crud.position import get_position_by_name
from backend.crud.rank import get_rank_by_name
from backend.core.auth import create_access_token
from backend.crud.user import change_user_type
from backend.crud.role import get_role_by_name


def get_player_by_user_id_region_id_service(db: Session, user_id: int, region_id: int) -> Optional[Player]:
    return get_player_by_user_id_region_id(db, user_id, region_id)


def register_player_services(db: Session, user_id: int,
                             user_data: PlayerRegisterRequest) -> PlayerRegisterResponse:
    try:
        main_position = get_position_by_name(db, user_data.main_position)
        secondary_position = get_position_by_name(db, user_data.secondary_position)

        highest_rank = get_rank_by_name(db, user_data.highest_rank)
        current_rank = get_rank_by_name(db, user_data.current_rank)

        player = create_player(db, user_id, main_position.Id, secondary_position.Id, highest_rank.Id, current_rank.Id,
                               user_data)


        token = create_access_token({
            "player_id": player.Id,
        })

        role = get_role_by_name(db, "player")
        if role is None:
            raise HTTPException(status_code=404, detail="'玩家'角色未找到")
        change_success = change_user_type(db, user_id, role.Id)
        if not change_success:
            raise HTTPException(status_code=400,detail="玩家状态修改失败")

        db.commit()
        db.refresh(player)

        return PlayerRegisterResponse(
            success=True,
            player_token=token,
            player_id=player.Id,
            message="选手注册成功.",
        )
    except IntegrityError as e:
        if "player_user_id_region_id" in str(e.orig):
            raise HTTPException(status_code=400, detail="该用户已在该赛区报名")
        elif "player_user_id_game_name_with_number" in str(e.orig):
            raise HTTPException(status_code=400, detail="该游戏名在该赛区已被使用")
        else:
            logger.error(e)
            raise HTTPException(status_code=400, detail="报名信息有误")
