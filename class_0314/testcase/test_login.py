# -*- coding:utf-8 -*-
# @Time :2020-03-13 15:05
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_login.PY
import unittest
from class_0314.common import do_excel
from class_0314.common import contants
from class_0314.common.http_request import HttpRequest2
from ddt import ddt, data
from class_0314.common import logger
logger=logger.get_logger(__name__)#__name__意思是把我在logger里面设置的case名字给这个用例用

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, "login")
    cases = excel.get_cases()
    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_login(self, case):
        logger.info("测试的title：{0}".format(case.title))
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "Fail")
            logger.error("测试报错了:{0}".format(e))
            raise e
        logger.info('结束测试：{0}'.format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info('测试结束后置处理')
        cls.http_request.close()
