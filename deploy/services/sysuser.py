# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the services of sysuser

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/16"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
from deploy.bo.sysuser import SysUserBo


class SysUserService(object):
    def __init__(self):
        super(SysUserService, self).__init__()
        self.sysuser_bo = SysUserBo()
        self.attrs = ['id', 'rtx_id', 'fullname', 'image',
                      'password', 'email', 'phone', 'is_admin']

    def get_user_by_params(self, user_id):
        user_res = dict()

        if not user_id:
            return user_res

        user = self.sysuser_bo.get_user_by_params(user_id)
        if user:
            for attr in self.attrs:
                if attr == 'id':
                    user_res[attr] = user.id
                elif attr == 'rtx_id':
                    user_res[attr] = user.rtx_id
                elif attr == 'fullname':
                    user_res[attr] = user.fullname
                elif attr == 'password':
                    user_res[attr] = user.password
                elif attr == 'email':
                    user_res[attr] = user.email
                elif attr == 'phone':
                    user_res[attr] = user.phone
                elif attr == 'is_admin':
                    user_res[attr] = user.is_admin
                elif attr == 'image':
                    user_res[attr] = user.image

        return user_res

    def check_user(self, user_id, password):
        if not user_id or not password:
            return None
        user = self.sysuser_bo.check_user(user_id, password)
        return user if user else False
