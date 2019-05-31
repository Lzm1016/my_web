#!/usr/bin/env python3

# @FileName : __init__.py.py
# @作者 : Liu
# @日期 : 2019年05月13日
# @时间 : 16时17分

from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import forms, views
