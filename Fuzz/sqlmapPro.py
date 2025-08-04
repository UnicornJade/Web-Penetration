import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import  time

def sql():
    for root, dirs, files in os.walk("/opt/sql/", topdown=False):
        for name in files:
            path = os.path.join(root, name)
            cmd = 'python /opt/sqlmap/sqlmap.py -r '+ path +' --batch --dbms=mysql -v 3 --level 5 --risk 3 --skip="Host,User-Agent,Accept-Language,Referer,Cookie,"  --threads=10 > /opt/result/'+ name +'  2>&1 &'
            print(cmd)
            os.system(cmd)

def send_email():
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "@163.com"  # 用户名
    mail_pass = ""  # 口令

    sender = '@163.com'
    receivers = ['@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('完成测试', 'plain', 'utf-8')
    message['From'] = Header("test", 'utf-8')
    message['To'] = Header("test", 'utf-8')

    subject = '完成测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print
        "邮件发送成功"
    except smtplib.SMTPException:
        print
        "Error: 无法发送邮件"
sql()

while True:
    result = int(os.popen('ps aux | grep sqlmap | wc -l ').read())
    print(result)
    print(type(result))
    if result < 3 :
        send_email()
        break
    else:
        time.sleep(10)
