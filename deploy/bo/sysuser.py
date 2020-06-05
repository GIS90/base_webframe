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
from deploy.models.sysuser import SysUserModel
from sqlalchemy import or_


class SysUserBo(BOBase):

    def __init__(self):
        super(SysUserBo, self).__init__()

    def get_user_by_params(self, user_id):
        q = self.session.query(SysUserModel)
        if not user_id:
            return None
        if user_id:
            q = q.filter(or_(SysUserModel.rtx_id == user_id,
                             SysUserModel.email == user_id,
                             SysUserModel.phone == user_id))
            return q.first()

    def check_user(self, user_id, password):
        if not user_id or not password:
            return None

        q = self.session.query(SysUserModel)
        q = q.filter(or_(SysUserModel.rtx_id == user_id,
                         SysUserModel.email == user_id,
                         SysUserModel.phone == user_id))
        q = q.filter(SysUserModel.password == password)
        return q.first()

    def update_by_rtx(self, rtx_id):
        pass
