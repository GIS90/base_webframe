# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/15"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
from flask import Blueprint, \
    render_template, request

from deploy.utils.logger import logger as LOG
from deploy.utils.utils import get_cur_user
from deploy.services.employee import EmployeeService
from deploy.utils.status import Status


employee = Blueprint('employee', __name__)


@employee.route('/employee/add/')
def html_add():
    menu = dict()
    menu['f'] = 'info'
    menu['sub'] = 'add'
    return render_template('employee/add.html',
                           current_user=get_cur_user(),
                           menu=menu)


@employee.route('/employee/list/')
def html_list():
    menu = dict()
    menu['f'] = 'info'
    menu['sub'] = 'list'
    return render_template('employee/list.html',
                           current_user=get_cur_user(),
                           menu=menu)


@employee.route('/employee/api_list/', methods=['GET', 'POST'])
def api_list_all():
    if request.method == 'GET':
        return Status(
                201,
                'failure',
                u'请求方法错误',
                {}
                ).json()

    json = request.get_json()
    result = EmployeeService().get_all(json)
    return result


@employee.route('/employee/edit/')
def html_edit():
    menu = dict()
    menu['f'] = 'info'
    menu['sub'] = 'edit'
    return render_template('employee/edit.html',
                           current_user=get_cur_user(),
                           menu=menu)





