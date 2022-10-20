#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# Version: 1.15
# Author(s): HyScript7
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import Blueprint, render_template, request, url_for
from flask.wrappers import Response 

web = Blueprint("web", __name__)

@web.route("/")
def home(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("index.html", cards=cards) 

@web.route("/auth")
def auth():
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("auth.html", cards=cards) 

@web.route("/wiki")
def wiki(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("index.html", cards=cards) 

@web.route("/forum")
def forum(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("index.html", cards=cards) 

@web.route("/dev")
def dev():
    temp = request.args.get("template", "index")
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template(f"{temp}.html", cards=cards) 

@web.route("/favicon.ico")
def favicon():
    return url_for("static", filename="/img/logo.png")
