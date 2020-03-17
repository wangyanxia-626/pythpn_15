# -*- coding:utf-8 -*-
# @Time :2020-03-07 21:09
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_request.PY
import requests
class HttpRequests:
    def http_request(self,url,method,parm):
        '''完成http的post和get请求
           method请求方法，可以是get or post
           URL请求地址
           :param 请求参数'''

        if method.lower()=="get":
            try:
                res=requests.get(url,parm)
                print("响应文本", res.text)
            except Exception as e:
                print("get请求出错：{}".format(e))
        else:
            try:
                res=requests.post(url,parm)
                print("响应文本",res.text)
            except Exception as e:
                print("post请求出错：{}".format(e))
        return res

if __name__ == '__main__':
    login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    parm = {"mobilephone": "18688773467", "pwd": "123456"}
    res=HttpRequests().http_request(login_url,"GEt",parm)
    print("结果是：{}".format(res.text))