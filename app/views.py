#!/usr/bin/env python3

# @FileName : views.py
# @作者 : Liu
# @日期 : 2019年04月30日
# @时间 : 17时33分

import json
from flask import request, render_template, redirect, url_for, session, Response, flash
from app.lib.tools import data_contrast
# from app import login_manager
# from app.model import User_mod


def init_views(app, mysql):
    @app.route("/", methods=['GET'])
    def login():
        print(request.cookies)
        # print(request.remote_addr)
        # print(request.user_agent)
        # print(request.headers)
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
                print("我设置了 session")
                session['username'] = username
                resp = Response()

                resp.set_cookie("Itcast_1", "python_1", max_age=3600)
                resp.set_cookie("Itcast_2", "python_2", max_age=3600)

                # return session.get('username')
                resp.data = json.dumps({"status": data})
                return resp
            else:
                return json.dumps({"status": data, 'error': '用户或密码错误!'})

        return redirect(url_for('login'))

def login_auth(fun):
    # @functools.wraps(fun)
    def login(*args, **kwargs):
        if session and session.get('username') == 'lzm':
            return fun(*args, **kwargs)
        return redirect(url_for('login'))

    return login
