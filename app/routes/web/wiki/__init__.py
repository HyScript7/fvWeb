from common.route_vars import css, js, navbar
from flask import Blueprint, render_template

web = Blueprint("wiki", __name__)


@web.route("/")
async def root():
    return render_template(
        "wiki/index.html", page="Wiki", title="Wiki", css=css, js=js, navbar=navbar
    )
