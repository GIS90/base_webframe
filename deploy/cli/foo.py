#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    the click of foo
    
    use to run the separate tasks

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/23 5:07 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""


# ------------------------------------------------------------
# usage: /usr/bin/python foo.py
# ------------------------------------------------------------
from deploy.utils.base_class import AppBaseClass


class Foo(AppBaseClass):
    def __init__(self):
        super(AppBaseClass, self).__init__()

    def run(self):
        print "run - " * 10
