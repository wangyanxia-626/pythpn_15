# -*- coding:utf-8 -*-
# @Time :2020-03-03 21:37
# @Email :876417305@qq.com
# @Author :yanxia
# @File :learn_requests.PY
# 安装 pip install requests
# 作用是什么：发送http请求。常见的有get，post，delete，put等
# 为什么学习它？http协议的接口
# request 客户端---服务端的请求 包含：请求头 请求地址 请求参数 http协议版本
# response 服务端对客户端的一个请求响应，包含：响应头 响应报文 状态码
import requests
url="http://www.lemfix.com/topics/1015"
# request是模拟客户端向服务端发送一个请求。
# 发送一个get请求
res=requests.get(url)
#requests.post(url)
print("状态码",res.status_code)
print("响应头",res.headers)
print(res.text)