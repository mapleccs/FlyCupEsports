from fastapi import APIRouter
from backend.routers.v1 import user, role, rank, position, player, team, region, refresh_auth

# 其他模块你也可以继续加

router = APIRouter(prefix="/v1")

# 聚合所有子模块的router
router.include_router(user.router)
router.include_router(role.router)
router.include_router(position.router)
router.include_router(player.router)
router.include_router(rank.router)
router.include_router(team.router)
router.include_router(region.router)
router.include_router(refresh_auth.router)
