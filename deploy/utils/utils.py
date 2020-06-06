# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the all collection of daily tools and methods
    main:
        path
        make dir
        date && time
        ......

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/16"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
import os
import sys
import inspect
import hashlib
import time
from datetime import datetime
from functools import wraps
from flask import session, render_template
from deploy.utils.status import Status
from deploy.services.sysuser import SysUserService
from deploy.utils.logger import logger as LOG


# get current folder, solve is or not frozen of the script
def get_cur_folder():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        cur_folder = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(cur_folder)


# md5加密
def md5(v):
    return hashlib.md5(v).hexdigest()


# 字符串转日期
def s2d(s, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(s, fmt)


# 日期转字符串
def d2s(d, fmt="%Y-%m-%d %H:%M:%S"):
    return d.strftime(fmt)


# 日期转ts
def d2ts(d):
    return time.mktime(d.timetuple())


# 字符串转ts
def s2ts(s, format="%Y-%m-%d %H:%M:%S"):
    d = s2d(s, format)
    return d2ts(d)


# 获取日期差额
def dura_date(d1, d2, need_d=False):
    if type(d1) is str:
        d1 = s2d(d1)
    if type(d2) is str:
        d2 = s2d(d2)
    d = d2 - d1
    if need_d is False:
        seconds = d.seconds
        mins = seconds / 60.00
        hours = mins / 60.00
        return seconds, mins, hours
    return d


# 获取当前时间
def get_now_date():
    return datetime.now()


# 获取当前时间str
def get_now(format="%Y-%m-%d %H:%M:%S"):
    return d2s(datetime.now(), format)


# 获取weekday
def get_week_day(date):
    weekdaylist = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天')
    weekday = weekdaylist[date.weekday()]
    return weekday


def get_user_id():
    return session.get('user_id')


# 检查是否登陆成功，修饰器
def is_login_ok(fn):
    @wraps(fn)
    def _wrapper(*args, **kwargs):
        user_id = get_user_id()
        if not user_id:
            return render_template("login.html", login_message="")
        result = fn(*args, **kwargs)
        return result

    return _wrapper


# 检查是否登陆成功，方法
def check_login():
    user_id = get_user_id()
    if not user_id:
        return False, Status(300,
                             'failed',
                             u'没有用户信息，请先登录',
                             {}).json()

    return True, user_id


def get_cur_user():
    user_id = session.get('user_id')
    if not user_id:
        return render_template("login.html",
                               login_message="")
    user = SysUserService().get_user_by_params(user_id)
    if not user:
        return render_template("login.html",
                               login_message='')
    return user


# 计时器
def timeer(fn):
    @wraps(fn)
    def _wrapper(*args, **kwargs):
        start = datetime.now()
        res = fn(*args, **kwargs)
        end = datetime.now()
        LOG.info('@timeer %s is run: %s' % (fn.__name__, (end-start).seconds))
        return res

    return _wrapper


# 建立文件夹（递归）
def mk_dirs(path):
    os.makedirs(path)
    return path


# 获取项目base目录（deploy）
def get_base_dir():
    return os.path.dirname(get_cur_folder())
