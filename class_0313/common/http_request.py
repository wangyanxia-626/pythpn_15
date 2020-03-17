# -*- coding:utf-8 -*-
# @Time :2020-03-13 11:58
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_request.PY
import requests
from class_0313.common.config import config

class HttpRequest:
    def request(self, method, url, data=None, json=None, cookies=None):
        if type(data) == str:
            data = eval(data)
        if method.lower() == "get":
            res = requests.get(url, params=data, cookies=cookies)
        elif method.lower() == "post":
            if json:
                res = requests.post(url, json=json, cookies=cookies)
            else:
                res = requests.post(url, data=data, cookies=cookies)
        else:
            print("un_support method")
        return res


# 第二种方法，不需要传cookies的写法，利用session这个对象，会自动传递cookies
class HttpRequest2:
    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        if type(data) == str:
            data = eval(data)
        # 拼接请求的url
        url=config.get('api','pre_url')+url
        if method.lower() == "get":
            resp = self.session.request(method=method,url=url,params=data)
        elif method.lower() == "post":
            if json:
                resp = self.session.request(method=method,url=url,json=json)
            else:
                resp = self.session.request(method=method,url=url,data=data)
        else:
            resp =None
            print("un_support method")
        #print("请求响应",resp.text)
        return resp

    def close(self):
        self.session.close()

if __name__ == '__main__':
    http_request = HttpRequest2()
    params = {"mobilephone":"18298461920","pwd":123456}
    resp = http_request.request("GET", "/member/login", data=params)
    print(resp.text)
