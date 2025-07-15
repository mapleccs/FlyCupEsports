from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db  # 负责返回数据库 Session
from backend import models  # 你的数据库模型

router = APIRouter()

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()  # 查询User表所有数据
    return users

@router.get("/ping")
async def ping():
    return {"msg": "pong"}
