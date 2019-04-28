#!/usr/bin/env python3

# @FileName : main.py
# @作者 : Liu
# @日期 : 2019年04月26日
# @时间 : 18时23分

import sys
import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def login():
    return '欢迎回家1'


if __name__ == '__main__':
    app.run(debug=True)
