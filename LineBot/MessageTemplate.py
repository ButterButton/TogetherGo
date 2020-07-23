# carouselTemplate
CarouselTemplate = {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://img2.momoshop.com.tw/goodsimg/0005/422/398/5422398_R.jpg?t=1561976651",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "2:3",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Brown's T-shirts",
                                "size": "xl",
                                "color": "#ffffff",
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "¥35,800",
                                "color": "#ebebeb",
                                "size": "sm",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "¥75,000",
                                "color": "#ffffffcc",
                                "decoration": "line-through",
                                "gravity": "bottom",
                                "flex": 0,
                                "size": "sm"
                            }
                            ],
                            "spacing": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                },
                                {
                                    "type": "text",
                                    "text": "詳細資料",
                                    "color": "#ffffff",
                                    "flex": 0,
                                    "offsetTop": "-2px",
                                    "action": {
                                        "type": "uri",
                                        "label": "Go To Product Website",
                                        "uri": "https://www.youtube.com/watch?v=n1h1AOeVQ38"
                                        }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "filler"
                            },
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                },
                                {
                                    "type": "text",
                                    "text": "Add to cart",
                                    "color": "#ffffff",
                                    "flex": 0,
                                    "offsetTop": "-2px",
                                    "action": {
                                        "type": "postback",
                                        "label": "return data",
                                        "data": "test20191129",
                                        "text" : "test20191129"
                                        }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "filler"
                            },
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px"
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#03303Acc",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    }
                ],
                "paddingAll": "0px"
            }
        }
    ]
}

DeatilTemplate = {
                    "type": "bubble",
                    "styles": {
                        "footer": {
                        "separator": True
                        }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "訂購完成!",
                            "weight": "bold",
                            "color": "#1DB446",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": "訂購單明細",
                            "weight": "bold",
                            "size": "xxl",
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "恭喜您已完成訂購，以下為本次訂購單明細",
                            "size": "xs",
                            "color": "#aaaaaa",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "xxl",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "A",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "B",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "C",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    }
                                    ]
                                }
                            ]
                        }]
                    }
                }


def GenerateCarouselTemplate(ProductName, ProdcutPrice, resultstr):
    ProductName = str(ProductName)
    ProdcutPrice = str(ProdcutPrice)

    return {
    "type": "carousel",
    "contents": [
        {
            "type": "bubble",
            "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://img2.momoshop.com.tw/goodsimg/0005/422/398/5422398_R.jpg?t=1561976651",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "2:3",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": ProductName,
                                "size": "xl",
                                "color": "#ffffff",
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": ProdcutPrice,
                                "color": "#ebebeb",
                                "size": "sm",
                                "flex": 0
                            }
                            ],
                            "spacing": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                },
                                {
                                    "type": "text",
                                    "text": "商品詳細資料",
                                    "color": "#ffffff",
                                    "flex": 0,
                                    "offsetTop": "-2px",
                                    "action": {
                                        "type": "uri",
                                        "label": "Go To Product Website",
                                        "uri": "https://www.youtube.com/watch?v=n1h1AOeVQ38"
                                        }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "filler"
                            },
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "text",
                                    "text": "我要加入!",
                                    "color": "#ffffff",
                                    "flex": 0,
                                    "offsetTop": "-2px",
                                    "action": {
                                        "type": "postback",
                                        "label": "return data",
                                        "data": "⊡" + resultstr,
                                        "text" : "⊡" + resultstr
                                        }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "filler"
                            },
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "text",
                                    "text": "Pass~",
                                    "color": "#ffffff",
                                    "flex": 0,
                                    "offsetTop": "-2px",
                                    "action": {
                                        "type": "postback",
                                        "label": "return data",
                                        "data": "msg=goodbye",
                                        "text" : "msg=goodbye"
                                        }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "filler"
                            },
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px"
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#03303Acc",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    }
                ],
                "paddingAll": "0px"
            }
        }
    ]
}

def GenerateFinishDeatilTemplate(Result):
    Contents = []
    for Item in Result["Selected"]:

        for Sel in Item["Attribute"]:
            Content =  {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": Sel["Name"] + ":" + Sel["Value"],
                        "size": "sm",
                        "color": "#555555",
                        "flex": 0
                    }
                ]
            }
            Contents.append(Content)

        QuantityContent =  {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "數量:" + str(Item["Quantity"]),
                        "size": "sm",
                        "color": "#555555",
                        "flex": 0
                    }
                ]
        }
        Contents.append(QuantityContent)
        SperateContent =  {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "---------------------------------",
                        "size": "sm",
                        "color": "#555555",
                        "flex": 0
                    }
                ]
        }
        Contents.append(SperateContent)       

    return {
                    "type": "bubble",
                    "styles": {
                        "footer": {
                        "separator": True
                        }
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "訂購完成",
                            "weight": "bold",
                            "color": "#1DB446",
                            "size": "sm"
                        },
                        {
                            "type": "text",
                            "text": "訂購單明細",
                            "weight": "bold",
                            "size": "xxl",
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "恭喜您已完成訂購，以下為本次訂購單明細",
                            "size": "xs",
                            "color": "#aaaaaa",
                            "wrap": True
                        },
                        {
                            "type": "separator",
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "xxl",
                            "spacing": "sm",
                            "contents": Contents
                        }]
                    }
                }

def GenerateUserOrderedTemplate(Result):
    UserOrderedTemplate = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": []
        },
        "styles": {
            "footer": {
            "separator": True
            }
        }
    }
    UserOrderedTemplate["body"]["contents"].append({
        "type": "text",
        "text": Result["Data"]["UserName"]+"的訂單",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      })
    UserOrderedTemplate["body"]["contents"].append({
        "type": "text",
        "text": Result["Data"]["ProductName"],
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      })
    UserOrderedTemplate["body"]["contents"].append({
        "type": "text",
        "text": "備註",
        "size": "xs",
        "color": "#aaaaaa",
        "wrap": True
      })
    totalqua = 0
    contests ={
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": []
        }
    sep = {
            "type": "separator",
            "margin": "xxl"
        }

    for item in Result["Data"]["Selected"]:
        totalqua = totalqua + int(item["Quantity"])

        for item2 in item["Attribute"]:
            content={
                "type": "box",
                "layout": "horizontal",
                "contents": []
            }
            content["contents"].append({
                "type": "text",
                "text": item2["Name"],
                "size": "sm",
                "color": "#555555",
                "flex": 0
            })
            content["contents"].append({
                "type": "text",
                "text": item2["Value"],
                "size": "sm",
                "color": "#111111",
                "align": "end"
            })
            contests["contents"].append(content)

        content_Qua={
            "type": "box",
            "layout": "horizontal",
            "contents": 
            [
                {
                    "type": "text",
                    "text": "數量",
                    "size": "sm",
                    "color": "#555555",
                    "flex": 0
                },
                {
                    "type": "text",
                    "text": str(item["Quantity"]),
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
            ]
        }
        contests["contents"].append(content_Qua)
        contests["contents"].append(sep)

    content_sum={
        "type": "box",
        "layout": "horizontal",
        "contents": 
        [
            {
                "type": "text",
                "text": "總計金額",
                "size": "sm",
                "color": "#555555",
                "flex": 0
            },
            {
                "type": "text",
                "text": "NT" + format(totalqua * int(Result["Data"]["Price"]), ","),
                "size": "sm",
                "color": "#111111",
                "align": "end"
            }
        ]
    }
    contests["contents"].append(content_sum)

    UserOrderedTemplate["body"]["contents"].append(sep)
    UserOrderedTemplate["body"]["contents"].append(contests)

    return UserOrderedTemplate