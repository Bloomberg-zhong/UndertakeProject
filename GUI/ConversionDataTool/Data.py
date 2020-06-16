# -*- encoding: utf-8 -*-
"""
@File    : Data.py
@Time    : 2020/6/11 4:11 下午
@Author  : Bloomberg zhong
@Email   : z136303452@hotmail.com
@Software: PyCharm
"""
import pandas as pd
import numpy as np
from GUI.ConversionDataTool.utils import *
import sys
from os import path

class ReportGeneraler():
    def __init__(self,
                 input_file_path,
                 output_file_path,
                 ):

        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.mailsendlog_path = path.join(output_file_path,u'邮件发送日期日志')
        self.dailylog_path = path.join(output_file_path ,u'日数据')
        self.weeklylog_path = path.join(output_file_path ,u'周数据')
        self.monthlog_path = path.join(output_file_path ,u'月数据')

    @staticmethod
    def file_path_check(self):
        mkdir(self.mailsendlog_path)
        mkdir(self.dailylog_path)
        mkdir(self.weeklylog_path)
        mkdir(self.monthlog_path)

    def input_file_check(self):
        origin_file = pd.read_excel(self.input_file_path, sheet_name=1)
        COLUMNS_LIST=[
            '订单编号',
            '公司简称',
            '订单时间',
            '编号',
            '日期',
            '抬头',
            '柜号',
            '订舱号',
            '报关单号',
            '报关费',
            '港建费',
            '续页费',
            '续柜费',
            '熏蒸费',
            '代理费',
            '其他费用',
            '合计',
            ]
        if not any(origin_file.columns.isin(COLUMNS_LIST)):
            return '打开文件中的必须包含模板中所包含列'

        try:
            origin_file['订单时间'] = pd.to_datetime(origin_file['订单时间'])
        except ValueError:
            return '请检查 订单时间 列数据格式,标准格式为 2020-06-01 '

        try:
            VALUESTYPE=[
                '报关费',
                '港建费',
                '续页费',
                '续柜费',
                '熏蒸费',
                '代理费',
                '其他费用'
            ]
            origin_file[VALUESTYPE] = origin_file[VALUESTYPE].astype('float')
        except ValueError:
            return '请检查 各项费用 列数据格式,默认应该是数字类型'


    def input_data_check(self):
        Users_df = pd.read_excel(self.input_file_path, sheet_name=0)
        origin_df = pd.read_excel(self.input_file_path, sheet_name=1)


    def file_data_adj(self):
        pass

    def file_data_word_output(self):
        pass

    def file_data_excel_output(self):
        pass

    def send_file_table_outpu(self):
        pass
if __name__ == '__main__':
    RG = ReportGeneraler()

