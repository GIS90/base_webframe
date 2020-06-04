# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/17"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
from flask import Blueprint, g, \
    render_template, request

from deploy.utils.logger import logger as LOG


set = Blueprint('set', __name__)


@set.route('/set/user/', methods=['GET', 'POST'])
def user_html():
    g.menuf = 'set'
    g.menusub = 'user'
    return render_template('set/user.html')
