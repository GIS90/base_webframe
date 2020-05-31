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
from sqlalchemy import (
        Column,
        String,
        Integer,
        Boolean
)
from deploy.models import base


__all__ = ("SysUserModel")


class SysUserModel(base.ModelBase):
    __tablename__ = 'sysuser'

    id = Column(Integer, primary_key=True)
    rtx_id = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(254))
    email = Column(String(50))
    phone = Column(String(50))
    is_admin = Column(Boolean())

