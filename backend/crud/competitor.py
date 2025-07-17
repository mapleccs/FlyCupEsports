from sqlalchemy.orm import Session
from backend.models.player import Player
from backend.schemas.v1.competitor import CompetitorCreateRequest


def create_competitor(db: Session,competitor:CompetitorCreateRequest ) -> Player:
    db_competitor = Player()


