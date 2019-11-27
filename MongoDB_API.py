from flask import Flask
from flask import Response
from flask import request
from flask_cors import CORS
import pymongo
import urllib.parse
from pprint import pprint
from pymongo import MongoClient
from bson.json_util import dumps
import configparser
import json
import datetime
import pytz
import time

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Welcome"
    
@app.route("/GET/Products/No/<value>", methods=["GET"])
def SerachByKey(value):
    db = connect_mongo()
    cursor = db.Products.find({"No":value})
    data = [d for d in cursor]
    return Response(dumps(data, ensure_ascii=False, indent=4), mimetype='text/json')

@app.route("/POST/Order/<JsonValue>", methods=["POST"])
def InsertByJson(JsonValue):
    db = connect_mongo()
    twtime = pytz.utc.localize(datetime.datetime.now()) + datetime.timedelta(hours=8)
    afterload = json.loads(JsonValue)
    afterload["Test"] = "87"
    print(afterload)
    # Result = db.Order.insert(json.loads(JsonValue))
    # Result = db.Order.insert({"Date":test1time})
    # Result = db.Order.insert_many([{"Date":test1time},{"Date":test2time},{"Date":test3time},{"Date":testtimestrTodatetime}])
    # data = [d for d in db.Order.find({"_id":Result})]
    # if(len(data) < 1):
    #     return Response(dumps({"Result":"Fail","Data":data}, ensure_ascii=False, indent=4), mimetype='text/json')

    # return Response(dumps({"Result":"Success","Data":data}, ensure_ascii=False, indent=4), mimetype='text/json')
    return "HI"

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
    ConfigFile = configparser.ConfigParser()
    ConfigFile.read("config.py")
    # print(ConfigFile["DB_TogetherGo"]["ConnectString"])
    # print("mongodb://%s:%s@%s:%s/TogetherGo"%(ConfigFile["DB_TogetherGo"]["USER"],ConfigFile["DB_TogetherGo"]["PWD"],ConfigFile["DB_TogetherGo"]["HOST"], ConfigFile["DB_TogetherGo"]["PORT"]))
    ConnectString = "mongodb://%s:%s@%s:%s/TogetherGo"%(ConfigFile["DB_TogetherGo"]["USER"],ConfigFile["DB_TogetherGo"]["PWD"],ConfigFile["DB_TogetherGo"]["HOST"], ConfigFile["DB_TogetherGo"]["PORT"])
    client = MongoClient(ConnectString)
    db = client.TogetherGo   
    # collection = db.Products

    return db


if __name__ == "__main__":
    app.run(debug=True)


