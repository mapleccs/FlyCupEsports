
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, Request
from backend.core.database import init_db
from backend.routers import v1_router

app = FastAPI(title="FlyCup")


# --- 添加这个调试中间件 ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"收到请求: {request.method} {request.url}")
    print(f"请求头: {request.headers}")
    response = await call_next(request)
    return response

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://192.168.1.3:8080",
        "http://127.0.0.1:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api")

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
# 运行用： uvicorn backend.main:app --reload
