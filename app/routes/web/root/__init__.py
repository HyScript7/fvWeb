from common.route_vars import css, js, navbar
from common.configuration import HOSTNAME
from flask import Blueprint, render_template, send_file

web = Blueprint("root", __name__)


@web.route("/")
async def root():
    return render_template(
        "root/index.html", page="Home", title="", css=css, js=js, navbar=navbar, hostname=HOSTNAME
    )


@web.route("/favicon.ico")
async def favicon():
    return send_file("./static/img/favicon.ico")
