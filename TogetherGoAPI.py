from flask import Flask
from flask import Response
from flask import request
from flask_cors import CORS
from DataBaseService import DataBaseService
import pytz
import datetime
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
DBService = DataBaseService()

@app.route("/")
def index():
    return "Welcome To TogetherAPI MySQL"

@app.route("/ProductComplete/ID/<value>", methods=["GET"])
def QueryProductCompleteByID(value):
    DBResult = DBService.QueryProductCompleteByID(str(value))

    return ConvertToProductCompleteFormat(DBResult)

@app.route("/ProductComplete/Top100", methods=["GET"])
def QueryProductCompleteTop100():
    DBResult = DBService.QueryProductCompleteTop100()

    return ConvertToProductCompleteFormat(DBResult)

@app.route("/ProductComplete/ID/<value>", methods=["DELETE"])
def DeleteProductComplete(value):
    return ResponseBoolResult(DBService.DeleteProductComplete(value))

@app.route("/Product", methods=["POST"])
def InsertProduct():
    DBResult = DBService.InsertProduct(json.loads(request.data))

    Result = ResponseBoolResult(DBResult["Result"])
    Result["ID"] = DBResult["ID"]

    return Result

@app.route("/ProductDetail", methods=["POST"])
def InsertProductDetail():
    return ResponseBoolResult(DBService.InsertProductDetail(json.loads(request.data)))

@app.route("/Order/ProductID/<value>", methods=["POST"])
def InsertOrder(value):
    return ResponseBoolResult(DBService.InsertOrder(value))

@app.route("/Order/Lastest", methods=["GET"])
def QueryOrderLastest():
    try:
        return ConvertToOrderFormat(DBService.GetLastestOrder())
    except:
        return ResponseBoolResult(False)

# 訂單明細
@app.route("/OrderedComplete", methods=["GET"])
def GetOrderedComplete():
    try:
        return ConvertToOrderComplete(DBService.GetOrderedComplete(json.loads(request.data)))
    except:
        return ResponseBoolResult(False)

@app.route("/OrderedComplete", methods=["POST"])
def InsertOrderedComplete():
    try:
        return ResponseBoolResult(DBService.InsertOrderedComplete(json.loads(request.data)))
    except:
        return ResponseBoolResult(False)

@app.route("/Ordered", methods=["GET"])
def GetOrderedByOrderIDAndLineID():
    try:
        return ConvertToOrdered(DBService.GetOrdered(json.loads(request.data)))
    except:
        return ResponseBoolResult(False)

@app.route("/Ordered/Quantity/Zero", methods=["PUT"])
def UpdateOrderedQuantity():
    try:
        return ResponseBoolResult(DBService.UpdateOrderedQuantity(json.loads(request.data)))
    except:
        return ResponseBoolResult(False)

    
def ConvertToProductCompleteFormat(DBResult):
    if len(DBResult) == 0:
        return ResponseBoolResult(False)

    PIDList = []
    for PID in DBResult:
        PIDList.append(PID[1])
    PIDList = set(PIDList)

    APIResultList = []
    for PID in PIDList:
        Result = list(filter(lambda x: x[1] == PID, DBResult))
        APIResult = {"ID":Result[0][1], "Name":Result[0][2], "Price":float(Result[0][3]), "Url":Result[0][4], "PicUrl":Result[0][5], "ProductDetail":[]}

        Attrlist = []
        for DBres in Result:
            Attrlist.append(DBres[9])

        Detail = {"Attribute":"", "Value":[]} 
        for at in set(Attrlist):
            Detail["Attribute"] = at
            for item in list(filter(lambda x: x[9] == at, Result)):
                Detail["Value"].append({"ValueName": item[10], "ValueID": item[8]})
            APIResult["ProductDetail"].append(Detail)
            Detail = {"Attribute":"", "Value":[]}
        APIResultList.append(APIResult)     

    return ResponseDataResult(APIResultList)

def ConvertToOrderFormat(DBResult):
    OrderFormat = {}
    if len(DBResult) > 0:
        OrderFormat = {"ID": DBResult[1], "CreateDate": DBResult[2].strftime("%Y-%m-%d"), "ProductID": DBResult[3], "IsOpen": DBResult[4]}

    return ResponseDataResult(OrderFormat)

def ConvertToOrdered(DBResult):
    Oredered = []
    for Res in DBResult:
        OrderedFormat = {"ID": Res[1], "OrderID": Res[2], "Quantity": Res[3], "LineID": Res[4], "LineName": Res[5]}
        Oredered.append(OrderedFormat)
    
    return ResponseDataResult(Oredered)

def ConvertToOrderComplete(DBResult):
    GroupHeader = DBResult[0]

    IDList = []
    for ODID in DBResult:
        IDList.append(ODID[1])
    IDList = set(IDList)

    #  0     1         2        3          4            5             6        7
    # O.ID, OD.ID, P.Name, P.Price, OD.LineName, OD.Quantity, PD.Attribute, PD.Value
    Ordered = {"OrderID": GroupHeader[0], "ProductName": GroupHeader[2], "Price": int(GroupHeader[3]), "UserName": GroupHeader[4],"Selected" : []}

    for ODID in IDList:
        SelectedOption = {"Quantity": 0, "Attribute":[]}

        for Item in filter(lambda x: x[1] == ODID, DBResult):
            SelectedOption["OrderedID"] = Item[1]
            SelectedOption["Quantity"] = Item[5]
            SelectedOption["Attribute"].append({"Name":Item[6], "Value":Item[7]})
            # SelectedOption["Attribute"].append(Item[17] + ":" + Item[18])

        SelectedOption["Attribute"].sort(key= lambda s:s["Name"])
        Ordered["Selected"].append(SelectedOption)

    return ResponseDataResult(Ordered)

def ResponseBoolResult(Resbool):
    if Resbool:
        return {"Result":"Success"}
    else:
        return {"Result":"Fail"}

def ResponseDataResult(Data):
    DataResult = ResponseBoolResult(len(Data) > 0)
    DataResult["Data"] = Data

    return Response(json.dumps(DataResult, ensure_ascii=False, indent=4), mimetype='text/json')

if __name__ == "__main__":
    app.run(debug=True)