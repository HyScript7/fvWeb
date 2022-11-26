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
import uuid
import hashlib
import base64
from routes.api import api, db_Client
from flask import session, request, redirect
from flask.wrappers import Response

#TODO: Might be a good idea to store this in the database instead - Will be easier to implement with an Admin interface on the web it self later.
with open("./static/img/default_avatar.png", "rb") as defavt:
    defaultavatar = "data:image/png;base64," + base64.b64encode(defavt.read()).decode("utf-8")

async def isTaken(username=None, email=None) -> bool:
    queryUsername = db_Client["fvWeb"]["Accounts"].find_one({"username": username})
    if queryUsername and not username is None:
        return True
    queryEmail = db_Client["fvWeb"]["Accounts"].find_one({"email": email})
    if queryEmail and not email is None:
        return True
    return False

async def getUser(uuid: str) -> dict:
    query = db_Client["fvWeb"]["Accounts"].find_one({"uuid": uuid})
    return query

async def getUUID(username: str) -> str:
    query = db_Client["fvWeb"]["Accounts"].find_one({"username": username})
    return query["uuid"]

async def checkPassword(uuid: str, password: str) -> bool:
    query = db_Client["fvWeb"]["Accounts"].find_one({"uuid": uuid})
    return query["password"] == password

@api.route("/auth/register", methods=["POST"])
async def auth_register():
    try:
        session["authSession"] # Will raise KeyError if no session is active, meaning the line below will not get executed.
        redirect_url = request.referrer
        if request.referrer is None:
            redirect_url = "/"
        return redirect(redirect_url, Response=Response("Already logged in", status=400))
    except KeyError:
        email = request.form["email"]
        username = request.form["username"]
        password = hashlib.sha256(request.form["password"].encode("utf-8")).hexdigest()
        avatar = request.files["avatar"] # Avatar file
        avatar_data = avatar.stream.read()
        if not len(avatar_data):
            avatar = defaultavatar
        else:
            avatar = "data:image/png;base64," + base64.b64encode(avatar_data).decode()
        # Check if the username or email are taken.
        if await isTaken(username, email):
            return redirect("/auth?error=3", Response=Response("Username or Email already taken", status=400))
        UUID = uuid.uuid3(uuid.uuid1(), uuid.uuid4().hex).hex
        db_Client["fvWeb"]["Accounts"].insert_one({"uuid": UUID, "email": email, "username": username, "password": password, "avatar": avatar})
        return redirect("/auth", Response=Response("Successfully Registered", status=200))

@api.route("/auth/login", methods=["POST"])
async def auth_login():
    try:
        session["authSession"] # Will raise KeyError if no session is active, meaning the line below will not get executed.
        redirect_url = request.referrer
        if request.referrer is None:
            redirect_url = "/"
        return redirect(redirect_url, Response=Response("Already logged in", status=200))
    except KeyError:
        username = request.form["username"]
        password = hashlib.sha256(request.form["password"].encode("utf-8")).hexdigest()
        if not await isTaken(username):
            return redirect("/auth?error=2", Response=Response("Invalid Username", status=400))
        uuid = await getUUID(username)
        if not await checkPassword(uuid, password):
            return redirect("/auth?error=2", Response=Response("Invalid Username", status=400))
        # Set Session
        session["authSession"] = [uuid, username]
        # Redirect
        redirect_url = request.referrer
        if request.referrer is None:
            redirect_url = "/"
        return redirect(redirect_url, Response=Response("Logged in", status=200))

@api.route("/auth/logout", methods=["GET", "POST"])
async def auth_logout():
    try:
        session["authSession"] # Will raise KeyError if no session is active, meaning the line below will not get executed.
        session.pop("authSession", None)
        redirect_url = request.referrer
        if request.referrer is None:
            redirect_url = "/"
        redirect_url.replace("error", "errorprev")
        return redirect(redirect_url, Response=Response("Logged out", status=200))
    except KeyError:
        redirect_url = request.referrer
        if request.referrer is None:
            redirect_url = "/"
        redirect_url.replace("error", "errorprev")
        return redirect(redirect_url, Response=Response("No Session", status=200))

@api.route("/auth/check", methods=["GET", "POST"])
async def auth_check():
    try:
        sessionID = session["authSession"]
        return Response(str(sessionID), status=200)
    except KeyError:
        return Response("No Session", status=200)
