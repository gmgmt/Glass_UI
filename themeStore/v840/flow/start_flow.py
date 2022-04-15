#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   : chuanwen.peng
# @Time     : 2022/4/15 14:21
# @File     : start_flow.py
# @Project  : Glass_UI
"""

import allure

from common.messagebox import box
from themeStore.v840.page import HomePage


class AppFlow(object):

    def __init__(self, driver):
        self.home_page = HomePage(driver)

    @allure.story("应用主题")
    def app_theme(self, **kwargs):
        self.home_page.click_home_tab()
        self.home_page.click_ranking()
        self.home_page.click_best_seller()
        self.home_page.click_free_list()
        self.home_page.click_app_theme()







