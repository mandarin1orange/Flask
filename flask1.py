#! /usr/bin/python
# -*- coding: UTF-8 -*-

import flask
from flask import Flask

# 创建flask程序
app = Flask(__name__)

@app.route('/a')
def a_page():
    return 'this is a page'
    pass

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)