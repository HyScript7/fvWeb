#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
import base64
import uuid

from models import db_Client

# TODO: Might be a good idea to store this in the database instead - Will be easier to implement with an Admin interface on the web it self later.
with open("./static/img/default_avatar.png", "rb") as defavt:
    defaultavatar = "data:image/png;base64," + base64.b64encode(defavt.read()).decode(
        "utf-8"
    )


def random_uuid() -> str:
    return uuid.uuid3(uuid.uuid1(), uuid.uuid4().hex).hex


class User:
    def __init__(self, id: str, username: str, password: str, email: str, avatar: str):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.avatar = avatar

    def dump(self) -> dict:
        return {
            "uuid": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "avatar": self.avatar,
        }

    def push(self) -> None:
        account = db_Client["fvWeb"]["Accounts"].find_one({"uuid": self.id})
        if account is None:
            db_Client["fvWeb"]["Accounts"].insert_one(self.dump())
            return
        account = db_Client["fvWeb"]["Accounts"].find_one_and_replace(
            {"uuid": self.id}, self.dump()
        )

    @classmethod
    def new(cls, username: str, email: str, password: str, avatar:bytes|None=None):
        if avatar is None:
            avatar = defaultavatar
        else:
            avatar = "data:image/png;base64," + base64.b64encode(avatar).decode()
        cls = cls(random_uuid(), username, password, email, avatar)
        cls.push()
        return cls

    @classmethod
    def pull(cls, filter: dict):
        account = db_Client["fvWeb"]["Accounts"].find_one(filter)
        if account is None:
            raise KeyError(f"No user was found using the filter '{filter}' !")
        return cls(
            account["uuid"],
            account["username"],
            account["password"],
            account["email"],
            account["avatar"],
        )
