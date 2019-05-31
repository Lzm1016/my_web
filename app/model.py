#!/usr/bin/env python3

# @FileName : model.py
# @作者 : Liu
# @日期 : 2019年05月09日
# @时间 : 11时30分

from flask_login import UserMixin, AnonymousUserMixin
from . import db, login_manager
from datetime import datetime
from markdown import markdown


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', back_populates='roles')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guests', 'Administrators']))
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    password = db.Column(db.String, nullable=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    roles = db.relationship('Role', back_populates='users')

    posts = db.relationship('Post', back_populates='users')
    comments = db.relationship('Comment', back_populates='users')

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        # target.password = md.update()
        target.roles = Role.query.filter_by(name='Guests').first()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


db.event.listen(User.name, 'set', User.on_created)


# @db.event.listens_for(User.password, 'set', raw=True, retval=True)
# def user_password(target, value, oldvalue, initiator):
#     return password_md5(value)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    body = db.Column(db.String, nullable=True)
    body_html = db.Column(db.String)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    comments = db.relationship('Comment', back_populates='posts')

    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User', back_populates='posts')

    @staticmethod
    def on_body_chenged(target, value, oldvalue, initiator):
        if value is None or value is '':
            target.body_html = ''
        else:
            target.body_html = markdown(value)


db.event.listen(Post.body, 'set', Post.on_body_chenged)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=True)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    posts_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    posts = db.relationship('Post', back_populates='comments')

    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User', back_populates='comments')

# @db.event.listens_for(db.session.query(['User']), 'before_compile')
# def user_load(query):
#     print(query)
