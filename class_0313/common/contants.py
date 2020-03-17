# -*- coding:utf-8 -*-
# @Time :2020-03-13 11:51
# @Email :876417305@qq.com
# @Author :yanxia
# @File :contants.PY
import os

# base_dir定义到class_0313
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
# 获取cases.xlsx
case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
print(case_file)
#获取总开关路径
global_file=os.path.join(base_dir,'config','global.conf')
print(global_file)
#获取线上
online_file=os.path.join(base_dir,'config','online.conf')
print(online_file)
#获取测试
test_file=os.path.join(base_dir,'config','test.conf')
print(test_file)
db_dir=os.path.join(base_dir,'config','online.conf')