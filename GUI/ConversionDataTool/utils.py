# -*- encoding: utf-8 -*-
"""
@File    : utils.py
@Time    : 2020/6/9 4:12 下午
@Author  : Bloomberg zhong
@Email   : z136303452@hotmail.com
@Software: PyCharm
"""

import six
import json
import copy
import datetime
import datetime as dt
from functools import wraps
from collections import namedtuple
import pandas as pd
import os
import calendar as Cal
import calendar
import shutil

# Defind formater
formater_dollar2 = "${:,.2f}".format
formater_dollar4 = "${:,.4f}".format
formater_dollar0 = "${:,.0f}".format
formater_2decimal = "{:,.02f}".format
formater_4decimal = "{:,.04f}".format
formater_0decimal = "{:,.0f}".format
formater_percent = '{:,.2f}%'.format
formater_percent0 = '{:,.0f}%'.format

if six.PY2:
    import cPickle as pickle
else:
    import pickle as pickle

try:
    from functools import lru_cache
except ImportError:
    from fastcache import lru_cache

class ParamsError(Exception):
    pass

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def table_exists(table_name,engine):
    ret = engine.dialect.has_table(engine, table_name)
    if not ret:
        print('Table "{}" is not exists: {}'.format(table_name, ret))
    return ret

def table_create(table_classname,engine):
    table_classname.__table__.create(bind = engine)
    print('Table "{}" is try to Create'.format(table_classname.__tablename__))

def to_date_str(dt):
    if dt is None:
        return None

    if isinstance(dt, six.string_types):
        return dt
    if isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(dt, datetime.date):
        return dt.strftime("%Y-%m-%d")

def is_str(s):
    return isinstance(s, six.string_types)


def to_date(date):
    """
    >>> convert_date('2015-1-1')
    datetime.date(2015, 1, 1)

    >>> convert_date('2015-01-01 00:00:00')
    datetime.date(2015, 1, 1)

    >>> convert_date(datetime.datetime(2015, 1, 1))
    datetime.date(2015, 1, 1)

    >>> convert_date(datetime.date(2015, 1, 1))
    datetime.date(2015, 1, 1)
    """
    if is_str(date):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    elif date is None:
        return None
    raise ParamsError("type error")


def mkdir(path,_debug = False):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        if _debug:
            print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        if _debug:
            print(path + ' 目录已存在')
        return False

def clear_file(filepath,_debug = False):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    isExists = os.path.exists(filepath)
    if isExists :
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        if _debug:
            print(filepath + ' 删除成功')
    else:
        if _debug:
            print(filepath + ' 文件不存在')


def SeasonDict(date=None, _Special=False):
    '''
    Desc :
        输入日期，返回一个dict(), 包含本周，本月，已经本季日期信息。

    Args :
        date :
            默认今天。
            e.g. '2018-07-25'

    Example :

    >>> SeasonDict()
    '''

    if date is None:
        date = dt.date.today()
    else:
        date = pd.to_datetime(date).date()

    if _Special:
        _week = str(str(date + dt.timedelta(days=(7 - date.weekday()))))
    else:
        _week = str(str(date + dt.timedelta(days=(6 - date.weekday()))))

    output = {
        'date': str(date),
        'week': [
            str(date - dt.timedelta(days=date.weekday())),
            _week
        ],
    }

    # MONTH
    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = Cal.monthrange(date.year, date.month)
    if _Special:
        # _date = date + dt.timedelta(days=monthRange)
        if date.month + 1 >= 13:
            _date = dt.date(date.year + 1, 1, 1)
        else:
            _date = dt.date(date.year, date.month + 1, 1)
    else:
        _date = date + dt.timedelta(days=monthRange - date.day)

    output['month'] = [
        str(date - dt.timedelta(days=date.day - 1)),
        str(_date)
    ]

    # SEACON
    _month = int((date.month - 1) / 3) * 3 + 1
    _season_start = dt.date(date.year, _month, 1)

    if _Special:
        if _month >=10:
            _season_end = dt.date(
                date.year+1,
                1,
                1
            )
        else:
            _season_end = dt.date(
                date.year,
                _month + 3,
                1
            )
    else:
        _season_end = dt.date(
            date.year,
            _month + 2,
            calendar.monthrange(int(date.year), _month + 2)[1]
        )
    output['season'] = [
        str(_season_start),
        str(_season_end)
    ]

    return output

def get_week_and_month(date_str=None,type =1):
    if date_str and isinstance(date_str, str):
        now_time = dt.datetime.strptime(date_str + " 00:00:00", "%Y-%m-%d %H:%M:%S")
    else:
        now_time = date_str.replace(hour=0, minute=0, second=0, microsecond=0)
    # 当月第一天
    one_time = now_time.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    # 当前日期处于本月第几周
    week_num = int(now_time.strftime('%W')) - int(one_time.strftime('%W')) + 1
    date_month = now_time.strftime('%Y-%m')
    if type ==1:
        output = date_month + 'W{}'.format(week_num)
    else:
        output = date_month
    return output