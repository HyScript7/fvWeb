from common.configuration import FVWEB_COLLECTION_ARTICLES, FVWEB_DATABASE
from common.ids import new_uuid
from common.wiki import contentTable

from . import Client
from .users import get_user_by_id

articles_db = Client()[FVWEB_DATABASE][FVWEB_COLLECTION_ARTICLES]


class Article:
    def __init__(self, document: dict) -> None:
        self.oid = document["_id"]
        self.id: str = document["id"]
        self.title: str = document["title"]
        self.description: str = document["description"]
        self.tags: list[str] = document["tags"]
        self.author: str = document["author"]
        self.created: int = document["created"]
        self.content: list[str] = document["content"]
        self.table: contentTable = contentTable(self.content)

    async def push(self):
        articles_db.find_one_and_replace({"_id": self.oid}, self.dump(self))

    @staticmethod
    def dump(article) -> dict:
        return {
            "_id": article.oid,
            "id": article.id,
            "title": article.title,
            "description": article.description,
            "tags": article.tags,
            "author": article.author,
            "created": article.created,
            "content": article.content,
        }

    @classmethod
    async def pull(cls, id: str):
        doc = articles_db.find_one({"id": id})
        if doc is None:
            raise NameError(f"An article with the ID '{id}' does not exist!")
        return cls(doc)

    @classmethod
    async def new(
        cls,
        title: str,
        description: str,
        tags: list[str],
        author: str,
        created: int,
        content: list[str],
    ):
        id = await new_uuid()
        articles_db.insert_one(
            {
                "id": id,
                "title": title,
                "description": description,
                "tags": tags,
                "author": author,
                "created": created,
                "content": content,
            }
        )
        return await cls.pull(id)


async def find_articles(tags: list[str]) -> list[Article]:
    results: list[Article] = []
    for article in articles_db.find({"tags": {"$in": tags}}):
        if article is None:
            continue
        article = Article(article)
        results.append(
            [
                article.id,
                article.title,
                [article.author, (await get_user_by_id(article.author)).username],
                article.tags,
            ]
        )
    return results
