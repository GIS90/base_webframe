#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    the table of insert sql
    
    tables:
        sysuser
        enums
        employee

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/31 11:20 AM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python print_insert_sql.py
# ------------------------------------------------------------
import random


def print_sysuser():
    # insert sysuser
    print """
insert into sysuser(rtx_id, fullname, password, email , phone, image, is_admin) 
VALUES('admin', '系统管理员', '1', 'gaomingliang971366@163.com', '1', 'uploads/20200604/avatar.jpg', 1);
    """


def _generator_name():
    first_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                   '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                   '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                   '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                   '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                   '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                   '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

    last_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
                  '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
                  '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
                  '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
                  '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
                  '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
                  '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
                  '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
                  '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
                  '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
                  '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
                  '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
                  '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
                  '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
                  '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
                  '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
                  '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
                  '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
                  '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
                  '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
                  '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
                  '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
                  '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
                  '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
                  '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
                  '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
                  '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
                  '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
                  '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
                  '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
                  '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
                  '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
                  '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
                  '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
                  '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
                  '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
                  '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
                  '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
                  '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
                  '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
                  '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
                  '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
                  '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
                  '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
                  '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
                  '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
                  '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
                  '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
                  '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
                  '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
                  '乾', '坤']

    def _get_ming(size):
        ming = ''
        for i in range(1, size, 1):
            ming += random.choice(last_names)
        else:
            return ming

    return random.choice(first_names) + _get_ming(random.randint(2, 3))


def _get_eng_name(size):
    eng_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    return ''.join([random.choice(eng_names) for i in range(1, size, 1)])


def _get_value_random(_type, size=2):
    """
    china_name, english_name, sex, birth_date, political_status, 
nation, nationality, education, marriage, phone, email, card_type, 
card_id, card_place, card_deadline, residence_type, current_address, 
bank_type, bank_country, bank_city, bank_id, bank_name
    :param _type: 
    :param size: 
    :return: 
    """
    if _type == 'sex':
        return random.randint(1, 2)
    elif _type == 'status':
        return 1
    elif _type == 'political_status':
        return random.randint(1, 5)
    elif _type == 'nation':
        return random.randint(1, 6)
    elif _type == 'nationality':
        return random.randint(1, 6)
    elif _type == 'education':
        return random.randint(1, 6)
    elif _type == 'marriage':
        return random.randint(1, 2)
    elif _type == 'card_type':
        return random.randint(1, 3)
    elif _type == 'card_id':
        return ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 17))
    elif _type == 'residence_type':
        return random.randint(1, 2)
    elif _type == 'bank_type':
        return random.randint(1, 2)
    elif _type == 'bank_country':
        return random.randint(1, 6)


def _get_random_bank_city():
    citys = [
        '北京', '上海', '武汉', '通辽',
        '满洲里', '包头', '呼和浩特', '呼伦贝尔',
        '西安', '重庆', '南京', '哈尔滨',
        '吉林', '沈阳', '南京', '哈尔滨',
    ]
    return random.choice(citys)


def _get_random_date():
    year = random.randint(1960, 2010)
    month = random.randint(1, 12)
    if year % 4 == 0:
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 29)
    else:
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    birthday = str(year) + '-' + str(month) + '-' + str(day)
    return birthday


def _get_random_phone():
    phone_number = [139, 138, 137, 136, 135, 134, 159, 158, 15, 150, 151, 152, 188,
                    130, 131, 132, 156, 155, 133, 153, 189]
    tel = ''
    tel += str(random.choice(phone_number))
    ran = ''
    for i in range(8):
        ran += str(random.randint(0, 9))
    tel += ran
    return tel


def _get_random_bank_id():
    bank_id = '62'
    for i in range(17):
        ran = str(random.randint(0, 9))
        bank_id += ran
    return bank_id


def _get_random_email(phone):
    email_suf = random.choice(['@163.com', '@qq.com', '@126.com', '@sina.com', '@sina.cn', '@soho.com', '@yeah.com'])
    email = phone + email_suf
    return email


def _get_random_address():
    address = [
        'A' * 12,
        'B' * 12,
        'C' * 12,
        'D' * 12,
        'E' * 12,
        'F' * 12,
        'G' * 12,
        'H' * 12,
        'I' * 12,
        'J' * 12,
        'K' * 12,
        'L' * 12,
        'M' * 12,
        'N' * 12,
        'O' * 12,
        'P' * 12,
        'Q' * 12,
        'R' * 12,
        'S' * 12,
        'T' * 12,
        'U' * 12,
        'V' * 12,
        'W' * 12,
        'X' * 12,
        'Y' * 12,
        'Z' * 20
    ]
    return random.choice(address)


def print_employee(max=50):
    # insert employee
    prefix = """insert into employee(china_name, english_name, sex, birth_date, political_status, nation, 
nationality, education, marriage, phone, email, card_type, 
card_id, card_place, card_deadline, residence_type, current_address, bank_type, 
bank_country, bank_city, bank_id, bank_name, entry_date, status,
entry_submit_time, entry_submit_rtx
) VALUES """
    suffix = ''
    for i in range(0, max, 1):
        name = _generator_name()
        phone = _get_random_phone()
        rtx = 'admin'
        val = """(
        '%s', '%s', '%s', '%s', '%s', '%s',
        '%s', '%s', '%s', '%s', '%s', '%s',
        '%s', '%s', '%s', '%s', '%s', '%s',
        '%s', '%s', '%s', '%s', '%s', '%s',
        '%s', '%s')
        """ % (
            name, _get_eng_name(random.randint(1, 8)), _get_value_random(_type='sex'), _get_random_date(), _get_value_random(_type='political_status'), _get_value_random(_type='nation'),
            _get_value_random(_type='nationality'), _get_value_random(_type='education'), _get_value_random(_type='marriage'), phone, _get_random_email(phone), _get_value_random(_type='card_type'),
            _get_value_random(_type='card_id'), _get_random_address(), _get_random_date(), _get_value_random(_type='residence_type'), _get_random_address(), _get_value_random(_type='bank_type'),
            _get_value_random(_type='bank_country'), _get_random_bank_city(), _get_random_bank_id(), name, _get_random_date(), _get_value_random(_type='status'),
            (_get_random_date() + ' 12:12:12'), rtx
        )
        if i == (max - 1):
            suffix += val + ';'
        else:
            suffix += val + ','

    print prefix + suffix


def print_enums():
    print """
insert into enums(subid, type, name) VALUES (1,'sex','男'),(2,'sex','女');
insert into enums(subid, type, name) VALUES (1,'status','在职'),(2,'status','离职');
insert into enums(subid, type, name) VALUES (1,'nation','汉族'),(2,'nation','蒙族'),(3,'nation','回族'),(4,'nation','满族'),(5,'nation','维吾尔族'),(6,'nation','其他');
insert into enums(subid, type, name) VALUES (1,'nationality','中华人民共和国'),(2,'nationality','美国'),(3,'nationality','英国'),(4,'nationality','德国'),(5,'nationality','刚果共和国'),(6,'nationality','梵蒂冈');
insert into enums(subid, type, name) VALUES (1,'political_status','党员'),(2,'political_status','预备党员'),(3,'political_status','共青团员'),(4,'political_status','群众'),(5,'political_status','其他民族党派');
insert into enums(subid, type, name) VALUES (1,'education','博士'),(2,'education','研究生'),(3,'education','本科'),(4,'education','专科'),(5,'education','高中'),(6,'education','其他');
insert into enums(subid, type, name) VALUES (1,'marriage','已婚'),(2,'marriage','未婚');
insert into enums(subid, type, name) VALUES (1,'residence_type','城镇户口'),(2,'residence_type','农业户口');
insert into enums(subid, type, name) VALUES (1,'card_type','二代身份证'),(2,'card_type','护照'),(3,'card_type','其他');
insert into enums(subid, type, name) VALUES (1,'bank_country','中华人民共和国'),(2,'bank_country','美国'),(3,'bank_country','英国'),(4,'bank_country','德国'),(5,'bank_country','日本'),(6,'bank_country','其他');
insert into enums(subid, type, name) VALUES (1,'bank_type','建设银行'),(2,'bank_type','农业银行'),(3,'bank_type','工商银行'),(4,'bank_type','邮政储蓄银行'),(5,'bank_type','中国银行'),(6,'bank_type','交通银行');
insert into enums(subid, type, name) VALUES (1,'bank_city','北京'),(2,'bank_city','上海'),(3,'bank_city','武汉'),(4,'bank_city','广州'),(5,'bank_city','深圳'),(6,'bank_city','通辽'),(7,'bank_city','满洲里'),(8,'bank_city','呼和浩特'),(9,'bank_city','重庆'),(10,'bank_city','包头'),(11,'bank_city','西安'),(12,'bank_city','呼伦贝尔'),(13,'bank_city','南京'),(14,'bank_city','哈尔滨'),(15,'bank_city','沈阳'),(16,'bank_city','吉林');
"""


if __name__ == '__main__':
    # print_sysuser()
    print_employee(20)
    # print_enums()
