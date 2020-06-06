# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the base class of query db

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/16"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""

from deploy.models.base import get_session


class BOBase(object):

    def __init__(self, model=None):
        self.session = get_session()
        self.model = model

    def get_model(self):
        return self.model

    def save_model(self):
        with self.session.begin():
            self.session.add(self.model)

    def merge_model(self, model):
        with self.session.begin():
            self.session.merge(model)

    def add_model(self, model):
        with self.session.begin():
            self.session.add(model)

    def merge_model_no_trans(self, model):
        self.session.merge(model)






