# -*- coding:utf-8 -*-
# @Time :2020-03-14 0:12
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_addproject.PY
import unittest
from ddt import ddt, data
from class_0313.common import do_excel
from class_0313.common import contants
from class_0313.common.config import config
from class_0313.common import context
from class_0313.common.http_request import HttpRequest2

@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, "add")  # 引入这个excel文件
    cases = excel.get_cases()  # 获取excel的值

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()  # 实例化sessio

    @data(*cases)
    def test_add(self, case):
        # 使用字典的方式替换
        # case.data = eval(case.data)
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #     case.data['mobilephone'] = config.get('case','normal_user')  # 拿到配置文件里面的的值，赋值给case.data
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
        #     case.data['pwd'] = config.get('case','normal_pwd')  # 拿到配置文件里面的值，赋值给case.data
        # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
        #     case.data['memberId'] = config.get('case','loan_member_id')  # 拿到配置文件里面的值，赋值给case.data
        # print(case.data)
        # print(case.title)
        case.data=context.replace(case.data)#使用context的replace函数做替换
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "FILE")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()  # 关闭session

