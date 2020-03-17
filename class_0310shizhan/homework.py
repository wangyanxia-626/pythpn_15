# -*- coding:utf-8 -*-
# @Time :2020-03-11 22:29
# @Email :876417305@qq.com
# @Author :yanxia
# @File :homework.PY
import requests
class HttpRequest:

    def http_request(self,method,url,params,cookies=None):
        if method.lower=="get":
            res=requests.get(url,params,cookies=cookies)
            print(res.json())
        else:
            res=requests.post(url,params,cookies=cookies)
            print(res.json())
        return res
if __name__ == '__main__':
    params={"mobilephone":"15810447878","pwd":123456}
    register_url="http://test.lemonban.com/futureloan/mvc/api/member/register"
    params1={"mobilephone":"15810447878","pwd":123456}
    login_url="http://test.lemonban.com/futureloan/mvc/api/member/login"
    params2={"mobilephone":"15810447878","amount":111}
    recharge_url="http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    res1=HttpRequest().http_request("POST",register_url,params)
    res2=HttpRequest().http_request("post",login_url,params1)
    res3=HttpRequest().http_request("post",recharge_url,params2,res2.cookies)
