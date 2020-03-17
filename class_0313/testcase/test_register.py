# -*- coding:utf-8 -*-
# @Time :2020-03-13 16:33
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_register.PY
import unittest
from class_0313.common.http_request import HttpRequest2
from class_0313.common import do_excel
from class_0313.common import contants
from ddt import ddt, data
from class_0313.common import do_mysql

@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, "register")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql=do_mysql.DoMysql()#为了避免资源浪费，所有的请求都在一个链接里面完成

    @data(*cases)
    def test_register(self, case):
        if case.data.find('register_mobile')>-1:#如果find没找到这个'register_mobile'，就返回-1
            sql='select min(mobilephone) from future.member'
            min_phone=self.mysql.fetch_one(sql)[0]#查询最大/最小手机号,fetch-one返回的是一个元祖
            #最大手机号码+1，从字符串转成int+1
            max_phone=int(min_phone) + 18
            case.data=case.data.replace('register_mobile',str(max_phone))#替换参数值，字符串是不可变数组，
                                                                         # 会生成一个新的值，不能再原有的上面替换，所以要给一个case.data值接收
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "FAIL")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()#关闭数据库的连接
