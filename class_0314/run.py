# -*- coding:utf-8 -*-
# @Time :2020-03-23 13:16
# @Email :876417305@qq.com
# @Author :yanxia
# @File :run.py.PY
import sys
sys.path.append('./')#project跟目录
print(sys.path)
import unittest
import HTMLTestRunnerNew
from class_0314.common import contants
discover=unittest.defaultTestLoader.discover(contants.case_dir,'test_*.py')
with open(contants.report_dir +'/report.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            title="python 接口测试API",
                                            description='测试接口',
                                            tester='yanxia')
    runner.run(discover)