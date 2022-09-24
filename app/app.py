#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 

from flask import Flask, render_template, request
from decouple import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/dev')
def dev():
    #TODO: Load the last 10 or so cards from activity
    temp = request.args.get("template", "index")
    cards = [["HyScript7", "HyScript7 has logged in", "avatar", "Relative Time"], ["Fusionverse", "Server has started!", "avatar", "Relative Time"]]
    return render_template(f"{temp}.html", cards=cards) 

if __name__ == '__main__':
    from sys import exit
    #* env = config('ENV_VARIABLE', cast='TYPE')
    # Get debug env
    debug = bool(config('FLASK_DEBUG'))
    app.run(host='0.0.0.0', port=5000, debug=debug)
    exit()
