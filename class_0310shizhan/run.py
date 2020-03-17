# -*- coding:utf-8 -*-
# @Time :2020-03-17 10:42
# @Email :876417305@qq.com
# @Author :yanxia
# @File :run.PY
import unittest
from class_0314.testcase import test_login
import HTMLTestRunnerNew
from class_0314.common import contants
# suite=unittest.TestSuite()#生成一个测试套件对象
# loader=unittest.TestLoader()#通过这个测试loader去加载这个测试套件
# suite.addTests(loader.loadTestsFromModule(test_login))

discover=unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")

with open(contants.report_dir+"/report.html","wb+") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title="python报告",
                                            description="前程贷",
                                            tester="yanxia")
    runner.run(discover)