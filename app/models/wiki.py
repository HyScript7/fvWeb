from common.configuration import FVWEB_COLLECTION_ARTICLES, FVWEB_DATABASE
from common.wiki import contentTable
from common.ids import new_uuid

from . import Client

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
        # TODO: Replace this with production code
        return cls(
            {
                "_id": "some-oid",
                "id": "some-id",
                "title": "Article Title",
                "description": "Article Description",
                "tags": ["Category 1", "Category 2"],
                "author": "Some-UUID",
                "created": 1670702154,
                "edited": 1670788550,
                "content": [
                    "# Title",
                    "Hello! This is the totally loaded from database and not hardcoded article content used for testing.",
                    "## Sub Title 1",
                    "This is some text under the first sub title",
                    "### Sub Sub Title 1",
                    "Here is some more text under a sub sub title",
                    "### Sub Sub Title 2",
                    "Here is some markdown text and an HTML link",
                    "<a href='/' class='link-secondary-dark text-decoration-none'>This link leads to Home</a>",
                    "## Sub Title 2",
                    "### Sub Sub Title 1",
                    "I don't know what to write anymore...",
                    "### Sub Sub Title 2",
                    "<hr>",
                    "This is the last sentence.",
                ],
            }
        )
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
                "content": content,
            }
        )
        return await cls.pull(id)
