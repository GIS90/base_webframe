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

    def new_mode(self):
        return EmployeeModel()

    def get_count(self):
        q = self.session.query(func.count(EmployeeModel.id)).scalar()
        return q

    def get_all(self, params, status=1):
        start = params.get('start')
        limit = params.get('limit')
        search = params.get('search')
        count = 0
        q = self.session.query(EmployeeModel)
        if status:
            q = q.filter(EmployeeModel.status == 1)
        if search:
            q = q.filter(or_(
                EmployeeModel.china_name.like(search),
                EmployeeModel.english_name.like(search),
                EmployeeModel.birth_date.like(search),
                EmployeeModel.email.like(search),
                EmployeeModel.phone.like(search),
                EmployeeModel.card_id.like(search),
            ))
        q = q.order_by(EmployeeModel.entry_date.desc())
        count = q.count()
        if start:
            q = q.offset(start)
        if limit:
            q = q.limit(limit)
        q = q.all()
        return q, count

    def is_exist_by_card_id(self, card_id):
        if not card_id:
            return False

        q = self.session.query(EmployeeModel)
        q = q.filter(EmployeeModel.card_id == card_id)
        return True if q.first() else False
