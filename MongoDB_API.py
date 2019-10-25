from flask import Flask
from flask import Response
from flask_cors import CORS
import pymongo
import urllib.parse
from pprint import pprint
from pymongo import MongoClient
from bson.json_util import dumps
import configparser

app = Flask(__name__)
CORS(app)
ConfigFile = configparser.ConfigParser()
ConfigFile.read("config.py")
MONGO_HOST = ConfigFile["DB_TogetherGo"]["ConnectString"]

@app.route("/")
def index():
    return "Welcome"
    
@app.route("/POST/<key>/<value>")
def SerachByKey(key, value):
    collection = connect_mongo()
    cursor = collection.find({key:value})
    data = [d for d in cursor]
    return Response(dumps(data, ensure_ascii=False, indent=4), mimetype='text/json')

def connect_mongo():
    # collection.stats
    # cursor = collection.find({"Products.ProductDetail.Value":{"$all":["S","M"]}})
    # data = [d for d in cursor]
    # print(data)

    # collectionOrder.stats
    # cursor = collection.find({"Products.Name":"Dress"})
    # data = [d for d in cursor]
    # pprint(data)
    
    # print(data)
    # pipeline = {"$lookup":{"from":"TogetherGo", "localField":"No", "foreignField":"No","as":"Notest"}}
    # pprint.pprint(list(db.get_collection("Order").aggregate([pipeline])))
    client = MongoClient(MONGO_HOST)
    db = client.TogetherGo   
    collection = db.Products

    return collection


if __name__ == "__main__":
    app.run(debug=True)
