#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   : chuanwen.peng
# @Time     : 2022/4/15 14:21
# @File     : test_theme.py
# @Project  : Glass_UI
"""
import allure
import pytest

from themeStore.v840.flow.start_flow import AppFlow

@allure.feature("主题应用测试")
class TestSetting:

    @allure.title("应用免费主题")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.S
    def test_setting_0001(self, driver, start_stop_app, data):
        theme_flow = AppFlow(driver)
        # setting_flow.goto_setting_page()
        theme_flow.app_theme()
