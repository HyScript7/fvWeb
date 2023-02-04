import uuid


async def new_uuid() -> str:
    return str(uuid.uuid3(uuid.uuid1(), uuid.uuid4().hex).hex)