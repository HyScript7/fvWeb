from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from ..config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from .models import models


async def database_setup(app: FastAPI):
    app.db = AsyncIOMotorClient(
        f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"
    )
    await init_beanie(database=app.db.get_database(DB_NAME), document_models=models)
