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
from flask import render_template, request, url_for
from routes.web import getCards, navBarLinks
from routes.web.wiki import web


async def getArticle(id):
    return {
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
            "<a href='/' class='link-secondary text-decoration-none'>This link leads to Home</a>",
            "## Sub Title 2",
            "### Sub Sub Title 1",
            "I don't know what to write anymore...",
            "### Sub Sub Title 2",
            "<hr>",
            "This is the last sentence."
        ],
    }

class contentTable:
    def __init__(self, content: list):
        self.table = self.parse(content)
        self.simple = self.simpleParse(self.table)
        pass
    def parse(self, content: list) -> dict:
        titles = {}
        path = []
        # eg:. ["# Title 1", "## Sub Title 1", "### Sub Sub Title 1"]
        for i in content:
            if not (i.startswith("#") and i.replace("#", "").startswith(" ")):
                continue
            # Modify path if necessary
            level = i.split(" ")[0].count("#")
            indentLevel = len(path)
            if indentLevel >= level:
                path = path[0 : level - 1]
                path.append(i)
            elif indentLevel < level:
                path.append(i)
            # Add path to corresponding title
            current = titles
            lp = path[0 : len(path) - 1]
            for y in lp:
                current = current[y]
            current[i] = {}
        return titles
    def simpleParse(self, table):
        """
        TODO: Make sure the first element in the list (i) is the prefix (Eg: 1.1.1 or 1.2.2 or 2.1.1)
        TODO: All the necessary changes should be done within this function, as we already have all the information we need from the parse function in the table dict. All that has to be done is keeping track.
        """
        # This function makes my life easier looping through the thing in the template
        titles = []
        for i, n in enumerate(table):
            titles.append([i, n])
            if len(table[n]):
                titles += self.simpleParse(table[n])
        return titles

@web.route("/")
async def index():
    cards = await getCards()
    return render_template(
        "wiki/index.html", thisPage="Wiki", cards=cards, navBarLinks=navBarLinks
    )


@web.route("/article/<id>")
async def article(id):
    cards = await getCards()
    content = await getArticle(id)
    content = content["content"]
    return render_template(
        "wiki/article.html",
        id=id,
        thisPage="Wiki",
        cards=cards,
        navBarLinks=navBarLinks,
        content=[contentTable(content).simple, content],
    )
