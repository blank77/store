# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEMultipart()
# subject = 'Python SMTP 测试结果' # 标题
# message['From'] = Header("python测试工程师", 'utf-8')  # 邮件中显示的发件人别称
# message['To'] = Header("项目经理", 'utf-8')  # ...收件人...
# message['Subject'] = Header(subject, 'utf-8')
#
# sender = '1353163580@qq.com' # 发件人（自己的邮箱）
# receivers = ['2929388227@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# message.attach(MIMEText('测试文件', 'plain', 'utf-8'))
#
# # 构造附件1，传送当前目录下的文件
# att1 = MIMEText(open('计算器.html', 'rb').read(),'base64', 'utf-8')
# # 邮件内容
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="test.html"'
# message.attach(att1)
# try:
#     smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465) # 服务器地址 163邮箱"smtp.163.com"  qq邮箱"smtp.qq.com"都需要开通smtp权限
#     smtpObj.login(sender,"odeepudgxpeobadg") #授权码
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
#
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")


# ! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os

mailto_list = ['2929388227qq.com']  # 收件人列表，以英文逗号分隔
mail_host = "smtp.qq.com"  # 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user = "1353163580@qq.com"  # 发件人
mail_pass = "odeepudgxpeobadg"  # 授权码，不是密码，授权码要在邮箱设置中获取


# 参数：收件人，主题，正文，文件名集合（可发送多个文件），文件路径（文件在同一个路径）
def send_mail(sub, content, files, path):
    me = sub + "<" + mail_user + ">"
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(mailto_list)  # 将收件人列表以‘,’分隔
    for file in files:
        if os.path.isfile(path + '/' + file):  # 判断路径下是否是文件
            # 构造附件
            att = MIMEText(open(path + '/' + file, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header("Content-Disposition", "attachment", filename=("gbk", "", file))
            msg.attach(att)
    try:
        server = smtplib.SMTP()
        if mail_host == 'smtp.gmail.com':
            server.connect(mail_host, port=465)  # 连接服务器
            server.starttls()
        else:
            server.connect(mail_host)
        server.login(mail_user, mail_pass)  # 登录操作
        server.sendmail(me, mailto_list, msg.as_string())
        server.close()
        print('Mail sent successfully')  # 邮件已成功发送
        return True
    except Exception as e:
        print('Mail sent failed')  # 邮件发送失败
        print(sys.exc_info()[0], sys.exc_info()[1])
        return False

if __name__ == '__main__':
    files = ['1.xlsx', '2.txt']
    send_mail('', '', '', '')  # 发送/home/data文件夹下面两个文件

''' 参数：收件人，主题，正文，文件名集合（可发送多个文件），文件路径（文件在同一个路径）'''