from sqlalchemy.orm import Session
from backend.models.competitor import Competitor
from backend.schemas.v1.competitor import CompetitorCreateRequest


def create_competitor(db: Session,competitor:CompetitorCreateRequest ) -> Competitor:
    db_competitor = Competitor()


