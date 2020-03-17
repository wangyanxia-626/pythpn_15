# -*- coding:utf-8 -*-
# @Time :2020-03-07 21:10
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_unittest.PY
import unittest
from class_0307.http_request import HttpRequests
from ddt import ddt,data,unpack

@ddt
class TestHttp_Request(unittest.TestCase):

    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    @data(["get",{"mobilephone": "18688773467", "pwd": "123456"},"登录成功"],
          ["post",{"mobilephone":"","pwd":"123456"},"手机号不能为空"],
          ["get",{"mobilephone":"18688773467","pwd":"126"},"用户名或密码错误"],
          ["post",{"mobilephone":"18688773467","pwd":""},"密码不能为空"])
    @unpack
    def test_login_request(self,method,data,expected):
        res=HttpRequests().http_request(self.url,method,data).json()
        try:
            self.assertEqual(expected,res["msg"])
        except AssertionError as e:
            raise e




