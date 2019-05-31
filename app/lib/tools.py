#!/usr/bin/env python3

# @FileName : tools.py
# @作者 : Liu
# @日期 : 2019年04月29日
# @时间 : 15时27分

import pandas as pd
from hashlib import md5
from wtforms import ValidationError, PasswordField


def data_contrast(mysql, username, password):
    data = mysql.get_oneline(username)
    df = pd.DataFrame(list(data), columns=['username', 'password'])
    data = df[df['password'] == password]
    return not data.empty


# 密码加密
def password_md5(value):
    md = md5()
    md.update(value.encode('ascii'))
    value = md.hexdigest()
    return value


# 定义新的password 字段 用来加密验证
class Password_Field(PasswordField):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = password_md5(valuelist[0])
        else:
            self.data = ''


# 定义个类用来判断 用户是否存在
class EXISTNAME(object):
    def __init__(self, model, label='name', message=None):
        self.label = label
        self.model = model
        self.message = message

    def __call__(self, form, field):

        other_name = self.model.query.filter_by(name=field.data).first()

        if self.label == 'email':
            other_name = self.model.query.filter_by(email=field.data).first()
        if other_name is not None:
            # 字段的label
            # print(field.label.text)
            message = self.message
            if message is None:
                message = field.gettext('%s已存在' % field.label.text)

            raise ValidationError(message)
