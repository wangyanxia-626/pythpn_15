# -*- coding:utf-8 -*-
# @Time :2020-03-07 16:21
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_suite.PY
# 第一种方法
import unittest
import HTMLTestRunnerNew
from class_0306.learn_unittest import *
#存储用例的容器suite 套件
suite=unittest.TestSuite()#创建了一个对象
suite.addTest(TestAdd(0,0,0,"test_add_zero"))#添加测试用例到suite这个套件里面
suite.addTest(TestAdd(1,-1,0,"test_add_zero"))
suite.addTest(TestAdd(99,10,109,"test_add_zero"))
#suite.addTest(TestAdd("test_add_positive_nagative"))
#
# #执行测试用例
# runner=unittest.TextTestRunner()#创建一个对象来
# runner.run(suite)


# #第二种方法 通过load加载用例,通过模块名加载用例
# from class_0306 import learn_unittest
# suite=unittest.TestSuite()#创建了一个对象
# loader=unittest.TestLoader()#用例的加载器
# suite.addTest(loader.loadTestsFromModule(learn_unittest))
 #执行测试用例
with open("test.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            title="自动化报告",
                                            verbosity=2,
                                            description="大家看下这是报告",
                                            tester="艳霞")
    runner.run(suite)

#第三种方法 通过load加载用例，通过测试类名来加载用例
# from class_0306.learn_unittest import *
# suite=unittest.TestSuite()#创建了一个对象
# loader=unittest.TestLoader()#用例的加载器
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))
#  #执行测试用例
# runner=unittest.TextTestRunner()#创建一个对象来
# runner.run(suite)

