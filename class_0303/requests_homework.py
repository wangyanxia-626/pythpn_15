# -*- coding:utf-8 -*-
# @Time :2020-03-03 22:43
# @Email :876417305@qq.com
# @Author :yanxia
# @File :requests_homework.PY
"""1：作业安排：
写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
每个请求要求有请求参数
登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
"""
import requests
class HttpRequests:
    def http_request(self,method,url,parm):
        '''完成http的post和get请求
           method请求方法，可以是get or post
           URL请求地址
           :param 请求参数'''

        if method.lower()=="get":
            try:
                res=requests.get(url,parm)
                print("状态码：", res.status_code)
                print("响应头：", res.headers)
                print("响应文本", res.text)
            except Exception as e:
                print("get请求出错：{}".format(e))
        else:
            try:
                res=requests.post(url,parm)
                print("状态码：",res.status_code)
                print("响应头：", res.headers)
                print("响应文本",res.text)
            except Exception as e:
                print("post请求出错：{}".format(e))
        return res

if __name__ == '__main__':
    login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    parm = {"mobilephone": "18688773467", "pwd": "123456"}
    res=HttpRequests().http_request("GEt",login_url,parm)
    print("结果是：{}".format(res.text))
