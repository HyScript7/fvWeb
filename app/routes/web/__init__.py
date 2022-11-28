#  ______   __   __   __     __     ______     ______    
# /\  ___\ /\ \ / /  /\ \  _ \ \   /\  ___\   /\  == \   
# \ \  __\ \ \ \'/   \ \ \/ ".\ \  \ \  __\   \ \  __<   
#  \ \_\    \ \__|    \ \__/".~\_\  \ \_____\  \ \_____\ 
#   \/_/     \/_/      \/_/   \/_/   \/_____/   \/_____/ 
#
# fvWeb
# License: MIT LICENSE
# For more information on copyright and licensing view the README.md file.
#
from decouple import config
from pymongo import MongoClient

dbhost = config("DB_HOST", "db")
dbport = config("DB_PORT", "27017")
dbuser = config("DB_USER", "root")
dbpass = config("DB_PASS", "root")

db_Client = MongoClient(f"mongodb://{dbuser}:{dbpass}@{dbhost}:{dbport}",serverSelectionTimeoutMS=3000)

async def getCards():
    r = []
    for i in db_Client["fvWeb"]["Activity"].find():
        r.append([i["title"], i["description"], i["avatar"], "Relative Time"])
    return r

navBarLinks = [
    ["Home", "/", False],
    ["Wiki", "/wiki", False],
    ["Forum", "/forum", False]
    # linkName, Href, Disabled
]
