# -*- coding:utf-8 -*-
# @Time :2020-03-11 21:40
# @Email :876417305@qq.com
# @Author :yanxia
# @File :call_web.PY
import requests
# params={"username":"zhuge2019","password":"QAZwsx123"}
# url="https://callapiv2.zhuge.com/home/index/index"
# res=requests.post(url=url,data=params)
# print(res.json())
# print(res.json()['data']['token'])
# params={"authorization":res.json()['data']['token'],"uid":"900","company_id":1,"super_manage":2}
# url="https://callapiv2.zhuge.com/Admin/v1/User/get_user_rule"
# res1=requests.post(url=url,data=params)
# print(res1.json())
session=requests.sessions.session()
#登录
params={"username":"zhuge2019","password":"QAZwsx123"}
res=session.request("post",url="https://callapiv2.zhuge.com/home/index/index",data=params)
print(res.text)
#获取左侧导航条
params={"authorization":res.json()['data']['token'],"uid":"900","company_id":1,"super_manage":2}
res=session.request("post",url="https://callapiv2.zhuge.com/Admin/v1/User/get_user_rule",data=params)
print(res.json())
