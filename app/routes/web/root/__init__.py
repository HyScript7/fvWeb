from common.route_vars import css, js, navbar
from common.configuration import HOSTNAME
from flask import Blueprint, render_template, send_file, redirect

web = Blueprint("root", __name__)


@web.route("/")
async def root():
    return render_template(
        "root/index.html", page="Home", title="", css=css, js=js, navbar=navbar, hostname=HOSTNAME
    )

@web.route("/auth")
async def authentication_redirect():
    return redirect("/auth/login")


@web.route("/auth/<request>")
async def authentication(request: str):
    if request.lower() == "login":
        request = "login"
    elif request.lower() == "register":
        request = "register"
    else:
        request = "login"
    return render_template(
        "root/auth.html", page="Auth", title=request, css=css, js=js, navbar=navbar, menu=request
    )


@web.route("/favicon.ico")
async def favicon():
    return send_file("./static/img/favicon.ico")
