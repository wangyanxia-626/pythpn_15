# -*- coding:utf-8 -*-
# @Time :2020-03-07 21:55
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http_suit.PY
import unittest
import HTMLTestRunnerNew
from class_0307.http_unittest import *
from class_0307 import http_unittest2
class HttpSuite:
        def http_suite_runner_001(self):
                suite=unittest.TestSuite() #创建一个对象
                # 第一种执行方法
                suite.addTest(TestHttp_Request("test_login_normal"))
                # 执行并生成测试报告----HTMLTestRunnerNew
                with open("test_report.html", "wb") as file:
                        runner = HTMLTestRunnerNew.HTMLTestRunner(
                                stream=file,
                                verbosity=2,
                                title="我的第一次测试报告",
                                description="这是自动化线上测试报告",
                                tester="yanxia")
                        runner.run(suite)
        def http_suite_runner_002(self):
                suite = unittest.TestSuite()
                # 第二种执行方法
                loader=unittest.TestLoader()
                suite.addTest(loader.loadTestsFromModule(http_unittest2))
                # 执行并生成测试报告----HTMLTestRunnerNew
                with open("test_report.html", "wb") as file:
                        runner = HTMLTestRunnerNew.HTMLTestRunner(
                                stream=file,
                                verbosity=2,
                                title="我的第一次测试报告",
                                description="这是自动化线上测试报告",
                                tester="yanxia")
                        runner.run(suite)

        def http_suite_runner_003(self):
                #第三种执行方法
                suite = unittest.TestSuite()
                loader=unittest.TestLoader()
                suite.addTest(loader.loadTestsFromTestCase(TestHttp_Request))
                # 执行并生成测试报告----HTMLTestRunnerNew
                with open("test_report.html", "wb") as file:
                        runner = HTMLTestRunnerNew.HTMLTestRunner(
                                stream=file,
                                verbosity=2,
                                title="我的第一次测试报告",
                                description="这是自动化线上测试报告",
                                tester="yanxia")
                        runner.run(suite)
#执行用例并生成测试报告
# with open("file.text","a+") as file:
#         runner=unittest.TextTestRunner(stream=file,verbosity=2)
#         runner.run(suite)

if __name__ == '__main__':
    HttpSuite().http_suite_runner_002()
{'memberId':300986,'password':123456,'loanId':146828,'amount':80000}