#! /usr/bin/python
# -*- coding: UTF-8 -*-

import flask
from flask import *

# 创建flask程序
app = Flask(__name__,
            static_url_path='/static',  # 静态文件路径
            static_folder='static',
            template_folder='templates'  # 模板文件
            )

@app.route('/woshihenchangdeluyou',endpoint='b1')
def b_page():
    return '你来了啊'

@app.route('/a/<id>')
def a_page(id):
    # python参数进来都是string类型
    m_int = int(id)+20
    m_str = 'haha nihao'
    m_list = ['xiaoming','xiaohong','xiaoli']
    return flask.render_template('tempa.html',mint=m_int,mstr=m_str,mlist=m_list)

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'

# 404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404

# 过滤器
@app.template_filter('dore')
def do_reverse(li):
    temp = list(li)
    temp.reverse()
    return temp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)