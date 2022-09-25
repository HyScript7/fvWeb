#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 

from flask import Flask, render_template, request, Response
from decouple import config
from pymongo import MongoClient
from hashlib import sha256
from base64 import b64encode, b64decode

Database = MongoClient("mongodb://root:6nUwMUy1kM4fcrQp@db:27017")["Fusionverse"]
Accounts = Database["Accounts"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/dev')
def dev():
    #TODO: Load the last 10 or so cards from activity
    temp = request.args.get("template", "index")
    cards = [["HyScript7", "HyScript7 has logged in", "avatar", "Relative Time"]]
    return render_template(f"{temp}.html", cards=cards) 

@app.route("/setupRoot")
def setupRoot():
    with open("/home/script/Obrázky/Admin/Fusionverse Logo Purple.png", "rb") as av:
        avatar = av.read()
    try:
        Accounts.insert_one({
            "username": "root",
            "password": sha256("Fusionverse.R00t".encode()).hexdigest(),
            "avatar": b64encode(avatar).decode()
        })
        return Response(status=200)
    except:
        return Response(status=500)

if __name__ == '__main__':
    from sys import exit
    #* env = config('ENV_VARIABLE', cast='TYPE')
    # Get debug env
    debug = bool(config('FLASK_DEBUG'))
    app.run(host='0.0.0.0', port=5000, debug=debug)
    exit()
