#!/usr/bin/env python3

# @FileName : test_model.py
# @作者 : Liu
# @日期 : 2019年04月29日
# @时间 : 17时14分

import unittest
from app import init_app, db
from app.model import User, Role


class ModelTest(unittest.TestCase):
    def setUp(self):
        # 开始 准备
        self.app = init_app('testing')
        self.app_ctx = self.app.app_context()
        # 推进app
        self.app_ctx.push()
        db.drop_all()
        db.create_all()
        Role.seed()

    def tearDown(self):
        # 结束 清理
        self.app_ctx.pop()

    def test_user_role_set(self):

        user = User(name='lzm1', password='123123', email='123123@qq.com')
        db.session.add(user)
        db.session.commit()
        print(self.assertEqual(user.roles.name, 'Guests'))
