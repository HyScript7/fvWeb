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
import asyncio
from flask import Flask
from flaskext.markdown import Markdown
from decouple import config
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from sassutils.wsgi import SassMiddleware
from datetime import timedelta
from routes.api import api
from routes.web import web

# Database Env Variables
dbhost = config("DB_HOST", "db")
dbport = config("DB_PORT", "27017")
dbuser = config("DB_USER", "root")
dbpass = config("DB_PASS", "root")

db_Client = MongoClient(f"mongodb://{dbuser}:{dbpass}@{dbhost}:{dbport}",serverSelectionTimeoutMS=3000)

# Define application
app = Flask(__name__)

# SASS Compilation
app.wsgi_app = SassMiddleware(app.wsgi_app, {__name__: ("static/sass", "static/css", "static/css/")})

# Markdown Support
Markdown(app)

# Setup Session
app.secret_key = str(config("FVWEB_SESSION_SECRET", "fvWebS3CR37")).strip()
app.permanent_session_lifetime = timedelta(minutes=int(config("FVWEB_SESSION_LIFETIME", 15)))

# Register routes
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(web)

# Define Main Function
async def main() -> None:
    FLASK_DEBUG = str(config('FLASK_DEBUG', "false")).lower() == "true"
    FLASK_PORT = int(config('FLASK_PORT', "8080"))
    if FLASK_DEBUG:
        app.run(host='0.0.0.0', port=FLASK_PORT, debug=FLASK_DEBUG)
        return
    for i in range(5):
        try:
            db_Client.server_info()
            print(f"[{i+1}/5] MongoDB connection verified")
        except ServerSelectionTimeoutError:
            print(f"[{i+1}/5] MongoDB connection timed out")
            if i == 2:
                print("Quitting: Application isn't in debug mode, but the database cannot be contacted!")
                return
    serve(app, host="0.0.0.0", port=FLASK_PORT)
    return

# Launch server
if __name__ == '__main__':
    from sys import exit
    from waitress import serve
    asyncio.run(main())
    exit(0)
