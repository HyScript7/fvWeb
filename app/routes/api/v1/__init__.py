from flask import Blueprint, Response

api = Blueprint("api", __name__)


@api.route("/")
async def root():
    return Response("OK!", status=200)

from .authentication import *
from .wiki import *
