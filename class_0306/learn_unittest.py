# -*- coding:utf-8 -*-
# @Time :2020-03-06 21:52
# @Email :876417305@qq.com
# @Author :yanxia
# @File :learn_unittest.PY
#单元测试
#类：属性、方法
#属性：类属性、类方法
#方法 类方法 静态方法 对象方法
# 单元测试时做什么呢？对某个功能去做测试，每一个功能都是封装在类里面
# ---类里面有属性和方法，单元测试测试的是方法：创建对象 调用方法  传参---通过传递多组数据来测试不同的情况
# 框架 unittest----pytest 断言：期望结果和实际结果的对比
import unittest
from class_0306.math_method import MathMethod
class TestAdd(unittest.TestCase):#测试类
    #没有测试用例 我们来加
    #测试用例：test开头
    def test_add_zero(self):
        #excepted=0#期望值
        print("a的值是：{}，b的值是{}，expected的值是{}".format(self.a,self.b,self.expected))
        res=MathMethod().add(self.a,self.b)
        #断言
        self.assertEqual(self.expected,res)
        print("test_add_zero")
    def test_add_positive_nagative(self):
        excepted=-2
        res=MathMethod().add(1,-3)
        #断言
        self.assertEqual(excepted,res)
        print("test_add_positive_nagative")
class TestSub(unittest.TestCase):
    def test_sub(self):
        excepted=1
        res=MathMethod().sub(2,1)
        self.assertEqual(excepted,res)
        print("执行的减法")





