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
from deploy.models.employee import EmployeeModel
from sqlalchemy import or_, func


class EmployeeBo(BOBase):

    def __init__(self):
        super(EmployeeBo, self).__init__()

    def get_count(self):
        q = self.session.query(func.count(EmployeeModel.id)).scalar()
        return q

    def get_all(self, params):
        start = params.get('start')
        limit = params.get('limit')
        search = params.get('search')
        count = 0
        q = self.session.query(EmployeeModel)
        if search:
            q = q.filter(or_(
                EmployeeModel.china_name.like(search),
                EmployeeModel.english_name.like(search),
                EmployeeModel.age.like(search),
                EmployeeModel.sex.like(search),
                EmployeeModel.birth_date.like(search),
                EmployeeModel.email.like(search),
                EmployeeModel.phone.like(search),
                EmployeeModel.education.like(search),
                EmployeeModel.birth_place.like(search),
                EmployeeModel.card_id.like(search),
                EmployeeModel.native_place.like(search),
            ))
        q = q.order_by(EmployeeModel.id.asc())
        count = q.count()
        if start:
            q = q.offset(start)
        if limit:
            q = q.limit(limit)
        q = q.all()
        return q, count
