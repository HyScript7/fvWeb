from common.configuration import (FVWEB_COLLECTION_ARTICLES,
                                  FVWEB_COLLECTION_DISCUSSIONS,
                                  FVWEB_COLLECTION_USERS, FVWEB_DATABASE,
                                  MONGO_URI, REDIS_HOST, REDIS_PASS,
                                  REDIS_PORT)
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

import redis

Redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, db=0)

for i in range(5):
    print(f"[{i+1}/5] Attempting to contact the caching server")
    try:
        Redis.ping()
        print(f"[{i+1}/5] Connection succeeded")
        break
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        print(f"[{i+1}/5] Connection failed")
        if i == 4:
            from sys import exit

            exit(1)


Client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

for i in range(5):
    print(f"[{i+1}/5] Attempting to contact the database server")
    try:
        Client.server_info()
        print(f"[{i+1}/5] Connection succeeded")
        break
    except ServerSelectionTimeoutError:
        print(f"[{i+1}/5] Connection failed")
        if i == 4:
            from sys import exit

            exit(1)

Database = Client[FVWEB_DATABASE]
Users = Database[FVWEB_COLLECTION_USERS]
Articles = Database[FVWEB_COLLECTION_ARTICLES]
Discussions = Database[FVWEB_COLLECTION_DISCUSSIONS]
