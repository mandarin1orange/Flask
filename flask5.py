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

@app.route('/b')
def b_page():
    return '你来了啊'

@app.route('/redirect')
def a_page():
    # 站外重定向
    # return flask.redirect('http://www.cctv.com')
    # 站内重定向
    return flask.redirect(flask.url_for('b_page'))

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)