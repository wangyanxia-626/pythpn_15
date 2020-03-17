# -*- coding:utf-8 -*-
# @Time :2020-03-12 10:56
# @Email :876417305@qq.com
# @Author :yanxia
# @File :study_session_request.PY
import requests
session=requests.sessions.session()
#登录
params={"mobilephone":"15810447878","pwd":123456}
"http://test.lemonban.com/futureloan/mvc/api/member/login"
resp=session.request('post',url="http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)
#充值
params={"mobilephone":"15810447878","amount":111}
resp=session.request('post',url="http://test.lemonban.com/futureloan/mvc/api/member/recharge",data=params)
print(resp.text)
session.close()
