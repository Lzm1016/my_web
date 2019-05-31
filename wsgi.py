#!/usr/bin/env python3

# @FileName : wsgi.py
# @作者 : Liu
# @日期 : 2019年05月30日
# @时间 : 11时08分

from app import init_app

application = init_app('default')

if __name__ == '__main__':
    application.run()
