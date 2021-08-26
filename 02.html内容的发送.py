import smtplib
from email.mime.multipart import MIMEMultipart
from  email.header import  Header
from email.mime.text import MIMEText

con = smtplib.SMTP_SSL('smtp.163.com',465)
con.login('wang140736399_29@163.com', 'URJWQFMGOLLYPJYQ')

msg = MIMEMultipart()
subject = Header('发送html内容','utf-8').encode()
msg['subject'] = subject
msg['From'] = 'wang140736399_29@163.com <wang140736399_29@163.com>'
msg['To'] = '1550505935@qq.com'

# 构建html内容
content = """
<img src = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'>
<h1>我是正文的大标题</h1>
<h3>我是副标题</h3>
<p>我是邮件正文段落文字</p>
<a href = 'https://www.baidu.com'>点击跳转</a>
"""
html = MIMEText(content,'html','utf-8')
msg.attach(html)

con.sendmail('wang140736399_29@163.com', '1550505935@qq.com', msg.as_string())
con.quit()