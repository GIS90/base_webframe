#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/19 4:24 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""
# ------------------------------------------------------------
# usage: /usr/bin/python wsgi.py
# ------------------------------------------------------------
import os
from deploy import create_app


config_file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'deploy/config.py')

app = create_app(config_file)

# # 手动启动
# app.run(host="0.0.0.0", port=11111, debug=True)
