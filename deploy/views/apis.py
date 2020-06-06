# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    the view of apis

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/15"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""
from flask import Blueprint, jsonify, \
    make_response, request, abort
from deploy.utils.logger import logger as LOG

apis = Blueprint('apis', __name__)


results = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@apis.route('/apis/show/<string:tid>', methods=['GET'])
def show_task(tid):
    if request.method != "GET":
        return jsonify({'status': 0, 'msg': u'show请求方法不为get方法', 'code': 4042})

    if tid == 'all':
        return jsonify({'tasks': results}), 200

    tid = int(tid)
    if tid <= len(results):
        return jsonify({'task': results[tid - 1]}), 200
    else:
        return abort(404)


@apis.route('/apis/create', methods=['GET', 'POST'])
def create_task():
    if request.method != 'POST':
        return jsonify({'status': 0, 'msg': u'show请求方法不为get方法', 'code': 4042})

    form = request.form
    tid = form.get('tid')
    title = form.get('title')
    done = form.get('done')
    description = form.get('description')

    new_task = dict()
    new_task['tid'] = tid
    new_task['title'] = title
    new_task['done'] = done
    new_task['description'] = description

    results.append(new_task)

    return jsonify({'status': 0, 'msg': u'create add success', 'code': 0})


@apis.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'status': 0, 'msg': u'task不存在', 'code': 404}))



