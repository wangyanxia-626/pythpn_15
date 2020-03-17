# -*- coding:utf-8 -*-
# @Time :2020-03-10 14:03
# @Email :876417305@qq.com
# @Author :yanxia
# @File :http接口基础.PY
# api的全称---applications programming interface
'''
服务端：服务器、后端 处理请求被动
客户端：前端浏览器 手机app 硬件 发送请求 主动
常见的请求方法:get post put delete head patch options
user-agent 篡改消息头，用来伪装成浏览器发送请求
三次握手和四次挥手 tcp/ip   get 请求和post请求的区别
cookies的原理：请求一个网址，会派发一个会员卡cookie（session_id）,浏览器会自动保存cookies值，默认是关闭浏览器就没有了
第二次请求的时候会自动带上cookies
响应信息
响应状态码是：是http协议规定的
响应ststus_code是人为规定的
'''