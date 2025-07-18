from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.core.config import settings
from backend.models.base import Base
import logging

logger = logging.getLogger(__name__)

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
    except Exception as e:
        db.rollback()
        logger.error(f"数据库写入失败: {e}")
        raise
    finally:
        db.close()
