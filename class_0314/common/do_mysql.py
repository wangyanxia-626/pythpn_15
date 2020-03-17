# -*- coding:utf-8 -*-
# @Time :2020-03-14 17:31
# @Email :876417305@qq.com
# @Author :yanxia
# @File :do_mysql.PY
import pymysql
from class_0314.common.config import config
class DoMysql:
    ''' 完成与mysql数据库的交互'''

    def __init__(self):
        #把这些参数放到配置文件里面，然后读取配置文件里面的值
        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        # port = 3306
        host=config.get("db","host")
        user = config.get("db", "user")
        password = config.get("db", "password")
        port = config.get("db", "port")
        self.mysql = pymysql.connect(host=host,user=user,password=password,port=int(port))
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)#创建游标的时候创建一个字典类型的游标
        #self.cursor = self.mysql.cursor()
    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()
    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def fetch_many(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchmany()
    def close(self):
        self.cursor.close()#关闭游标
        self.mysql.close()#关闭连接

if __name__ == '__main__':
   mysql=DoMysql()
   #result=mysql.fetch_one('select max(mobilephone) from future.member')
   result=mysql.fetch_one('select * from future.loan where MemberID=88538 order by id desc limit 1')
   print(result)
   mysql.close()