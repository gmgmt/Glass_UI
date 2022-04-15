#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   : chuanwen.peng
# @Time     : 2022/4/15 14:21
# @File     : element_router.py
# @Project  : Glass_UI
"""
import os

from common.config_parser import ReadConfig
from common.yaml_parser import ReadYaml
from themeStore.v840 import root_dir

mapping = {
    "HomePage": "home_cn_element.yaml"
}


class ElementRouter:
    """定位元素选择路由"""

    @staticmethod
    def select(page_name):
        region = ReadConfig().get_region
        platform = ReadConfig().get_platform
        filename = None
        if platform == "android":
            if region == "cn":
                filename = mapping.get(page_name)
        elif platform == "ios":
            pass
        if filename is None:
            raise TypeError("cannot find the mapping relationship for " + page_name)
        return ReadYaml().read(os.path.join(root_dir, "element", filename))
