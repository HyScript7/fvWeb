from common.route_vars import css, js, navbar
from flask import Blueprint, render_template

web = Blueprint("admin", __name__)


@web.route("/")
async def root():
    return render_template(
        "admin/index.html", page="Admin", title="Admin", css=css, js=js, navbar=navbar
    )

