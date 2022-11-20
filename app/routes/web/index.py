#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# Version: 2.1
# Author(s): HyScript7
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import render_template, request, url_for
from routes.web import web, db_Client

async def getCards():
    r = []
    for i in db_Client["fvWeb"]["Activity"].find():
        r.append([i["title"], i["description"], i["avatar"], "Relative Time"])
    return r

navBarLinks = [
    ["Home", "/", False],
    ["Wiki", "/wiki", False],
    ["Forum", "/forum", False],
    ["fvWorld", "#", True],
    ["fvCards", "#", True]
    # linkName, Href, Disabled
]

@web.route("/")
async def home(): 
    cards = await getCards()
    return render_template("home.html", thisPage="Home",cards=cards, navBarLinks=navBarLinks) 

@web.route("/auth")
async def auth():
    error = request.args.get("error", 0)
    version = request.args.get("version", "none")
    size = request.args.get("size", 2)
    cards = await getCards()
    return render_template("auth.html", thisPage="Auth",cards=cards, navBarLinks=navBarLinks, error=error, version=version, size=size)

@web.route("/wiki")
async def wiki(): 
    cards = await getCards()
    return render_template("home.html", thisPage="Wiki",cards=cards, navBarLinks=navBarLinks) 

@web.route("/forum")
async def forum(): 
    cards = await getCards()
    return render_template("home.html", thisPage="Forum",cards=cards, navBarLinks=navBarLinks) 

@web.route("/favicon.ico")
async def favicon():
    return url_for("static", filename="/img/logo.png")
