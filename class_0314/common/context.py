# -*- coding:utf-8 -*-
# @Time :2020-03-16 10:18
# @Email :876417305@qq.com
# @Author :yanxia
# @File :context.PY
#上下文处理
import re
from class_0314.common.config import config
import configparser


class Context:
    loan_id=None
def replace(data):
    p="#(.*?)#"#正则表达式
    while re.search(p,data):#从任意位置开始找，找第一个就返回Match object ,如果没找到就返回false
        m=re.search(p,data)#拿到参数化的key
        g=m.group(1)
        try:
            v=config.get("case",g)#根据key取配置文件里面的值
        except configparser.NoOptionError as e:#如果配置文件里面没有，取context里面取
            if hasattr(Context,g):
                v=getattr(Context,g)
            else:
                print("找不到参数化的值")
                raise e
        print(v)
        data = re.sub(p, v, data, count=1)
    return data
