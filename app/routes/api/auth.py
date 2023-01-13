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
import hashlib
import time

from flask import make_response, redirect, request, session
from flask.wrappers import Response
from routes.api import api, models, db_Client


def is_logged_in(s: session) -> bool | list:
    """Returns a boolean, whether the user is logged in or not

    Args:
        s (session): The session we are checking against

    Returns:
        bool: If the user isn't logged in (False)
        list: If the user is logged in [uuid, username]
    """
    try:
        return s["authSession"]
    except KeyError:
        return False


async def fetch_user(
    username: str | None = None, id: str | None = None
) -> None | models.User:
    """Returns the user object or none.

    Keyword arguments:
    argument -- description
    username -- The username of the user we are looking up
    id       -- The id of the user we are looking up
    Return: models.User if the user exists, None if the user doesn't exist.
    """

    if username is None and id is None:
        raise ValueError("fetch_user requires either a username or an id")
    filter = {"username": username} if id is None else {"uuid": id}
    try:
        return models.User.pull(filter)
    except KeyError:
        return None


def login_session(s: session, user: models.User) -> None:
    """Sets up the session with the provided user data

    Args:
        s (session): The session object from flask
        user (models.User): The user we logged in as
    """
    s["authSession"] = [user.id, user.username]


async def is_taken(username: str, email: str=None) -> bool:
    """Returns whether the username & email aren't taken

    Args:
        username (str): Username we are checking
        email (str): Email we are checking

    Returns:
        bool: Are the username & email free
    """
    u = db_Client["fvWeb"]["Accounts"].find_one({"username": username})
    if email is None:
        return not u is None
    e = db_Client["fvWeb"]["Accounts"].find_one({"email": email})
    return not (u is None or e is None)


def build_redirect(url: str, status: int, message: str) -> redirect:
    if url is None:
        url = "/"
    url.replace("?error", "?_error")
    return redirect(url, Response=Response(message, status=status))


@api.route("/auth/register", methods=["POST"])
async def auth_register():
    if is_logged_in(session):
        return build_redirect(request.referrer, 400, "Already Logged in")
    email = request.form["email"]
    if not email:
        return redirect(
            "/auth?register&error=1",
            Response=Response("No email address", status=400),
        )
    username = request.form["username"]
    if not username:
        return redirect(
            "/auth?register&error=1",
            Response=Response("No username", status=400),
        )
    if not request.form["password"]:
        return redirect(
            "/auth?register&error=1",
            Response=Response("No password", status=400),
        )
    password = hashlib.sha256(request.form["password"].encode("utf-8")).hexdigest()
    avatar_data = request.files["avatar"].stream.read()  # Avatar file
    if not len(avatar_data):
        avatar = None
    # Check if the username or email are taken.
    if await is_taken(username, email):
        return redirect(
            "/auth?register&error=3",
            Response=Response("Username or Email taken", status=400),
        )
    models.User.new(username, email, password, avatar)
    return redirect("/auth?login", Response=Response("Registered", status=200))


@api.route("/auth/login", methods=["POST"])
async def auth_login():
    if is_logged_in(session):
        return build_redirect(request.referrer, 400, "Already Logged In")
    username = request.form["username"]
    if not username:
        return redirect(
            "/auth?login&error=2",
            Response=Response("No username", status=400),
        )
    if not request.form["password"]:
        return redirect(
            "/auth?login&error=2",
            Response=Response("No password", status=400),
        )
    password = hashlib.sha256(request.form["password"].encode("utf-8")).hexdigest()
    user = await fetch_user(username, None)
    if user is None:
        return redirect(
            "/auth?login&error=2", Response=Response("Invalid Username", status=400)
        )
    if not password == user.password:
        return redirect(
            "/auth?login&error=2", Response=Response("Wrong Password", status=400)
        )
    # Set Session
    login_session(session, user)
    # Redirect
    return build_redirect(request.referrer, 200, "Logged In")


@api.route("/auth/logout", methods=["GET", "POST"])
async def auth_logout():
    if is_logged_in(session):
        session.pop("authSession", None)
        redirect_url = request.referrer
        if request.referrer is None:
            redirect_url = "/"
        redirect_url = redirect_url.replace("?error", "?_error")
        return redirect(redirect_url, Response=Response("Logged out", status=200))
    redirect_url = request.referrer
    if request.referrer is None:
        redirect_url = "/"
    redirect_url = redirect_url.replace("?error", "?_error")
    return redirect(redirect_url, Response=Response("No Session", status=200))


@api.route("/auth/check", methods=["GET", "POST"])
async def auth_check():
    logon = is_logged_in(session)
    return logon if logon else "Signed out"


@api.route("/cookiesAccepted")
async def cookies_accepted():
    redirect_url = request.referrer
    if request.referrer is None:
        redirect_url = "/"
    resp = make_response(
        redirect(redirect_url, Response=Response("Cookies Accepted", status=200))
    )
    resp.set_cookie("cookies", "True", expires=time.time() + 2628000)
    return resp
