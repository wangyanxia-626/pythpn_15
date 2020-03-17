# -*- coding:utf-8 -*-
# @Time :2020-03-04 20:38
# @Email :876417305@qq.com
# @Author :yanxia
# @File :demo_conf.PY
from configparser import ConfigParser
#实例化类
cf=ConfigParser()
#读取conf文件:文件路径 编码方式
#相对路径
cf.read("demo.cfg",encoding="utf-8")
#绝对路径
# cf.read("C:\Users\10977\Desktop\剪切")
#读取所有的sections 以列表的形式存在
secs=cf.sections()
print(secs)
# 获取某一个sections下面的options 的值
# cf.options("db")
print(cf.options(secs[0]))
# 获取某一个section下面的某一个options的值
res=cf.get("db","db_port")#获取的所有结果都是字符串
print(res,type(res))
# 获取int类型的值 cf.getint
old =cf.getint("db","db_port")
print(old,type(old))
# 获取bool 类型的值
res1=cf.getboolean("excel","res")
print(res1,type(res1))

# 获取float类型的值
res2=cf.getfloat("excel","row")
print(res2,type(res2))


sex=cf.get("person_info","sex")
print(eval(sex))