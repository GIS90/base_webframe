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


setter = Blueprint('setter', __name__, url_prefix='/setter')


@setter.route('/user/', methods=['GET', 'POST'])
def user_html():
    g.menuf = 'setter'
    g.menusub = 'user'
    return render_template('setter/user.html')
