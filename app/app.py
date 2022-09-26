#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 

from flask import Flask
from decouple import config
from pymongo import MongoClient
from sassutils.wsgi import SassMiddleware
from routes.api import api
from routes.web import web

# Database Client
Database = MongoClient("mongodb://root:6nUwMUy1kM4fcrQp@localhost:27017")["Fusionverse"]
Accounts = Database["Accounts"]

# Define application
app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {__name__: ('static/sass', 'static/css', '/static/css')})

# Register routes
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(web)

# Launch server
if __name__ == '__main__':
    from sys import exit
    debug = bool(config('FLASK_DEBUG'))
    app.run(host='0.0.0.0', port=5000, debug=debug)
    exit()
