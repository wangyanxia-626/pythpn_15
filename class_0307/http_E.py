# -*- coding:utf-8 -*-
# @Time :2020-03-09 21:34
# @Email :876417305@qq.com
# @Author :yanxia
# @File :send_email.PY
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class SendEmail:

    def __init__(self):
        self.mailhost='smtp.163.com'
        self.emailname = 'yanxia_626@163.com'
        self.emailpwd = 'gdd610626wyx'
        self.sendto = 'yanxia_626@163.com'
        self.subject= 'python邮件测试'
        self.msg_from = 'yanxia_626@163.com'
        self.port=465
        self.msg_raw="""<p>Python 邮件发送测试...</p>
            <p><a href="https://www.ketangpai.com/Home/User/login.html">点击</a></p>
            """#内容
    def send_email(self):
        # 总的邮件内容，分为不同的模块
        msg_total = MIMEMultipart()
        #正文模块
        msg_raw = self.msg_raw
        msg=MIMEText(msg_raw,'html','utf-8')
        msg_total['Subject']= self.subject
        msg_total['From']= self.msg_from
        msg_total['To']= self.sendto
        msg_total.attach(msg)
        #附件模块
        mfile = MIMEApplication(open('demo.txt','rb').read())
        #修改添加附件的头信息
        mfile.add_header('Content-Dispostion','attachment',file_name = 'demo.txt')
        mfile.add_header('Content-ID', '<0>')
        mfile.add_header('X-Attachment-Id', '0')
        #附件模块添加到总的模块里面
        msg_total.attach(mfile)
        server = smtplib.SMTP_SSL(self.mailhost,self.port)
        # 登录 参数为用户名密码
        server.login(self.emailname, self.emailpwd)
        try:
            server.send_message(self.emailname,self.sendto, msg_total.as_string())
            print("发送成功")
        except Exception as e:
            print("发送失败")
            raise e
        finally:
            server.quit()

if __name__ == '__main__':
    send=SendEmail()
    send.send_email()
