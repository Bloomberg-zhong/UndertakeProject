# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 589)
        MainWindow.setMinimumSize(QtCore.QSize(802, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.DataConversionButon = QtWidgets.QWidget()
        self.DataConversionButon.setObjectName("DataConversionButon")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.DataConversionButon)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.OutputFilsePathButton = QtWidgets.QPushButton(self.DataConversionButon)
        self.OutputFilsePathButton.setObjectName("OutputFilsePathButton")
        self.gridLayout_3.addWidget(self.OutputFilsePathButton, 0, 1, 1, 1)
        self.OutPutTableView = QtWidgets.QTableWidget(self.DataConversionButon)
        self.OutPutTableView.setObjectName("OutPutTableView")
        self.gridLayout_3.addWidget(self.OutPutTableView, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FreshDataButton = QtWidgets.QPushButton(self.DataConversionButon)
        self.FreshDataButton.setObjectName("FreshDataButton")
        self.horizontalLayout_2.addWidget(self.FreshDataButton)
        self.ChooseFileButon = QtWidgets.QPushButton(self.DataConversionButon)
        self.ChooseFileButon.setObjectName("ChooseFileButon")
        self.horizontalLayout_2.addWidget(self.ChooseFileButon)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DailyDataButton = QtWidgets.QPushButton(self.DataConversionButon)
        self.DailyDataButton.setObjectName("DailyDataButton")
        self.horizontalLayout.addWidget(self.DailyDataButton)
        self.WeeklyDataButton = QtWidgets.QPushButton(self.DataConversionButon)
        self.WeeklyDataButton.setObjectName("WeeklyDataButton")
        self.horizontalLayout.addWidget(self.WeeklyDataButton)
        self.MonthDataButton = QtWidgets.QPushButton(self.DataConversionButon)
        self.MonthDataButton.setObjectName("MonthDataButton")
        self.horizontalLayout.addWidget(self.MonthDataButton)
        self.SendMail = QtWidgets.QPushButton(self.DataConversionButon)
        self.SendMail.setObjectName("SendMail")
        self.horizontalLayout.addWidget(self.SendMail)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.tabWidget.addTab(self.DataConversionButon, "")
        self.MailSet = QtWidgets.QWidget()
        self.MailSet.setObjectName("MailSet")
        self.formLayoutWidget = QtWidgets.QWidget(self.MailSet)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 641, 421))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ProtocolTypeBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.ProtocolTypeBox.setObjectName("ProtocolTypeBox")
        self.ProtocolTypeBox.addItem("")
        self.ProtocolTypeBox.addItem("")
        self.ProtocolTypeBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ProtocolTypeBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.EmailAccountID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.EmailAccountID.setObjectName("EmailAccountID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.EmailAccountID)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.SendMailServer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SendMailServer.setObjectName("SendMailServer")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.SendMailServer)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.SendMailPort = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SendMailPort.setObjectName("SendMailPort")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.SendMailPort)
        self.SendProtocolTypeBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.SendProtocolTypeBox.setObjectName("SendProtocolTypeBox")
        self.SendProtocolTypeBox.addItem("")
        self.SendProtocolTypeBox.addItem("")
        self.SendProtocolTypeBox.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.SendProtocolTypeBox)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.SendMailAccount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SendMailAccount.setObjectName("SendMailAccount")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.SendMailAccount)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.SendMailPassWord = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.SendMailPassWord.setObjectName("SendMailPassWord")

        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.SendMailPassWord)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.EmailSaveButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.EmailSaveButton.setObjectName("EmailSaveButton")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.EmailSaveButton)
        self.EmailPassWord = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.EmailPassWord.setObjectName("EmailPassWord")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.EmailPassWord)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.TakeEmailServer = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.TakeEmailServer.setObjectName("TakeEmailServer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TakeEmailServer)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Port = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Port.setObjectName("Port")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Port)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.EncryptionButton = QtWidgets.QComboBox(self.formLayoutWidget)
        self.EncryptionButton.setObjectName("EncryptionButton")
        self.EncryptionButton.addItem("")
        self.EncryptionButton.addItem("")
        self.EncryptionButton.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.EncryptionButton)
        self.tabWidget.addTab(self.MailSet, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.EmailAccountstate = QtWidgets.QLabel('{:<40}'.format('邮箱状态'))
        self.ExcelFilesState = QtWidgets.QLabel('{:^40}'.format('文件状态'))
        self.statusbar.addWidget(self.EmailAccountstate)
        self.statusbar.addWidget(self.ExcelFilesState)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OutputFilsePathButton.setText(_translate("MainWindow", "保存文件路径"))
        self.FreshDataButton.setText(_translate("MainWindow", "刷新数据"))
        self.ChooseFileButon.setText(_translate("MainWindow", "选择文件"))
        self.DailyDataButton.setText(_translate("MainWindow", "生成日报"))
        self.WeeklyDataButton.setText(_translate("MainWindow", "生成周报"))
        self.MonthDataButton.setText(_translate("MainWindow", "生成月报"))
        self.SendMail.setText(_translate("MainWindow", "一键发送邮件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DataConversionButon), _translate("MainWindow", "数据转换"))
        self.label_5.setText(_translate("MainWindow", "协议类型"))
        self.ProtocolTypeBox.setItemText(0, _translate("MainWindow", "IMAP"))
        self.ProtocolTypeBox.setItemText(1, _translate("MainWindow", "POP3"))
        self.ProtocolTypeBox.setItemText(2, _translate("MainWindow", "Exchange"))
        self.label.setText(_translate("MainWindow", "邮件账户"))
        self.label_7.setText(_translate("MainWindow", "发送服务器"))
        self.label_8.setText(_translate("MainWindow", "端口"))
        self.SendMailPort.setText(_translate("MainWindow", "24"))
        self.SendProtocolTypeBox.setItemText(0, _translate("MainWindow", "无"))
        self.SendProtocolTypeBox.setItemText(1, _translate("MainWindow", "SSL/TLS"))
        self.SendProtocolTypeBox.setItemText(2, _translate("MainWindow", "STARTTLS"))
        self.label_10.setText(_translate("MainWindow", "账户"))
        self.label_11.setText(_translate("MainWindow", "密码"))
        self.label_9.setText(_translate("MainWindow", "加密"))
        self.EmailSaveButton.setText(_translate("MainWindow", "保存"))
        self.label_6.setText(_translate("MainWindow", "密码"))
        self.label_2.setText(_translate("MainWindow", "接收服务器"))
        self.label_3.setText(_translate("MainWindow", "端口"))
        self.Port.setText(_translate("MainWindow", "143"))
        self.label_4.setText(_translate("MainWindow", "加密"))
        self.EncryptionButton.setItemText(0, _translate("MainWindow", "无"))
        self.EncryptionButton.setItemText(1, _translate("MainWindow", "SSL/TLS"))
        self.EncryptionButton.setItemText(2, _translate("MainWindow", "STARTTLS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MailSet), _translate("MainWindow", "邮箱设定"))
        self.EmailPassWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SendMailPassWord.setEchoMode(QtWidgets.QLineEdit.Password)



