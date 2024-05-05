import pytest_asyncio
from app import app
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

ROOT_ROUTE: str = "/api"


@pytest_asyncio.fixture
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as client:
            yield client
