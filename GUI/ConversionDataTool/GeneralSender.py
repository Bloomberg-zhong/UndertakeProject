# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GeneralSender.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Sender_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(814, 477)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.StartDate = QtWidgets.QDateEdit(Dialog)
        self.StartDate.setObjectName("StartDate")
        self.horizontalLayout.addWidget(self.StartDate)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.EndDate = QtWidgets.QDateEdit(Dialog)
        self.EndDate.setObjectName("EndDate")
        self.horizontalLayout.addWidget(self.EndDate)
        self.SendDatatype = QtWidgets.QComboBox(Dialog)
        self.SendDatatype.setObjectName("SendDatatype")
        self.SendDatatype.addItem("")
        self.SendDatatype.addItem("")
        self.SendDatatype.addItem("")
        self.horizontalLayout.addWidget(self.SendDatatype)
        self.GeneralSendlistButton = QtWidgets.QPushButton(Dialog)
        self.GeneralSendlistButton.setObjectName("GeneralSendlistButton")
        self.horizontalLayout.addWidget(self.GeneralSendlistButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.GeneralDailySendlistButton = QtWidgets.QPushButton(Dialog)
        self.GeneralDailySendlistButton.setObjectName("GeneralDailySendlistButton")
        self.verticalLayout.addWidget(self.GeneralDailySendlistButton)
        self.GeneralWeeklySendlistButton = QtWidgets.QPushButton(Dialog)
        self.GeneralWeeklySendlistButton.setObjectName("GeneralWeeklySendlistButton")
        self.verticalLayout.addWidget(self.GeneralWeeklySendlistButton)
        self.GeneralMonthSendlistButton = QtWidgets.QPushButton(Dialog)
        self.GeneralMonthSendlistButton.setObjectName("GeneralMonthSendlistButton")
        self.verticalLayout.addWidget(self.GeneralMonthSendlistButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tempSendTable = QtWidgets.QTableView(Dialog)
        self.tempSendTable.setObjectName("tempSendTable")
        self.gridLayout.addWidget(self.tempSendTable, 1, 0, 1, 2)
        self.SendState = QtWidgets.QTextBrowser(Dialog)
        self.SendState.setObjectName("SendState")
        self.gridLayout.addWidget(self.SendState, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.CancalButton = QtWidgets.QPushButton(Dialog)
        self.CancalButton.setObjectName("CancalButton")
        self.horizontalLayout_2.addWidget(self.CancalButton)
        self.StartSendButton = QtWidgets.QPushButton(Dialog)
        self.StartSendButton.setObjectName("StartSendButton")
        self.horizontalLayout_2.addWidget(self.StartSendButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        self.CancalButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "开始发送日期"))
        self.label_2.setText(_translate("Dialog", "结束发送时间"))
        self.SendDatatype.setItemText(0, _translate("Dialog", "日"))
        self.SendDatatype.setItemText(1, _translate("Dialog", "周"))
        self.SendDatatype.setItemText(2, _translate("Dialog", "月"))
        self.GeneralSendlistButton.setText(_translate("Dialog", "生成发送表"))
        self.GeneralDailySendlistButton.setText(_translate("Dialog", "生成今日内的结算单"))
        self.GeneralWeeklySendlistButton.setText(_translate("Dialog", "生成本周内的结算单"))
        self.GeneralMonthSendlistButton.setText(_translate("Dialog", "生成本月内的结算单"))
        self.CancalButton.setText(_translate("Dialog", "取消"))
        self.StartSendButton.setText(_translate("Dialog", "发送"))


