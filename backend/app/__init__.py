from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import database_setup
from .routers import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database_setup(app)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api)
