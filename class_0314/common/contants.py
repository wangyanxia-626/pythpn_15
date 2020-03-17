# -*- coding:utf-8 -*-
# @Time :2020-03-13 11:51
# @Email :876417305@qq.com
# @Author :yanxia
# @File :contants.PY
import os

# base_dir定义到class_0313
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取cases.xlsx
case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
#获取总开关路径
global_file=os.path.join(base_dir,'config','global.conf')
#获取线上
online_file=os.path.join(base_dir,'config','online.conf')
#获取测试
test_file=os.path.join(base_dir,'config','test.conf')
#获取数据库
db_dir=os.path.join(base_dir,'config','online.conf')
#获取存放日志信息的路径
log_dir=os.path.join(base_dir,'log')
#获取控制台日志级别的信息
console_level=os.path.join(base_dir,'config','online_file')
#获取log存放路径日志级别的信息
file_level=os.path.join(base_dir,'config','online_file')
#用例目录
case_dir=os.path.join(base_dir,'testcase')

#报告的目录
report_dir=os.path.join(base_dir,'reports')
