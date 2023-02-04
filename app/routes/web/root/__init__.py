from common.configuration import HOSTNAME
from common.route_vars import css, js, navbar
from flask import Blueprint, redirect, render_template, request, send_file

web = Blueprint("root", __name__)


@web.route("/")
async def root():
    return render_template(
        "root/index.html",
        page="Home",
        title="",
        css=css,
        js=js,
        navbar=navbar,
        hostname=HOSTNAME,
    )


@web.route("/auth")
async def authentication_redirect():
    return redirect("/auth/login")


@web.route("/auth/<action>")
async def authentication(action: str):
    error = request.args.get("error")
    if error is None:
        error = 0
    else:
        error = int(error)
    if action.lower() == "login":
        action = "login"
    elif action.lower() == "register":
        action = "register"
    else:
        action = "login"
    return render_template(
        "root/auth.html",
        page="Auth",
        title=action,
        css=css,
        js=js,
        navbar=navbar,
        menu=action,
        error=error,
    )


@web.route("/favicon.ico")
async def favicon():
    return send_file("./static/img/favicon.ico")
