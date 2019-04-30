#!/usr/bin/env python3

# @FileName : __init__.py.py
# @作者 : Liu
# @日期 : 2019年04月28日
# @时间 : 21时29分

from datetime import timedelta
from flask import Flask
from app.lib.mysql_util import mysql_util
from app.views import init_views


def init_app():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    mysq = mysql_util('db.conf')
    init_views(app, mysq)
    return app


app = init_app()
