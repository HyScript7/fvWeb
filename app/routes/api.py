from flask import Blueprint
from flask.wrappers import Response 

api = Blueprint("api", __name__)

@api.route("/")
def test():
    return Response("OK", status=200)
