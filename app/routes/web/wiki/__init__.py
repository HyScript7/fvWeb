from common.route_vars import css, js, navbar
from flask import Blueprint, redirect, render_template, request, session
from models.users import get_user_by_id
from models import wiki

web = Blueprint("wiki", __name__)


@web.route("/")
async def root():
    articles = [["some-uuid", "Test Article", ["Some tag", "another tag"]]]
    return render_template(
        "wiki/index.html",
        page="Wiki",
        title="Wiki",
        css=css,
        js=js,
        navbar=navbar,
        wiki_rows=[
            [
                ["Testing", await wiki.find_articles(["Testing"])],
                ["My tag", await wiki.find_articles(["My tag"])],
            ],
            [
                ["Red", await wiki.find_articles(["Red"])],
                ["Green", await wiki.find_articles(["Green"])],
                ["Blue", await wiki.find_articles(["Blue"])],
            ],
            [
                ["Lonely", await wiki.find_articles(["Lonely"])],
            ]
        ],
    )


@web.route("/article/")
async def article_no_id():
    content = [
        [],
        [
            "# Error 400",
            "You must provide an article id: /wiki/article/ID",
            'Example: <a class="link-secondary-dark" href="/wiki/article/0">/wiki/article/0</a> (Note: This will return a 404 error, as there is no article with the ID 0)',
        ],
    ]
    return render_template(
        "wiki/article.html",
        page="Wiki",
        title="Wiki",
        css=css,
        js=js,
        navbar=navbar,
        content=content,
        id=0,
    )


@web.route("/article/<id>")
async def article(id: int):
    try:
        article: wiki.Article = await wiki.Article.pull(id)
        content = [article.table.simple, article.content]
        title = article.title
        id = article.id
    except NameError:
        content = [
            [],
            [
                "# Error 404",
                "The article ID you have entered has not been found in the database!",
            ],
        ]
        title = "404"
        id = 0
    return render_template(
        "wiki/article.html",
        page="Wiki",
        title="Wiki " + title,
        css=css,
        js=js,
        navbar=navbar,
        content=content,
        id=id,
    )


@web.route("/editor/")
async def editor_new():
    try:
        session["signed_in"]
    except KeyError:
        session["signed_in"] = False
    if not session["signed_in"]:
        return redirect("/auth/login")
    content = request.args.get("content", None)
    if not content is None:
        return render_template(
            "wiki/editor.html",
            page="Wiki",
            title="Wiki Editor",
            css=css + ["/static/css/quill.snow.css"],
            js=js + ["/static/js/quill.min.js", "/static/js/fvWikiEditor.js"],
            navbar=navbar,
            content=content.replace("\r", "").split("\n"),
        )
    return render_template(
        "wiki/editor.html",
        page="Wiki",
        title="Wiki Editor",
        css=css + ["/static/css/quill.snow.css"],
        js=js + ["/static/js/quill.min.js", "/static/js/fvWikiEditor.js"],
        navbar=navbar,
    )


@web.route("/editor/<id>")
async def editor_existing(id):
    try:
        session["signed_in"]
    except KeyError:
        session["signed_in"] = False
    if not session["signed_in"]:
        return redirect("/auth/login")
    try:
        article: wiki.Article = await wiki.Article.pull(id)
    except NameError:
        return redirect(f"/wiki/article/{id}")
    original_author = await get_user_by_id(article.author)
    return render_template(
        "wiki/editor.html",
        page="Wiki",
        title="Wiki Editor",
        css=css + ["/static/css/quill.snow.css"],
        js=js + ["/static/js/quill.min.js", "/static/js/fvWikiEditor.js"],
        navbar=navbar,
        content=article.content,
        id=article.id,
        article_title=article.title,
        author=[original_author.id, original_author.username],
        description=article.description,
        tags=article.tags,
        created=article.created,
    )
