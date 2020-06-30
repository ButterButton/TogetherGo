import mysql.connector
import configparser
import datetime
import pytz
from enum import Enum

class DBTable(Enum):
    Product = "P"
    ProductDetail = "PD"
    Order = "O"
    Ordered = "OD"
    OrderedDetail = "ODD"

class DataBaseService:

    def GetDataBase(self):
        ConfigFile = configparser.ConfigParser()
        ConfigFile.read("config.py")
        DB = mysql.connector.connect(
            host = ConfigFile["DBProject_Steam"]["Host"],
            port =ConfigFile["DBProject_Steam"]["Port"],
            user = ConfigFile["DBProject_Steam"]["User"],
            passwd = ConfigFile["DBProject_Steam"]["Passwd"],
            database = ConfigFile["DBProject_Steam"]["Name"]
        )

        return DB
     
    def QueryProductCompleteByID(self, ProductID):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()
        SelectQuery = "SELECT * FROM TogetherGo.Product P , TogetherGo.ProductDetail PD WHERE P.ID = PD.ProductID AND P.ID = '%s'"

        DBCursor.execute(SelectQuery % ProductID)
        Result = DBCursor.fetchall()
        DBService.close()

        return Result
    
    def QueryProductCompleteTop100(self):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()
        SelectQuery = "SELECT * FROM TogetherGo.Product P , TogetherGo.ProductDetail PD WHERE P.ID = PD.ProductID Order By P.No Desc Limit 100"

        DBCursor.execute(SelectQuery)
        Result = DBCursor.fetchall()
        DBService.close()

        return Result

    def DeleteProductComplete(self, ProductID):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        DeleteSQL = "DELETE FROM TogetherGo.ProductDetail WHERE ProductID = '%s'"
        DBCursor.execute(DeleteSQL % ProductID)
        DBService.commit()

        DeleteSQL = "DELETE FROM TogetherGo.Product WHERE ID = '%s'"
        DBCursor.execute(DeleteSQL % ProductID)
        DBService.commit()

        DBService.close()

        if DBCursor.rowcount > 0:
            return True
        
        return False

    def InsertProduct(self, InsertData):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        NewID = self.GetNewID(DBTable.Product, DBCursor)

        InsertTuple = (NewID, InsertData["Name"], InsertData["Price"], InsertData["Url"], InsertData["PicUrl"])
        InsertSQL = """INSERT INTO TogetherGo.Product(ID, Name, Price, Url, PicUrl) VALUES(%s, %s, %s, %s, %s)"""

        DBCursor.execute(InsertSQL, InsertTuple)
        DBService.commit()
        DBService.close()

        if DBCursor.rowcount > 0:
            return {"ID": NewID, "Result": True}
        
        return {"ID": "", "Result": False}

    def InsertProductDetail(self, InsertData):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        NewID = self.GetNewID(DBTable.ProductDetail, DBCursor)
        LastNumber = int(NewID.lstrip(DBTable.ProductDetail.value))
        InsertTupleList = []
        for Attribute in InsertData["AttributeList"]:
            for Value in Attribute["Value"]:
                NewPK = DBTable.ProductDetail.value + str(LastNumber)
                InsertTupleList.append((InsertData["ID"], NewPK, Attribute["Attribute"], Value))
                LastNumber = LastNumber + 1

        InsertSQL = """INSERT INTO TogetherGo.ProductDetail(ProductID, ID, Attribute, Value) VALUES(%s, %s, %s, %s)"""

        DBCursor.executemany(InsertSQL, InsertTupleList)
        DBService.commit()
        DBService.close()

        if DBCursor.rowcount > 0:
            return True
        
        return False
    
    def InsertOrder(self, ProductID):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        TimeNowTaipei = self.GetTaipeiTimeNow()
        
        InsertSQL = """INSERT INTO TogetherGo.Order(ID, CreateDate, ProductID) VALUES(%s, %s, %s)"""
        InsertTuple = (self.GetNewID(DBTable.Order, DBCursor), TimeNowTaipei, ProductID)

        DBCursor.execute(InsertSQL, InsertTuple)
        DBService.commit()
        DBService.close()

        if DBCursor.rowcount > 0:
            return True
        
        return False

    def GetLastestOrder(self):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        TimeNowTaipei = self.GetTaipeiTimeNow()

        SelectQuery = "SELECT * FROM TogetherGo.Order WHERE CreateDate <= '" + TimeNowTaipei +"' AND IsOpen = 'OPEN' ORDER BY CreateDate DESC;"
        DBCursor.execute(SelectQuery)
        Result = DBCursor.fetchone()
        DBService.close()

        return Result

    def GetOrdered(self, IDdata):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        SelectQuery = "SELECT * FROM TogetherGo.Ordered WHERE OrderID = '" + IDdata["OrderID"] + "' AND LineID = '" + IDdata["LineID"] + "';"
        DBCursor.execute(SelectQuery)
        Result = DBCursor.fetchall()
        DBService.close()

        return Result

    def GetOrderedComplete(self, QueryData):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        SelectQuery = """SELECT * FROM TogetherGo.Order O, TogetherGo.Ordered OD, TogetherGo.OrderedDetail ODD, TogetherGo.ProductDetail PD
                        WHERE O.ID = OD.OrderID AND OD.ID = ODD.OrderedID AND OD.OrderID = %s AND OD.LineID = %s
                        AND OD.No IN (SELECT No FROM TogetherGo.Ordered WHERE OrderID = %s AND LineID = %s)
                        AND PD.ID = ODD.ProductDetailID
                        ORDER BY OD.No"""
        DBCursor.execute(SelectQuery, (QueryData["OrderID"], QueryData["LineID"], QueryData["OrderID"], QueryData["LineID"]))
        Result = DBCursor.fetchall()
        DBService.close()

        return Result

    def InsertOrderedComplete(self, InsertData):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        NewID = self.GetNewID(DBTable.Ordered, DBCursor)
        InsertSQL = """INSERT INTO TogetherGo.Ordered(ID, OrderID, Quantity, LineID, LineName) VALUES(%s, %s, %s, %s, %s)"""
        InsertTuple = (NewID, InsertData["OrderID"], InsertData["Quantity"], InsertData["LineID"], InsertData["LineName"])

        DBCursor.execute(InsertSQL, InsertTuple)
        DBService.commit()

        InsertSQL = """INSERT INTO TogetherGo.OrderedDetail(OrderedID, ProductDetailID) VALUES(%s, %s)"""
        InsertTuple = []
        for Item in InsertData["OrderedDetail"]:
            InsertTuple.append((NewID, Item["ValueID"]))

        DBCursor.executemany(InsertSQL, InsertTuple)
        DBService.commit()
        DBService.close()

        if DBCursor.rowcount > 0:
            return True
        
        return False

    def UpdateOrderedQuantity(self, UpdateData):
        DBService = self.GetDataBase()
        DBCursor = DBService.cursor()

        UpdateSQL = """UPDATE TogetherGo.Ordered SET Quantity = %s WHERE LineID = %s AND Quantity = 0;"""
        UpdateTuple = (int(UpdateData["Quantity"]), UpdateData["LineID"])

        DBCursor.execute(UpdateSQL, UpdateTuple)
        DBService.commit()
        DBService.close()

        if DBCursor.rowcount > 0:
            return True
        
        return False



    def GetNewID(self, DBTable, DBCursor):
        SelectLastID = "SELECT ID FROM TogetherGo." + DBTable.name + " ORDER BY No Desc Limit 1;"
        DBCursor.execute(SelectLastID)
        Result = DBCursor.fetchone()
        NewID = ""
        if  Result == None:
            NewID = DBTable.value + "1"
        else:
            LastNumber = int(Result[0].lstrip(DBTable.value))
            NewID = DBTable.value + str(LastNumber + 1)
        
        return NewID

    def GetTaipeiTimeNow(self):
        TimeNow = datetime.datetime.now()

        return TimeNow.astimezone(pytz.timezone('Asia/Taipei')).strftime("%Y-%m-%d")