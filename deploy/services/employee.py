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
from deploy.bo.enums import EnumsBo
from deploy.utils.utils import d2s
from deploy.utils.status import Status
from deploy.utils.logger import logger as LOG


class EmployeeService(object):

    employee_all_attrs = [
        'id',
        'china_name',
        'english_name',
        'sex',
        'birth_date',
        'nationality',
        'email',
        'phone',
        'education',
        'card_id',
        'entry_date'
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
        self.enums_bo = EnumsBo()

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
                if isinstance(v, unicode):
                    v = v.encode('utf-8')
                new_args[k] = "%" + str(v) + "%"
            else:
                new_args[k] = v
        # start = (int(new_args['index']) - 1) * int(new_args.get('limit'))
        # new_args['start'] = start
        all_empls, count = self.employee_bo.get_all(new_args)
        data = dict()
        LOG.info('employee>api_list: %s' % count)
        if not all_empls:
            data['totalCount'] = 0
            data['datalist'] = []
            return Status(
                    101,
                    'success',
                    u'成功，但数据为空',
                    data
                    ).json()

        results = list()
        for empl in all_empls:
            if not empl:
                continue

            result = dict()
            for attr in self.employee_all_attrs:
                params = dict()
                if attr == 'id':
                    result[attr] = start + 1
                elif attr == 'china_name':
                    result[attr] = empl.china_name
                elif attr == 'english_name':
                    result[attr] = empl.english_name
                elif attr == 'nationality':
                    nationality = empl.nationality
                    if not nationality:
                        result[attr] = empl.nationality
                    else:
                        params['enum_type'] = attr
                        params['enum_subid'] = empl.nationality
                        result[attr] = self.enums_bo.get_enumname_by_params(params)
                elif attr == 'sex':
                    sex = empl.sex
                    if not sex:
                        result[attr] = empl.sex
                    else:
                        params['enum_type'] = attr
                        params['enum_subid'] = empl.sex
                        result[attr] = self.enums_bo.get_enumname_by_params(params)
                elif attr == 'birth_date':
                    result[attr] = d2s(empl.birth_date, fmt="%Y-%m-%d") \
                        if empl.birth_date else ''
                elif attr == 'entry_date':
                    result[attr] = d2s(empl.entry_date, fmt="%Y-%m-%d") \
                        if empl.entry_date else ''
                elif attr == 'email':
                    result[attr] = empl.email
                elif attr == 'phone':
                    result[attr] = empl.phone
                elif attr == 'card_id':
                    result[attr] = empl.card_id

            start += 1
            results.append(result)
        data['totalCount'] = count
        data['datalist'] = results

        return Status(
                    100,
                    'success',
                    u'成功',
                    data
                    ).json()
