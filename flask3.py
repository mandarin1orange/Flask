#! /usr/bin/python
# -*- coding: UTF-8 -*-

import flask
from flask import Flask
from flask import request

# 创建flask程序
app = Flask(__name__,
            static_url_path='/static',  # 静态文件路径
            static_folder='static',
            template_folder='templates'  # 模板文件
            )

@app.route('/a',methods=['GET','POST'])
def a_page():
    user_name = request.form.get('uname')
    user_pass = request.form.get('upass')
    return 'this is a page %s hahahaha'%(request.method)  # 获取请求类型

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)