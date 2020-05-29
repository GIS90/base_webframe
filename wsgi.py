#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    the entry point of webframe
    use gunicorn to start project(gunicorn -c etc/dev/gunicorn.conf wsgi:app) 
    or directly execute  the file to start(python wsgi.py)
    python version: python2
    
    Enjoy the good lift everyday！！!

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/19 4:24 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""
# ------------------------------------------------------------
# usage: /usr/bin/python wsgi.py
# ------------------------------------------------------------
from deploy import create_app


app = create_app()

# # 手动启动
# app.run(host="0.0.0.0", port=11111, debug=True)
