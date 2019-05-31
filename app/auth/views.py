#!/usr/bin/env python3

# @FileName : views.py
# @作者 : Liu
# @日期 : 2019年05月13日
# @时间 : 17时55分

from flask import render_template, redirect, url_for

from app import db
from app.model import User
from .forms import RegistrationForm, LoginForm
from . import auth
from flask_login import login_user, logout_user
from app.lib.tools import password_md5


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(name=form.username.data, password=form.password.data).first()

        if user is not None:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html', title='登录', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit() and not User.query.filter_by(name=form.username.data).first():
        user = User(email=form.email.data, name=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='注册', form=form)
