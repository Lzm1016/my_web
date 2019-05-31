#!/usr/bin/env python3

# @FileName : setup.py
# @作者 : Liu
# @日期 : 2019年05月30日
# @时间 : 11时43分

from setuptools import setup, find_packages

print(find_packages())
setup(
    name="blog",
    version="0.1",
    author='tangren',
    author_email="923425198@qq.com",
    url='loalhost',
    # 脚本
    # scripts=['wsgi.py'],
    packages=find_packages(),
    install_requires=[
        'Flask >= 1.0.2',
        'Flask-Bootstrap >= 3.3.7',
        'Jinja2 >= 2.10',
        'Markdown >=1.0.2',
        'Flask-SQLAlchemy >= 2.3.2',
        'Flask-PageDown >= 0.2.2',
        'Flask-Login >= 0.4.1',
        'Flask-WTF >= 0.14.2',
        'Flask-Migrate >= 2.4.0',
        'Flask-Script >= 2.0.6',
    ],
    package_data={
        'app': [
            'static/*/*',
            'templates/**/*',
            'templates/*',
        ],
        'app.main': [
            'static/*/*',
            'templates/*',
            'templates/**/*',
        ],
    },
    data_files=['wsgi.py', 'config.py', 'manager.py'],
)
