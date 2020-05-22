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
from flask import Flask, make_response, Blueprint, jsonify

from deploy.utils.logger import logger as LOG
from deploy.utils.utils import get_now
from deploy.utils.status import Status

from deploy.services.employee import EmployeeService


home = Blueprint('home', __name__)


@home.route('/home/summary/')
def summary():
    cur_date = get_now(format="%Y-%m-%d")
    employee_count = EmployeeService().get_count()
    return Status(100,
                 'success',
                 u'成功',
                 {'cur_date': cur_date,
                  'employee_count': employee_count
                  }).json()







