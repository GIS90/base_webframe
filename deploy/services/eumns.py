#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/31 1:50 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python eumns.py
# ------------------------------------------------------------
from deploy.bo.enums import EnumsBo
from deploy.utils.utils import d2s
from deploy.utils.status import Status


class EnumsService(object):

    enums_all_attrs = [
        'id',
        'subid',
        'type',
        'name'
    ]

    enums_type_list = [
        'sex',
        'residence_type',
        'political_status',
        'nationality',
        'nation',
        'marriage',
        'education',
        'card_type',
        'bank_type',
        'bank_country',
        'bank_city'
    ]

    def __init__(self):
        super(EnumsService, self).__init__()
        self.enums_bo = EnumsBo()

    def get_count(self):
        count = self.enums_bo.get_count()
        return count if count else 0

    def get_all_enums(self):
        results = dict()
        for t in self.enums_type_list:
            if not t:
                continue
            data = dict()
            res, count = self.enums_bo.get_enums_by_type(t)
            for line in res:
                if not line:
                    continue
                if not line.subid or not line.name:
                    continue

                data[str(line.subid)] = line.name

            results[t] = data

        return results
