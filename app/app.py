#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# Version: 1.15
# Author(s): HyScript7
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#

from flask import Flask, session
from flaskext.markdown import Markdown
from decouple import config
from pymongo import MongoClient
from sassutils.wsgi import SassMiddleware
from datetime import timedelta
from routes.api import api
from routes.web import web

# Database Env Variables
dbhost = config("DB_HOST", "db").strip()  # type: ignore
dbport = config("DB_PORT", "27017").strip()  # type: ignore
dbuser = config("DB_USER", "root").strip()  # type: ignore
dbpass = config("DB_PASS", "root").strip()  # type: ignore

# TODO: Move db connection and testing into functions

dbConnectionTested = True

if not dbConnectionTested:
    Client = MongoClient(f"mongodb://{dbuser}:{dbpass}@{dbhost}:{dbport}",serverSelectionTimeoutMS=5000)
    Database = Client["Fusionverse"]
    Accounts = Database["Accounts"]
    for i in range(3):
        print(f"[{i+1}/3] Attempting to connect to MongoDB")
        try:
            Client.server_info()
            print(f"[{i+1}/3] Connection successful!")
            break
        except KeyboardInterrupt:
            print(f"[{i+1}/3] Verification skipped by user input")
            break
        except Exception:
            print(f"[{i+1}/3] Connection failed!")
    dbConnectionTested = True

# Define application
app = Flask(__name__)

# SASS Compilation
app.wsgi_app = SassMiddleware(app.wsgi_app, {__name__: ("static/sass", "static/css", "static/css/")})

# Markdown Support
Markdown(app)

# Setup Session
session_lifetime = int(config("FVWEB_SESSION_LIFETIME", 15))

app.secret_key = str(config("FVWEB_SESSION_SECRET", "fvWebS3CR37")).strip()
app.permanent_session_lifetime = timedelta(minutes=session_lifetime)

# Register routes
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(web)

# Launch server
if __name__ == '__main__':
    from sys import exit
    FLASK_DEBUG = bool(config('FLASK_DEBUG', False).strip())  # type: ignore
    FLASK_PORT = int(config('FLASK_PORT', "8080"))
    if FLASK_DEBUG:
        app.run(host='0.0.0.0', port=FLASK_PORT, debug=True)
        exit(0)
    from waitress import serve
    serve(app, host="0.0.0.0", port=FLASK_PORT)
    exit()
