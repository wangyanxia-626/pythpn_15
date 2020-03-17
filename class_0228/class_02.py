# -*- coding:utf-8 -*-
# @Time :2020-02-28 22:47
# @Email :876417305@qq.com
# @Author :yanxia
# @File :class_02.PY
# 手机
# 属性：价格 品牌 颜色 尺寸
# 方法：打电话 发短信 听音乐
class Phone:
    #手机属性
    # color="black"
    # price=4500
    # brand="oppo"
    # size="5.5"
    #初始化方法-参数化-魔法方法
    def __init__(self,color,price,brand,size):
        self.color=color
        self.price=price #加了self就是对象属性
        self.brand=brand
        self.size=size


    #类方法
    @classmethod
    def call(cls,tell_number):
        print("拨号{}，开始打电话".format(tell_number))
    def send_message(self,tell_number,content):
        print("给{}，发短信：{}".format(tell_number,content))
    def watch_tv(self,*args):
        app=""
        for item in args:
            app+=item
            app+="、"
        print("可以利用这些APP看电视，比如说：{}看电视".format(app))
    def take_shoot(self):
        print("拍照")

    @staticmethod
    def add(a,b):
        print(a+b)
    def phone_info(self):
        print("颜色{}，品牌{}，价格{}，尺寸{}".format(self.color,self.brand,self.price,self.size))

if __name__ == '__main__':
    # t = Phone()
    t=Phone("red","vivo",500,"5.0")#有初始化方法的时候，调用时，必须传参数
    # t.add(4,5)
    # t.take_shoot()
    # t.watch_tv("爱奇艺","腾讯")
    # t.send_message("18394428623","上课啦")
    # t.phone_info()
    Phone.call("178272821")