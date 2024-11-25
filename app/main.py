from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routers import tasks
from .providers.db.engine import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
