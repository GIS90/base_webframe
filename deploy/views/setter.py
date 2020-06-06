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


@setter.route('/user/', methods=['GET', 'POST'])
def user_html():
    g.menuf = 'setter'
    g.menusub = 'user'
    return render_template('setter/user.html')


@setter.route('/upload_image/', methods=['POST'])
@timeer
def upload_image():
    image = request.files.get('avatar')
    if not image:
        return Status(
                200,
                'failure',
                u'请先上传图片',
                {}
                ).json()

    g.menuf = 'setter'
    g.menusub = 'user'
    LOG.info('%s update image' % get_user_id())
    return SetterService().upload_image(image)

