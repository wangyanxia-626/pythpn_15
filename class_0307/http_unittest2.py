# -*- coding:utf-8 -*-
# @Time :2020-03-09 12:31
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_unittest2.PY
import unittest
from class_0307.http_request import HttpRequests
from ddt import ddt,data,unpack
from class_0307.http_xlsx import get_datavalue
from class_0307.http_xlsx import write_result
@ddt
class TestHttp_Request(unittest.TestCase):
    @data(*get_datavalue())
    @unpack
    def test_login_request(self,url,method,data,expected,case_id):
        res=HttpRequests().http_request(url,method,data).json()
        try:
            self.assertEqual(expected,res["msg"])
        except AssertionError as e:
            row=int(case_id)+1
            write_result(row,"failed")
            raise e


