#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# Version: 2.2
# Author(s): HyScript7
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import render_template, request, url_for
from routes.web import getCards, navBarLinks
from routes.web.wiki import web

@web.route("/")
async def index(): 
    cards = await getCards()
    return render_template("wiki/index.html", thisPage="Home",cards=cards, navBarLinks=navBarLinks) 

@web.route("/article/<id>")
async def article(id):
    cards = await getCards()
    return render_template("wiki/article.html", id=id, thisPage="Home",cards=cards, navBarLinks=navBarLinks) 
