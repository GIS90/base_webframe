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
from deploy.bo.employee import EmployeeBo
from deploy.utils.utils import d2s
from deploy.utils.status import Status


class EmployeeService(object):

    employee_all_attrs = [
        'id',
        'china_name',
        'english_name',
        'age',
        'sex',
        'birth_date',
        'email',
        'phone',
        'education',
        'birth_place',
        'card_id',
        'native_place'
    ]

    request_attrs = [
        'index',
        'limit',
        'search',
        'start',
    ]

    def __init__(self):
        super(EmployeeService, self).__init__()
        self.employee_bo = EmployeeBo()

    def get_count(self):
        count = self.employee_bo.get_count()
        return count if count else 0

    def get_all(self, args):

        data = dict()
        new_args = dict()
        start = 0
        for k, v in args.items():
            if k not in self.request_attrs:
                return Status(
                    201,
                    'success',
                    u'%s参数不合法' % k,
                    data
                    ).json()
            if k == 'start':
                start = int(v)
                new_args[k] = start
            elif k == 'search':
                new_args[k] = "%" + str(v) + "%"
            else:
                new_args[k] = v
        # start = (int(new_args['index']) - 1) * int(new_args.get('limit'))
        # new_args['start'] = start
        all_empls, count = self.employee_bo.get_all(new_args)
        if not all_empls:
            return [], 0

        results = list()
        for empl in all_empls:
            if not empl:
                continue

            result = dict()
            for attr in self.employee_all_attrs:
                if attr == 'id':
                    result[attr] = start + 1
                elif attr == 'china_name':
                    result[attr] = empl.china_name
                elif attr == 'english_name':
                    result[attr] = empl.english_name
                elif attr == 'age':
                    result[attr] = empl.age
                elif attr == 'sex':
                    result[attr] = '男' if empl.sex == 'M' \
                        else '女'
                elif attr == 'birth_date':
                    result[attr] = d2s(empl.birth_date, fmt="%Y-%m-%d") \
                        if empl.birth_date else ''
                elif attr == 'email':
                    result[attr] = empl.email
                elif attr == 'phone':
                    result[attr] = empl.phone
                elif attr == 'education':
                    result[attr] = empl.education
                elif attr == 'birth_place':
                    result[attr] = empl.birth_place
                elif attr == 'card_id':
                    result[attr] = empl.card_id
                elif attr == 'native_place':
                    result[attr] = empl.native_place

            start += 1
            results.append(result)

        return results, count






