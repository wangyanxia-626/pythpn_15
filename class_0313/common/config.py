# -*- coding:utf-8 -*-
# @Time :2020-03-13 21:46
# @Email :876417305@qq.com
# @Author :yanxia
# @File :config.PY
import configparser
from class_0313.common import contants
class ReadConfig:
    '''完成配置文件的读取'''
    def __init__(self):
        self.config=configparser.ConfigParser()#实例化这个ConfigParser()类
        self.config.read(contants.global_file)#先加载global里面的
        switch=self.config.getboolean("switch","on")
        if switch:#如果开关打开为True，使用online的配置
            self.config.read(contants.online_file)
        else:#开关关闭的时候用test
            self.config.read(contants.test_file)
    def get(self,section,option):
        return self.config.get(section,option)

config=ReadConfig()

# if __name__ == '__main__':
#     config=ReadConfig()
#     print(config.get("api","pre_url"))

