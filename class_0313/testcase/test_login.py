# -*- coding:utf-8 -*-
# @Time :2020-03-13 15:05
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_login.PY
import unittest
from class_0313.common import do_excel
from class_0313.common import contants
from class_0313.common.http_request import HttpRequest2
from ddt import ddt, data, unpack

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, "login")
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_login(self, case):
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "Fail")
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
