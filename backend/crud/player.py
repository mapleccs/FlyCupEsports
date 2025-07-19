from typing import Optional

from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.player import Player
from backend.schemas.v1.player import PlayerRegisterRequest, PlayerRegisterResponse
from datetime import datetime


def get_player_by_user_id_region_id(db: Session, user_id: int, region_id: int) -> Optional[Player]:
    return db.query(Player).filter(Player.UserId == user_id, Player.RegionId == region_id).first()


def create_player(db: Session, user_id: int, primary_position_id: int, secondary_position_id: int, highest_rank_id: int,
                  current_rank_id: int, player_request: PlayerRegisterRequest) -> Player:
    db_player = Player(
        UserId=user_id,
        Name=player_request.personal_name,
        GameNameWithNumber=player_request.gameId,
        PrimaryPositionId=primary_position_id,
        SecondaryPositionId=secondary_position_id,
        HighestRankId=highest_rank_id,
        CurrentRankId=current_rank_id,
        QQ=player_request.QQ,
        Contact=player_request.contact,
        RegionId=player_request.region,
        PaymentMethod=player_request.payment_method,
        RegisterTime=datetime.now(),
        RegisterCost=0.0,
        IsApproved=0
    )
    db.add(db_player)
    return db_player
