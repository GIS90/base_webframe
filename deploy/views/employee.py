# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the view of employee

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/15"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
import json
from flask import Blueprint, g, \
    render_template, request

from deploy.utils.logger import logger as LOG
from deploy.services.employee import EmployeeService
from deploy.services.eumns import EnumsService
from deploy.utils.status import Status
from deploy.utils.utils import timeer


employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route('/edit/<string:card_id>', methods=['GET', 'POST'])
@timeer
def html_edit(card_id):
    g.menuf = 'info'
    g.menusub = 'edit'
    params = dict()
    if isinstance(card_id, unicode):
        card_id = card_id.encode('utf-8')
    em_profile = EmployeeService().get_empl_by_card_id(card_id) \
        if card_id != 'new' else {}
    is_add = '0' if em_profile else '1'
    enums = EnumsService().get_all_enums()
    params['is_add'] = is_add
    params['enums'] = enums
    params['em_profile'] = em_profile

    return render_template('employee/edit.html',
                           params=params)


@employee.route('/add_or_edit_api/', methods=['GET', 'POST'])
def add_or_edit_api():
    if request.method == 'GET':
        return Status(
            201,
            'failure',
            u'add_or_edit_api API请求方法错误',
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


@employee.route('/list/')
def html_list():
    g.menuf = 'info'
    g.menusub = 'list'
    return render_template('employee/list.html')


@employee.route('/api_list/', methods=['GET', 'POST'])
@timeer
def api_list_all():
    if request.method == 'GET':
        return Status(
            201,
            'failure',
            u'api_list API请求方法错误',
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


@employee.route('/quit_empl/', methods=['GET', 'POST'])
@timeer
def quit_empl():
    if request.method == 'GET':
        return Status(
            201,
            'failure',
            u'quit_empl API请求方法错误',
            {}
        ).json()

    try:
        req_json = request.get_json()
        _type = req_json.get('type')
        if _type in ['one', u'one']:
            return EmployeeService().quit_empl(req_json.get('data_id'))

        _res = list()
        data_ids = req_json.get('data_id')
        for order_id in data_ids:
            if not order_id:
                continue
            res = EmployeeService().quit_empl(order_id)
            res = json.loads(res)
            if res.get('status_id') != 100:
                _res.append(res.get('data').get('data_id'))
        if len(_res) > 0:
            return Status(
                201,
                'failure',
                u'订单：%s删除失败' % ','.join(_res),
                {}
            ).json()

        return Status(
            100,
            'failure',
            u'订单：%s删除成功' % ','.join(data_ids),
            {}
        ).json()
    except Exception as e:
        LOG.error("employee>quit_empl is error: %s" % e)
        return Status(101,
                      'failure',
                      u'Server发生错误，获取失败',
                      {}).json()
