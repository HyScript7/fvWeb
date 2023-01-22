import hashlib
import uuid

from common.configuration import FVWEB_COLLECTION_USERS, FVWEB_DATABASE, PASSWORD_SALT

from . import Client

users_db = Client()[FVWEB_DATABASE][FVWEB_COLLECTION_USERS]


async def new_uuid() -> str:
    return str(uuid.uuid3(uuid.uuid1(), uuid.uuid4().hex).hex)


async def hash_password(password: str) -> str:
    return hashlib.sha256(f"{password}{PASSWORD_SALT}".encode()).hexdigest()


class User:
    def __init__(self, doc: dict):
        self.oid = doc["_id"]
        self.id = doc["id"]
        self.username = doc["username"]
        self.password = doc["password"]
        self.email = doc["email"]

    def dump(self) -> dict:
        """Returns the object as a document

        Returns:
            dict: The user document
        """
        return {
            "_id": self.oid,
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }

    @classmethod
    async def register(cls, username: str, password: str, email: str):
        """Registers a new user if possible

        Args:
            username (str): The username of the new user
            password (str): The password for the new user
            email (str): The email of the new user

        Returns:
            None: Registration failed
            User: Registered successfully
        """
        if (await is_taken_email(email)) or (await is_taken_username(username)):
            return None
        uuid = await new_uuid()
        document = {
            "id": uuid,
            "username": username,
            "password": password,
            "email": email,
        }
        result = users_db.insert_one(document)
        document.update({"_id": result.inserted_id})
        return cls(document)

    @staticmethod
    async def login(user, username: str, password: str):
        """Login as an existing user
        Use User.pull or User.dump to get the user document

        Args:
            username (str): The username of the user
            password (str): The password of the user

        Returns:
            User: Logged in successfully
            None: Incorrect credentials or non existent user
        """
        if user.password == password:
            return user
        return None

    @staticmethod
    async def pull(username: str | None=None, id: str | None=None):
        """Pulls a user document from the database
        Use User.login to get the user object

        Args:
            username (str): The username of the user

        Returns:
            dict: The document of the user
            None: No user with that username exists
        """
        if not id is None:
            user = await get_user_by_id(id)
        elif not username is None:
            user = await get_user_by_username(username)
        else:
            raise ValueError("You must provide either a username or an id!")
        return user


async def get_user(filter: dict) -> None | User:
    query = users_db.find_one(filter)
    if query is None:
        return None
    return User(query)


async def get_user_by_id(id: str) -> None | User:
    return await get_user({"id": id})


async def get_user_by_username(username: str) -> None | User:
    return await get_user({"username": username})


async def get_user_by_email(email: str) -> None | User:
    return await get_user({"email": email})


async def is_taken_username(username: str) -> bool:
    return not await get_user({"username": username}) is None


async def is_taken_email(email: str) -> bool:
    return not await get_user({"email": email}) is None
