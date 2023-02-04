from flask import Response, request, session, redirect
from models import users

from . import api


async def sign_in(session: session, User: users.User):
    session["signed_in"] = True
    session["username"] = User.username
    session["email"] = User.email
    session["id"] = User.id


async def sign_out(session: session):
    session["signed_in"] = False
    for i in ["username", "email", "id"]:
        session.pop(i)


@api.route("/auth/login", methods=["POST"])
async def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if None in [
        username,
        password,
        None if not (len(username) or len(password)) else True,
    ]:
        return Response("Invalid Arguments", status=400)
    User = await users.User.login(await users.User.pull(username), username, await users.hash_password(password))
    if User is None:
        return redirect("/auth/login?error=1", Response=Response("Invalid Credentials or User does not exist", status=400))
    await sign_in(session, User)
    return redirect("/", Response=Response("Signed in!", status=200))


@api.route("/auth/register", methods=["POST"])
async def register():
    email = request.form.get("email", None)
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    terms = request.form.get("termsofservice", False)
    privacy = request.form.get("privacypolicy", False)
    if None in [
        email,
        username,
        password,
        terms,
        privacy,
        None if not (len(username) or len(password) or len(email)) else True,
    ]:
        return Response("Invalid Arguments", status=400)
    if not terms or not privacy:
        return redirect("/auth/register?error=2", Response=Response("Terms or Privacy Not Accepted", status=400))
    User = await users.User.register(username, await users.hash_password(password), email)
    if User is None:
        return redirect("/auth/register?error=3", Response=Response("Username or Email already registered!", status=400))
    await sign_in(session, User)
    return redirect("/", Response=Response("Registered!", status=200))


@api.route("/auth/logout", methods=["GET", "POST"])
async def logout():
    if not session["signed_in"]:
        return Response("No session found", status=401)
    await sign_out(session)
    return redirect("/", Response=Response("Signed out!", status=200))
