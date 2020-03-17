# -*- coding:utf-8 -*-
# @Time :2020-03-05 17:44
# @Email :876417305@qq.com
# @Author :yanxia
# @File :read_config.PY
from configparser import ConfigParser
class ReadConfig:
    def __init__(self,conf_filepath,encoding="utf-8"):
        # 打开配置文件
        self.cf=ConfigParser()
        self.cf.read(conf_filepath,encoding)

    #获取sections
    def get_section(self):
        return self.cf.sections()
    #获取options
    def get_options(self,section):
        return self.cf.options(section)
    #获取str的值
    def get_strValue(self,section,option):
        return self.cf.get(section,option)
    #获取整数的值
    def get_intValue(self,section,option):
        return self.cf.getint(section,option)
    # 获取浮点数的值
    def get_floatValue(self, section, option):
        return self.cf.getfloat(section, option)
    # 获取布尔数的值
    def get_boolValue(self, section, option):
        return self.cf.getboolean(section, option)

if __name__ == '__main__':
    mf=ReadConfig("demo.cfg")
    db_mame=eval(mf.get_strValue("person_info","sex"))
    print(db_mame,type(db_mame))
    #db_port=mf.get_intValue("db","db_port")
    #print(db_port)
    section=mf.get_section()
    print(section)
    option=mf.get_options("excel")
    print(option)
