# -*- coding:utf-8 -*-
# @Time :2020-02-29 11:09
# @Email :876417305@qq.com
# @Author :yanxia
# @File :class_03.PY
# 继承 拓展 重写
# 新加了支付功能
from class_0228.class_02 import Phone
class Phone_1(Phone): #括号里面的是父类 Phone_1是子类
    # def __init__(self): #如果子类有自己的初始化，就不用继续使用父类的初始化,同样调用有用到父类里面的初始化函数的类时，就会报错
    #     pass
    def phone_info(self):# 重写 父类以前有的，子类进行重写（如果子类与父类有重名函数，那么子类的操作就叫重写）
        print("这是一款智能手机")#重写的生效范围只在子类里面
    @classmethod
    def pay(cls):# 子类的方法，子类的拓展 如果子类里面有父类没有的方法，那么子类的操作就叫做拓展
        print("可以支付")
# 子类可以拥有父类里面的所有属性所有方法--就可以直接调用
if __name__ == '__main__': #导入模块
    Phone_1.call("18989013321")
    t=Phone_1("red","vivo",500,"5.0")
    t.call("19989013321")
    t.pay()# 要不要传参，主要是看有没有把父类的初始化方法继承过来，如果
    Phone_1.pay()    #父类有初始化函数，那子类对象调用就一定要传参
    t.phone_info()
 
