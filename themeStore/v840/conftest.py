#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   : chuanwen.peng
# @Time     : 2022/4/15 14:21
# @File     : conftest.py
# @Project  : Glass_UI
"""
import os

import pytest

from common.config_parser import ReadConfig
from common.utils import get_installed_package_name
from common.yaml_parser import ReadYaml
from themeStore.v840 import root_dir
from themeStore.v840.flow.start_flow import AppFlow

package_name = get_installed_package_name()


@pytest.fixture(scope="session")
def change_environment(driver):
    driver.app_start(package_name, "com.nearme.wallet.envswitch.EnvSwitchTestActivity")
    driver(text="测试4").click()
    driver.sleep(1.0)
    driver(text="测试4").click()
    driver.press("recent")
    driver.swipe_ext("up", 0.5)


@pytest.fixture(scope="function")
def data():
    filename = "data.yaml"
    return ReadYaml().read(os.path.join(root_dir, "data", filename))


@pytest.fixture(scope="function")
def clear_all_message(driver):
    driver.open_notification()
    if ReadConfig().get_platform == "android":
        element = driver(resourceId="com.android.systemui:id/shelf_dismiss_text")
        if element.wait(timeout=3.0):
            element.click()
        else:
            driver.press("back")
