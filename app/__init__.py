#!/usr/bin/env python3

# @FileName : __init__.py.py
# @作者 : Liu
# @日期 : 2019年04月28日
# @时间 : 21时29分

import os
from flask import Flask
# from app.lib.mysql_util import mysql_util
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from flask_login import LoginManager

from config import config

bootstrap = Bootstrap()
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
login_manager = LoginManager()
pagedown = PageDown()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def init_app(config_name='default'):
    app = Flask(__name__)
    # app.config["CSRF_ENABLED"] = True
    # app.config["SECRET_KEY"] = "renyizifuchuan"
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    from app.auth import auth as auth_blueprint
    from app.main import main as main_blueprint
    app.config.from_object(config[config_name])
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    bootstrap.init_app(app)
    pagedown.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # mysq = mysql_util('db.conf')

    # init_views(app, mysq)

    return app
