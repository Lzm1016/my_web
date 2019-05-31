#!/usr/bin/env python3

# @FileName : forms.py
# @作者 : Liu
# @日期 : 2019年05月13日
# @时间 : 11时34分

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo
from app.model import User
from app.lib.tools import EXISTNAME, Password_Field


class LoginForm(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired()])
    password = Password_Field(label='密码', validators=[DataRequired()])
    submit = SubmitField(label='提交')


class RegistrationForm(FlaskForm):
    email = StringField(label='邮箱地址', validators=[DataRequired(),
                                                  EXISTNAME(User, 'email'),
                                                  Length(1, 64),
                                                  Email(message='请输入正确的邮箱地址')])
    username = StringField(label='用户名', validators=[DataRequired(),
                                                    EXISTNAME(User),
                                                    Length(1, 64),
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户必须由字母、数字、下划线或者 . 组成')])

    password = Password_Field(label='密码', validators=[DataRequired(), EqualTo('password2', message='两次密码必须一致')])
    password2 = Password_Field(label='确认密码', validators=[DataRequired()])
    submit = SubmitField(label='马上注册')
