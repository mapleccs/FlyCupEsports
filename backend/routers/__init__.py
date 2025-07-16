# backend/routers/__init__.py
from fastapi import APIRouter
from backend.routers import user  # 其他模块你也可以继续加

router = APIRouter(prefix="/v1")

# 聚合所有子模块的router
router.include_router(user.router)
