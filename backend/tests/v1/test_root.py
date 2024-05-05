import pytest
from fastapi import status

from .. import client
from . import V1_ROUTE


@pytest.mark.asyncio
async def test_root(client):
    response = await client.get(V1_ROUTE + "/")
    assert response.status_code == status.HTTP_200_OK
