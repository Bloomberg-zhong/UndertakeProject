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
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from GUI.ConversionDataTool.MainWindow import Ui_MainWindow
from GUI.ConversionDataTool.GeneralSender import Sender_Dialog

class MainWindow(QMainWindow, Ui_MainWindow,):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # GeneralSenderWindows

        self.setupUi(self)
        # 打开文件功能
        self.ChooseFileButon.clicked.connect(self.openfile)
        self.ChooseFileButon.clicked.connect(self.creat_table_show)
        self.FreshDataButton.clicked.connect(self.refrashdisplay)

    def refrashdisplay(self):
        #利用line Edit控件对象text()函数获取界面输入

        if hasattr(self,'path_openfile_name'):
            if len(path_openfile_name) > 0:
                print(self.path_openfile_name)
                self.ExcelFilesState.setText('{:<10}'.format(self.path_openfile_name))

        else:
            print('Not choose File!')
            self.ExcelFilesState.setText('{:<10}'.format(u'没有选择文件'))
            self.openfile()
            self.creat_table_show()


    def openfile(self):

        ###获取路径===================================================================

        openfile_name = QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')

        #print(openfile_name)
        global path_openfile_name

        ###获取路径====================================================================
        self.path_openfile_name = openfile_name[0]
        path_openfile_name = openfile_name[0]


    def creat_table_show(self):
        self.ExcelFilesState.setText('{:<40}'.format(path_openfile_name))
        ###===========读取表格，转换表格，===========================================
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name,sheet_name=1)
        #print(input_table)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
        #print(input_table_rows)
        #print(input_table_colunms)
            input_table_header = input_table.columns.values.tolist()
        #print(input_table_header)

        ###===========读取表格，转换表格，============================================
        ###======================给tablewidget设置行列表头============================

            self.OutPutTableView.setColumnCount(input_table_colunms)
            self.OutPutTableView.setRowCount(input_table_rows)
            self.OutPutTableView.setHorizontalHeaderLabels(input_table_header)

        ###======================给tablewidget设置行列表头============================

        ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                #print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            #print(input_table_rows_values_list)
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                #print(input_table_items_list)
                # print(type(input_table_items_list))

        ###==============将遍历的元素添加到tablewidget中并显示=======================

                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items)
                    # newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.OutPutTableView.setItem(i, j, newItem)

        ###================遍历表格每个元素，同时添加到tablewidget中========================
        else:
            self.centralwidget.show()


class GeneralSenderWindows(Sender_Dialog,QDialog):
    def __init__(self,parent=None):
        super(Sender_Dialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = MainWindow()
    filesender = GeneralSenderWindows()

    # 通过toolButton将两个窗体关联
    btn = widgets.SendMail
    btn.clicked.connect(filesender.show)
    # 显示
    widgets.show()
    sys.exit(app.exec_())