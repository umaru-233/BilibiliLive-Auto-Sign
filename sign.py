# -*- coding: utf8 -*-
*Copyright: Copyright (c) 2022
*Created on 2022-02-15
*Author:umaru-233
*Version 1.0
*Title: Bilibili-Auto-sign

import json
import time
import requests as r

def main_handler(event, context):
    print("程序将在5秒后执行...")
    time.sleep(5) //等待五秒继续执行
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  //读时间

    sessdata = "xxxxxxxxxxxxxxxxxxxxxxxxxx"   //替换成自己的B站cookie

    userinfo = json.loads(r.get("https://api.bilibili.com/x/web-interface/nav", cookies={"SESSDATA":sessdata}).text)
    if userinfo["data"]["isLogin"] == False:
        print("登录失败")
        return("Login Failed")
    print("用户名："+userinfo["data"]["uname"])
    print("UID："+str(userinfo["data"]["mid"]))

    sign = r.get("https://api.live.bilibili.com/sign/doSign", cookies={"SESSDATA":sessdata})
    sign_info = json.loads(sign.text)
    if sign_info["code"] == 0:  //执行成功
        print("今日收获: "+sign_info["data"]["text"])
        print(sign_info["data"]["specialText"])
        r.get('https://wx.xtuis.cn/xxxxxxxxxxxxxxxxx.send?text=签到成功')//推送token
    else:
        print("签到失败："+sign_info["message"])   //执行失败
        r.get('https://wx.xtuis.cn/xxxxxxxxxxxxxxxxx.send?text=签到失败')//推送token
        return "Sign Failed"

    return("Finish")

main_handler("", "")
