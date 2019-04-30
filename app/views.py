#!/usr/bin/env python3

# @FileName : views.py
# @作者 : Liu
# @日期 : 2019年04月30日
# @时间 : 17时33分

import json
from flask import request, render_template, redirect, url_for
from app.lib.tools import data_contrast


def init_views(app, mysql):
    @app.route("/", methods=['GET'])
    def login():
        return render_template('logintest.html')

    @app.route('/login/', methods=['POST'])
    def login_data():
        if request.method == 'POST':
            # 获取登录名
            username = request.form.get('username')
            # 获取登录密码
            password = request.form.get('password')

            data = data_contrast(mysql, username, password)
            if data:
                return json.dumps({"status": data})
            else:
                return json.dumps({"status": data, 'error': '用户或密码错误!'})

        return redirect(url_for('login'))

    @app.route("/index")
    def idnex():
        return "你是猪吗？"
