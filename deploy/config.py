#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    config

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/20 10:00 AM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python config.py
# ------------------------------------------------------------
import os
import sys
import inspect
import logging


logger = logging.getLogger(__name__)


# get current folder, solve is or not frozen of the script
def _get_cur_folder():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        cur_folder = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(cur_folder)


base_dir = _get_cur_folder()

# server
NAME = 'BaseWebFrame'
VERSION = '1.0.0'
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'belivemeIcanfly'

# mail
MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
MAIL_PORT = int(os.environ.get('MAIL_PORT') or '25')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') == 'True'
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'XXXXXX@163.com'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'XXXXXX'

# db(sqlalchemy)，default is mysql
DB_LINK = "mysql+pymysql://mingliang.gao:910809ecb44c92db12ad5fa369375d00@212.64.61.62:3306/blog?charset=utf8"

# log
LOG_DIR = "/Users/gaomingliang/github/base_webframe/log"
LOG_LEVEL = "debug"
LOG_FORMATTER = "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s - %(message)s"
LOG_FILENAME_PREFIX = 'base_webframe'
