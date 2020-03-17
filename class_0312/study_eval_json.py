# -*- coding:utf-8 -*-
# @Time :2020-03-12 20:42
# @Email :876417305@qq.com
# @Author :yanxia
# @File :study_eval_json.PY
import json
params='{"status":0,"code":"20103","data":null,"msg":"手机号不能为空"}'
#json.loads()
# d=eval(params)
# print(d["pwd"])
d1=json.loads(params)
print(type(d1),d1)