import smtplib
from email.mime.multipart import MIMEMultipart
from  email.header import  Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

con = smtplib.SMTP_SSL('smtp.163.com',465)
con.login('wang140736399_29@163.com', 'URJWQFMGOLLYPJYQ')

msg = MIMEMultipart()
subject = Header('发送带图片的内容','utf-8').encode()
msg['subject'] = subject
msg['From'] = 'wang140736399_29@163.com <wang140736399_29@163.com>'
msg['To'] = '1550505935@qq.com'

# 发送图片作为附件
# MIMEImage(图片二进制数据)
image_data1 = open('image1.jpg','rb').read()
image1 = MIMEImage(image_data1)
# 设置附件名
image1['Content-Disposition'] = "attachment;filename='image1.jpg'"
# 添加到邮件附件
msg.attach(image1)

# 发送图片作为内容(需要使用html内容来发送)
image_data2 = open('image2.jpg','rb').read()
image2 = MIMEImage(image_data2)
image2.add_header('Content-ID','<test1>')  # 设置一个ID在html中调用
msg.attach(image2)

content = '''
<p>这是一条发送图片的邮件</p>
<img src='cid:test1'>
'''
html = MIMEText(content,'html','utf-8')
msg.attach(html)

con.sendmail('wang140736399_29@163.com', '1550505935@qq.com', msg.as_string())
con.quit()