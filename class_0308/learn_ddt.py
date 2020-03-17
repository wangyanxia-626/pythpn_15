# -*- coding:utf-8 -*-
# @Time :2020-03-08 15:24
# @Email :876417305@qq.com
# @Author :yanxia
# @File :learn_ddt.PY
import unittest
from ddt import ddt,data,unpack

@ddt #@ddt装饰测试类unittest.TestCase的子类
class TestAdd(unittest.TestCase):
    # data里面的数据传进来是一个元组，共有一个元素，执行一条用例
    # data加上*,变成了元组，有3个元素，执行3条用例
    #unpack 根据逗号来进行拆分，变成了3个参数，测试方法就要用三个参数接收
    # @data(*[[0,0,0],[1,1,2],[-2,-1,-1]]) #data装饰我们的方法 跟for循环一样遍历每个数据 传递给被装饰的方法的参数 有几条数据就执行几次用例
    # @unpack
    # def test_001(self,a,b,expected):
    #     print("a的值是：",a)
    #     print("b的值是：",b)
    #     print("expected的值是:",expected)


     # @data(*[{"a":0,"b":0,"expected":0},{"a":1,"b":0,"expected":1},{"a":-10,"b":8,"expected":-2}])
     # @unpack   #字典进行拆分是针对每一条用例的数据进行拆分
     # def test_add_zero(self,a,b,expected):#如果是字典话，要用它的key作为参数来进行数据的接收
     #     print("a的值是：",a)
     #     print("b的值是：",b)
     #     print("excepted的值是：",expected)

    # 如果参数长短不一样，可以用默认值如：d=None这样的默认参数
     @data(*[[0,0,0,4],[1,1,2]])  # data装饰我们的方法 跟for循环一样遍历每个数据 传递给被装饰的方法的参数 有几条数据就执行几次用例
     @unpack
     def test_001(self,a,b,expected,d=None):
         print("a的值是：",a)
         print("b的值是：",b)
         print("expected的值是:",expected)
         print("d的值是:",d)
