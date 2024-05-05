from fastapi import APIRouter, status

v1 = APIRouter(prefix="/v1")


@v1.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}
