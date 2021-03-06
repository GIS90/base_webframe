# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the model of employee

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
        TIMESTAMP,
        Date
)
from deploy.models import base


__all__ = ("EmployeeModel")


class EmployeeModel(base.ModelBase):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    # 基本信息
    china_name = Column(String(30))
    english_name = Column(String(30))
    sex = Column(String(10))
    birth_date = Column(Date())
    political_status = Column(String(10))
    nation = Column(String(10))
    nationality = Column(String(10))
    education = Column(String(10))
    marriage = Column(String(10))
    email = Column(String(30))
    phone = Column(String(30))
    # 证件信息
    card_type = Column(String(10))
    card_id = Column(String(30))
    card_place = Column(String(100))
    card_deadline = Column(Date())
    residence_type = Column(String(10))
    current_address = Column(String(100))
    # 银行卡信息
    bank_type = Column(String(10))
    bank_country = Column(String(10))
    bank_city = Column(String(30))
    bank_id = Column(String(30))
    bank_name = Column(String(30))
    # 入职信息
    entry_date = Column(Date())
    quit_date = Column(Date())
    status = Column(String(10))
    entry_submit_time = Column(TIMESTAMP())
    entry_submit_rtx = Column(String(30))
    quit_submit_time = Column(TIMESTAMP())
    quit_submit_rtx = Column(String(30))
    last_update_time = Column(TIMESTAMP())
    last_update_rtx = Column(String(30))
