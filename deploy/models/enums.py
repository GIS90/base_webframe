#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    the model of enums

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/31 1:46 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python enums.py
# ------------------------------------------------------------
from sqlalchemy import (
        Column,
        String,
        Integer
)
from deploy.models import base


__all__ = ("EnumsModel")


class EnumsModel(base.ModelBase):
    __tablename__ = 'enums'

    id = Column(Integer, primary_key=True)
    subid = Column(Integer)
    type = Column(String(30))
    name = Column(String(254))
