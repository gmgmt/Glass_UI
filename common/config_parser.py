#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   : chuanwen.peng
# @Time     : 2022/4/15 14:21
# @File     : config_parser.py
# @Project  : Glass_UI
"""

import configparser
import json
import os

from common.logger import setup_logger


class ReadConfig:
    """ 读取配置的类 """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ReadConfig, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取当前文件所在目录的上一级目录
        self.root_config_path = os.path.join(self.root_dir, "config.ini")
        self.cf.read(self.root_config_path, "utf-8")
        package_name = self.cf.get("DIRECTORY", "dir_name")
        self.pkg_config_path = os.path.join(self.root_dir, package_name, "config.ini")
        setup_logger()  # 初始化日志配置

    @property
    def get_platform(self) -> str:
        self.cf.read(self.pkg_config_path, "utf-8")
        platform = self.cf.get("DRIVER", "platform")
        return platform.lower()

    @property
    def get_implicitly_wait(self) -> float:
        self.cf.read(self.pkg_config_path, "utf-8")
        implicitly_wait = self.cf.get("DRIVER", "implicitly_wait")
        return float(implicitly_wait)

    @property
    def get_check_error_toast(self) -> bool:
        self.cf.read(self.pkg_config_path, "utf-8")
        check_error_toast = self.cf.get("DRIVER", "check_error_toast")
        return True if check_error_toast.lower() == "true" else False

    @property
    def get_package_name(self) -> list:
        self.cf.read(self.pkg_config_path, "utf-8")
        package_name = self.cf.get(self.get_platform.upper(), "package_name")
        return json.loads(package_name)

    @property
    def get_popup_elements(self) -> list:
        self.cf.read(self.pkg_config_path, "utf-8")
        popup_elements = self.cf.get(self.get_platform.upper(), "popup_element")
        return json.loads(popup_elements)

    @property
    def get_env(self) -> str:
        self.cf.read(self.root_config_path, "utf-8")
        env = self.cf.get("ENVIRONMENT", "env")
        return env.lower()

    @property
    def get_region(self) -> str:
        self.cf.read(self.root_config_path, "utf-8")
        region = self.cf.get("ENVIRONMENT", "region")
        return region.lower()

    @property
    def get_project_dir(self):
        return str(self.root_dir)


if __name__ == "__main__":
    d = ReadConfig()
