# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2020/6/11 3:38 下午
@Author  : Bloomberg zhong
@Email   : z136303452@hotmail.com
@Software: PyCharm
"""
import sys
import pandas as pd
import numpy as np
from GUI.ConversionDataTool.utils import *
# from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.ConversionDataTool.MainWindow import Ui_MainWindow
from GUI.ConversionDataTool.GeneralSender import Sender_Dialog
from GUI.ConversionDataTool.Data import ReportGeneraler


class MainWindow(QMainWindow, Ui_MainWindow,):
    def __init__(self, parent=None, _debug=True):
        super(MainWindow, self).__init__(parent)

        # GeneralSenderWindows
        self.setupUi(self)
        # 邮件发送子窗口

        self._debug = _debug
        self.init_output_filepath()
        self.init_email_sender()
        self.EmailSaveButton.clicked.connect(self.save_email_setting)
        self.ChooseFileButon.clicked.connect(self.openfile)
        self.ChooseFileButon.clicked.connect(self.creat_table_show)
        self.FreshDataButton.clicked.connect(self.refresh_display)
        self.OutputFilsePathButton.clicked.connect(self.save_output_filepath)
        self.DailyDataButton.clicked.connect(self.save_output_daily_file)
        self.WeeklyDataButton.clicked.connect(self.save_output_weekly_file)
        self.MonthDataButton.clicked.connect(self.save_output_month_file)
        self.SendMail.clicked.connect(self.openDialog)

    def init_output_filepath(self):
        # 初始化登录信息
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("Dataadj","Filepath")                 #
        # 方法2：使用注册表
        self.output_path = settings.value("outputfilepath")
        if self.output_path is None:
            self.output_path = GetDesktopPath()
        if self._debug:
            print(self.output_path)

    def init_email_sender(self):
        # 初始化登录信息
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("Dataadj","EmailSender")                 #
        # 方法2：使用注册表

        ProtocolTypeBox_vales = settings.value("ProtocolTypeBox")
        self.ProtocolTypeBox.setCurrentText(ProtocolTypeBox_vales)

        TakeEmailServer_vales = settings.value("TakeEmailServer")
        self.TakeEmailServer.setText(TakeEmailServer_vales)

        EmailAccountID_vales = settings.value("EmailAccountID")
        self.EmailAccountID.setText(EmailAccountID_vales)

        EmailPassWord_vales = settings.value("EmailPassWord")
        self.EmailPassWord.setText(EmailPassWord_vales)

        Port_vales = settings.value("Port")
        self.Port.setText(Port_vales)

        EncryptionButton_vales = settings.value("EncryptionButton")
        self.EncryptionButton.setCurrentText(EncryptionButton_vales)

        # 发送邮箱
        SendMailServer_vales = settings.value("SendMailServer")
        self.SendMailServer.setText(SendMailServer_vales)

        SendMailPort_vales = settings.value("SendMailPort")
        self.SendMailPort.setText(SendMailPort_vales)

        SendProtocolTypeBox_vales = settings.value("SendProtocolTypeBox")
        self.SendProtocolTypeBox.setCurrentText(SendProtocolTypeBox_vales)

        SendMailAccount_vales = settings.value("SendMailAccount")
        self.SendMailAccount.setText(SendMailAccount_vales)

        SendMailPassWord_vales = settings.value("SendMailPassWord")
        self.SendMailPassWord.setText(SendMailPassWord_vales)

        if self._debug:
            print('ProtocolTypeBox :{}'.format(ProtocolTypeBox_vales))
            print('TakeEmailServer :{}'.format(TakeEmailServer_vales))
            print('EmailAccountID :{}'.format(EmailAccountID_vales))
            print('EmailPassWord :{}'.format(EmailPassWord_vales))
            print('Port :{}'.format(Port_vales))
            print('EncryptionButton :{}'.format(EncryptionButton_vales))
            print('SendMailServer :{}'.format(SendMailServer_vales))
            print('SendMailPort :{}'.format(SendMailPort_vales))
            print('SendProtocolTypeBox :{}'.format(SendProtocolTypeBox_vales))
            print('SendMailAccount :{}'.format(SendMailAccount_vales))
            print('SendMailPassWord :{}'.format(SendMailPassWord_vales))

    def refresh_display(self):
        # 重新数据界面并进行调整
        if hasattr(self, 'path_openfile_name'):
            if len(path_openfile_name) > 0:
                if self._debug:
                    print(self.path_openfile_name)
                self.ExcelFilesState.setText(
                    '{:<40}'.format(self.path_openfile_name))
        else:
            print('Not choose File!')
            self.ExcelFilesState.setText('{:<40}'.format(u'没有选择文件'))
            self.openfile()
            self.creat_table_show()

    def save_output_filepath(self):
        output_filepath = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("Dataadj", "Filepath")  # 方法2：使用注册表
        settings.setValue("outputfilepath", output_filepath)
        self.init_output_filepath()

    def save_email_setting(self):
        settings = QSettings("config.ini", QSettings.IniFormat)
        # 接受邮箱地址
        # settings = QSettings("Dataadj", "EmailSender")
        settings.setValue(
            "ProtocolTypeBox",
            self.ProtocolTypeBox.currentText())
        settings.setValue("TakeEmailServer", self.TakeEmailServer.text())
        settings.setValue("EmailAccountID", self.EmailAccountID.text())
        settings.setValue("EmailPassWord", self.EmailPassWord.text())
        settings.setValue("Port", self.Port.text())
        settings.setValue(
            "EncryptionButton",
            self.EncryptionButton.currentText())

        # 发送邮箱
        settings.setValue("SendMailServer", self.SendMailServer.text())
        settings.setValue("SendMailPort", self.SendMailPort.text())
        settings.setValue(
            "SendProtocolTypeBox",
            self.SendProtocolTypeBox.currentText())
        settings.setValue("SendMailAccount", self.SendMailAccount.text())
        settings.setValue("SendMailPassWord", self.SendMailPassWord.text())

        if self._debug:
            print(self.ProtocolTypeBox.currentText())
            print(self.TakeEmailServer.text())
            print(self.EmailAccountID.text())
            print(self.EmailPassWord.text())
            print(self.Port.text())
            print(self.EncryptionButton.currentText())
            print(self.SendMailServer.text())
            print(self.SendMailPort.text())
            print(self.SendProtocolTypeBox.currentText())
            print(self.SendMailAccount.text())
            print(self.SendMailPassWord.text())

        # self.init_email_sender()

    def save_output_daily_file(self,):
        self.init_output_filepath()
        if hasattr(self, 'path_openfile_name'):
            RG = ReportGeneraler(input_file_path=self.path_openfile_name)
            RG.file_path_check(output_file_path=self.output_path)
            file_check = RG.input_file_check()
            if file_check is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_check))
            File_data = RG.input_data_check()
            if File_data is not True:
                self.ExcelFilesState.setText('{:<40}'.format(File_data))
            file_save_state = RG.file_data_excel_output(output_type=0)
            if file_save_state is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_save_state))
        else:
            self.ExcelFilesState.setText('{:<40}'.format('请选择文件'))

    def save_output_weekly_file(self,):
        if hasattr(self, 'path_openfile_name'):
            RG = ReportGeneraler(input_file_path=self.path_openfile_name)
            RG.file_path_check(output_file_path=self.output_path)
            file_check = RG.input_file_check()
            if file_check is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_check))
            File_data = RG.input_data_check()
            if File_data is not True:
                self.ExcelFilesState.setText('{:<40}'.format(File_data))
            file_save_state = RG.file_data_excel_output(output_type=1)
            if file_save_state is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_save_state))
        else:
            self.ExcelFilesState.setText('{:<40}'.format('请选择文件'))

    def save_output_month_file(self,):
        if hasattr(self, 'path_openfile_name'):
            RG = ReportGeneraler(input_file_path=self.path_openfile_name)
            RG.file_path_check(output_file_path=self.output_path)
            file_check = RG.input_file_check()
            if file_check is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_check))
            File_data = RG.input_data_check()
            if File_data is not True:
                self.ExcelFilesState.setText('{:<40}'.format(File_data))
            file_save_state = RG.file_data_excel_output(output_type=2)
            if file_save_state is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_save_state))
        else:
            self.ExcelFilesState.setText('{:<40}'.format('请选择文件'))

    def openfile(self):

        # 获取路径===================================================================

        openfile_name = QFileDialog.getOpenFileName(
            self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')

        # print(openfile_name)
        global path_openfile_name

        # 获取路径====================================================================
        self.path_openfile_name = openfile_name[0]
        path_openfile_name = openfile_name[0]

    def creat_table_show(self):
        self.ExcelFilesState.setText('{:<40}'.format(path_openfile_name))
        # ===========读取表格，转换表格，===========================================
        if len(path_openfile_name) > 0:
            RG = ReportGeneraler(input_file_path=path_openfile_name)
            file_check = RG.input_file_check()
            print(file_check)
            if file_check is not True:
                self.ExcelFilesState.setText('{:<40}'.format(file_check))
                print(1)
                return
            else:
                input_table = RG.file_data_adj()
                self.ExcelFilesState.setText('{:<40}'.format('成功打开文件'))

        # print(input_table)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
        # print(input_table_rows)
        # print(input_table_colunms)
            input_table_header = input_table.columns.values.tolist()
        # print(input_table_header)

        # ===========读取表格，转换表格，============================================
        # ======================给tablewidget设置行列表头============================

            self.OutPutTableView.setColumnCount(input_table_colunms)
            self.OutPutTableView.setRowCount(input_table_rows)
            self.OutPutTableView.setHorizontalHeaderLabels(input_table_header)

        # ======================给tablewidget设置行列表头============================

        # ================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                # print(input_table_rows_values)
                input_table_rows_values_array = np.array(
                    input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[
                    0]
            # print(input_table_rows_values_list)
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                # print(input_table_items_list)
                # print(type(input_table_items_list))

        # ==============将遍历的元素添加到tablewidget中并显示=======================

                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items)
                    # newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.OutPutTableView.setItem(i, j, newItem)

        # ================遍历表格每个元素，同时添加到tablewidget中========================
        else:
            self.centralwidget.show()



    def openDialog(self):
        self.refresh_display()
        GeneralSenderWindowslog = GeneralSenderWindows(self,path_openfile_name=self.path_openfile_name,
                                                       output_path = self.output_path
                                                       )
        # 连接【子窗口内置消息和主窗口的槽函数】
        GeneralSenderWindowslog.GeneralDailySendlistButton.clicked.connect(self.mail_add_check)
        GeneralSenderWindowslog.show()

    def mail_add_check(self):
        pass



class GeneralSenderWindows(QDialog,Sender_Dialog):
    dialogSignel = pyqtSignal(int, str)

    def __init__(self,parent=None,**kwargs):
        super(GeneralSenderWindows, self).__init__(parent)
        self.path_openfile_name = kwargs.get('path_openfile_name', None)
        self.output_path = kwargs.get('output_path', None)

        self.setupUi(self)
        self.retranslateUi(self)
        self.GeneralDailySendlistButton.clicked.connect(self.general_daily_send_report)
        self.GeneralWeeklySendlistButton.clicked.connect(self.general_weekly_send_report)
        self.GeneralMonthSendlistButton.clicked.connect(self.general_month_send_report)
        self.GeneralSendlistButton.clicked.connect(self.general_custom_send_report)



    def general_daily_send_report(self):
        SD = SeasonDict()
        RG = ReportGeneraler(input_file_path=self.path_openfile_name)
        RG.file_path_check(output_file_path = self.output_path)
        SendMail_Info_Path,Send_df_state = RG.send_file_table_output(
            StartDate=SD['date'],
            EndDate=SD['date'],
            output_type=0,
            if_mail=True
        )

        if Send_df_state:
            self.creat_table_show(file_path=SendMail_Info_Path)
        else:
            self.tempSendTable.show()


    def general_weekly_send_report(self):
        SD = SeasonDict()
        RG = ReportGeneraler(input_file_path=self.path_openfile_name)
        RG.file_path_check(output_file_path = self.output_path)
        SendMail_Info_Path,Send_df_state = RG.send_file_table_output(
            StartDate=SD['week'],
            EndDate=SD['week'],
            output_type=1,
            if_mail=True
        )

        if Send_df_state:
            self.creat_table_show(file_path=SendMail_Info_Path)
        else:
            self.tempSendTable.show()


    def general_month_send_report(self):
        SD = SeasonDict()
        RG = ReportGeneraler(input_file_path=self.path_openfile_name)
        RG.file_path_check(output_file_path=self.output_path)
        SendMail_Info_Path, Send_df_state = RG.send_file_table_output(
            StartDate=SD['month'],
            EndDate=SD['month'],
            output_type=2,
            if_mail=True
        )

        if Send_df_state:
            self.creat_table_show(file_path=SendMail_Info_Path)
        else:
            self.tempSendTable.show()

    def general_custom_send_report(self):
        RG = ReportGeneraler(input_file_path=self.path_openfile_name)
        RG.file_path_check(output_file_path=self.output_path)

        print(self.SendDatatype.currentText())
        _temp_sendtype = self.SendDatatype.currentText()
        sendtype_dict = {
            "日":0,
            "周":1,
            "月":2
        }

        SendMail_Info_Path, Send_df_state = RG.send_file_table_output(
            StartDate=self.StartDate.text(),
            EndDate=self.EndDate.text(),
            output_type=sendtype_dict[_temp_sendtype],
            if_mail=True
        )

        if Send_df_state:
            self.creat_table_show(file_path=SendMail_Info_Path)
        else:
            self.tempSendTable.show()


    def creat_table_show(self,file_path):
        # ===========读取表格，转换表格，===========================================
        input_table = pd.read_excel(file_path,index_col=0)

    # print(input_table)
        input_table_rows = input_table.shape[0]
        input_table_colunms = input_table.shape[1]
    # print(input_table_rows)
    # print(input_table_colunms)
        input_table_header = input_table.columns.values.tolist()
    # print(input_table_header)

    # ===========读取表格，转换表格，============================================
    # ======================给tablewidget设置行列表头============================

        self.tempSendTable.setColumnCount(input_table_colunms)
        self.tempSendTable.setRowCount(input_table_rows)
        self.tempSendTable.setHorizontalHeaderLabels(input_table_header)

    # ======================给tablewidget设置行列表头============================

    # ================遍历表格每个元素，同时添加到tablewidget中========================
        for i in range(input_table_rows):
            input_table_rows_values = input_table.iloc[[i]]
            # print(input_table_rows_values)
            input_table_rows_values_array = np.array(
                input_table_rows_values)
            input_table_rows_values_list = input_table_rows_values_array.tolist()[
                0]
        # print(input_table_rows_values_list)
            for j in range(input_table_colunms):
                input_table_items_list = input_table_rows_values_list[j]
            # print(input_table_items_list)
            # print(type(input_table_items_list))

    # ==============将遍历的元素添加到tablewidget中并显示=======================

                input_table_items = str(input_table_items_list)
                newItem = QTableWidgetItem(input_table_items)
                # newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                self.tempSendTable.setItem(i, j, newItem)

    # ================遍历表格每个元素，同时添加到tablewidget中========================






if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = MainWindow()
    filesender = GeneralSenderWindows()

    # 通过toolButton将两个窗体关联
    # btn = widgets.SendMail
    # btn.clicked.connect(filesender.show)
    # 显示
    widgets.show()
    sys.exit(app.exec_())
