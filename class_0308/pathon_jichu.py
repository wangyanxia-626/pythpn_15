# -*- coding:utf-8 -*-
# @Time :2020-03-09 15:10
# @Email :876417305@qq.com
# @Author :yanxia
# @File :pathon_sade.PY
#变量
#数据类型：
#1.string 不可变类型
#boolean 条件判断或者逻辑控制的依据 多种运算形式的返回值
#list 有顺序的容器 可变的
#dict 是没有顺序的 可变的
#tuple元组 解包 不可变类型
'''
逻辑控制 流程控制 控制流程
条件：if。。。elif。。else
遍历 for。。。in
while
continue
break
函数
1、参数 形式参数，实际参数，位置参数，关键字参数，默认参数，动态参数
'''
#面试题1：range的特性：与列表非常相似的一种结构数据
# print(type(range(1,10)))
#面试题2：
#1.string 不可变类型,不支持修改
# str="myclass"
# str[2]="s"
# def run(a):
#     if a!=10:
#         return None
#     print("hell0")

# def add(a,mylist=[]):
#     mylist.append(a)
#     return mylist
# print(add(4))#添加完4以后，就变成了默认参数是[4]
# print(add(5))#有默认参数4以后，再加进来5
# print(add(6,["a"]))#传了个实际参数["a"],再加上一个.append的值，所以打印结果是：['a', 6]
# print(add(7))
"""
类和对象：是python里面最核心的  
"""
# class Movie:
#     works=["导演","演员","场记"]
#     def __init__(self,name):
#         self.works=[]
#         self.name=name
#
#     # def __new__(cls, *args, **kwargs):
#     #     pass
# print(Movie("琅琊榜").works)
# print(Movie.works)
try:
    1/0
    print("没出错")
except Exception as e:
    print("真的出错了")
    raise
finally:
    pass
# 文件处理