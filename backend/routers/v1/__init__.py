from fastapi import APIRouter
from backend.routers.v1 import user, role,position

# 其他模块你也可以继续加

router = APIRouter(prefix="/v1")

# 聚合所有子模块的router
router.include_router(user.router)
router.include_router(role.router)
router.include_router(position.router)
