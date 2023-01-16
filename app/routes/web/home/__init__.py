from common.route_vars import css, js, navbar
from flask import Blueprint, render_template

web = Blueprint("home", __name__)


@web.route("/")
async def root():
    return render_template(
        "home/index.html", page="Profile", title="Profile", css=css, js=js, navbar=navbar
    )
