# -*- coding:utf-8 -*-
# @Time :2020-03-10 17:23
# @Email :876417305@qq.com
# @Author :yanxia
# @File :基础面试题.PY
# a=[1,2,3,5,7,"q",3]#去重复数
# def del_repeat(a):
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b
# print(del_repeat (a))

# a=["t","2","6","a"]
# print("".join(a))
# a_str=""
# for i in a:
#     a_str+=str(i)
# print(a_str)
# b="asdfghgkjhk"
# list_b=[]
# for i in b:
#     list_b.append(i)
# print(list_b)
# #字符串去重,并排序
# a="qwewrtadfqrewqwq"
# s=[]
# for i in a:
#     if i not in s:
#         s.append(i)
#     s.sort()
# print(s)
# a=['3']
# b=a
# c=a[:]
# a.append(10)
# print(a)
# print(b)
# print(c)
class A:
    a_intance=[]
    def __new__(cls):
        if cls.a_intance is None:
            cls.a_intance=super.__new__(cls)
            return cls.a_intance
        else:
            return cls.a_intance

    def __init__(self):
        pass
a=A()
print(id(A))
print(id(A))
print(id(A))
