# -*- coding:utf-8 -*-
# @Time :2020-03-10 21:52
# @Email :876417305@qq.com
# @Author :yanxia
# @File :study_request.PY
import requests
'''
1、构造请求:请求方式、请求地址、请求参数
2、发起请求
3、返回响应
4、判断响应码，响应体'''
#注册接口
params={"mobilephone":"15810447833","pwd":123456}
resp=requests.get("http://test.lemonban.com/futureloan/mvc/api/member/register",params=params)
print(resp.text)
# 登录接口
params={"mobilephone":"15810447878","pwd":123456}
resp=requests.post("http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)
print(resp.text)
print(resp.cookies)
#充值接口
params={"mobilephone":"15810447878","amount":111}
resp=requests.post("http://test.lemonban.com/futureloan/mvc/api/member/recharge",
                   data=params,cookies=resp.cookies)
print(resp.text)
print(resp.cookies)
