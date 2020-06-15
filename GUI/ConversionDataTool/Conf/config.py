#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 14:19
# @Author  : Noel
# @Site    :
# @File    : Config.py
# @Software: PyCharm

import os
import configparser
import GUI.ConversionDataTool as CD


class Config():
    def __init__(self):
        """
            Desc:
                Congfig实例
                The Singleton Class to Control Configurations
            Example:
                from RiskReport.Config import Config
                config = Config()
                config.cfg.getint('DST_or_GMT','DST')
        """
        self.path = os.path.join(
            os.path.dirname(
                CD.Conf.__file__),
            r'Default.cfg')
        self.cfg = configparser.ConfigParser()

        # Read Configurations
        self.cfg.read(self.path)

    def dispaly(self,):
        """
            Desc:
                To Display all Available Configurations

        """
        with open(self.path, 'r') as file:
            print(file.read())

    def overwrite(self, section, key, value, debug=True):
        """
            Desc:
                To overwrite an entry in configuration file
            Example:
                from RiskReport.Config import Config
                config = Config()
                config.overwrite(
                section='DST_or_GMT',
                key = 'DST'
                value = 6
                )
        """
        with open(self.path, 'r+') as configfile:
            cfg = configparser.ConfigParser()
            cfg.read(self.path)
            cfg.set(section, key, value)

        with open(self.path, 'w+') as configfile:
            cfg.write(configfile)
            print('Config overwrite successfully.')

        with open(self.path, 'r') as file:
            print(file.read())

    def pathch(self, path=None, debug=True):
        """
            Desc:
                使用其他的cfg文件。并且定义明确
            Args:
                path:cfg文件目录
            Example:
                from RiskReport.Config import Config
                config = Config()
                config.pathch(path:"D//test.cfg")
        """
        if path is None:
            os.path.join(
                os.path.dirname(
                    CD.Conf.__file__),
                r'Default.cfg')
        else:
            self.path = path

        if debug:
            print('Change path to ' + self.path)

    def reset(self):
        """
        Desc:
            重置到默认状态
        """
        # 量化组本地服务器设置
        # Database_Local_Report
        cfg = configparser.ConfigParser()
        cfg.add_section('DB_local_Server')

        # Log日志文件路径
        cfg.add_section('Server_State_Log')
        cfg.set('Server_State_Log', 'Path', r'D:\QuantTeamHK\UpdateService\Task\log')
        cfg.set('Server_State_Log', 'DeBug_Mode', 'False')

        # 此处用到的几种方式
        # Local 本地服务器是本地服务器
        # Hong Kong是在香港使用的服务器
        cfg.add_section('Local_Server_Choose')
        cfg.set('Local_Server_Choose',
                'Local_Server_Whice', 'Hong Kong')
        cfg.set('Local_Server_Choose',
                'Local_Server_File_Path', r'D:\QuantTeamHK\UpdateService\每日风控报告')

        cfg.add_section('Server_State')
        cfg.set('Server_State', 'DEBUG', 'True')
        cfg.set('Server_State', 'TESTING', 'True')
        cfg.set('Server_State', 'PRODUCTION', 'False')

        with open(self.path, "w+") as f:
            cfg.write(f)
        print('Success Reset Default.cfg')


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


class TestingConfig(Config):
    """测试环境配置"""
    MAIL_SUPPRESS_SEND = True
    TESTING = True


class ProductionConfig(Config):
    """生产环境配置"""
    PRODUCTION = True


# config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
#     'default': DevelopmentConfig
# }

