from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests
import json 
from flask_cors import CORS

import MessageTemplate
import configparser

app = Flask(__name__)
CORS(app)

ConfigFile = configparser.ConfigParser()
ConfigFile.read("config.py")
beartoken = ConfigFile["Base_Info"]["beartoken"]
line_bot_api = LineBotApi(beartoken)
handler = WebhookHandler(ConfigFile["Base_Info"]["handler"])
APIUrl = ConfigFile["Base_Info"]["APIUrl"]

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(PostbackEvent)
def handle_postback(event):
    print("收到PostData")

    OrderLastest = requests.get(APIUrl + "Order/Lastest")
    Order = json.loads(OrderLastest.text)
    OrderID = ""

    if Order["Result"] == "Success":
        OrderID = Order["Data"]["ID"]

    if(event.postback.data == "ShowMyOrder"):
        print("收到顯示訂單訊號")
        UserInfo = {"OrderID": OrderID, "LineID":event.source.user_id}
        UserOrdered = requests.get(APIUrl + "OrderedComplete", data = json.dumps(UserInfo))
        UserOrdered_data = json.loads(UserOrdered.text)
        print(UserOrdered_data)

        if(UserOrdered_data["Result"] == "Success"):
            print("拿到資料了")
            UserOrdered_Template = MessageTemplate.GenerateUserOrderedTemplate(UserOrdered_data)
            print(UserOrdered_Template)
            line_bot_api.reply_message(event.reply_token, FlexSendMessage(
                        alt_text= "UserOrdered",
                        contents= UserOrdered_Template
                    ))

@app.route("/Test/LinePushMessage_CORSHelper/", methods=["POST"])
def HelpCORS(): 
    url = "https://api.line.me/v2/bot/message/push"
    loaddata = json.loads(request.data)
    headers = {'Content-Type':'application/json; charset=UTF-8', 'Authorization': 'Bearer ' + beartoken}
    payload = {'to':loaddata["to"],'messages':loaddata["messages"]}
    requests.post(url, data=json.dumps(payload), headers=headers)
    print("發送完成訂單中")
    return url

if __name__ == "__main__":
    app.run()