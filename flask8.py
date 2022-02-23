#! /usr/bin/python
# -*- coding: UTF-8 -*-

import flask
from flask import Flask
from flask import request
from flask import json

# 创建flask程序
app = Flask(__name__,
            static_url_path='/static',  # 静态文件路径
            static_folder='static',
            template_folder='templates'  # 模板文件
            )

@app.route('/woshihenchangdeluyou',endpoint='b1')
def b_page():
    return '你来了啊'

# 404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404

@app.route('/a')
def a_page():
    # 主动抛出异常
    flask.abort(404)
    return 'a'

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)