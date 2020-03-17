# -*- coding:utf-8 -*-
# @Time :2020-02-28 22:29
# @Email :876417305@qq.com
# @Author :yanxia
# @File :home.PY
class User:
    frist_name="yanxia"
    last_name="wang"
    sex="女"
    heigh=162

    def describe_user(self):
        print("我叫{}{}，性别{}，身高{}".format(self.last_name,self.frist_name,self.sex,self.heigh))

    def greet_user(self,name,information):
        print("{}{}".format(name,information))
if __name__ == '__main__':
    t=User()
    t.describe_user()
    t.greet_user("hello","欢迎来到python的世界")
