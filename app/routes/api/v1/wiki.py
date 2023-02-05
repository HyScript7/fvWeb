import time

from flask import Response, redirect, request, session
from models import wiki

from . import api


async def parse_editor_content(content: str) -> list[str]:
    content = content.replace("\r", "").split("\n")
    for i, v in enumerate(content):
        if v[0:3] in ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6"] and v[len(v)-4:len(v)] in ["/h1>", "/h2>", "/h3>", "/h4>", "/h5>", "/h6>"]:
            content[i] = int(v[2])*"#" + " " + v[4:len(v)-5]
    return content


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
        tags=tags.replace(", ", ",").split(","),
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
