import sys
import os

import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from backend.core.database import init_db
from backend.routers import router

app = FastAPI(title="FlyCup")


@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(router, prefix="/api")


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
# 运行用： uvicorn backend.main:app --reload
