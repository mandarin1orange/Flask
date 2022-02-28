#! /usr/bin/python
# -*- coding: UTF-8 -*-

import flask
from flask import *
from datetime import timedelta
import pymysql

# 创建flask程序
app = Flask(__name__,
            static_url_path='/static',  # 静态文件路径
            static_folder='static',
            template_folder='templates'  # 模板文件
            )

@app.route('/chuli',methods=['POST'])
def chuli():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('passwd')
        print('用户名提交了'+username+'密码提交了'+password)
    # 打开数据库
    db = pymysql.connect(host='localhost',user='root',password='root',db='haha')
    # 创建游标对象
    cursor = db.cursor()
    # sql语句
    sql = '''
    INSERT INTO table1(username,password)VALUES('%s','9999')
    '''%('test4')
    try:
        # 执行sql
        cursor.execute(sql)
        # 确认
        db.commit()
    except:
        # 执行失败就回滚
        db.rollback()

    db.close()

    return render_template('chuli.html')

@app.route('/test1')
def test1():
    return render_template('test1.html')

# 装饰器，关联路由
@app.route('/')
def index():
    return 'haha'

# 404重定向
@app.errorhandler(404)
def page_not_found(e):
    return '你出错了',404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)