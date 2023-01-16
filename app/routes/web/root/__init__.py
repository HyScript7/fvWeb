from common.route_vars import css, js, navbar
from common.configuration import HOSTNAME
from flask import Blueprint, render_template

web = Blueprint("root", __name__)


@web.route("/")
async def root():
    return render_template(
        "root/index.html", page="Home", title="", css=css, js=js, navbar=navbar, hostname=HOSTNAME
    )
