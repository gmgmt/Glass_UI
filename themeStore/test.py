#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 17:47
# @Author  : chuanwen.peng
import time
import uiautomator2 as u2

d = u2.connect()

d.screenrecord('output.mp4')

time.sleep(3)
# or do something else

d.screenrecord.stop()
