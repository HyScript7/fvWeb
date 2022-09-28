from flask import Blueprint, render_template, request
from flask.wrappers import Response 

web = Blueprint("web", __name__)

@web.route('/')
def home(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("index.html", cards=cards) 

@web.route('/wiki')
def wiki(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("index.html", cards=cards) 

@web.route('/forum')
def forum(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    return render_template("index.html", cards=cards) 

@web.route('/dev')
def dev():
    temp = request.args.get("template", "index")
    cards = [["Title", "Description", "#", "Relative Time"]]
    content = ["<p>Hello World (/dev)</p>"]
    return render_template(f"{temp}.html", cards=cards, content=content) 
