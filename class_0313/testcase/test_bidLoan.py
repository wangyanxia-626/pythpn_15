# -*- coding:utf-8 -*-
# @Time :2020-03-16 14:48
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_bidLoan.PY
import unittest
from ddt import ddt,data
from class_0313.common import do_excel
from class_0313.common import contants
from class_0313.common.http_request import HttpRequest2
from class_0313.common import context
from class_0313.common import do_mysql
from class_0313.common.context import Context
@ddt
class BidloanTeat(unittest.TestCase):
    excel=do_excel.DoExcel(contants.case_file,"bidLoan")
    cases=excel.get_cases()
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()
        cls.mysql = do_mysql.DoMysql()  # 为了避免资源浪费，所有的请求都在一个链接里面完成
    @data(*cases)
    def test_bidloan(self,case):
        print("开始执行测试",case.title)
        print(case.url)
        print(case.data)
        case.data=context.replace(case.data)
        resp=self.http_request.request(case.method,case.url,case.data)
        print(resp.text)
        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,"PASS")
            #增加数据库的操作，判断加标成功后，取到loan_id
            if resp.json()["msg"]=="加标成功":
                sql='select * from future.loan where MemberID=88538 order by id desc limit 1'
                loan_id=self.mysql.fetch_one(sql)[0]
                print("加标之后的标id",loan_id)
                #保存到类属性里面
                setattr(Context,"loan_id",str(loan_id))
        except Exception as e:
            self.excel.write_result(case.case_id+1,resp.text,"FAIL")
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()

#!!!!注意写sql语句的时候，一定要带上表名，不然就会报 pymysql.err.InternalError: (1046, 'No database selected')