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

@app.route('/a')
def a_page():
    # 定义一个字典
    json_dict = {
        'name':'xiaoli',
        'age':'18',
        'score':'100'
    }
    # 字典转化为json字符串
    result = json.dumps(json_dict)
    # json转化为字典
    dict1 = json.loads('{"age": "18", "name": "xiaoli", "score": "100"}')
    print(dict1)
    return 'x'

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)