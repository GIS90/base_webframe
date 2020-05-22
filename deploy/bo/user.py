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
from deploy.bo.bo_base import BOBase
from deploy.models.user import UserModel
from sqlalchemy import or_


class UserBo(BOBase):

    def __init__(self):
        super(UserBo, self).__init__()

    def get_user_by_params(self, user_id):
        q = self.session.query(UserModel)
        if not user_id:
            return None
        if user_id:
            q = q.filter(or_(UserModel.rtx_id == user_id,
                             UserModel.email == user_id,
                             UserModel.phone == user_id))
            return q.first()

    def check_user(self, user_id, password):
        if not user_id or not password:
            return None

        q = self.session.query(UserModel)
        q = q.filter(or_(UserModel.rtx_id == user_id,
                             UserModel.email == user_id,
                             UserModel.phone == user_id))
        q = q.filter(UserModel.password == password)
        return q.first()
