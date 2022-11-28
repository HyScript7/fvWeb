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
from flask import render_template, request, url_for
from routes.web import getCards, navBarLinks
from routes.web.wiki import web

@web.route("/")
async def index(): 
    cards = await getCards()
    return render_template("wiki/index.html", thisPage="Wiki",cards=cards, navBarLinks=navBarLinks) 

@web.route("/article/<id>")
async def article(id):
    cards = await getCards()
    content = []
    return render_template("wiki/article.html", id=id, thisPage="Wiki",cards=cards, navBarLinks=navBarLinks, content=content) 
