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
from flask import render_template, request, url_for, send_file, session, redirect, Response
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


@web.route('/profile/<user>')
def profile(user=None):
    if user is None:
        try:
            user = session["authSession"][0]
        except:
           return redirect("/auth?login", Response=Response("Cannot display a blank profile, prompting login", status=400))
    #TODO: Verify the the profile exists
    #TODO: Get profile data from DB
    # Return content
    return render_template('home/profile.html', userid=user)


@web.route('/settings')
def settings():
    return render_template('home/settings.html')


@web.route("/favicon.ico")
async def favicon():
    return send_file("./static/img/favicon.ico")
