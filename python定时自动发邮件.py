import time
import schedule as schedule
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

def send_email():
    try:
        # 设置邮箱的域名
        HOST = 'smtp.163.com'
        # 设置邮件标题
        SUBJECT = '工作汇报'
        # 设置发件人邮箱
        FROM = 'wang140736399_29@163.com'
        # 设置收件人邮箱，可以同时发送到多个邮箱（用list）
        TO = '1550505935@qq.com'
        # 设置附件模式
        message = MIMEMultipart()

        ''' 添加正文 '''
        content = 'sir，附件为最新日期文件，请查收！'
        content_msg = MIMEText(content,'plain','utf-8')
        message.attach(content_msg)

        ''' 添加word文件附件 '''
        doc = '大气化学动力学.docx'
        doc_file = MIMEApplication(open(doc, 'rb').read())
        doc_file.add_header('Content-Disposition', 'attachment', filename=doc)
        message.attach(doc_file)

        ''' 添加pdf文件附件 '''
        pdf = 'zhao2004.pdf'
        pdf_file = MIMEApplication(open(pdf, 'rb').read())
        pdf_file.add_header('Content-Disposition', 'attachment', filename=pdf)
        message.attach(pdf_file)

        ''' 添加表格文件附件 '''
        csv_file = open('YX-SUP.xlsx', 'rb').read()
        csv = MIMEApplication(csv_file)
        csv.add_header('Content-Disposition', 'attachment', filename='YX-SUP.xlsx')
        message.attach(csv)

        ''' 添加图片文件附件 '''
        image_file = open('image1.jpg', 'rb').read()
        image = MIMEImage(image_file)
        image.add_header('Content-Disposition', 'attachment', filename='imag1.jpg')
        message.attach(image)

        # 设置邮件发件人
        message['From'] = 'wang140736399_29@163.com <wang140736399_29@163.com>'
        # 设置邮件收件人
        message['To'] = TO
        # 设置邮件标题
        message['Subject'] = SUBJECT

        # 获取SSL证书
        email_client = smtplib.SMTP_SSL(HOST,465)
        # 设置域名和端口，端口为465
        # email_client.connect(HOST, 465)
        # 邮箱授权码
        email_client.login(FROM, 'URJWQFMGOLLYPJYQ')
        email_client.sendmail(from_addr=FROM, to_addrs=TO, msg=message.as_string())
        # 关闭邮件发送客户端
        email_client.quit()
        print('发送成功！')
    except:
        print('发送失败！')

if __name__ == '__main__':

    # 每1分钟执行一次任务:
    schedule.every(1).minutes.do(send_email)
    # 每小时执行一次任务:
    # schedule.every().hour.do(send_email)
    # 每天在什么时间点执行一次任务:
    # schedule.every().day.at('10:30').do(send_email)
    # 每10-20分钟(随机)执行一次任务:
    # schedule.every(10).to(20).minutes.do(send_email)
    # 每周一执行一次任务:
    # schedule.every().monday.do(send_email)
    # 每周一什么时间点执行一次任务:
    # schedule.every().monday.at('09:30').do(send_email)
    # 每分钟在第45秒的时候执行任务:
    # schedule.every().minute.at(':45').do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1) #防止运算速度过快，添加等待。如果不添加可能会导致计算机卡顿。Cpu直线飙升