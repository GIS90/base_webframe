# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/17"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
from sqlalchemy import (
        Column,
        String,
        Integer,
        Boolean,
        Date
)
from deploy.models import base


__all__ = ("EmployeeModel")


class EmployeeModel(base.ModelBase):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    china_name = Column(String(30))
    english_name = Column(String(30))
    age = Column(Integer())
    sex = Column(String(5))
    birth_date = Column(Date())
    email = Column(String(30))
    phone = Column(String(30))
    education = Column(String(30))
    birth_place = Column(String(50))
    card_id = Column(String(30))
    native_place = Column(String(50))




