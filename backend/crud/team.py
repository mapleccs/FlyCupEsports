from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.team import Team
from backend.schemas.v1.team import TeamRegisterRequest, TeamRegisterResponse
from datetime import datetime


def create_team(db: Session, player_id: int, team_request: TeamRegisterRequest) -> Team:
    db_team = Team(
        TeamName=team_request.name,
        TeamShortName=team_request.shortname,
        TeamLogo=team_request.logo,
        TeamSlogan=team_request.slogan,
        CreatePlayerId=player_id,
        RegionId=team_request.region_id,
        RegisterCost=0.0,
        RegisterTime=datetime.now(),
    )
    db.add(db_team)
    return db_team
