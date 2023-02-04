from common.route_vars import css, js, navbar
from flask import Blueprint, redirect, render_template, request
from models.users import get_user_by_id
from models.wiki import Article

web = Blueprint("wiki", __name__)


@web.route("/")
async def root():
    return render_template(
        "wiki/index.html", page="Wiki", title="Wiki", css=css, js=js, navbar=navbar
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
        article: Article = await Article.pull(id)
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
        article: Article = await Article.pull(id)
    except NameError:
        return redirect(f"/wiki/article/{id}")
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
        author=[article.author, await get_user_by_id(article.author)],
        description=article.description,
        tags=article.tags,
        created=article.created,
    )
