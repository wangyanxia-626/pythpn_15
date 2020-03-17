# -*- coding:utf-8 -*-
# @Time :2020-03-09 18:29
# @Email :876417305@qq.com
# @Author :yanxia
# @File :lujing.PY
# 文件的路径处理
import json
a={"memberId":88538,"title":"借款300万","amount":300000,"loanRate":18.0,"loanTerm":6,"loanDateType":0,"repaymemtWay":5,"biddingDays":10}
b=json.dumps(a)
print(type(b))
