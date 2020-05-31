#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/31 1:55 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python enums.py
# ------------------------------------------------------------
from deploy.bo.bo_base import BOBase
from deploy.models.enums import EnumsModel
from sqlalchemy import or_, func


class EnumsBo(BOBase):

    def __init__(self):
        super(EnumsBo, self).__init__()

    def get_count(self):
        q = self.session.query(func.count(EnumsModel.id)).scalar()
        return q

    def get_all_enums(self):
        q = self.session.query(EnumsModel)
        q = q.order_by(EnumsModel.id.asc())
        count = q.count()
        q = q.all()
        return q, count

    def get_enums_by_type(self, enum_type):
        if not enum_type:
            return None, 0

        q = self.session.query(EnumsModel)
        q = q.filter(EnumsModel.type == enum_type)
        q = q.order_by(EnumsModel.id.asc())
        count = q.count()
        q = q.all()
        return q, count

    def get_enumname_by_params(self, params):
        if not params:
            return None

        enum_type = params.get('enum_type')
        enum_subid = params.get('enum_subid')
        q = self.session.query(EnumsModel)
        if enum_type:
            q = q.filter(EnumsModel.type == enum_type)
        if enum_subid:
            q = q.filter(EnumsModel.subid == enum_subid)
        q = q.first()
        return q.name if q else None


