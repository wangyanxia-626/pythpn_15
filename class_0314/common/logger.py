# -*- coding:utf-8 -*-
# @Time :2020-03-17 9:10
# @Email :876417305@qq.com
# @Author :yanxia
# @File :logger.PY
'''日志模块'''
import logging
from class_0314.common import contants
from class_0314.common.config import config
def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel('DEBUG')
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-日志信息：%(message)s-[%(filename)s:%(lineno)d]")
    console_handler=logging.StreamHandler()#指定输出到控制台
    #把日志级别放到配置文件里面获取
    console_level=config.get('logger','console_level')
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)

    file_handler=logging.FileHandler(contants.log_dir+'/case.log')#指定输出到文件
    #把日志级别放到配置文件里面获取
    file_level = config.get('logger','file_level')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

logger=get_logger('case')
logger.info('测试开始啦')
logger.error('测试报错啦')
logger.debug('测试数据')
logger.info("测试结束")