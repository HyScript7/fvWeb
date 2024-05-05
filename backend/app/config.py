import secrets
import os

import dotenv

dotenv.load_dotenv(".env")

APP_VERSION = "0.1.0"

FASTAPI_ENV = os.getenv("FASTAPI_ENV") or "prod"
DB_HOST = os.getenv("DB_HOST") or "mongo"
DB_PORT = os.getenv("DB_PORT") or 27017
DB_USER = os.getenv("DB_USER") or "fvweb"
DB_PASSWORD = os.getenv("DB_PASSWORD") or "password"
DB_NAME = os.getenv("DB_NAME") or "fvweb"
CACHE_HOST = os.getenv("CACHE_HOST") or "memcached"
CACHE_PORT = os.getenv("CACHE_PORT") or 11211

# TODO: Sync this with other instances at runtime
JWT_SECRET: str = secrets.token_hex(32)
