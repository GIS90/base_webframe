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
from flask import Blueprint, g, \
    render_template, request

from deploy.utils.logger import logger as LOG
from deploy.services.employee import EmployeeService
from deploy.utils.status import Status


employee = Blueprint('employee', __name__)


@employee.route('/employee/add/')
def html_add():
    g.menuf = 'info'
    g.menusub = 'add'
    return render_template('employee/add.html')


@employee.route('/employee/list/')
def html_list():
    g.menuf = 'info'
    g.menusub = 'list'
    return render_template('employee/list.html')


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
    all_empls, count = EmployeeService().get_all(json)
    data = dict()
    data['totalCount'] = count
    data['datalist'] = all_empls
    LOG.info('/employee/api_list: %s' % count)
    if not all_empls:
        return Status(
                101,
                'success',
                u'成功，但数据为空',
                data
                ).json()
    return Status(
                100,
                'success',
                u'成功',
                data
                ).json()


@employee.route('/employee/edit/')
def html_edit():
    g.menuf = 'info'
    g.menusub = 'edit'
    return render_template('employee/edit.html')





