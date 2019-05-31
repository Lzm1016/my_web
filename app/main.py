#!/usr/bin/env python3

# @FileName : main.py
# @作者 : Liu
# @日期 : 2019年04月26日
# @时间 : 18时23分

from app import init_app

app = init_app()

if __name__ == '__main__':
    app.run(debug=True)
