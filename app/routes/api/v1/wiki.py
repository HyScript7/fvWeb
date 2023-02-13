import time

from flask import Response, redirect, request, session
from models import wiki

from . import api


async def parse_editor_content(content: str) -> list[str]:
    content = content.replace("\r", "").split("\n")
    for i, v in enumerate(content):
        if v.startswith("<span") and v.endswith("</span>"):
            try:
                if (
                    content[i - 1].startswith("<h")
                    and int(content[i - 1][2]) in [1, 2, 3, 4, 5, 6]
                    and content[i + 1].startswith("</h")
                    and int(content[i + 1][3]) in [1, 2, 3, 4, 5, 6]
                ):
                    content[i - 1] += v + content[i + 1]
                    content.pop(i)
                    content.pop(i)
            except ValueError:
                continue
    return content


@api.route("/wiki/save", methods=["GET", "POST"])
async def article_create():
    try:
        session["signed_in"]
    except KeyError:
        session["signed_in"] = False
    if not session["signed_in"]:
        return redirect("/auth/login")
    if request.method == "POST":
        title = request.form.get("title", None)
        description = request.form.get("description", None)
        tags = request.form.get("tags", None)
        author = request.form.get("author", None)
        content = request.form.get("content", None)
    else:
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


@api.route("/wiki/save/<id>", methods=["GET", "POST"])
async def article_save(id):
    try:
        session["signed_in"]
    except KeyError:
        session["signed_in"] = False
    if not session["signed_in"]:
        return redirect("/auth/login")
    if request.method == "POST":
        title = request.form.get("title", None)
        description = request.form.get("description", None)
        tags = request.form.get("tags", None)
        author = request.form.get("author", None)
        content = request.form.get("content", None)
        created = int(request.form.get("created", round(time.time())))
    else:
        title = request.args.get("title", None)
        description = request.args.get("description", None)
        tags = request.args.get("tags", None)
        author = request.args.get("author", None)
        content = request.args.get("content", None)
        created = int(request.args.get("created", round(time.time())))
    if None in [title, description, tags, author, content, created]:
        return Response("Invalid Arguments", status=400)
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
