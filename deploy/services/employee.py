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
from deploy.utils.utils import d2s, get_user_id, get_now
from deploy.utils.status import Status
from deploy.utils.logger import logger as LOG


class EmployeeService(object):

    employee_show_attrs = [
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
        'start'
    ]

    request_add_attrs = [
        'china_name',
        'english_name',
        'email',
        'phone',
        'entry_date',
        'sex',
        'nation',
        'birth_date',
        'political_status',
        'nationality',
        'residence_type',
        'education',
        'marriage',
        'card_type',
        'card_id',
        'card_deadline',
        'card_place',
        'current_address',
        'bank_type',
        'bank_country',
        'bank_city',
        'bank_id',
        'bank_name',
        'status',
        'is_add'
    ]

    employee_emuns_attrs = [
        'sex',
        'nation',
        'political_status',
        'nationality',
        'residence_type',
        'education',
        'marriage',
        'card_type',
        'bank_type',
        'bank_country',
        'bank_city'
    ]

    employee_attrs_dict = {
        'china_name': "中文名称",
        'english_name': "英文文名称",
        'email': "邮箱",
        'phone': "电话",
        'entry_date': "入职日期",
        'sex': "性别",
        'nation': "民族",
        'birth_date': "出生日期",
        'political_status': "政治面貌",
        'nationality': "国籍",
        'residence_type': "户口类型",
        'education': "教育程度",
        'marriage': "婚姻状况",
        'card_type': "证件类型",
        'card_id': "证件编号",
        'card_deadline': "过期日期",
        'card_place': "证件地址",
        'current_address': "现住地址",
        'bank_type': "开户行",
        'bank_country': "开户行国家",
        'bank_city': "开户城市",
        'bank_id': "工资卡号",
        'bank_name': "开户姓名"
    }

    request_not_need_attrs = [
        'english_name',
        'email'
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
                    202,
                    'failure',
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

        # status 任职状态 1在职 2离职
        all_empls, count = self.employee_bo.get_all(new_args, status=1)
        data = dict()
        LOG.info('employee>api_list: %s' % count)
        if not all_empls:
            data['totalCount'] = 0
            data['datalist'] = []
            return Status(
                    101,
                    'failure',
                    u'成功，但数据为空',
                    data
                    ).json()

        results = list()
        for empl in all_empls:
            if not empl:
                continue

            result = dict()
            for attr in self.employee_show_attrs:
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

    def add_or_edit_empl(self, args):
        """
        add employee
        :param args: form parameters
        :return: 
        """
        new_args = dict()
        for k, v in args.items():
            if isinstance(k, unicode):
                k = k.encode('utf-8')
            if v and isinstance(v, unicode):
                v = v.encode('utf-8')
            if k not in self.request_add_attrs:
                return Status(
                    202,
                    'failure',
                    u'%s参数不合法' % k,
                    {}
                    ).json()

            if k in self.request_not_need_attrs:
                new_args[k] = str(v)
                continue

            if k and not v:
                attr_name = self.employee_attrs_dict.get(k)
                return Status(
                    203,
                    'failure',
                    u'%s内容需要进行填写' % attr_name,
                    {}
                    ).json()

            new_args[k] = v

        card_id = args.get('card_id')
        is_add = new_args['is_add']
        china_name = args.get('china_name')
        if isinstance(card_id, unicode):
            card_id = card_id.encode('utf-8')
        exist_empl_mode = self.employee_bo.get_empl_by_card_id(card_id)

        if is_add in ['1', 1] and exist_empl_mode:
            return Status(
                    204,
                    'failure',
                    u'%s用户已存在，无需重新建立信息档案' % china_name,
                    {}
                    ).json()

        empl_mode = self.employee_bo.new_mode() if is_add == '1' \
            else exist_empl_mode

        # submit
        for attr in self.request_add_attrs:
            if not attr:
                continue

            if attr == 'china_name':
                empl_mode.china_name = new_args.get(attr)
            elif attr == 'english_name':
                empl_mode.english_name = new_args[attr]
            elif attr == 'email':
                empl_mode.email = new_args[attr]
            elif attr == 'phone':
                empl_mode.phone = new_args[attr]
            elif attr == 'entry_date':
                empl_mode.entry_date = new_args[attr]
            elif attr == 'sex':
                empl_mode.sex = new_args[attr]
            elif attr == 'nation':
                empl_mode.nation = new_args[attr]
            elif attr == 'birth_date':
                empl_mode.birth_date = new_args[attr]
            elif attr == 'political_status':
                empl_mode.political_status = new_args[attr]
            elif attr == 'nationality':
                empl_mode.nationality = new_args[attr]
            elif attr == 'residence_type':
                empl_mode.residence_type = new_args[attr]
            elif attr == 'education':
                empl_mode.education = new_args[attr]
            elif attr == 'marriage':
                empl_mode.marriage = new_args[attr]
            elif attr == 'card_type':
                empl_mode.card_type = new_args[attr]
            elif attr == 'card_id':
                empl_mode.card_id = new_args[attr]
            elif attr == 'card_deadline':
                empl_mode.card_deadline = new_args[attr]
            elif attr == 'card_place':
                empl_mode.card_place = new_args[attr]
            elif attr == 'current_address':
                empl_mode.current_address = new_args[attr]
            elif attr == 'bank_type':
                empl_mode.bank_type = new_args[attr]
            elif attr == 'bank_country':
                empl_mode.bank_country = new_args[attr]
            elif attr == 'bank_city':
                empl_mode.bank_city = new_args[attr]
            elif attr == 'bank_id':
                empl_mode.bank_id = new_args[attr]
            elif attr == 'bank_name':
                empl_mode.bank_name = new_args[attr]
            elif attr == 'status':
                empl_mode.status = new_args[attr] if new_args[attr] else '1'

        # record
        if is_add in [1, '1']:
            empl_mode.entry_submit_rtx = get_user_id()
            empl_mode.entry_submit_time = get_now()
        else:
            empl_mode.last_update_rtx = get_user_id()
            empl_mode.last_update_time = get_now()

        self.employee_bo.add_model(empl_mode) if is_add == '1' \
            else self.employee_bo.merge_model(empl_mode)

        if is_add == '1':
            LOG.info("%s add employee is success" % card_id)
            return Status(
                         100,
                         'success',
                         u'新增%s成功' % china_name,
                         {}
                         ).json()

        LOG.info("%s edit employee is success" % card_id)
        return Status(
                     110,
                     'success',
                     u'%s信息编辑成功' % china_name,
                     {}
                     ).json()

    def get_empl_by_card_id(self, card_id):
        return self.employee_bo.get_empl_by_card_id(str(card_id)) \
            if card_id else {}

    def quit_empl(self, json_args):
        card_id = json_args.get('card_id')
        if not card_id:
            return Status(
                    202,
                    'failure',
                    u'quit_empl API无card_id参数',
                    {}
                    ).json()
        if isinstance(card_id, unicode):
            card_id = card_id.encode('utf-8')

        empl_mode = self.employee_bo.get_empl_by_card_id(card_id)
        if not empl_mode:
            return Status(
                    203,
                    'failure',
                    u'quit_empl删除不存在用户：%s' % json_args.get('card_id'),
                    {}
                    ).json()

        empl_mode.status = '2'
        empl_mode.quit_submit_time = get_now()
        empl_mode.quit_submit_rtx = get_user_id()
        self.employee_bo.merge_model(empl_mode)
        return Status(
                    100,
                    'failure',
                    u'%s操作离职成功' % empl_mode.china_name,
                    {}
                    ).json()
