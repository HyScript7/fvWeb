#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 

from flask import Flask, render_template
from decouple import config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('web.html')

@app.route('/dev')
def dev():
    return render_template("index.html")

if __name__ == '__main__':
    from sys import exit
    #* env = config('ENV_VARIABLE', cast='TYPE')
    # Get debug env
    debug = len(str(config('FLASK_DEBUG')))!=5 # I am too lazy to fuck around with types
    app.run(host='127.0.0.1', port=8000, debug=debug)

