#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    singleton class + execute base class

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/18 2:34 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python base_class.py
# ------------------------------------------------------------
import threading


class BaseClass(object):

    _instance = None
    _instance_lock = threading.Lock()

    def __init__(self):
        super(BaseClass, self).__init__()
        self.init_run()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with BaseClass._instance_lock:
                cls._instance = object.__new__(cls)
        return cls._instance

    def init_run(self):
        pass


