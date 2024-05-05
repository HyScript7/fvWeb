import uvicorn

if __name__ == "__main__":
    from .config import FASTAPI_ENV
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=FASTAPI_ENV.lower().startswith("dev"),
    )
