from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.core.config import settings
from backend.models.base import Base

engine = create_engine(
    settings.database_url,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def init_db():
    Base.metadata.create_all(bind=engine)

# FastAPI 依赖注入用
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
