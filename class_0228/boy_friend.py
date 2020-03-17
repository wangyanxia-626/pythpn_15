# -*- coding:utf-8 -*-
# @Time :2020-02-28 21:08
# @Email :876417305@qq.com
# @Author :yanxia
# @File :boy_friend.PY
class BoyFriend:#类
    sex='boy'
    height=180# 类属性
    @staticmethod# 静态方法
    def coding(language='python'):#类方法
        print("会写{}代码，并且写得很好".format(language))
    def cooking(self,*args):
        cook_name=""
        for item in args:
            cook_name+=item
            cook_name+="、"
        print("会做饭，会做{}".format(cook_name))
    @classmethod#类方法
    def paly_basketball(cls):
        print("我男朋友的身高是{}：".format(cls.height))
        print("最喜欢打篮球")
        cls.coding()
        cls().cooking()
    def print_self(self):#对象方法：只能对象来调用
        print("self",self)
        print("男票的身高是{}".format(self.height))
        self.cooking("麻辣烫","小炒肉")
        self.paly_basketball()
        self.coding()


x=BoyFriend()
#BoyFriend.print_self()# 对象方法只能由对象来调用，不然就会报错 TypeError: print_self() missing 1 required positional argument: 'self'
# BoyFriend.paly_basketball()#类调用
#x.paly_basketball()#对象调用
# BoyFriend.coding()#类调用
x.coding()#对象调用
#x.paly_basketball()
#x.print_self()

#x.cooking("niurou")
