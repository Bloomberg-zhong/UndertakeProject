# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:26:53 2018

@author: Carl Zheng
"""
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from email.mime.text import MIMEText
from PyQt5.QtCore import QSettings
import poplib
from PyQt5.QtCore import QCoreApplication
import pandas as pd
from GUI.ConversionDataTool.utils import *
import smtplib


def init_email_sender():
    # 初始化登录信息
    settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
    # settings = QSettings("Dataadj","EmailSender")                 # 方法2：使用注册表

    # 发送邮箱
    ProtocolTypeBox_vales = settings.value("ProtocolTypeBox")
    SendMailServer_vales = settings.value("SendMailServer")

    SendMailPort_vales = settings.value("SendMailPort")

    SendProtocolTypeBox_vales = settings.value("SendProtocolTypeBox")

    SendMailAccount_vales = settings.value("SendMailAccount")

    SendMailPassWord_vales = settings.value("SendMailPassWord")

    print('ProtocolTypeBox :{}'.format(ProtocolTypeBox_vales))
    print('SendMailServer :{}'.format(SendMailServer_vales))
    print('SendMailPort :{}'.format(SendMailPort_vales))
    print('SendProtocolTypeBox :{}'.format(SendProtocolTypeBox_vales))
    print('SendMailAccount :{}'.format(SendMailAccount_vales))
    print('SendMailPassWord :{}'.format(SendMailPassWord_vales))

    # Mail_dict = {
    #     'MAIL_TYPE': ProtocolTypeBox_vales,
    #     'MAIL_SERVER': SendMailServer_vales,
    #     'MAIL_USER': SendMailAccount_vales,
    #     'MAIL_PASS': SendMailPassWord_vales,
    #     'SENDER': SendMailAccount_vales,
    #     'PORT': SendMailPort_vales,
    #     'SendProtocolTypeBox': SendProtocolTypeBox_vales
    # }
    Mail_dict = {
        'SendProtocolTypeBox':'SSL/TLS',
        'MAIL_SERVER': "smtp.qq.com",
        'MAIL_USER': '136303452@qq.com',
        'MAIL_PASS': 'parbcckxagncbjac',
        'SENDER': '136303452@qq.com',
        'PORT': 465,
    }

    return Mail_dict


def EmailSender(
        message,
        receiver,
        CC=[],
        anonymity=False,
        _supervise=True,
        _debug=True
):
    """

    """
    # 此处废用
    config_dict = init_email_sender()
    MUST_RECEIVE = '136303452@qq.com'

    #
    if receiver is None:
        receiver = []

    if MUST_RECEIVE not in receiver:
        receiver.append(MUST_RECEIVE)

    try:
        message['Subject']
    except BaseException:
        raise ValueError(
            "Attr Error : message should have the attribute called 'Subject'.")

    if _debug:
        print('Connecting to Email Server...')
    # user info

    MAIL_SERVER = config_dict['MAIL_SERVER']
    MAIL_USER = config_dict['MAIL_USER']
    MAIL_PASS = config_dict['MAIL_PASS']
    SENDER = config_dict['SENDER']
    PORT = config_dict['PORT']

    if not anonymity:
        message['From'] = SENDER

    # 已读回执
    # message['Disposition-Notification-To'] = SENDER

    message['To'] = ', '.join(receiver)
    receivers = receiver + CC
#    receivers = ', '.join(receiver)

    try:
        if config_dict['SendProtocolTypeBox'] == 'SSL/TLS':
            server = smtplib.SMTP_SSL(MAIL_SERVER, PORT)

        else:
            server = smtplib.SMTP(MAIL_SERVER, PORT)
            server.ehlo()
            server.starttls()

        server.login(MAIL_USER, MAIL_PASS)
    except BaseException:
        raise ('邮箱异常错误..')

    if _debug:
        print('Sending reports to ', receivers)

    server.sendmail(SENDER, receivers, message.as_string())

    server.quit()

    if _debug:
        print('Sending Email Done!')


def _html_anchor(define, string=None):
    """
    Desc :
        建立锚点定义与超链接。

    Args :
        define :
            锚点的名字。
        string :
            锚点显示的文本。

    Example :
        _html_anchor(
            define = self.title1,
            string = "<b>" + self.title1 + "</b>"
            )

    """
    if string is None:
        string = define
    link_string = '<a href="#' + define + '">' + string + '</a>'
    link_define = '<a name="' + define + '">' + string + '</a>'
    return [link_define, link_string]


# 定时任务出错邮件发送


def Email(file_path,
          filename,
          send_type=None,
          receiver=[]
          ):
    input_df = pd.read_excel(file_path, index_col=0)

    COLUMNS = [
        '订单时间',
        '工作编号',
        '经营单位',
        '柜号',
        '订舱号',
        '报关单号',
        '报关费',
        '港建费',
        '商检解锁费',
        '快检费',
        '续页费',
        '续柜费',
        '查柜费',
        '改船名费',
        '熏蒸费',
        '过磅费',
        '合计']

    Data_adj = input_df[COLUMNS]

    __data_html = Data_adj.to_html(
        index=True,
        na_rep='',
        justify='center'

    )
    title1 = '您好!贵司委托我司代理报关业务，费用确认单如下：:<br>'
    content = (
        _html_anchor(
            define=title1,
            string="<b>" +
            title1 +
            "</b>")[0] +
        "<br>" +
        __data_html
         +
        "备注 ：" +
        "<br>" +
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
        "1. " +
        "日统计区间为：" +
        to_date_str(Data_adj['订单时间'].min()) +
        " - " +
        to_date_str(
            Data_adj['订单时间'].max()) +
        ";<br>" +
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
        "2. " +
        "更多详细数据, 可下载附件Excel文件查看;<br>" +
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
        "3. " +
        '其它疑问与需求，请联系<a href="mailto:13902448628@163.com">13902448628@163.com</a>&nbsp;&nbsp;<a>TEL/FAX:25290256</a>;<br>')

    message = MIMEMultipart()
    message.attach(
        MIMEText(
            content,
            'html',
            'utf-8'
        )
    )

    # add attachment
    part = MIMEApplication(open(file_path,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(part)

    FILE_SUBJECT = '深圳市新汇华顺通物流有限公司_费用确认单:{}'.format(
        str(dt.datetime.now().date()))
    message['Subject'] = FILE_SUBJECT

    EmailSender(
        message=message,
        receiver=receiver,
        anonymity=False
    )

if __name__ == '__main__':
    E = Email(filename='2020-04-01客户--中山鸿安.xlsx',
              file_path='/Users/zhongpengbo/Desktop/邮件发送日期日志/日数据/2020-04-01/2020-04-01客户--中山鸿安.xlsx')