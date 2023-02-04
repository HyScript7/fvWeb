from common.route_vars import css, js, navbar
from models.wiki import Article
from flask import Blueprint, render_template

web = Blueprint("wiki", __name__)


@web.route("/")
async def root():
    return render_template(
        "wiki/index.html", page="Wiki", title="Wiki", css=css, js=js, navbar=navbar
    )

@web.route("/article/")
async def article_no_id():
    content = [[], ["# Error 400", "You must provide an article id: /wiki/article/ID", "Example: <a class=\"link-secondary-dark\" href=\"/wiki/article/0\">/wiki/article/0</a> (Note: This will return a 404 error, as there is no article with the ID 0)"]]
    return render_template(
        "wiki/article.html", page="Wiki", title="Wiki", css=css, js=js, navbar=navbar, content=content, id=0
    )


@web.route("/article/<id>")
async def article(id: int):
    try:
        article: Article = await Article.pull(id)
        content = [article.table.simple, article.content]
        id = article.id
    except NameError:
        content = [[], ["# Error 404", "The article ID you have entered has not been found in the database!"]]
        id = 0
    return render_template(
        "wiki/article.html", page="Wiki", title="Wiki", css=css, js=js, navbar=navbar, content=content, id=id
    )
