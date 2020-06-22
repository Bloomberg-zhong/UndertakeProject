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
import shutil

CV_VALUES_TYPE = [
    '报关费', '港建费', '商检解锁费', '快检费', '续页费',
    '续柜费', '查柜费', '改船名费', '熏蒸费', '过磅费',
    '代理费', '其他费用'
]


class ReportGeneraler():
    def __init__(self,
                 input_file_path,
                 _debug=True
                 ):

        self.input_file_path = input_file_path
        self._debug = _debug

    def file_path_check(self, output_file_path):
        self.output_file_path = output_file_path
        self.mailsendlog_path = path.join(output_file_path, u'邮件发送日期日志')
        self.dailylog_path = path.join(output_file_path, u'日数据')
        self.weeklylog_path = path.join(output_file_path, u'周数据')
        self.monthlog_path = path.join(output_file_path, u'月数据')
        mkdir(self.mailsendlog_path)
        mkdir(self.dailylog_path)
        mkdir(self.weeklylog_path)
        mkdir(self.monthlog_path)

    def input_file_check(self):

        # 文件打开检查
        try:
            origin_df = pd.read_excel(self.input_file_path, sheet_name=1)
            users_df = pd.read_excel(self.input_file_path, sheet_name=0)
        except BaseException:
            return '文件无法打开，请检查!'

        ORDERS_COLUMNS_LIST = [
            '订单时间', '工作编号', '客户名称', '项目', '经营单位', '柜号', '订舱号', '报关单号',
            '报关费', '港建费', '商检解锁费', '快检费', '续页费', '续柜费', '查柜费', '改船名费',
            '熏蒸费', '过磅费', '代理费', '其他费用', '合计', '返佣费'
        ]
        USERS_INFO = ['编号', '客户名称', '客户公司名称', '联系人姓名',
                      '客户联系电话', '客户邮箱地址', '客户财务邮箱地址',
                      '发送日报', '发送周报', '发送月报']

        if not any(origin_df.columns.isin(ORDERS_COLUMNS_LIST)):
            return '打开订单表中的必须包含模板中所包含列'

        if not any(users_df.columns.isin(USERS_INFO)):
            return '打开用户信息表中的必须包含模板中所包含列'

        # 订单时间格式检查
        try:
            origin_df['订单时间'] = pd.to_datetime(origin_df['订单时间'])
        except BaseException:
            return '请检查 订单时间 列数据格式,标准格式为 2020-06-01 '

        # 费用数据格式检查
        try:
            VALUESTYPE = [
                '报关费', '港建费', '商检解锁费', '快检费', '续页费',
                '续柜费', '查柜费', '改船名费', '熏蒸费', '过磅费',
                '代理费', '其他费用', '合计', '返佣费',
            ]
            origin_df[VALUESTYPE] = origin_df[VALUESTYPE].astype('float')
        except BaseException:
            return '请检查 各项费用 列数据格式,默认应该是数字类型'
        if self._debug:
            print('All Check Finish!!')

        return True

    def input_data_check(self):
        users_df = pd.read_excel(self.input_file_path, sheet_name=0)
        origin_df = pd.read_excel(self.input_file_path, sheet_name=1)
        try:
            _temp_user_df = origin_df[~origin_df['客户名称'].isin(
                users_df['客户名称'])]
            not_excent_users = _temp_user_df['客户名称'].unique().tolist()
            not_excent_users_str = ",".join(not_excent_users)
            if not_excent_users_str != '':
                return '以下客户在客户信息表中不存在信息:{}'.format(not_excent_users_str)
        except BaseException:
            return '请检查客户基本信息表中 客户名称 与订单流水表中 客户名称 是否存在'
        # 邮箱检查
        try:
            empty_email_add = users_df[(users_df['客户邮箱地址'].isna()) & (
                users_df['客户财务邮箱地址'].isna())]['客户名称']
            empty_email_add_str = ",".join(empty_email_add)
            if empty_email_add_str != '':
                return '以下客户在客户信息表中不存邮箱地址:{}'.format(empty_email_add_str)
        except BaseException:
            return '客户信息表中邮箱地址至少存在一条才能进行发送'

        # 客户表邮箱发送规则
        try:
            daily_empty_send_mail_type = users_df[users_df['发送日报'].isna()]
            weekly_empty_send_mail_type = users_df[users_df['发送周报'].isna()]
            month_empty_send_mail_type = users_df[users_df['发送月报'].isna()]
            all_empty_send_mail_type = pd.concat([
                month_empty_send_mail_type,
                weekly_empty_send_mail_type,
                daily_empty_send_mail_type
            ])
            all_empty_send_mail_type_list = all_empty_send_mail_type['客户名称'].unique(
            ).tolist()
            empty_send_mail_type_str = ",".join(all_empty_send_mail_type_list)
            if empty_send_mail_type_str != '':
                return '以下客户在客户信息表中不存是否发送邮件规则:{}'.format(
                    empty_send_mail_type_str)
        except BaseException:
            return '客户信息表中必须包含发送规则，具体发送那种规则数据，且必须为\'是|否\''
        if self._debug:
            print('All Check Finish!!')
        return True

    def file_data_adj(self):
        self.input_file_check()
        origin_df = pd.read_excel(self.input_file_path, sheet_name=1)
        origin_df[CV_VALUES_TYPE] = origin_df[CV_VALUES_TYPE].astype(float)
        self.finis_adj_input_df = origin_df
        return origin_df

    def file_data_excel_output(self, output_type=0, if_mail=False):
        """
            Desc:
                深圳按照规则产生的数据报告
            ARG:
            output_type：
             0 = 日
             1 = 周
             2 = 月
        """

        OUTPUTCOLUMNS = [
            '编号',
            '通关方式',
            '订单时间',
            '工作编号',
            '客户名称',
            '项目',
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
            '代理费',
            '其他费用',
            '合计',
            '返佣费',
            '备注',
            ]
        if if_mail:
            OUTPUTCOLUMNS.remove('返佣费')

        try:

            input_df_adj = self.file_data_adj()
            if if_mail:
                self.input_data_check()

            users_name_list = input_df_adj['客户名称'].unique().tolist()

            # 按天的方式进行输出数据
            if output_type == 0:
                input_df_adj['归属日'] = input_df_adj['订单时间'].astype('str')
                datetime_list = input_df_adj['归属日'].unique().tolist()
                if if_mail:
                    temp_path = path.join(self.mailsendlog_path, u'日数据')
                else:
                    temp_path = self.dailylog_path

            # 按照周的方式进行输出
            elif output_type == 1:
                input_df_adj['归属周'] = input_df_adj['订单时间'].apply(
                    lambda x: get_week_and_month(date_str=x, type=1)).astype('str')
                datetime_list = input_df_adj['归属周'].unique().tolist()
                if if_mail:
                    temp_path = path.join(self.mailsendlog_path, u'周数据')
                else:
                    temp_path = self.weeklylog_path

            # 按照月的方式进行输出
            elif output_type == 2:
                input_df_adj['归属月'] = input_df_adj['订单时间'].apply(
                    lambda x: get_week_and_month(date_str=x, type=0)).astype('str')
                datetime_list = input_df_adj['归属月'].unique().tolist()
                if if_mail:
                    temp_path = path.join(self.mailsendlog_path, u'周数据')
                else:
                    temp_path = self.monthlog_path

            else:
                raise ('output_type should in (0,1,2)')

            Users_send_file_path = []
            for i in range(len(datetime_list)):
                _temp_file_path = path.join(temp_path, datetime_list[i])
                mkdir(_temp_file_path)
                for j in range(len(users_name_list)):
                    if output_type == 0:
                        _temp_file_adj = input_df_adj[(input_df_adj['归属日'] == datetime_list[i]) & (
                            input_df_adj['客户名称'] == users_name_list[j])].copy().reset_index(drop=True)

                    elif output_type == 1:
                        _temp_file_adj = input_df_adj[(input_df_adj['归属周'] == datetime_list[i]) & (
                            input_df_adj['客户名称'] == users_name_list[j])].copy().reset_index(drop=True)

                    else:
                        _temp_file_adj = input_df_adj[(input_df_adj['归属月'] == datetime_list[i]) & (
                            input_df_adj['客户名称'] == users_name_list[j])].copy().reset_index(drop=True)

                    if _temp_file_adj.empty:
                        continue
                    if if_mail:
                        del _temp_file_adj['返佣费']
                        _temp_file_adj['合计'] = _temp_file_adj[CV_VALUES_TYPE].apply(
                            lambda x: x.sum(), axis=1)
                        _temp_file_adj.loc['合计'] = _temp_file_adj[CV_VALUES_TYPE +
                                                                  ['合计']].apply(lambda x: x.sum())
                    else:
                        _temp_file_adj['合计'] = _temp_file_adj[CV_VALUES_TYPE + \
                            ['返佣费']].apply(lambda x: x.sum(), axis=1)
                        _temp_file_adj.loc['合计'] = _temp_file_adj[CV_VALUES_TYPE + \
                            ['返佣费'] + ['合计']].apply(lambda x: x.sum())

                    if if_mail:
                        output_file = _temp_file_adj[OUTPUTCOLUMNS]
                    else:
                        output_file = _temp_file_adj[OUTPUTCOLUMNS]

                    _temp_file_name = datetime_list[i] + '客户--' + users_name_list[j] + '.xlsx'
                    _temp_output_file_path = path.join(_temp_file_path, _temp_file_name)

                    Users_send_file_path.append([datetime_list[i],users_name_list[j],_temp_file_name,_temp_output_file_path])
                    output_file.to_excel(_temp_output_file_path, index=True)
            OUTPUT_File = pd.DataFrame(Users_send_file_path, columns=['Date','客户名称','文件名','文件路径'])

        except BaseException:
            return '发生未知错误'

        if if_mail:
            return OUTPUT_File

        return True

    def send_file_table_outpu(self,
                              StartDate,
                              EndDate,
                              output_type=0,
                              if_mail=True
                              ):
        """
        Desc:
            生成邮件输出报告文件
        """
        self.input_data_check()
        users_df = pd.read_excel(self.input_file_path, sheet_name=0)

        clear_file(filepath=self.mailsendlog_path)
        out_put_file_path = self.file_data_excel_output(output_type=output_type, if_mail=if_mail)
        USER_COLUMNS = ['客户名称', '客户公司名称', '客户邮箱地址', '发送日报', '发送周报', '发送月报']
        Users_df_info = users_df[USER_COLUMNS]
        out_put_df = pd.merge(left=out_put_file_path,right=Users_df_info,how='left',left_on=['客户名称'],right_on=['客户名称'])
        # 数据调整
        output_df_adj = out_put_df[(out_put_df['Date']>=StartDate) & (out_put_df['Date']<=EndDate)].reset_index(drop=True)


        return output_df_adj



if __name__ == '__main__':

    RG = ReportGeneraler(
        input_file_path='/Users/zhongpengbo/Documents/GitHub/UndertakeProject/GUI/ConversionDataTool/自动发送程序使用模板.xlsx',

    )

    RG.input_file_check()
    RG.input_data_check()
