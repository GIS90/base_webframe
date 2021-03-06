#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    WebFlaskServer initialize 
    flask app and blueprint collections
    
    Singleton mode

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/19 3:42 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python __init__.py.py
# ------------------------------------------------------------
import os
import sys
from flask import (Flask,
                   render_template,
                   session,
                   redirect,
                   url_for,
                   g,
                   request)

from deploy.config import VERSION, NAME, SECRET_KEY
from deploy.models.base import get_session
from deploy.utils.base_class import WebBaseClass
from deploy.utils.logger import logger as LOG
from deploy.utils.utils import get_user_id
from deploy.views.employee import employee
from deploy.views.apis import apis
from deploy.views.manage import manage
from deploy.views.home import home
from deploy.views.setter import setter
from deploy.services.sysuser import SysUserService


app = Flask(__name__)


class WebFlaskServer(WebBaseClass):
    app = None
    version = VERSION
    name = NAME

    def __init__(self, app):
        """
        Initialize webFlaskServer instance
        and flask configuration
        """
        self.app = app
        if not self.app:
            LOG.info('Web server initialize is failure......')
            sys.exit(1)

        _realpath = os.path.dirname(os.path.realpath(__file__))
        self.app.template_folder = _realpath + '/templates/'
        self.app.secret_key = SECRET_KEY or 'python'
        self.app.static_folder = _realpath + '/static'
        self.app.static_url_path = '/static'
        self.app.add_url_rule(self.app.static_url_path + '/<path:filename>',
                              endpoint='static',
                              view_func=self.app.send_static_file)

        super(WebFlaskServer, self).__init__()

        @self.app.before_request
        def before_request():
            if get_user_id():
                return
            # api: rest apis
            # manage: login apis
            if request.blueprint in ['api', 'manage', None]:
                return
            # special api for blueprints
            if request.endpoint.endswith('ForApi') or \
                    request.endpoint.endswith('for_api'):
                return

            return redirect(url_for('manage.index'))

        @self.app.before_first_request
        def before_first_request():
            g._session = get_session()

        @self.app.errorhandler(404)
        def not_found_error(error):
            LOG.error("%s is not found 404" % request.url)
            return render_template('errors/404.html', ), 404

        @self.app.errorhandler(500)
        def server_error(error):
            LOG.error("%s is server error 500" % request.url)
            return render_template('errors/500.html'), 500

        @self.app.context_processor
        def default_context_processor():
            user_id = session.get('user_id')
            menu = current_user = dict()
            if hasattr(g, 'menuf'):
                menu['f'] = g.menuf or 'index'
            if hasattr(g, 'menusub'):
                menu['sub'] = g.menusub or 'index'
            if user_id:
                current_user = SysUserService().get_user_by_params(user_id)

            return {
                'current_user': current_user,
                'sysversion': VERSION,
                'menu': menu
            }

        # set favicon
        @self.app.route('/favicon.ico')
        def get_defaule_favicon():
            return self.app.send_static_file('images/favicon.ico')

    def register_blueprint(self, obj_n, obj):
        """
        view blueprint register
        :param obj_n: blueprint object
        :param obj: blueprint name
        :return: None
        """
        if obj:
            LOG.info('Blueprint %s is register' % obj_n)
            self.app.register_blueprint(obj)

    def _autoinit_register_blueprint(self):
        self.register_blueprint('employee', employee)
        self.register_blueprint('apis', apis)
        self.register_blueprint('manage', manage)
        self.register_blueprint('home', home)
        self.register_blueprint('setter', setter)

    def init_run(self):
        LOG.debug('Server is initializing......')
        self._autoinit_register_blueprint()
        LOG.info('Web server is running......')


def create_app():
    return WebFlaskServer(app).app
