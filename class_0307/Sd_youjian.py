# -*- coding:utf-8 -*-
# @Time :2020-03-10 15:49
# @Email :876417305@qq.com
# @Author :yanxia
# @File :email_colose.PY
import ssl
from smtplib import SMTP,SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
#配置各种邮件服务器
emailname="yanxia_626@163.com"
emailpwd="gdd610626wyx"
email_severs={"163.com":{"smtp":{"host":"smtp.163.com","port":25,"ssl_port":465}},}
#创建ssl context用于加密
context=ssl.create_default_context()
def parse_mail(mailname):
    """解析邮件名 返回对应的邮件服务商"""
    server_name=mailname.split("@")
    if len(server_name)==1:
        raise TypeError("email format error")
    server_name=server_name[-1]
    if server_name not in list(email_severs.keys()):
        raise NameError("no this emial server")
    sever=email_severs.get(server_name,"")
    return sever

class HttpEmail(SMTP):
    def __init__(self,mailname,pwd):
        self.mailname=mailname
        self.login(mailname,pwd)
    def mail_msg(self,msg,type="html",subject=""):
        """组装邮件正文"""
        msg=MIMEText(msg,type)
        msg["Subject"]="自动化的报告"
        return msg
    def send_email(self,to,msg,files=None,type="plain",subject=""):
        """
        发送邮件的主函数
        :param to: 发送给谁
        :param msg: 原始邮件数据
        :param files: 发送的附件文件路径
        :param type: 格式类型
        :param subject: 标题
        """
        total=MIMEMultipart()
        total["Subject"]=subject

        body=self.mail_msg(msg,type=type,subject=subject)
        total.attach(body)

        if files and isinstance(files,list):
            for fiename in files:
                file=MIMEApplication(open(fiename,"rb").read())
                file.add_header("Content-Disposition","attachment",fiename=fiename)
                #附件添加到总的里面
                total.attach(file)

        return self.send_email(self.mailname,to,total.as_string())

class MyEmailSSL(SMTP_SSL,HttpEmail):
    """SSL发送邮件"""
    def __init__(self,mail_name,pwd):
        self.mailname=mail_name
        server=parse_mail(mail_name).get("smtp","")
        super().__init__(server.get("host"),server.get("ssl_port"))
        super().login(mail_name,pwd)

if __name__ == '__main__':
    msg="""
    春暖花开的时候，
    希望一切都会好起来
    我想这是最好的结果
    """
    with HttpEmail(emailname,emailpwd) as mail:
        mail.send_email("yanxia_626@163.com",msg["demo.txt"],subject="告诉你一件好事儿")




