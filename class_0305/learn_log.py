# -*- coding:utf-8 -*-
# @Time :2020-03-06 16:39
# @Email :876417305@qq.com
# @Author :yanxia
# @File :learn_log.PY
'''
logging是什么？作用是什么？日志 记录程序代码 操作
如何打印日志？利用logging模块输出自定义的日志

主要目的 我们要写一个自己的类
logging python自带 写日志模块
log的等级 debug  info  warning error critical/fatal从底到高
面试题：logging的等级有多少种
原理：收集啥都收 输出有区别 只输出info级别以上的且不包含info 输出渠道：控制台 指定文件file 默认的是控制台
步骤：
1/新建一个日志收集器文件logging.getLogger()
2/指定输出渠道 logging.StreamHandler()
3/addHandler拼接起来 把my_logger收集的数据添加到handler这个输出渠道
4/设置收集和输出指定信息的级别setlevel
5/收集日志
'''
import logging
my_logger=logging.getLogger()#新建日志收集器文件
my_logger.setLevel("DEBUG")#设定我们收集的级别
#设置输出的时候指定的格式
fmt=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s")

ch=logging.StreamHandler()#指定输出渠道
ch.setLevel("INFO")#设定输出信息的级别
ch.setFormatter(fmt)
#指定输出到文本渠道
file_hander=logging.FileHandler("py15.log")
file_hander.setLevel("DEBUG")
file_hander.setFormatter(fmt)

#配合关系
my_logger.addHandler(ch)#添加渠道，我把这个收集的数据添加到这个输出渠道
my_logger.addHandler(file_hander)

#收集日志
my_logger.debug("this is a debug msg")
my_logger.info("this is a info msg")
my_logger.warning("this is a warning msg")
my_logger.error("this is a error msg")
my_logger.critical("this is a critical msg")















