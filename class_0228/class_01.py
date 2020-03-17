# -*- coding:utf-8 -*-
# @Time :2020-02-28 20:51
# @Email :876417305@qq.com
# @Author :yanxia
# @File :class_01.PY
class BoyFriend:#类
    sex='boy'
    height=180# 类属性

    def coding(self,language='python'):#类方法
        print("会写{}代码，并且写得很好".format(language))

    def cooking(self,*args):
        cook_name=""
        for item in args:
            cook_name+=item
            cook_name+="、"
        print("会做饭，会做{}".format(cook_name))

    def paly_basketball(self):
        return "最喜欢打篮球"

t=BoyFriend()#对象
print(t.height)
print(t.sex)
t.cooking('西红柿炒蛋','酸菜鱼')
t.coding()
print(t.paly_basketball())
