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
    return "Welcome TogetherGo MongoDB API"
    
@app.route("/GET/Products/No/<value>", methods=["GET"])
def SerachByKey(value):
    db = connect_mongo()
    cursor = db.Products.find({"No":value})
    data = [d for d in cursor]
    return Response(dumps(data, ensure_ascii=False, indent=4), mimetype='text/json')

@app.route("/GET/Products/Top100", methods=["GET"])
def SerachProductsTop100():
    db = connect_mongo()
    cursor = db.Products.find({}).sort("No", pymongo.ASCENDING).limit(100)
    data = [d for d in cursor]
    return Response(dumps(data, ensure_ascii=False, indent=4), mimetype='text/json')

@app.route("/POST/Products/<InsertProductJson>", methods=["POST"])
def InsertProductByJson(InsertProductJson):
    db = connect_mongo()
    InsertProductJson = json.loads(InsertProductJson)
    LastestProductNo = db.Products.find({},{"No":1}).sort("No", pymongo.DESCENDING).limit(1)[0]["No"]
    LastestProductNo = GetLastestNumber(LastestProductNo, "P")
    ProductsFormat = {"No":LastestProductNo,"Name":InsertProductJson["Name"],"Price":InsertProductJson["Price"],"Url":InsertProductJson["Url"],"PicUrl":InsertProductJson["PicUrl"], "ProductDetail":[]}
    Result = db.Products.insert(ProductsFormat)
    ResultData = db.Products.find({"_id":Result})[0]

    return ResponseResult(ResultData)

@app.route("/POST/ProductDetail/<ProductNo>/<InsertProductDetailJson>", methods=["POST"])
def InsertProductDetailByJson(ProductNo, InsertProductDetailJson):
    db = connect_mongo()
    ProductDetailJson = json.loads(InsertProductDetailJson)
    ProductNo = ProductNo
    ResultData = db.Products.update({"No":ProductNo},{"$set":{"ProductDetail":ProductDetailJson}})

    return ResponseResult(ResultData)

@app.route("/POST/Order/<InsertPrdouctNo>", methods=["POST"])
def InsertOrderByJson(InsertPrdouctNo):
    db = connect_mongo()

    # 伺服器電腦時間轉換
    twtime = pytz.utc.localize(datetime.datetime.now()) + datetime.timedelta(hours=8)
    # 本機(台灣)電腦時間
    # twtime = datetime.datetime.now()

    LastestOrderNo = db.Order.find({},{"No":1}).sort("No", pymongo.DESCENDING).limit(1)[0]["No"]
    # LastestNumber = int(str(LastestOrderNo).lstrip("O")) + 1
    LastestOrderNo = GetLastestNumber(LastestOrderNo, "O")
    print(LastestOrderNo)
    Order = {"OrderDate":twtime, "No":LastestOrderNo, "ProductNo":InsertPrdouctNo, "OrderList":[]}
    Result = db.Order.insert(Order)
    data = db.Order.find({"_id":Result})[0]

    return ResponseResult(data)

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

def GetLastestNumber(EndNumber, PkCode):
    LastestNumber = int(str(EndNumber).lstrip(PkCode)) + 1
    LastestOrderNo = PkCode + str(LastestNumber)

    return LastestOrderNo

def ResponseResult(ResultData):
    if(len(ResultData) < 1):
        return Response(dumps({"Result":"Fail", "Data":[]}, ensure_ascii=False, indent=4), mimetype='text/json')

    return Response(dumps({"Result":"Success", "Data":ResultData}, ensure_ascii=False, indent=4), mimetype='text/json')
if __name__ == "__main__":
    app.run(debug=True)


