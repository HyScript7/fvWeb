#  ______   __   __   __     __     ______     ______
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/
#
# fvWeb
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import render_template, request, url_for, send_file
from routes.web import getCards, navBarLinks
from routes.web.home import web


@web.route("/")
async def home():
    cards = await getCards()
    return render_template(
        "home.html", thisPage="Home", cards=cards, navBarLinks=navBarLinks
    )


@web.route("/auth")
async def auth():
    error = request.args.get("error", 0)
    cards = await getCards()
    authtype = (
        "register"
        if not request.args.get("register", True)
        else "login"
        if not request.args.get("login", True)
        else "selection"
    )
    return render_template(
        "auth.html",
        thisPage="Auth",
        cards=cards,
        navBarLinks=navBarLinks,
        error=error,
        authtype=authtype,
    )


@web.route("/favicon.ico")
async def favicon():
    return send_file("./static/img/favicon.ico")
