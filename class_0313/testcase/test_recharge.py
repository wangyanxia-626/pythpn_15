# -*- coding:utf-8 -*-
# @Time :2020-03-13 16:33
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_recharge.PY
import unittest
from class_0313.common.http_request import HttpRequest2
from class_0313.common import do_excel
from class_0313.common import contants
from ddt import ddt, data
from class_0313.common.do_mysql import DoMysql

@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, "recharge")  # 引入这个excel文件
    cases = excel.get_cases()  # 获取excel的值


    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()  # 实例化sessio
        cls.mysql=DoMysql()

    @data(*cases)
    def test_recharge(self, case):
        print(case.title)
        #请求之前判断是否执行sql
        #如果执行的sql不是一条，可以用字典，或者列表
        if case.sql is not None:
            sql=eval(case.sql)['sql1']
            member=self.mysql.fetch_one(sql)#执行sql
            print(member['LeaveAmount'])
            before=member['LeaveAmount']#取sql里面的值，存到before这个变量里面
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected), actual_code)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
            #成功之后，判断是否执行SQL
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member['LeaveAmount'])
                after = member['LeaveAmount']
                recharge_amount=int(eval(case.data)['amount'])#充值金额
                self.assertEqual(before+recharge_amount,after)
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "FILE")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()  # 关闭session
