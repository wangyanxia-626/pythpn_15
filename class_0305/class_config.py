# -*- coding:utf-8 -*-
# @Time :2020-03-06 21:15
# @Email :876417305@qq.com
# @Author :yanxia
# @File :class_config.PY
import logging
class LogCat:
    my_log=logging.getLogger()
    my_log.setLevel("DEBUG")
    fmt=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s")
    ch=logging.StreamHandler
    ch.setLevel("INFO")
    ch.setFormatter(fmt)
    my_log.addHandler(ch)
    def log_debug(self):
        log_dug=self.my_log.debug("这是debug信息")
        return log_dug
    def log_info(self):
        log_info = self.my_log.info("这是info信息")
        return log_info
    def log_warning(self):
        log_waring = self.my_log.warning("这是waring信息")
        return log_waring
    def log_error(self):
        log_error = self.my_log.error("这是error信息")
        return log_error
    def log_critical(self):
        log_critical = self.my_log.critical("这是log_critical信息")
        return log_critical

if __name__ == '__main__':
    t=LogCat()

    t.log_error()