#!/usr/bin/env python3

# @FileName : __init__.py.py
# @作者 : Liu
# @日期 : 2019年05月13日
# @时间 : 16时17分
import os

from flask import Blueprint

path = os.path.abspath(os.path.dirname(__file__))
# print(os.path.join(path, 'static'))
main = Blueprint('main', __name__, static_folder='static',static_url_path='/main', template_folder='templates')

from . import views, forms
