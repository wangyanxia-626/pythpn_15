# -*- coding:utf-8 -*-
# @Time :2020-03-16 14:14
# @Email :876417305@qq.com
# @Author :yanxia
# @File :study_reflect.PY
class people:
    number_eye=2
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    p=people('mongo',18)
    print(people.number_eye)
    print(p.number_eye)
    print(getattr(people,"number_eye"))

    setattr(people,"number_leg",5)
    print(hasattr(people, 'number_leg'))
    #delattr(p,"number_leg")

