#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# Version: 1.14
# Author(s): HyScript7
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from flask import Blueprint, render_template, request
from flask.wrappers import Response 

web = Blueprint("web", __name__)

@web.route('/')
def home(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    content = ["md;# Index"]
    return render_template("index.html", cards=cards, content=content) 

@web.route('/wiki')
def wiki(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    content = ["md;# Wiki"]
    return render_template("index.html", cards=cards, content=content) 

@web.route('/forum')
def forum(): 
    cards = [["Title", "Description", "#", "Relative Time"]]
    content = ["md;# Forum"]
    return render_template("index.html", cards=cards, content=content) 

@web.route('/dev')
def dev():
    temp = request.args.get("template", "index")
    cards = [["Title", "Description", "#", "Relative Time"]]
    content = ["<h1>HTML Heading</h1>", "<p>Hello World</p>", "md;# Markdown Heading\n- Markdown List\n- Another line"]
    return render_template(f"{temp}.html", cards=cards, content=content) 
