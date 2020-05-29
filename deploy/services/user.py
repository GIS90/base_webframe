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
from deploy.bo.user import UserBo


class UserService(object):
    def __init__(self):
        super(UserService, self).__init__()
        self.user_bo = UserBo()

    def get_user_by_params(self, user_id):
        if not user_id:
            return None
        user = self.user_bo.get_user_by_params(user_id)
        return user

    def check_user(self, user_id, password):
        if not user_id or not password:
            return None
        user = self.user_bo.check_user(user_id, password)
        return user if user else False






