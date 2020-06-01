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
from deploy.services.eumns import EnumsService
from deploy.utils.status import Status


employee = Blueprint('employee', __name__)


@employee.route('/employee/edit/')
def html_edit():
    g.menuf = 'info'
    g.menusub = 'edit'
    enums = EnumsService().get_all_enums()
    em_profile = dict()
    is_add = '0' if em_profile else '1'
    return render_template('employee/edit.html',
                           enums=enums,
                           em_profile=em_profile,
                           is_add=is_add)


@employee.route('/employee/add_or_edit_api/', methods=['GET', 'POST'])
def add_or_edit_api():
    if request.method == 'GET':
        return Status(
            201,
            'failure',
            u'请求方法错误',
            {}
        ).json()

    try:
        json = request.get_json()
        res = EmployeeService().add_or_edit_empl(json)
    except Exception as e:
        LOG.error("employee>add_api is error: %s" % e)
        res = Status(101,
                     'failure',
                     u'Server发生错误，新增失败',
                     {}).json()
    return res


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

    try:
        json = request.get_json()
        res = EmployeeService().get_all(json)
    except Exception as e:
        LOG.error("employee>api_list is error: %s" % e)
        res = Status(101,
                     'failure',
                     u'Server发生错误，获取失败',
                     {}).json()
    return res
