from flask import Response, request, session
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
        return Response("Invalid Credentials or User does not exist", status=400)
    await sign_in(session, User)
    return Response("Signed in!", status=200)


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
        return Response("Terms or Privacy Not Accepted", status=400)
    User = await users.User.register(username, await users.hash_password(password), email)
    if User is None:
        return Response("Username or Email already registered!", status=400)
    await sign_in(session, User)
    return Response("Registered!", status=200)


@api.route("/auth/logout", methods=["GET", "POST"])
async def logout():
    if not session["signed_in"]:
        return Response("No session found", status=401)
    await sign_out(session)
    return Response("Signed out!", status=200)


@api.route("/test")
async def test():
    results = {}
    try:
        result = await users.get_user_by_email("hyscript7@gmail.com")
        results["query_email"] = f"Returned: {result}"
    except Exception as e:
        results["query_email"] = str(e)
    try:
        result = await users.get_user_by_username("HyScript7")
        results["query_username"] = f"Returned: {result}"
    except Exception as e:
        results["query_username"] = str(e)
    try:
        result = await users.get_user_by_id(0)
        results["query_id"] = f"Returned: {result}"
    except Exception as e:
        results["query_id"] = str(e)
    try:
        result = await users.is_taken_email("hyscript7@gmail.com")
        results["query_taken_email"] = f"Returned: {result}"
    except Exception as e:
        results["query_taken_email"] = str(e)
    try:
        result = await users.is_taken_username("HyScript7")
        results["query_taken_username"] = f"Returned: {result}"
    except Exception as e:
        results["query_taken_username"] = str(e)
    document = "<html><head><title>Fusionverse API - Testing</title></head><body><ul>"
    for i in results:
        document += f"<li>{i} | {results[i]}</li>"
    document += "</ul></body></html>"
    return document
