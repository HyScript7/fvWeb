#    __      __        __   _     
#   / _|_   _\ \      / /__| |__  
#  | |_\ \ / /\ \ /\ / / _ \ '_ \ 
#  |  _|\ V /  \ V  V /  __/ |_) |
#  |_|   \_/    \_/\_/ \___|_.__/  
# 
# fvWeb
# License: MIT License
# For more information on copyright and licensing view the README.md and LICENSE.md files.
#
import asyncio
from datetime import timedelta

from common.configuration import (FLASK_DEBUG, FLASK_PORT, FLASK_SECRET,
                                  FLASK_SESSION_LIFETIME)
from flask import Flask
from flaskext.markdown import Markdown
from routes import routes
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)

app.wsgi_app = SassMiddleware(
    app.wsgi_app, {__name__: ("static/sass", "static/css", "static/css/")}
)

Markdown(app)

app.secret_key = FLASK_SECRET
app.permanent_session_lifetime = timedelta(minutes=FLASK_SESSION_LIFETIME)


for route, prefix in routes:
    app.register_blueprint(route, url_prefix=prefix)


async def main() -> None:
    if FLASK_DEBUG:
        app.run(host="0.0.0.0", port=FLASK_PORT, debug=FLASK_DEBUG)
        return
    serve(app, host="0.0.0.0", port=FLASK_PORT)
    return


if __name__ == "__main__":
    from sys import exit

    from waitress import serve

    asyncio.run(main())
    exit(0)
