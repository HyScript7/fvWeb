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
from flask import Blueprint, render_template, request, url_for
from pymongo import MongoClient
from decouple import config

dbhost = config("DB_HOST", "db")
dbport = config("DB_PORT", "27017")
dbuser = config("DB_USER", "root")
dbpass = config("DB_PASS", "root")

db_Client = MongoClient(f"mongodb://{dbuser}:{dbpass}@{dbhost}:{dbport}",serverSelectionTimeoutMS=3000)

web = Blueprint("web", __name__)

async def getUsers():
    r = [["Admin", "Currently displaying all registered users for debugging and development purposes.", url_for("static", filename="/img/logo.png"), "Relative Time"]]
    for i in db_Client["fvWeb"]["Accounts"].find():
        r.append([i["username"], i["email"], i["avatar"], "Relative Time"])
    return r

async def getCards():
    return await getUsers()

@web.route("/")
async def home(): 
    cards = await getCards()
    return render_template("home.html", cards=cards) 

@web.route("/auth")
async def auth():
    error = request.args.get("error", 0)
    version = request.args.get("version", "none")
    cards = await getCards()
    return render_template("auth.html", cards=cards, error=error, version=version)

@web.route("/wiki")
async def wiki(): 
    cards = await getCards()
    return render_template("home.html", cards=cards) 

@web.route("/forum")
async def forum(): 
    cards = await getCards()
    return render_template("home.html", cards=cards) 

@web.route("/dev")
async def dev():
    temp = request.args.get("template", "home")
    cards = await getCards()
    return render_template(f"{temp}.html", cards=cards) 

@web.route("/favicon.ico")
async def favicon():
    return url_for("static", filename="/img/logo.png")
