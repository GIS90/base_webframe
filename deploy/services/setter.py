#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/6/6 12:07 AM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python setter.py
# ------------------------------------------------------------
import os

from deploy.utils.utils import get_now, md5, \
    mk_dirs, get_base_dir, \
    get_user_id
from deploy.config import UPLOAD_BASE_DIR
from deploy.utils.status import Status
from deploy.utils.logger import logger as LOG

from deploy.bo.sysuser import SysUserBo


class SetterService(object):

    ALLOWED_EXTENSIONS = [
        '.png',
        '.jpg',
        '.bmp',
        '.jpeg'
    ]

    def __init__(self):
        super(SetterService, self).__init__()
        self.sysuser_bo = SysUserBo()

    def __allow_format_img(self, fname):
        if isinstance(fname, unicode):
            fname = fname.encode('utf-8')
        return True if (os.path.splitext(fname)[1]).lower() in self.ALLOWED_EXTENSIONS else False

    def upload_image(self, image_file):
        image_name = image_file.filename
        if not self.__allow_format_img(image_name):
            return Status(
                    201,
                    'failure',
                    u'图片格式支持：jpg、png、bmp、jpeg',
                    {}
                    ).json()

        _base_dir = get_base_dir()
        now_date = get_now(format="%Y-%m-%d")

        def __get_filename_by_md5(file_name):
            suffix = (os.path.splitext(file_name)[1]).lower()
            _v = get_now() + file_name
            return (md5(_v)
                    + suffix)

        store_file_name = __get_filename_by_md5(image_name)
        db_image = os.path.join((UPLOAD_BASE_DIR + now_date), store_file_name)
        store_dir = _base_dir + UPLOAD_BASE_DIR + now_date
        if not os.path.exists(store_dir):
            mk_dirs(store_dir)
        image_file.save(os.path.join(store_dir, store_file_name))
        try:
            user_mode = self.sysuser_bo.get_user_by_params(get_user_id())
            user_mode.image = db_image
            self.sysuser_bo.merge_model(user_mode)
        except Exception as e:
            LOG.error("upload image is error: %s" % e)
            return Status(
                    300,
                    'failure',
                    u'upload image更新db失败',
                    {}
                    ).json()

        return Status(
                    100,
                    'success',
                    u'图片上传成功',
                    {'image': db_image}
                    ).json()

