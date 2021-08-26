import smtplib
from email.mime.multipart import MIMEMultipart
from  email.header import  Header
from email.mime.text import MIMEText

con = smtplib.SMTP_SSL('smtp.163.com',465)
con.login('wang140736399_29@163.com', 'URJWQFMGOLLYPJYQ')

msg = MIMEMultipart()
subject = Header('发送文件附件','utf-8').encode()
msg['subject'] = subject
msg['From'] = 'wang140736399_29@163.com <wang140736399_29@163.com>'
msg['To'] = '1550505935@qq.com'

# 准备附件1
content1 = open('YX-SUP.xlsx','rb').read()
file1 = MIMEText(content1,'base64','utf-8')
file1['Content-Disposition'] = "attachment; filename='YX-SUP.xlsx'"
msg.attach(file1)

# 准备附件2
content2 = open('20210816组会.pptx','rb').read()
file2 = MIMEText(content2,'base64','utf-8')
file2['Content-Disposition'] = "attachment; filename='0816meeting.pptx'"
msg.attach(file2)

con.sendmail('wang140736399_29@163.com', '1550505935@qq.com', msg.as_string())
con.quit()