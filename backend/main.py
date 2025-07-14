from fastapi import FastAPI
from backend.core.database import init_db
from backend.routers import router  # 注意这里导入的是 router，不是 foo

app = FastAPI(title="FlyCup")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router, prefix="/api")

# 运行用： uvicorn backend.main:app --reload
