import asyncio

from common.configuration import (FVWEB_DATABASE, MONGO_URI, REDIS_HOST,
                                  REDIS_PASS, REDIS_PORT)
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

import redis

Redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, db=0)

Client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)


class Database:
    """Custom wrapper for PyMongo and Redis. Handles communication with MongoDB and caching using Redis"""

    def __init__(self, database: MongoClient, cache: redis.Redis):
        self.mongo = database
        self.redis = cache
        x = asyncio.run(self.verify())
        if not x:
            from sys import exit

            exit(1)

    async def verify(self) -> bool:
        """Verifies if we can communicate with the databases

        Returns:
            bool: True if we can, False if we failed to contact the database
        """
        for i in range(5):
            print(f"[{i+1}/5] Attempting to contact the database server")
            try:
                Client.server_info()
                print(f"[{i+1}/5] Mongo Connection succeeded")
                break
            except ServerSelectionTimeoutError:
                print(f"[{i+1}/5] Mongo Connection failed")
                if i == 4:
                    return False
            except KeyboardInterrupt:
                print(f"[{i+1}/5] Mongo verification override")
                break

        for i in range(5):
            print(f"[{i+1}/5] Attempting to contact the caching server")
            try:
                Redis.ping()
                print(f"[{i+1}/5] Redis Connection succeeded")
                break
            except (redis.exceptions.ConnectionError, ConnectionRefusedError):
                print(f"[{i+1}/5] Redis Connection failed")
                if i == 4:
                    return False
            except KeyboardInterrupt:
                print(f"[{i+1}/5] Redis verification override")
                break
        return True


Database = Database(Client, Redis)
