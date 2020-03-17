# -*- coding:utf-8 -*-
# @Time :2020-03-16 8:51
# @Email :876417305@qq.com
# @Author :yanxia
# @File :re_study.PY
import re #解析正则表达式 查找 替换
from class_0313.common.config import config
# 正则表达式学习
data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
# 原本字符、元字符来组成
p = "#(.*?)#" # #表示开始和结束，.代表匹配除了换行符以外的任何字符，*表示匹配前面的多次
# m=re.search(p,data)#从任意位置找，找到就返回Match object 找不到就返回None
# #print(m.group(0))#返回表达式和租里面的内容match='#normal_user#'>打印是#normal_user#
# print(m.group(1))#只返回指定组的内容
# g=m.group(1)#获取到参数化的key
# v=config.get('case',g)#根据key去配置文件里面的值
# print(v)
# data_new=re.sub(p,v,data,count=1) #查找替换 count代表查找替换的次数
# print(data_new)
#ms=re.findall(p,data)#查找全部 返回列表
#print(m)
#print(ms)
# 如果要匹配多次，替换多次，使用循环来解决
while re.search(p,data):
    print(data)
    m = re.search(p, data)
    g = m.group(1)  # 获取到参数化的key
    v = config.get('case', g)  # 根据key去配置文件里面的值
    print(v)
    data=re.sub(p,v,data,count=1)
print("最后的data",data)
