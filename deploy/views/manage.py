# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/16"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
from flask import Blueprint, g,\
    render_template, request, \
    session, redirect, url_for

from deploy.utils.logger import logger as LOG
from deploy.utils.utils import (is_login_ok,
                                check_login,
                                get_user_id)
from deploy.services.sysuser import SysUserService


manage = Blueprint('manage', __name__)


@manage.route('/', methods=['GET', 'POST'])
@is_login_ok
def index():
    user_id = get_user_id()
    if not user_id:
        return render_template("login.html",
                               login_message="")

    g.menuf = 'index'
    g.menusub = 'index'
    return render_template("index.html")


@manage.route('/login/', methods=['GET', 'POST'])
def login_in():
    if request.method == 'GET':
        is_ok, message = check_login()
        if not is_ok:
            return render_template("login.html",
                                   login_message="")

        g.menuf = 'index'
        g.menusub = 'index'
        return render_template("index.html")
    elif request.method == 'POST':
        form = request.form
        user_id = form.get('login_user')
        user_pwd = form.get('login_password')
        is_register_user = SysUserService().get_user_by_params(user_id)
        if not is_register_user:
            return render_template("login.html",
                                   login_message='账户未注册')
        user = SysUserService().check_user(user_id, user_pwd)
        if not user:
            return render_template("login.html",
                                   login_message='账号密码不匹配')
        session['user_id'] = user_id
        g.menuf = 'index'
        g.menusub = 'index'
        LOG.info('%s login in ==========' % user_id)
        return render_template("index.html")
    else:
        return render_template("login.html",
                               login_message="")


@manage.route('/logout/', methods=['GET', 'POST'])
def login_out():
    user_id = get_user_id()
    if user_id:
        LOG.info('%s login out ==========' % user_id)
    session.clear()
    return redirect(url_for('manage.index'))
