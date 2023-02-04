import time

from flask import Response, redirect, request, session
from models import wiki

from . import api


async def parse_editor_content(content: str) -> list[str]:
    return content.replace("\r", "").split("\n")


@api.route("/wiki/save")
async def article_create():
    title = request.args.get("title", None)
    description = request.args.get("description", None)
    tags = request.args.get("tags", None)
    author = request.args.get("author", None)
    content = request.args.get("content", None)
    created = round(time.time())
    if None in [title, description, tags, author, content]:
        return Response("Invalid Arguments", status=400)
    # TODO: Check if the user has permissions to create articles
    content = await parse_editor_content(content)
    Article = await wiki.Article.new(
        title=title,
        description=description,
        tags=tags,
        author=author,
        content=content,
        created=created,
    )
    return redirect(
        f"/wiki/article/{Article.id}", Response=Response("Article created!", status=200)
    )


@api.route("/wiki/save/<id>")
async def article_save(id):
    title = request.args.get("title", None)
    description = request.args.get("description", None)
    tags = request.args.get("tags", None)
    author = request.args.get("author", None)
    content = request.args.get("content", None)
    created = int(request.args.get("created", round(time.time())))
    if None in [title, description, tags, author, content, created]:
        return Response("Invalid Arguments!", status=400)
    try:
        Article = await wiki.Article.pull(id)
    except NameError:
        return redirect(
            f"/wiki/article/{id}",
            Response=Response("Article with this ID does not exist!", status=400),
        )
    # TODO: Check if the user has permissions to overwrite this article
    Article.title = title
    Article.description = description
    Article.tags = tags.replace(", ", ",").split(",")
    Article.author = author
    Article.content = await parse_editor_content(content)
    Article.created = created
    await Article.push()
    return redirect(
        f"/wiki/article/{Article.id}", Response=Response("Article saved!", status=200)
    )
