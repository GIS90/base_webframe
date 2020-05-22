#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    setup config

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/19 3:41 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python setup.py.py
# ------------------------------------------------------------
from setuptools import setup


try:
    import multiprocessing
except ImportError:
    pass

setup(
    setup_requires=['pbr'],
    pbr=True,
)

