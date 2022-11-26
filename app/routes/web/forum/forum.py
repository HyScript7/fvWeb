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
from routes.web.forum import web

@web.route("/")
async def index(): 
    cards = await getCards()
    return render_template("forum/index.html", thisPage="Home",cards=cards, navBarLinks=navBarLinks) 
