# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the view of setter

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
from deploy.utils.status import Status
from deploy.utils.utils import timeer, get_user_id
from deploy.services.setter import SetterService


setter = Blueprint('setter', __name__, url_prefix='/setter')


@setter.route('/user/<string:oprtype>/', methods=['GET', 'POST'])
def user_html(oprtype):
    g.menuf = 'setter'
    g.menusub = 'user'

    if isinstance(oprtype, unicode):
        oprtype = oprtype.encode('utf-8')

    if oprtype not in ['info', 'edit']:
        oprtype = 'info'
    res = dict()
    res['oprtype'] = oprtype
    return render_template('setter/user.html', oprtype=oprtype)


@setter.route('/upload_info/', methods=['POST'])
@timeer
def upload_image():
    image = request.files.get('avatar')
    g.menuf = 'setter'
    g.menusub = 'user'
    try:
        form = request.form
        res = SetterService().upload_info(image, form)
    except Exception as e:
        LOG.error("setter>upload_info is error: %s" % e)
        res = Status(101,
                     'failure',
                     u'Server发生错误，获取失败',
                     {}).json()
    LOG.info('%s update information' % get_user_id())
    return res
