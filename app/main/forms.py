#!/usr/bin/env python3

# @FileName : forms.py
# @作者 : Liu
# @日期 : 2019年05月14日
# @时间 : 14时48分

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField


class PostForm(FlaskForm):
    title = StringField(label='标题', validators=[DataRequired()])
    body = PageDownField(label='正文', validators=[DataRequired()])
    submit = SubmitField('发表')


class CommentForm(FlaskForm):
    body = StringField(label='评论', validators=[DataRequired()])
    submit = SubmitField('Submit')
