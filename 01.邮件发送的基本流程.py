import smtplib

# 用于创建邮件对象(真正用于发送的内容)
from email.mime.multipart import MIMEMultipart
# 邮件的主题
from  email.header import  Header
# 构建文本内容
from email.mime.text import MIMEText

# 1.连接邮箱服务器，登录邮箱
# 1.1) 连接邮箱服务器：smtplib.SMTP_SSL(邮箱连接地址，端口号)
# 163邮箱的连接地址：'smtp.163.com'
# qq邮箱的连接地址：'smtp.qq.com'
# 端口号：465/25
con = smtplib.SMTP_SSL('smtp.163.com',465) # 获取连接对象

# 1.2) 登陆邮箱
con.login('wang140736399_29@163.com', 'URJWQFMGOLLYPJYQ')

# 2.准备邮件发送内容
# 2.1) 创建邮件对象
msg = MIMEMultipart()

# 设置邮件主题
subject = Header('主题名','utf-8').encode()
msg['subject'] = subject

# 设置邮件发送人
msg['From'] = 'wang140736399_29@163.com <wang140736399_29@163.com>'

# 设置邮件的收件人，'收件人1;收件人2;...'
msg['To'] = '1550505935@qq.com'

# 设置邮件正文(邮件需要发送的内容)
# 普通文本:MIMEText(文字内容，文本类型[普通文本plain,超链接html,附件base64]，编码方式)
text = MIMEText('python-smtplib发送的邮件','plain','utf-8')
msg.attach(text)

# 3.发送邮件
# 连接对象.sendmail(发件人，收件人，字符串类型的邮件对象)
con.sendmail('wang140736399_29@163.com', '1550505935@qq.com', msg.as_string())
con.quit()