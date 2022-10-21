#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# Version: 2.0
# Author(s): HyScript7
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import Blueprint, session, request, redirect
from flask.wrappers import Response
from pymongo import MongoClient
from decouple import config

dbhost = config("DB_HOST", "db")
dbport = config("DB_PORT", "27017")
dbuser = config("DB_USER", "root")
dbpass = config("DB_PASS", "root")

db_Client = MongoClient(f"mongodb://{dbuser}:{dbpass}@{dbhost}:{dbport}",serverSelectionTimeoutMS=3000)

api = Blueprint("api", __name__)

@api.route("/")
async def test():
    return Response("OK", status=200)

@api.route("/db")
async def testdb():
    try:
        db_Client.server_info()
        connected = True
    except:
        connected = False
    return str(connected)

@api.route("/auth/login", methods=["GET", "POST"])
async def login():
    try:
        session["authSession"] # Will raise KeyError if no session is active
        return redirect(request.referrer, Response=Response("Already logged in", status=200))
    except KeyError:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
        else:
            username = request.args.get("username", "username")
            password = request.args.get("password", "password")
        session["authSession"] = [username, password]
        return redirect(request.referrer, Response=Response("Logged in", status=200))

@api.route("/auth/logout", methods=["GET", "POST"])
async def logout():
    try:
        session["authSession"] # Will raise KeyError if no session is active
        session.pop("authSession", None)
        return redirect(request.referrer, Response=Response("Logged out", status=200))
    except KeyError:
        return redirect(request.referrer, Response=Response("No Session", status=200))

@api.route("/auth/check", methods=["GET", "POST"])
async def check():
    try:
        sessionID = session["authSession"]
        return Response(str(sessionID), status=200)
    except KeyError:
        return Response("No Session", status=200)

# When calling the auth routes directly, you will get redirected here.
@api.route("/auth/None")
async def fallback():
    return redirect("/")
