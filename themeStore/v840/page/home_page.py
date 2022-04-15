#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import allure

from common.base_page import BasePage
from themeStore.v840.element import ElementRouter


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- Tab -------------------
    @allure.step("点击首页")
    def click_home_tab(self):
        self.find_element_and_click(**self.element["home_tab"])

    # ----------------- 工具栏 -------------------
    @allure.step("点击排行")
    def click_ranking(self):
        self.find_element_and_click(**self.element["paihang_code"])

    @allure.step("点击福利")
    def click_payment_code(self):
        self.find_element_and_click(**self.element["fuli_code"])

    @allure.step("点击免费")
    def click_scan_it(self):
        self.find_element_and_click(**self.element["mianfei_code"])

    @allure.step("点击畅销榜")
    def click_best_seller(self):
        self.find_element_and_click(**self.element["changxiao_code"])

    @allure.step("点击主题大赏")
    def click_card_package2(self):
        # self.sleep(3.0)
        self.find_element_and_click(**self.element["dashang_code"])

    @allure.step("点击免费榜")
    def click_free_list(self):
        # self.sleep(3.0)
        self.find_element_and_click(**self.element["free_code"])

    @allure.step("点击超级IP")
    def click_go_by_bus(self):
        self.find_element_and_click(**self.element["chaojiIP_code"])

    @allure.step("点击TOP")
    def click_app_theme(self):
        self.find_element_and_click(**self.element["top_code"])

    @allure.step("点击应用")
    def click_go_open_door(self):
        time.sleep(5.0)
        self.find_element_and_click(**self.element["test_code"])

    # ----------------- 卡包 -------------------
    @allure.step("点击遇见")
    def click_add(self):
        self.find_element_and_click(**self.element["yujian_code"])

    @allure.step("点击推荐")
    def click_Cards_for_other_devices(self):
        self.find_element_and_click(**self.element["tuijian_code"])

    @allure.step("点击主题")
    def click_add_key(self):
        self.find_element_and_click(**self.element["zhuti_code"])

    @allure.step("点击字体")
    def click_add_bank_card(self):
        self.find_element_and_click(**self.element["ziti_code"])

    @allure.step("点击壁纸")
    def click_add_transit_card(self):
        self.find_element_and_click(**self.element["bizhi_code"])


