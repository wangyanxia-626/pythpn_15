# -*- coding:utf-8 -*-
# @Time :2020-03-14 16:46
# @Email :876417305@qq.com
# @Author :yanxia
# @File :study_pymysql.PY
import pymysql
#建立连接：数据库的连接信息
host="test.lemonban.com"
user="test"
password="test"
port=3306
mysql=pymysql.connect(host=host,user=user,password=password,port=port)
#2、新建一个查询页面（用创建的一个链接，创建一个游标)
cursor=mysql.cursor()
#3、编写sql
#sql='select max(mobilephone) from future.member'
sql='select * from future.loan limit 10'
#4、执行sql
cursor.execute(sql)
#5、查看结果
result=cursor.fetchone()#获取查询结果集里面最近的一条返回数据
result=cursor.fetchall()#获取全部结果集
print(type(result),result)
#6、关闭查询
cursor.close()
#7、关闭数据库连接
mysql.close()
