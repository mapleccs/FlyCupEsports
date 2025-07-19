from sqlalchemy import Row
from sqlalchemy.orm import Session
from backend.models.position import Position


def get_position_by_name(db: Session, name: str) -> Position | None:
    return db.query(Position).filter(Position.Name == name).first()


def get_all_position(db: Session) -> list[Position]:
    positions = db.query(Position).all()
    return positions
