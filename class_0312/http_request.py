# -*- coding:utf-8 -*-
# @Time :2020-03-12 9:59
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_request.PY
import requests
class HttpRequest:
    """
    使用这类的request方法去完成不同的http请求，并且返回响应结果
    """
    def request(self,method,url,data=None,json=None,cookies=None):
        '''
        :param method: 请求方法
        :param url: 请求参数
        :param data: 请求数据
        :param json: 请求数据为json
        :param cookies: cookies值
        :return: 返回res是response对象
        '''
        if type(data)==str:
            data=eval(data)
        if method.lower() =="get":
            resp=requests.get(url,params=data,cookies=cookies)
        elif method.lower()=="post":
            if json:#意思是json不为空
                resp=requests.post(url,json=json,cookies=cookies)
            else:
                resp=requests.post(url,params=data,cookies=cookies)
        else:
            print("UN-support method")
        return resp
# 第二种方法，不需要传cookies的写法，利用session这个对象，会自动传递cookies
class HttpRequest2:
    def __init__(self):
        self.session=requests.sessions.session()
    def request(self,method,url,data=None,json=None):
        if method.lower()=="get":
            resp=self.session.request(method=method,url=url,data=data)
        elif method.lower()=="post":
            if json:
                resp=self.session.request(method=method,url=url,json=json)
            else:
                resp=self.session.request(method=method,url=url,data=data)
        else:
            print("UN-support method")
        return resp
    def close(self):
        self.session.close()#用完记得关闭，很关键

if __name__ == '__main__':
    http_request=HttpRequest()
    #调用登录
    params = {"mobilephone":"15810447878","pwd": 123456}
    res=http_request.request("post","http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)
    print(res.json())
    #调用充值
    params = {"mobilephone":"15810447878","amount": 111}
    res = http_request.request("post","http://test.lemonban.com/futureloan/mvc/api/member/recharge",data=params,cookies=res.cookies)
    print(res.json())
    print(res.request.method)
    # http_request2=HttpRequest2()
    # params = {"mobilephone": "15810447878", "pwd": 123456}
    # res=http_request2.request("post","http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)
    # params={"mobilephone":"15810447878","amount": 111}
    # res=http_request2.request("post","http://test.lemonban.com/futureloan/mvc/api/member/recharge",data=params)
    # http_request2.close()
    # print(res.json())
