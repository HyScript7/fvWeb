from common.configuration import FVWEB_COLLECTION_USERS, FVWEB_DATABASE

from . import Client

users_db = Client()[FVWEB_DATABASE][FVWEB_COLLECTION_USERS]


class User:
    def __init__(self):
        pass

    def dump(self) -> dict:
        raise NotImplementedError

    @classmethod
    def register(cls, username: str, password: str, email: str):
        raise NotImplementedError

    @classmethod
    def login(cls, username: str, password: str):
        raise NotImplementedError
